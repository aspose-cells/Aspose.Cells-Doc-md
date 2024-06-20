---
title: Avinstallera Aspose.Cells for SharePoint licens
type: docs
weight: 30
url: /sv/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}} 

För att avinstallera Aspose.Cells for SharePoint licens, använd följande steg från serverns konsol. 

{{% /alert %}} 

1. Dra tillbaka licenslösningen från farmen:
   stsadm.exe -o retractsolution -name Aspose.Cells.SharePoint.License.wsp -immediate
1. Utför administrativa timer-jobb för att slutföra borttagningen omedelbart:
   stsadm.exe -o execadmsvcjobs
1. Vänta tills borttagningen är klar.
   Du kan använda Centraladministrationen för att kontrollera om borttagningen har slutförts genom att gå till **Centraladministrationen**, sedan till **Åtgärder** och **Lösningshantering**.
1. Ta bort lösningen från SharePoint-lösningsslaggen:
   stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp
