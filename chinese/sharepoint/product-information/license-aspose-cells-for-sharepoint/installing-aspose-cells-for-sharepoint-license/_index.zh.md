---
title: 安装 Aspose.Cells for SharePoint 许可证
type: docs
weight: 10
url: /zh/sharepoint/installing-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}}

一旦你满意你的[评估](/cells/zh/sharepoint/evaluate-aspose-cells/), [购买许可证](https://purchase.aspose.com/buy).

购买前，请确保您了解并同意许可订阅条款。

{{% /alert %}}

订单付款后，许可证将通过电子邮件发送给您。该许可证是一个包含常规 SharePoint 解决方案包的 ZIP 存档。

许可证 ZIP 包含：

- **Aspose.Cells.SharePoint.License.wsp** – SharePoint 解决方案包文件。 Aspose.Cells for SharePoint 许可证被打包为 SharePoint 解决方案，以方便跨服务器场的部署和收回。
- **自述文件.txt**– 许可证安装说明。许可证安装是通过服务器控制台执行的**stsadm.exe**.安装许可证所需的步骤如下。

#### **安装许可证**

{{% alert color="primary" %}}

为清楚起见，省略了路径。将实际路径添加到**stsadm.exe**和/或执行以下步骤时的解决方案文件。

{{% /alert %}}

1. 运行 stsadm 以将解决方案添加到 SharePoint 解决方案存储区：
 stsadm.exe -o addsolution -文件名 Aspose.Cells.SharePoint.License.wsp
1. 将解决方案部署到场中的所有服务器：
 stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. 执行管理计时器作业以立即完成部署：
 stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

如果 Windows SharePoint Services Administration 服务尚未启动，您将在运行部署步骤时收到警告。**Stsadm.exe**依赖此服务和 Windows SharePoint Timer Service 在服务器场中复制解决方案数据。如果这些服务未在您的服务器场上运行，您可能需要将许可证单独部署到每台服务器。

{{% /alert %}}
