---
title: Webbutökningar  Office tillägg
type: docs
weight: 120
url: /sv/java/web-extensions-office-add-ins/
---

Webbutökningar utökar Office-applikationer och interagerar med innehållet i Office-dokument. Webbutökningar lägger till ytterligare funktionalitet till Office-klienten för att förbättra användarupplevelsen och produktiviteten.

Aspose.Cells ger också möjligheten att arbeta med webbutökningar.

## **Lägg till webbförlängning**

Du kan lägga till Webbförlängningar (Office-tillägg) i Excel genom att klicka på fliken **Infoga** och sedan klicka på länken **Butik**/**Hämta tillägg**. I fönstret för tillägg, bläddra efter tillägget du vill ha och lägg till det.

Aspose.Cells har också funktionen att lägga till webbförlängningar genom att använda klasserna WebExtension och WebExtensionTaskPane. Följande kodexempel demonstrerar användningen av klasserna WebExtension och WebExtensionTaskPane för att lägga till en webbförlängning till Excel-filen. Vänligen se den genererade [utdatafilen Excel](AddWebExtension_Out.xlsx) för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddWebExtension-1.java" >}}

## **Få tillgång till information om webbförlängning**

Aspose.Cells ger möjlighet att få tillgång till information om webbförlängningar i Excel-filen. Följande kodexempel demonstrerar hur man får tillgång till information om webbförlängning genom att ladda [exempel Excel-filen](WebExtensionsSample.xlsx). Vänligen se konsolens utdata som genereras av koden för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AccessWebExtensionInformation-1.java" >}}

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
{{< app/cells/assistant language="java" >}}
