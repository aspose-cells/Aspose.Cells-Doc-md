---
title: 安装Aspose.Cells for SharePoint
type: docs
weight: 10
url: /zh/sharepoint/installing-aspose-cells-for-sharepoint/
---

{{% alert color="primary" %}} 

Aspose.Cells for SharePoint可以作为Aspose.Cells.SharePoint.zip压缩包进行下载。 

{{% /alert %}} 
### **压缩包内容**
Aspose.Cells.SharePoint.zip 压缩包包括：

- Aspose.Cells.SharePoint.wsp – SharePoint解决方案文件。Aspose.Cells for SharePoint打包为SharePoint解决方案，以便在服务器农场中方便地进行部署/撤回和特征激活/停用。
- Aspose_LicenseAgreement.rtf – 最终用户许可协议
- Aspose.Cells for SharePoint.pdf – 用户文档
- Aspose.Cells for SharePoint Documentation.chm – 公共API参考的用户文档
- setup.exe – 安装程序
- setup.exe.config – 安装配置文件

安装程序在继续安装前会检查以下条件：

- WSS 3.0、MOSS 2007 或 SharePoint 2010 已安装。
- 用户有权限安装 SharePoint 解决方案。
- SharePoint 数据库在线。
- WSS 管理服务已启动。
- WSS 定时器服务已启动。

WSS 管理服务和定时器服务是必需的，因为一些设置操作依赖于定时作业传播到服务器群中的所有服务器。 
#### **安装Aspose.Cells for SharePoint**
1. 将 Aspose.Cells.SharePoint 压缩包解压到 MOSS 7.0 或 WSS 3.0 服务器的本地驱动器。
1. 运行 setup.exe 并按照屏幕上的说明进行操作。

安装程序执行以下操作：

1. 检查安装先决条件。 如果任何检查失败，安装将不会继续。 

   **系统检查** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_1.png)




1. 显示最终用户许可协议。 用户必须接受协议才能继续。 

   **最终用户许可协议** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_2.png)




1. 显示部署目标选择对话框。 用户选择要激活功能的 Web 应用程序和站点集。 请参阅下图。 

   **部署目标** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_3.png)




1. 将功能部署到服务器群。 

   安装中 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_4.png)




1. 激活选定站点集的功能并配置其父网站应用程序。
1. 显示已部署和激活功能的网站应用程序和站点集的列表。 

   安装完成 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_5.png)
