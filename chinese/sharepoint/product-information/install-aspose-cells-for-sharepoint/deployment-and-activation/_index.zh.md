---
title: 部署和激活
type: docs
weight: 20
url: /zh/sharepoint/deployment-and-activation/
---

{{% alert color="primary" %}} 

[安装Aspose.Cells for SharePoint](/cells/zh/sharepoint/installing-aspose-cells-for-sharepoint/)指导你完成安装过程。本文解释了安装过程是如何部署和激活的。

{{% /alert %}} 
### **部署**
在部署期间，Aspose.Cells for SharePoint执行以下操作：

1. 将**Aspose.Cells.SharePoint.dll**安装到全局程序集缓存中，并在**web.config**文件中添加一个SafeControl条目。
1. 安装功能清单和其他必要文件到适当的目录。
1. 在SharePoint数据库中注册功能，并使其在功能范围处激活。
### **激活**
Aspose.Cells for SharePoint被打包为站点（站点集）级功能，在站点集上可以激活和停用。 

在激活过程中，该功能会对站点集的父Web应用程序的虚拟目录进行一些更改：

1. 将转换设置页面添加到站点地图文件。
1. 将必要的资源文件复制到虚拟目录中的App_GlobalResources文件夹。
