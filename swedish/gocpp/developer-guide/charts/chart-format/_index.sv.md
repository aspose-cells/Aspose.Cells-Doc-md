---
title: Ställa in diagramutseende med Golang via C++
linktitle: Diagramformat
description: Lär dig att konfigurera diagramutséendet i Aspose.Cells for C++. Vår guide visar hur du ändrar diagramlayouter, färger, typsnitt och effekter för att skapa det önskade visuella stilen och förbättra dina kalkylblad.
keywords: Aspose.Cells for C++, diagram, diagramutseende, layouter, färger, typsnitt, effekter, kalkylblad.
type: docs
weight: 20
url: /sv/go-cpp/setting-chart-appearance/
---

## **Ställa in diagramens utseende**
I Hur man skapar ett diagram gav vi en kort introduktion till typerna av diagram och diagramobjekt som erbjuds av Aspose.Cells, och beskrev hur man skapar ett. Den här artikeln diskuterar hur man anpassar diagrammens utseende genom att ställa in deras egenskaper:

- Inställning av diagramområdet.
- Inställning av diagramlinjer.
- Tillämpa teman.
- Ställa in titlar på diagram och axlar.
- Arbeta med rutnät.

### **Inställning av diagramområde**
Det finns olika typer av områden i ett diagram och Aspose.Cells ger flexibilitet att modifiera utseendet på varje område. Utvecklare kan tillämpa olika formateringsinställningar på ett område genom att ändra dess förgrundsfärg, bakgrundsfärg och fyllning osv.

I det givna exemplet har vi tillämpat olika formateringsinställningar på olika typer av områden i ett diagram. Dessa områden inkluderar:

- Plotområde
- Diagramområde
- Serieområdesamling
- Område för en enskild punkt i en serieområdesamling

Följande kodsnuttdemonstrerar hur man ställer in diagramområdet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat.go" >}}
### **Inställning av diagramlinjer**
Utvecklare kan också tillämpa olika typer av stilar på linjer eller datapunkter i [SeriesCollection](https://reference.aspose.com/cells/go-cpp/seriescollection/). Följande kodexempel visar hur man ställer in diagramlinjer med Aspose.Cells API.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-1.go" >}}
### **Tillämpning av Microsoft Excel 2007/2010 teman på diagram**
 Utvecklare kan tillämpa olika Microsoft Excel-teman/färger på [SeriesCollection](https://reference.aspose.com/cells/go-cpp/seriescollection/) eller andra diagramobjekt, som visas i exemplet nedan.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-2.go" >}}
### **Inställning av diagram- eller axeltitlar**
Du kan använda Microsoft Excel för att ställa in titlar för ett diagram och dess axlar i en WYSIWYG-miljö. Aspose.Cells tillåter också utvecklare att ställa in titlar för diagram och dess axlar vid körning. Alla diagram och deras axlar innehåller en [Title](https://reference.aspose.com/cells/go-cpp/title/) – egenskap som kan användas för att ställa in deras titlar, som visas i ett exempel.

Följande kodsnutt demonstrerar hur man ställer in titlar på diagram och axlar.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-3.go" >}}
### **Arbeta med stora rutnätlinjer**
Det är möjligt att anpassa utseendet på stora rutnätlinjer. Dölj eller visa rutnätlinjer, eller definiera deras färg och andra inställningar. Nedan visar vi hur man döljer rutnätlinjer och hur man ändrar deras färg.

#### **Dölja stora rutnät**
Utvecklare kan kontrollera synligheten av huvudgridlinjer genom att ställa in [IsVisible](https://reference.aspose.com/cells/go-cpp/line/isvisible/) egenskapen för [Line](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/line/) objektet till **true** eller **false**.

Följande kodsnutt demonstrerar hur man döljer stora rutnätlinjer. Efter att ha dolt de stora rutnätlinjerna kommer ett kolumn- diagram att läggas till i arbetsbladet utan rutnätlinjer.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-4.go" >}}
#### **Ändra inställningar för stora rutnät**
Utvecklare kan inte bara kontrollera synligheten för stora rutnät utan också andra egenskaper inklusive dess färg osv.

Följande kodsnutt demonstrerar hur man ändrar färgen på stora rutnätlinjer. Efter att ha ställt in färgen på stora rutnätlinjer kommer ett kolumn- diagram att läggas till i arbetsbladet med modifierade rutnätlinjer.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartFormat-5.go" >}}
## **Fortsatta ämnen**
- [Ställ in värdenas formatkod för diagramserier](/cells/sv/cpp/set-the-values-format-code-of-chart-series/)
- [Ange bild som bakgrundsfyllning i diagrammet.](/cells/sv/cpp/set-picture-as-background-fill-in-the-chart/)
