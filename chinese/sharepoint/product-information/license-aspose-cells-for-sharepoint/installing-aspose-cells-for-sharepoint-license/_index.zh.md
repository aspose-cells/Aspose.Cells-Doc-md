---
title: 安装Aspose.Cells for SharePoint许可证
type: docs
weight: 10
url: /zh/sharepoint/installing-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}}

一旦满意您的 [评估](/cells/zh/sharepoint/evaluate-aspose-cells/)，请 [购买许可证](https://purchase.aspose.com/buy)。

购买前，请确保您理解并同意许可证订阅条款。

{{% /alert %}}

订购支付后，许可证将通过电子邮件发送给您。许可证是一个包含常规SharePoint解决方案包的ZIP归档文件。

许可证ZIP包含：

- **Aspose.Cells.SharePoint.License.wsp** – SharePoint解决方案包文件。 Aspose.Cells for SharePoint许可证被打包为SharePoint解决方案，以方便在服务器群中部署和撤消。
- **readme.txt** – 许可证安装说明。许可证安装通过 **stsadm.exe** 从服务器控制台执行。执行以下步骤以安装许可证。

#### **安装许可证**

{{% alert color="primary" %}}

为了清晰起见，路径已被省略。在执行下面的步骤时，请添加实际路径到 **stsadm.exe** 和/或解决方案文件。

{{% /alert %}}

1. 运行stsadm将解决方案添加到SharePoint解决方案存储库:
   stsadm.exe -o addsolution -filename Aspose.Cells.SharePoint.License.wsp
1. 将解决方案部署到农场中的所有服务器:
   stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. 执行管理计时作业以立即完成部署:
   stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

如果Windows SharePoint Services管理服务尚未启动，运行部署步骤时您会收到警告。 **Stsadm.exe** 依赖于此服务和Windows SharePoint定时服务在农场中复制解决方案数据。如果这些服务未在您的服务器农场上运行，您可能需要单独将许可证部署到每台服务器。

{{% /alert %}}
