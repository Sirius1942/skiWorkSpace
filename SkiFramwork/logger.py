#encoding=utf-8
import logging

global logger

def getLogLevel(str):
	if(str=="DEBUG"):
		return logging.DEBUG
	if(str=="INFO"):
		return logging.INFO
	if(str=="WARNING"):
		return logging.WARNING
	if(str=="ERROR"):
		return logging.ERROR
	if(str=="CRITICAL"):
		return logging.CRITICAL	

def getlogger(livel,lfname):

	log = logging.getLogger('dp')
	log.setLevel(getLogLevel(livel))

	# 创建一个handler，用于写入日志文件
	fh = logging.FileHandler(lfname)
	fh.setLevel(logging.DEBUG)

	# 再创建一个handler，用于输出到控制台
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)

	# 定义handler的输出格式
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	fh.setFormatter(formatter)
	ch.setFormatter(formatter)

	# 给logger添加handler
	log.addHandler(fh)
	log.addHandler(ch)
	
	return log