---
title: 部署和激活
type: docs
weight: 20
url: /zh/sharepoint/deployment-and-activation/
---
{{% alert color="primary" %}} 

[为 SharePoint 安装 Aspose.Cells](/cells/zh/sharepoint/installing-aspose-cells-for-sharepoint/)引导您完成安装过程。本文介绍了部署和激活的安装过程。

{{% /alert %}} 
### **部署**
Aspose.Cells for SharePoint 在部署期间执行以下操作：

1. 安装**Aspose.Cells.SharePoint.dll**进入全局程序集缓存并添加一个 SafeControl 条目到**配置文件**文件。
1. 将功能清单和其他必要文件安装到适当的目录。
1. 在 SharePoint 数据库中注册功能并使其可用于在功能范围内激活。
### **激活**
Aspose.Cells for SharePoint 打包为网站（网站集）级别的功能，可以在网站集上激活和停用。

在激活期间，该功能会对网站集的父 Web 应用程序的虚拟目录进行一些更改：

1. 将转换设置页面添加到站点地图文件。
1. 将必要的资源文件复制到虚拟目录中的 App_GlobalResources 文件夹。
