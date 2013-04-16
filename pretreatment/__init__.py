# coding=utf-8
"""

"""

__author__  = 'Shine tong<linuxtong@gmail.com>'
__version__  = "0.1.0"
__date__     = "2013-04-08"
__all__      = ['linuxhost','linuxcpu','linuxdisk','linuxio',
                'linuxload','linuxmem','linuxnet','linuxprocess']

from dataprocessing import datapro


def linuxhost(data,ipadd):
    return datapro.linuxHostinfo(data,ipadd)

def linuxcpu(data,ipadd):
    return datapro.linuxCpuinfo(data,ipadd)

def linuxdisk(data,ipadd):
    return  datapro.linuxDiskinfo(data,ipadd)

def linuxio(data,ipadd):
    return datapro.linuxIoinfo(data,ipadd)

def linuxload(data,ipadd):
    return datapro.linuxLoadinfo(data,ipadd)

def linuxmem(data,ipadd):
    return datapro.linuxMemoryinfo(data,ipadd)

def linuxnet(data,ipadd):
    return datapro.linuxNetinfo(data,ipadd)
def linuxprocess(data,ipadd):
    return datapro.linuxProcessinfo(data,ipadd)

def linuxhardware(data,ipadd):
    return datapro.linuxHardwareinfo(data,ipadd)

def linuxtotal(data,ipadd):
    total = [linuxhost(data,ipadd),linuxcpu(data,ipadd),linuxdisk(data,ipadd),
             linuxio(data,ipadd),linuxload(data,ipadd),linuxmem(data,ipadd),
             linuxnet(data,ipadd),linuxprocess(data,ipadd),linuxhardware(data,ipadd)]
    return total
