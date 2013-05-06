# coding=utf-8
"""
数据预处理，解析数据，便于插入到MYSQL中
"""
from json import dumps
from sys import stderr

class Datapro():
    """

    """
    def __init__(self):
        self.hostInfokeys = ('hostid', 'osversion','osname','kernel','ipadd','timestamp')
        self.cpuInfokeys = ('hostid','us','sy','ni','idle', 'wa','hi','si','st','timestamp')
        self.diskInfokeys = ('hostid','filesystem','mountedon','size','used','availused',
                        'sizeuse','nodeuse','timestamp')
        self.ioInfokeys = ('hostid','rsec','wsec','await','util','device','timestamp')
        self.loadInfokeys = ('hostid','load1','load5','load15','uptime','freetime','timestamp')
        self.memoryInfokeys = ('hostid','physical_total','physical_used','physical_free',
                          'physical_shard','physical_buffers','physical_cached',
                          'buffers_used','buffers_cache',
                          'swap_total','swap_used','swap_free','timestamp')
        self.netInfokeys = ('hostid','input','output', 'ipadd','name','timestamp')
        self.processInfokeys = ('hostid','total','running','sleeping','stopped','zombie','timestamp')
        self.hardwareInfokeys = ('hostid','hdmd5','blos','system','cpu','mem','cache','disk','net','timestamp')

    def linuxHostinfo(self,data,ipadd):
        """
        处理主机表信息
        """
        table = 'hostinfo'
        hostInfokeys = self.hostInfokeys
        value = []
        values = []
        try:
            for key in data.keys():
                info = data[key]
                value.append(info['hostid'])
                value.append(info['osVersion'])
                value.append(info['osName'])
                value.append(info['kernel'])
                value.append(info['ipadd'])
                value.append(info['time'])
                values.append(tuple(value))
                break
        except (IndexError,KeyError,TypeError),error:
            stderr.writelines("Ip:%s,linux host info data error:%s\n" %(ipadd,error))
        return table,hostInfokeys,values

    def linuxCpuinfo(self,data,ipadd):
        """
        处理CPU表信息
        """
        cpuInfokeys = self.cpuInfokeys
        table = 'cpuinfo'
        keys = cpuInfokeys[1:-1]
        value = []
        values = []
        try:
            for key in data.keys():
                info = data[key]
                cpuinfo = info['system']['cpu']
                value.append(info['hostid'])
                for k in keys:
                    value.append(cpuinfo[k])
                value.append(info['time'])
                values.append(tuple(value))
                value = []
        except (IndexError,KeyError,TypeError),error:
            stderr.writelines("Ip:%s,linux cpu info data error:%s\n" %(ipadd,error))
        return  table,cpuInfokeys,values

    def linuxDiskinfo(self,data,ipadd):
        """
        处理硬盘表信息
        """
        diskInfokeys = self.diskInfokeys
        table = 'diskinfo'
        keys = diskInfokeys[1:-1]
        value = []
        values = []
        try:
            for key in data.keys():
                info = data[key]
                diskinfo = info['system']['partition']
                for dev in diskinfo:
                    devinfo = diskinfo[dev]
                    value.append(info['hostid'])
                    for k in keys:
                        value.append(devinfo[k])
                    value.append(info['time'])
                    values.append(tuple(value))
                    value = []
        except (IndexError,KeyError,TypeError),error:
            stderr.writelines("Ip:%s,linux disk info data error:%s\n" %(ipadd,error))
        return table,diskInfokeys,values

    def linuxIoinfo(self,data,ipadd):
        """
        处理io表信息
        """
        ioInfokeys = self.ioInfokeys
        table = 'ioinfo'
        keys = ioInfokeys[1:-1]
        value = []
        values = []
        try:
            for key in data.keys():
                info = data[key]
                ioinfo = info['system']['io']
                for dev in ioinfo:
                    devinfo = ioinfo[dev]
                    value.append(info['hostid'])
                    for k in keys:
                        value.append(devinfo[k])
                    value.append(info['time'])
                    values.append(tuple(value))
                    value = []
        except (IndexError,KeyError,TypeError),error:
            stderr.writelines("Ip:%s,linux io info data error:%s\n" %(ipadd,error))
        return table,ioInfokeys,values

    def linuxLoadinfo(self,data,ipadd):
        """
        处理负载表信息
        """
        loadInfokeys = self.loadInfokeys
        table = 'loadsinfo'
        keys = loadInfokeys[1:-1]
        value = []
        values = []
        try:
            for key in data.keys():
                info = data[key]
                loadinfo = info['system']['uptime']
                value.append(info['hostid'])
                for k in keys:
                    value.append(loadinfo[k])
                value.append(info['time'])
                values.append(tuple(value))
                value = []
        except (IndexError,KeyError,TypeError),error:
            stderr.writelines("Ip:%s,linux load info data error:%s\n" %(ipadd,error))
        return table,loadInfokeys,values

    def linuxMemoryinfo(self,data,ipadd):
        """
        处理内存表信息
        """
        memoryInfokeys = self.memoryInfokeys
        table = 'memoryinfo'
        keys = memoryInfokeys[1:-1]
        value = []
        values = []
        try:
            for key in data.keys():
                info = data[key]
                value.append(info['hostid'])
                mem = info['system']['mem']
                for k in keys:
                    value.append(mem[k])
                value.append(info['time'])
                values.append(tuple(value))
                value = []
        except (IndexError,KeyError,TypeError),error:
            stderr.writelines("Ip:%s,linux mem info data error:%s\n" %(ipadd,error))
        return table,memoryInfokeys,values

    def linuxNetinfo(self,data,ipadd):
        """
        处理网卡表信息
        """
        netInfokeys = self.netInfokeys
        table = 'netinfo'
        keys = netInfokeys[1:-1]
        value = []
        values = []
        try:
            for key in data.keys():
                info = data[key]
                netinfo = info['system']['netCard']
                for dev in netinfo:
                    devinfo = netinfo[dev]
                    value.append(info['hostid'])
                    for k in keys:
                        value.append(devinfo[k])
                    value.append(info['time'])
                    values.append(tuple(value))
                    value = []
        except (IndexError,KeyError,TypeError),error:
            stderr.writelines("Ip:%s,linux net info data error:%s\n" %(ipadd,error))
        return table,netInfokeys,values

    def linuxProcessinfo(self,data,ipadd):
        """
        处理进程表信息
        """
        processInfokeys = self.processInfokeys
        table = 'processinfo'
        keys = processInfokeys[1:-1]
        value = []
        values = []
        try:
            for key in data.keys():
                info = data[key]
                processinfo = info['system']['process']
                value.append(info['hostid'])
                for k in keys:
                    value.append(processinfo[k])
                value.append(info['time'])
                values.append(tuple(value))
                value = []
        except (IndexError,KeyError,TypeError),error:
            stderr.writelines("Ip:%s,linux process info data error:%s\n" %(ipadd,error))
        return table,processInfokeys,values

    def linuxHardwareinfo(self,data,ipadd):
        """
        处理硬件表信息
        """
        hardwareInfokeys = self.hardwareInfokeys
        table = 'hardwareinfo'
        keys = hardwareInfokeys[1:-1]
        value = []
        values = []
        try:
            for key in data.keys():
                info = data[key]
                hardwareinfo = info['hardware']
                if hardwareinfo is None:continue
                value.append(info['hostid'])
                for k in keys:
                    value.append(dumps(hardwareinfo[k]))
                value.append(info['time'])
                values.append(tuple(value))
                value = []
        except (IndexError,KeyError,TypeError),error:
            stderr.writelines("Ip:%s,linux hardware info data error:%s\n" %(ipadd,error))
        return table,hardwareInfokeys,values

datapro = Datapro()
if __name__ == "__main__":
    print "linux"
