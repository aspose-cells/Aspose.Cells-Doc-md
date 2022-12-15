---
title: Installerar Aspose.Cells for SharePoint
type: docs
weight: 10
url: /sv/sharepoint/installing-aspose-cells-for-sharepoint/
---
{{% alert color="primary" %}} 

Aspose.Cells for SharePoint är nedladdningsbart som Aspose.Cells.SharePoint.zip-arkivet.

{{% /alert %}} 
### **Arkivinnehåll**
Arkivet Aspose.Cells.SharePoint.zip innehåller:

- Aspose.Cells.SharePoint.wsp – SharePoint-lösningsfil. Aspose.Cells for SharePoint är paketerad som en SharePoint-lösning för att underlätta driftsättning/återdragning och funktionsaktivering/deaktivering över serverfarmen.
- Aspose_LicenseAgreement.rtf – Slutanvändarlicensavtal
- Aspose.Cells for SharePoint.pdf – Användardokumentation
- Aspose.Cells for SharePoint Documentation.chm – Användardokumentation med offentlig referens API
- setup.exe – installationsprogram
- setup.exe.config – Installationskonfigurationsfil

Installationsprogrammet kontrollerar följande villkor innan du fortsätter med installationen:

- WSS 3.0, MOSS 2007 eller SharePoint 2010 är installerat.
- Användaren har behörighet att installera SharePoint-lösningar.
- SharePoint-databasen är online.
- WSS Administrationstjänst startas.
- WSS Timer-tjänst startas.

WSS Administrationstjänst och Timertjänst behövs eftersom vissa installationsåtgärder förlitar sig på ett timerjobb för att spridas till alla servrar i serverfarmen.
#### **För att installera Aspose.Cells for SharePoint**
1. Packa upp Aspose.Cells.SharePoint zip till den lokala enheten på MOSS 7.0- eller WSS 3.0-servern.
1. Kör setup.exe och följ instruktionerna på skärmen.

Installationsprogrammet utför följande åtgärder:

1.  Kontrollera installationsförutsättningarna. Installationen fortsätter inte om någon kontroll misslyckas.

   **Systemkontroll** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_1.png)




1.  Visa slutanvändarlicensavtal. Användaren måste acceptera avtalet för att kunna fortsätta.

   **EULA** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_2.png)




1.  Visa dialogrutan för val av distributionsmål. Användaren väljer webbapplikationer och webbplatssamlingar där funktionen ska aktiveras. Se figuren nedan.

   **Utbyggnadsmål** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_3.png)




1.  Distribuera funktionen till serverfarmen.

   **Kör installation** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_4.png)




1. Aktivera funktionen för de valda webbplatssamlingarna och konfigurera deras överordnade webbapplikationer.
1. Visa en lista över webbapplikationer och webbplatssamlingar där funktionen har distribuerats och aktiverats.

   **Installationen är klar** 

![todo:image_alt_text](installing-aspose-cells-for-sharepoint_5.png)
