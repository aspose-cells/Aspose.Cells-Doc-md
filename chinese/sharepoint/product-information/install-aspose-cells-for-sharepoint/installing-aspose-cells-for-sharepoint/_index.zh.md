---
title: 安装Aspose.Cells for SharePoint
type: docs
weight: 10
url: /zh/sharepoint/installing-aspose-cells-for-sharepoint/
---

{{% alert color="primary" %}} 

Aspose.Cells for SharePoint可作为Aspose.Cells.SharePoint.zip存档进行下载。 

{{% /alert %}} 
### **存档内容**
Aspose.Cells.SharePoint.zip存档包含：

- Aspose.Cells.SharePoint.wsp – SharePoint解决方案文件。 Aspose.Cells for SharePoint被打包为SharePoint解决方案，以便跨服务器农场进行部署/撤回和功能的激活/停用。
- Aspose_LicenseAgreement.rtf – 最终用户许可协议
- Aspose.Cells for SharePoint.pdf – 用户文档
- Aspose.Cells for SharePoint Documentation.chm – 具有公共API参考的用户文档
- setup.exe – 安装程序
- setup.exe.config – 设置配置文件

安装程序在继续安装之前检查以下条件：

- 已安装WSS 3.0、MOSS 2007或SharePoint 2010。
- 用户有权限安装SharePoint解决方案。
- SharePoint数据库在线。
- WSS管理服务已启动。
- WSS定时器服务已启动。

WSS管理服务和定时器服务是必需的，因为某些设置操作依赖于定时作业在服务器群中的所有服务器上传播。 
#### **安装Aspose.Cells for SharePoint**
1. 将Aspose.Cells.SharePoint zip解压到MOSS 7.0或WSS 3.0服务器的本地驱动器。
1. 运行setup.exe并按照屏幕上的说明操作。

安装程序执行以下操作：

1. 检查安装先决条件。如果任何检查失败，安装将不会继续。 

   **系统检查** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_1.png)




1. 显示最终用户许可协议。用户必须接受协议才能继续。 

   **最终用户许可协议** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_2.png)




1. 显示部署目标选择对话框。用户选择要激活功能的Web应用程序和站点集。请参见下图。 

   **部署目标** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_3.png)




1. 在服务器群中部署功能。 

   **正在运行安装** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_4.png)




1. 为所选站点集激活功能并配置它们的父Web应用程序。
1. 显示已部署并激活功能的Web应用程序和站点集的列表。 

   **安装完成** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_5.png)
