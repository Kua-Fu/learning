# 安装git 最新版本

### 参考

	[安装git](https://ehlxr.me/2016/07/30/CentOS-7-%e5%ae%89%e8%a3%85%e6%9c%80%e6%96%b0%e7%9a%84-Git/)

## 1. 查看yum 源仓库中git信息
      
	  yum info git
	  
## 2. 安装依赖库
     
	  yum install curl-devel expat-devel gettext-devel openssl-devel zlib-devel
	  
      yum install  gcc perl-ExtUtils-MakeMaker
	  
	  
## 3. 卸载低版本git
     
	  yum remove git
	  
	  
## 4. 下载安装最新的git源码包
   
      wget https://github.com/git/git/archive/v2.9.2.tar.gz
	  
	  tar -xzvf v2.9.2.tar.gz -C /home
	  
	  cd /home/git-2.9.2
	  
	  make prefix=/usr/local/git all
	  
	  make prefix=/usr/local/git install


## 5. 添加到环境变量

      echo "export PATH=$PATH:/usr/local/git/bin" >> /etc/bashrc
	  
	  source /etc/bashrc # 实时生效
	  

## 6. 查看新的版本号
  
      git --version
