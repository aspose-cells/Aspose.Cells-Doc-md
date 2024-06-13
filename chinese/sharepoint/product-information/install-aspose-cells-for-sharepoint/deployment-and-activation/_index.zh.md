---
title: 部署和激活
type: docs
weight: 20
url: /zh/sharepoint/deployment-and-activation/
---

{{% alert color="primary" %}} 

[安装Aspose.Cells for SharePoint](/cells/zh/sharepoint/installing-aspose-cells-for-sharepoint/)将引导您完成安装过程。本文解释了安装过程是如何部署和激活的。

{{% /alert %}} 
### **部署**
部署期间，Aspose.Cells for SharePoint执行以下操作:

1. 将 **Aspose.Cells.SharePoint.dll** 安装到全局程序集缓存，并将 SafeControl 条目添加到 **web.config** 文件。
1. 将功能清单和其他必要文件安装到适当的目录。
1. 在 SharePoint 数据库中注册功能，并使其在功能范围上可用于激活。
### **激活**
Aspose.Cells for SharePoint打包为站点（站点集）级功能，并可在站点集上进行激活和停用。 

在激活期间，该功能对站点集的父网站应用程序的虚拟目录进行了一些更改：

1. 添加转换设置页面到网站地图文件。
1. 将必要的资源文件复制到虚拟目录中的 App_GlobalResources 文件夹。
