# magit 的使用方法

## 1. git 
      
	  1.1 M-x magit-status 查看项目的当前状态
	  
		  在init.el中添加快捷键绑定
		  
		  (global-set-key (kbd "C-x g") 'magit-status)
	  
	  1.2 在显示的项目状态中，tab键可以展开折叠记录
	  
	  1.3 C-h m 可以查看所有的帮助信息
	  
	  1.4 magit-status显示如下信息:
	  
		  head 指向当前分支的最近一次提交
		  
		  merge 远程分支的最近一次提交
		  
		  untracked files 工作区中有，但是没有添加到git 管理
		  
		  unstaged files 在工作区已经修改了，但是没有用git add添加进入staged状态
		  
		  staged changes 用git add变成了 staged状态
		  
		  unpulled commits 
		  
		  unpushed commits
		  
	  1.5 状态变化的快捷键:
	       
	      s -- magit-stage-file -- git add 
		  
		  c -- magit-commit     -- git commit
		  
		  F -- magit-pull       -- git pull
		  
		  P -- magit-push       -- git push
		  
		  
	  
