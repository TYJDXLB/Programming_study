# 本文档旨在系统性的展示如何使用git与GitHub进行关联的相关步骤(详细内容参考git_study.md文件)

## 一、安装git，进行本地全局配置
- 下载地址： https://git-scm.com/downloads
- 使用默认值安装
- 资源管理器内单击鼠标右键选择 `Git Bash Here`
- 输入`git --version` 检查是否安装成功
* 桌面右键 --> 更多 --> "Git Bash Here" 打开命令窗口
* 输入以下代码配置用户名和邮箱(建议写GitHub用户名与邮箱)
```
git config --global user.name "用户名"
git config --golbal user.email "邮箱地址"
---通过以下代码检验是否配置正确：---
git config --global user.name
git config --golbal user.email
```

## 二、创建并初始化本地仓库
> 可在git界面使用 `$ mkdir 文件夹名称` 创建新的文件夹  
> 可以再窗口使用 `cd 文件夹名称` 进入目录，或者在目录界面"Git Bash Here"打开命令窗口
- 初始化git仓库 `git init` (创建一个新的本地git仓库，完成后文件夹中会出现一个.git文件夹)

## 三、检查主分支名称
> 由于旧版git主分支名称为master，新版GitHub主分支名称为main。因此要更改本地仓库主分支名称
- 重命名本地分支
```
git branch -m master main
```
- 设置Git全局默认分支名称(以后新建都为main)
```
git config --global init.defaultBranch main
```

## 四、与线上GitHub仓库进行配对(用HTTP通信)
- 查看是否已关联远程仓库：`git remote` 若无输出则尚未关联任何仓库
- 添加远程仓库：(地址在GitHub中Code里面HTTP选项中)
```
git remote add 仓库别名 仓库地址
```
- 使用 `git remote` 验证是否关联成功
- 首次推送并建立跟踪关系：(后续可直接使用git push/pull)
```
git push -u 仓库别名 分支名称(一般为master)
```
