#!/usr/bin/env python
#encoding:utf8

from warnings import filterwarnings
from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from json import loads
import os,sys
import MySQLdb
import logging
import logging.handlers
import pretreatment


#[认证配置]
PASSWD  = "abc"
#[数据库配置]
SQLHOST = "localhost"
SQLUSER = "servers"
SQLPWD  = "p@ssw0ld_#!@3A"
DBNAME  = "servers"
#[]
BINDADD  = '0.0.0.0'
TCP_PORT = 1088
LogName  = 'server.log'

#------------------------WORK CLASS---------------------------------------------

class Mysql:
    """This is pretreatment module"""
    def __init__(self,sqlhost,sqluser,sqlpassword,databasename):
        self.sqlhost = sqlhost
        self.sqluser = sqluser
        self.sqlpwd  = sqlpassword
        self.dbname  = databasename

    def insertLinux(self,data):
        """
        插入数据到网络质量检测表
        一次插入多条数据
        value必须为元组
        """
        kyes,sql,values = 0,0,0
        try:
            conn = MySQLdb.connect(host   = self.sqlhost,
                db     = self.dbname,
                user   = self.sqluser,
                passwd = self.sqlpwd)
            curs  = conn.cursor()
            for info in data:
                #print info
                table,keys,values = info
                formatValues = "%s," * len(keys)
                formatValues = formatValues.strip(',')
                if table == 'hostinfo':
                    sql = "insert  ignore into %s%s values (%s)" %(table,keys,formatValues)
                else:
                    sql = "insert into %s%s values (%s)" %(table,keys,formatValues)
                sql = sql.replace("'",'')
                #if table == 'hardwareinfo':
                if not values:
                    continue
                curs.executemany(sql,values)
            #curs.execute(strsql)
            conn.commit()
            curs.close()
            conn.close()
        except Exception,error:
            logging.error("insert error,code:%s,sql:%s,values:%s" %(error,sql,values))

class MyReceiver(LineReceiver):
    """

    """
    MAX_LENGTH = 10240000 #单行最大长度10M
    def  connectionLost(self, reason):
        #Protocol.connectionLost(self, reason)
        #self.factory.number_of_connections -= 1
        logging.info("Disconnected at:%s:%s "%(self.ipadd,self.port))

    def connectionMade(self):
        """开始连接"""
        self.ipadd,self.port = self.transport.client
        if  DENY_IPLIST.count(self.ipadd):
            self.transport.loseConnection()
            logging.critical("Deny from client connect,ipadd:%s" %self.ipadd)
        logging.info("Connection from %s:%s" %(self.ipadd,self.port))

    def lineReceived(self, line):
        """
        00  正确接收，通知客户端清零发送缓存
        01  密码错误
        02  未知错误
        """
        try:
            data = loads(line.strip('\r\n'))
            autuPass = data[data.keys()[0]]['passwrod']
            osversion = data[data.keys()[0]]['osVersion']
            if autuPass == PASSWD:
                if osversion == "Linux":
                    data = pretreatment.linuxtotal(data,self.ipadd)
                    sql.insertLinux(data)
                    self.transport.write('00')
                elif osversion == "Windows":
                    self.transport.write('00')
                else:
                    self.transport.write('02')
            else:
                self.transport.write('01')
        except Exception,error:
            logging.error("Received Data not json,code:%s" %error)
            logging.critical("data:%s" %line)
            self.transport.write('00')
        self.transport.loseConnection()

def initlog(loglevel,path,logname):
    """
    @RotatingFileHandler( filename[, mode[, maxBytes[,backupCount]]])
    @setLevel
        CRITICAL 50
        ERROR    40
        WARNING  30
        DEBUG    20
        NOTSET   0
    """
    logpath =  path + os.sep +'log'
    logname = logpath + os.sep + logname
    if not os.path.exists(logpath):
        os.makedirs(logpath,0755)
        #os.popen("mkdir %s" %logpath)
    logger    = logging.getLogger()
    hdlr      = logging.handlers.RotatingFileHandler(logname,'a', 10*1024*1024,7)
    console   = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
    hdlr.setFormatter(formatter)
    console.setFormatter(formatter)
    logger.addHandler(hdlr)
    if loglevel < 20:
        logger.addHandler(console)
    logger.setLevel(loglevel)
    return logger

def daemonize(pidfile='/dev/null',
              stdin='/dev/null',
              stdout='/dev/null',
              stderr='/dev/null',
              startmsg = 'started with pid %s' ):
    """
         This forks the current process into a daemon.
         The stdin, stdout, and stderr arguments are file names that
         will be opened and be used to replace the standard file descriptors
         in sys.stdin, sys.stdout, and sys.stderr.
         These arguments are optional and default to /dev/null.
        Note that stderr is opened unbuffered, so
        if it shares a file with stdout then interleaved output
         may not appear in the order that you expect.
     """
    # flush io
    sys.stdout.flush()
    sys.stderr.flush()
    # Do first fork.
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0) # Exit first parent.
    except OSError, e:
        sys.stderr.write("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror))
        sys.exit(1)
        # Decouple from parent environment.
    cwd = os.getcwd()
    os.chdir(cwd)
    os.umask(0022)
    os.setsid()
    # Do second fork.
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0) # Exit second parent.
    except OSError, e:
        sys.stderr.write("fork #2 failed: (%d) %s\n" % (e.errno, e.strerror))
        sys.exit(1)
        # Open file descriptors and print start message
    si = file(stdin, 'r')
    so = file(stdout, 'a+')
    se = file(stderr, 'a+', 0)  #unbuffered
    pid = str(os.getpid())
    sys.stderr.write("\n%s\n" % startmsg % pid)
    sys.stderr.flush()
    if pidfile:
        file(pidfile,'w+').write("%s\n" % pid)
        # Redirect standard file descriptors.
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

if __name__ == "__main__":
    ProPath   = sys.path[0]
    Pidfile   = ProPath + os.sep + "server.pid"
    ProStdin  = "/dev/null"
    ProStdout = "/dev/null"
    ProStderr = ProPath + os.sep + "error.log"
    try:
        options = sys.argv[1]
    except IndexError:
        options = ''
    if options == '-d':
        initlog(10,ProPath,LogName)
    else:
        daemonize(Pidfile,ProStdin,ProStdout,ProStderr)
        initlog(20,ProPath,LogName)
    filterwarnings('ignore', category = MySQLdb.Warning)
    DENY_IPLIST=['172.16.30.12']
    sql  = Mysql(SQLHOST,SQLUSER,SQLPWD,DBNAME)
    factory = Factory()
    factory.protocol = MyReceiver
    reactor.listenTCP(TCP_PORT, factory)
    reactor.run()