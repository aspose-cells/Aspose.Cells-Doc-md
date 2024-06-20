---
title: Installera Aspose.Cells for SharePoint licensen
type: docs
weight: 10
url: /sv/sharepoint/installing-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}}

När du är nöjd med din [utvärdering](/cells/sv/sharepoint/evaluate-aspose-cells/), [köp en licens](https://purchase.aspose.com/buy).

Innan du köper, se till att du förstår och godkänner licensprenumerationsvillkoren.

{{% /alert %}}

Licensen skickas till dig när beställningen har betalats. Licensen är en ZIP-arkiv som innehåller en vanlig SharePoint-lösningspaket.

Licens-ZIP innehåller:

- **Aspose.Cells.SharePoint.License.wsp** – SharePoint-lösningspaketfilen. Aspose.Cells for SharePoint-licensen är förpackad som en SharePoint-lösning för att underlätta distribution och tillbakadragande på servergården.
- **readme.txt** – Instruktioner för licensinstallation. Licensinstallationen utförs från serverkonsolen via **stsadm.exe**. De steg som krävs för att installera licensen ges nedan.

#### **Installera licensen**

{{% alert color="primary" %}}

Sökvägar utelämnas av tydlighetsskäl. Lägg till den faktiska sökvägen till **stsadm.exe** och/eller lösningsfilen vid utförandet av stegen nedan.

{{% /alert %}}

1. Kör stsadm för att lägga till lösningen i SharePoint-lösningsslagret:
   stsadm.exe -o addsolution -filename Aspose.Cells.SharePoint.License.wsp
1. Implementera lösningen på alla servrar i farmen:
   stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. Utför administrativa timer-jobb för att slutföra implementeringen omedelbart:
   stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

Du kommer att få en varning när du kör implementeringssteget om Windows SharePoint Services Administration-tjänsten inte har startats. **Stsadm.exe** förlitar sig på denna tjänst och Windows SharePoint Timer Service för att replikera lösningens data över farmen. Om dessa tjänster inte körs på din serverfarm kan du behöva implementera licensen separat på varje server.

{{% /alert %}}
