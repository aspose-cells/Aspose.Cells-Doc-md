---
title: Avinstallerar Aspose.Cells för SharePoint-licens
type: docs
weight: 30
url: /sv/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}} 

 För att avinstallera Aspose.Cells för SharePoint-licens, använd stegen nedan från serverkonsolen.

{{% /alert %}} 

1. Dra tillbaka licenslösningen från gården:
stsadm.exe -o retractsolution -namn Aspose.Cells.SharePoint.License.wsp -omedelbar
1. Utför administrativa timerjobb för att slutföra återkallelsen omedelbart:
 stsadm.exe -o execadmsvcjobs
1. Vänta tills indragningen är klar.
 Du kan använda Central Administration för att kontrollera om återkallelsen har slutförts genom att gå till**Centralförvaltningen** , då**Operationer** och**Lösningshantering**.
1. Ta bort lösningen från SharePoint-lösningsarkivet:
 stsadm.exe -o deletesolution -namn Aspose.Cells.SharePoint.License.wsp
