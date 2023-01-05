---
title: Installerar Aspose.Cells for SharePoint Licens
type: docs
weight: 10
url: /sv/sharepoint/installing-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}}

 När du är nöjd med din[utvärdering](/cells/sv/sharepoint/evaluate-aspose-cells/), [köpa en licens](https://purchase.aspose.com/buy).

Innan du köper, se till att du förstår och godkänner licensvillkoren för prenumeration.

{{% /alert %}}

Licensen mailas till dig när beställningen är betald. Licensen är ett ZIP-arkiv som innehåller ett vanligt SharePoint-lösningspaket.

Licensen ZIP innehåller:

- **Aspose.Cells.SharePoint.License.wsp** – SharePoint-lösningspaketfil. Aspose.Cells for SharePoint-licensen är paketerad som en SharePoint-lösning för att underlätta driftsättning och indragning över serverfarmen.
- **readme.txt**– Installationsanvisningar för licens. Licensinstallation utförs från serverkonsolen via**stsadm.exe**. De steg som krävs för att installera licensen anges nedan.

#### **Installation av licensen**

{{% alert color="primary" %}}

 Vägar utelämnas för tydlighetens skull. Lägg till den faktiska sökvägen till**stsadm.exe** och/eller lösningsfil när du utför stegen nedan.

{{% /alert %}}

1. Kör stsadm för att lägga till lösningen i SharePoint-lösningsarkivet:
 stsadm.exe -o addsolution -filnamn Aspose.Cells.SharePoint.License.wsp
1. Distribuera lösningen på alla servrar i farmen:
 stsadm.exe -o deploysolution -namn Aspose.Cells.SharePoint.License.wsp -immediate -force
1. Utför administrativa timerjobb för att slutföra distributionen omedelbart:
 stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

 Du kommer att få en varning när du kör distributionssteget om administrationstjänsten Windows SharePoint Services inte har startats.**Stsadm.exe**förlitar sig på denna tjänst och Windows SharePoint Timer Service för att replikera lösningsdata över hela gården. Om dessa tjänster inte körs på din serverfarm kan du behöva distribuera licensen separat till varje server.

{{% /alert %}}
