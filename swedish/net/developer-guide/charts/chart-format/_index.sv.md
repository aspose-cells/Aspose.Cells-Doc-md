---
title: Ställa in diagrammets utseende
linktitle: Diagramformat
type: docs
weight: 20
url: /sv/net/setting-chart-appearance/
---
## **Ställa in diagrammets utseende**
I Hur man skapar ett diagram gav vi en kort introduktion till de typer av diagram och diagramobjekt som erbjuds av Aspose.Cells, och beskrev hur man skapar ett. Den här artikeln diskuterar hur du anpassar diagrammets utseende genom att ställa in deras egenskaper:

- Ställa in sjökortsområdet.
- Ställa in diagramlinjer.
- Använda teman.
- Ställa in titlar till diagram och axlar.
- Arbeta med rutnät.
### **Inställning av sjökortsområde**
Det finns olika typer av områden i ett diagram och Aspose.Cells ger flexibiliteten att ändra utseendet på varje område. Utvecklare kan tillämpa olika formateringsinställningar på ett område genom att ändra dess förgrundsfärg, bakgrundsfärg och fyllningsformat etc.

I exemplet nedan har vi tillämpat olika formateringsinställningar på olika typer av områden i ett diagram. Dessa områden inkluderar:

- Tomtområde
- Kartområde
- SeriesCollection område
- Area för en enda punkt i en SeriesCollection

Följande kodavsnitt visar hur man ställer in diagramområdet.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartArea-1.cs" >}}
### **Ställa in sjökortslinjer**
 Utvecklare kan också tillämpa olika typer av stilar på linjerna eller datamarkörerna för[Seriekollektion](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection). Följande kodavsnitt visar hur man ställer in diagramlinjer med Aspose.Cells API.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingChartLines-1.cs" >}}
### **Tillämpa Microsoft Excel 2007/2010-teman på diagram**
 Utvecklare kan tillämpa olika Microsoft Excel-teman/färger på[Seriekollektion](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)eller andra diagramobjekt som visas nedan i exemplet.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ApplyingThemes-1.cs" >}}
### **Ställa in titlar på diagram eller axlar**
Du kan använda Microsoft Excel för att ställa in titlarna på ett diagram och dess axlar i en WYSIWYG-miljö. Aspose.Cells tillåter också utvecklare att ställa in titlarna på ett diagram och dess axlar under körning. Alla diagram och deras axlar innehåller en[Titel](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/title)egenskap som kan användas för att ställa in deras titlar som visas nedan i ett exempel.

Följande kodavsnitt visar hur du ställer in titlar till diagram och axlar.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-SettingTitlesAxes-1.cs" >}}
### **Arbeta med Major Gridlines**
Det är möjligt att anpassa utseendet på större rutnät. Dölj eller visa rutnät, eller definiera deras färg och andra inställningar. Nedan visar vi hur man döljer rutnät och hur man ändrar deras färg.
#### **Döljer stora rutnät**
Utvecklare kan kontrollera synligheten för större rutnät genom att ställa in[Är synlig](https://reference.aspose.com/cells/net/aspose.cells.drawing/line/properties/isvisible) egendom av[Linje](https://reference.aspose.com/cells/net/aspose.cells.drawing/line) protestera mot**Sann** eller**falsk**.

Följande kodavsnitt visar hur man döljer stora rutnät. Efter att ha gömt de stora rutnätslinjerna kommer ett kolumndiagram att läggas till i kalkylbladet som inte har rutnätslinjer.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-MajorGridlines-1.cs" >}}
#### **Ändra större rutnätsinställningar**
Utvecklare kan inte bara kontrollera synligheten för större rutnät utan även andra egenskaper inklusive dess färg etc.

Följande kodavsnitt visar hur man ändrar färgen på de stora rutnätslinjerna. Efter att ha ställt in färgen på de stora rutnätslinjerna kommer ett kolumndiagram att läggas till i kalkylbladet med modifierade rutnätslinjer.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsAppearance-ChangingMajorGridlines-1.cs" >}}

## **Förhandsämnen**
- [Ställ in värdeformatets kod för diagramserien](/cells/sv/net/set-the-values-format-code-of-chart-series/)
- [Ställ in bild som bakgrund Fyll i diagrammet](/cells/sv/net/set-picture-as-background-fill-in-the-chart/)
