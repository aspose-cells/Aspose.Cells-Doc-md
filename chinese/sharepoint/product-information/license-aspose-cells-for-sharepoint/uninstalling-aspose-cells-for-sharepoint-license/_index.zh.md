---
title: 卸载 SharePoint 许可证 Aspose.Cells
type: docs
weight: 30
url: /zh/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}} 

要卸载 Aspose.Cells for SharePoint 许可证，请从服务器控制台使用以下步骤。

{{% /alert %}} 

1. 从场中收回许可证解决方案：
stsadm.exe -o retractsolution -name Aspose.Cells.SharePoint.License.wsp -immediate
1. 执行管理计时器作业以立即完成撤回：
 stsadm.exe -o execadmsvcjobs
1. 等待撤回完成。
您可以使用 Central Administration 检查撤回是否已完成，方法是转到**中央行政**， 然后**操作**和**解决方案管理**.
1. 从 SharePoint 解决方案存储中删除解决方案：
 stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp
