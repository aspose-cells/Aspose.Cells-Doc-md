---
title: Webbutökningar  Office tillägg
type: docs
weight: 130
url: /sv/python-net/web-extensions-office-add-ins/
---

Webbutökningar utökar Office-applikationer och interagerar med innehållet i Office-dokument. Webbutökningar lägger till ytterligare funktionalitet till Office-klienten för att förbättra användarupplevelsen och produktiviteten.

Aspose.Cells för Python via .NET ger också möjlighet att arbeta med Web Extensions.

## **Lägg till webbförlängning**

Du kan lägga till webbtillägg (Office-tillägg) i Excel genom att klicka på fliken **Infoga** och sedan klicka på länken **Butik**/**Hämta tillägg**. I Tillägg-rutan bläddrar du efter det tillägg du vill ha och lägger till det.

Aspose.Cells för Python via .NET ger också möjlighet att lägga till Web Extensions med hjälp av klasserna [**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension) och [**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane). Följande kodexempel visar användningen av klasserna [**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension) och [**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane) för att lägga till en webbtillägg till Excel-filen. Se gärna [utdata Excel-fil](89849869.xlsx) som genererats av koden för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AddWebExtension-1.py" >}}

## **Få tillgång till information om webbförlängning**

Aspose.Cells för Python via .NET ger tillgång till information om Web Extensions i en Excel-fil. Följande kodexempel visar hur man hämtar information om webbtillägg genom att ladda [prov-excelfilen](89849870.xlsx). Se gärna konsolutmatningen som genereras av koden för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AccessWebExtensionInformation-1.py" >}}

### **Konsoloutput**

{{< highlight java >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}
