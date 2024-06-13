---
title: 安装 Aspose.Cells for SharePoint 许可证
type: docs
weight: 10
url: /zh/sharepoint/installing-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}}

购买 [评估](/cells/zh/sharepoint/evaluate-aspose-cells/) 后，请确保您满意后 [购买许可证](https://purchase.aspose.com/buy)。

购买前，请确保您了解并同意许可证订阅条款。

{{% /alert %}}

订单支付后，许可证将通过电子邮件发送给您。许可证是一个包含常规 SharePoint 解决方案包的 ZIP 存档。

许可证 ZIP 包含如下内容：

- **Aspose.Cells.SharePoint.License.wsp** – SharePoint 解决方案包文件。Aspose.Cells for SharePoint许可证被打包为SharePoint解决方案，以便在服务器群中进行部署和撤消。
- **readme.txt** – 许可证安装说明。许可证安装通过 **stsadm.exe** 从服务器控制台执行。下面给出了安装许可证所需的步骤。

#### **安装许可证**

{{% alert color="primary" %}}

出于清晰起见，省略了路径信息。在执行下面的步骤时，需要添加实际的 **stsadm.exe** 和/或解决方案文件路径。

{{% /alert %}}

1. 运行 stsadm 将解决方案添加到 SharePoint 解决方案存储区：
   stsadm.exe -o addsolution -filename Aspose.Cells.SharePoint.License.wsp
1. 部署解决方案到服务器群中的所有服务器：
   stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. 执行管理计时作业以立即完成部署：
   stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

在运行部署步骤时，如果Windows SharePoint Services Administration服务尚未启动，您将收到警告。**Stsadm.exe**依赖此服务和Windows SharePoint Timer服务，以在整个农场中复制解决方案数据。如果这些服务在您的服务器农场上未运行，则可能需要为每个服务器单独部署许可证。

{{% /alert %}}
