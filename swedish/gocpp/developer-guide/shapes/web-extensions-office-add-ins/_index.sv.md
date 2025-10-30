---
title: Webbförlängningar  Office tillägg med Golang via C++
linktitle: Webbutökningar  Office tillägg
type: docs
weight: 130
url: /sv/go-cpp/web-extensions-office-add-ins/
description: Lär dig att lägga till och komma åt webbförlängningar (Office tillägg) i Excel filer med Aspose.Cells med Golang via C++.
---

Webutvidgningar utökar Office-applikationer och interagerar med innehållet i Office-dokument. Webutvidgningar tillför ytterligare funktionalitet till Office-klienter för att förbättra användarupplevelsen och produktiviteten.

Aspose.Cells ger också möjligheten att arbeta med webbutökningar.

## **Lägg till webbförlängning**

Du kan lägga till Webutvidgningar (Office-tillägg) i Excel genom att klicka på fliken **Insätt** och sedan klicka på länken **Butik**/**Hämta tillägg**. I Tilläggsboxen bläddrar du efter det tillägg du vill ha och lägger till det.

Aspose.Cells erbjuder också möjligheten att lägga till Webutvidgningar med hjälp av [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/)- och [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/)-klasserna. Följande kodexempel visar hur man använder [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/)- och [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/)-klasser för att lägga till ett webbutvidgning till en Excel-fil. Se [utdata-Excelfilen](89849869.xlsx) genererad av koden för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns.go" >}}
## **Få tillgång till information om webbförlängning**

Aspose.Cells ger möjligheten att komma åt information om Webutvidgningar i en Excel-fil. Följande kodexempel visar hur man får åtkomst till webbutvidgningsinformation genom att ladda [exempel-Excelfilen](89849870.xlsx). Se den genererade konsolutmatningen för referens.

### **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns-1.go" >}}
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
