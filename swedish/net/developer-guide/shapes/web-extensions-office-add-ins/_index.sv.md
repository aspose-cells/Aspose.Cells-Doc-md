---
title: Webbutökningar  Office tillägg
type: docs
weight: 130
url: /sv/net/web-extensions-office-add-ins/
---

Webbutökningar utökar Office-applikationer och interagerar med innehållet i Office-dokument. Webbutökningar lägger till ytterligare funktionalitet till Office-klienten för att förbättra användarupplevelsen och produktiviteten.

Aspose.Cells ger också möjligheten att arbeta med webbutökningar.

## **Lägg till webbförlängning**

Du kan lägga till webbtillägg (Office-tillägg) i Excel genom att klicka på fliken **Infoga** och sedan klicka på länken **Butik**/**Hämta tillägg**. I Tillägg-rutan bläddrar du efter det tillägg du vill ha och lägger till det.

Aspose.Cells tillhandahåller också funktionen att lägga till webbtillägg genom att använda [**WebExtension**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextension) och [**WebExtensionTaskPane**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextensiontaskpane) klasserna. Följande kodprov demonstrerar användningen av [**WebExtension**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextension) och [**WebExtensionTaskPane**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextensiontaskpane) klasserna för att lägga till ett webbtillägg i Excel-filen. Se den [utmatnings Excel-filen](89849869.xlsx) som genereras av koden som referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddWebExtension-1.cs" >}}

## **Få tillgång till information om webbförlängning**

Aspose.Cells tillhandahåller möjlighet att komma åt information om webbtillägg i Excel-filen. Följande kodprov demonstrerar hur man kommer åt information om webbtillägg genom att ladda den [exempel Excel-filen](89849870.xlsx). Se den genererade konsolutmatningen som referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AccessWebExtensionInformation-1.cs" >}}

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
