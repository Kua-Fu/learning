# 1. git 对象模型

## 1.1 表示 
  
      40个字符组成的对象名标识
	  
	  6ff87c4664981e4397625791c8ea3bbb5f2279a3
	  
## 1.2 组成

	每个对象包含3个部分: 类型、大小、内容
	
	大小是指内容的大小
	
	内容取决于对象的类型
	
	类型分为4种：
	
	blob: 存储文件数据，通常是一个文件
	
	tree: 像是一个目录，管理一些tree, blob
	
	commit: 
