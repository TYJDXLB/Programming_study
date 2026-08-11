# 本文档旨在系统性的展示如何使用git，与GitHub进行关联的相关步骤

## 一、安装git，进行本地全局配置
- 下载地址： https://git-scm.com/downloads
- 使用默认值安装
- 资源管理器内单击鼠标右键选择 `Git Bash Here`
- 输入`git --version` 检查是否安装成功
* 桌面右键 --> 更多 --> "Git Bash Here" 打开命令窗口
* 输入以下代码配置用户名和邮箱(建议写GitHub用户名与邮箱)
```
$ git config --global user.name "用户名"
$ git config --golbal user.email "邮箱地址"
---通过以下代码检验是否配置正确：---
$ git config --global user.name
$ git config --golbal user.email
```




## 二、进行本地全局配置
* 