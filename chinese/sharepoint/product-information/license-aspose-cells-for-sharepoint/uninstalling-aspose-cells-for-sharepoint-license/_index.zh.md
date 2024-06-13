---
title: 卸载 Aspose.Cells for SharePoint 许可证
type: docs
weight: 30
url: /zh/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}} 

要卸载 Aspose.Cells for SharePoint 许可证，请从服务器控制台中使用以下步骤。 

{{% /alert %}} 

1. 从农场中撤消许可证解决方案:
   stsadm.exe -o retractsolution -name Aspose.Cells.SharePoint.License.wsp -immediate
1. 执行管理定时作业以立即完成撤消:
   stsadm.exe -o execadmsvcjobs
1. 等待撤消完成。
   您可以使用中央管理来检查撤消是否完成，方法是转到**中央管理**，然后选择**运营**和**解决方案管理**。
1. 从SharePoint解决方案存储库中移除解决方案:
   stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp
