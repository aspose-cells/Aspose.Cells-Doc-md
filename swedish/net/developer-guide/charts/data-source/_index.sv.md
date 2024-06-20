---
title: Ange datakälla för diagrammet
description: Lär dig om de olika datakällor som stöds av Aspose.Cells for .NET. Vår guide kommer att lotsa dig genom de olika typerna av datakällor som är tillgängliga och visa dig hur du ansluter till dem och hämtar data från dem för att fylla dina arbetsblad.
keywords: Aspose.Cells for .NET, diagram, dataformatering, etiketter, färger, typsnitt, utseende, användbarhet.
linktitle: Datakälla
type: docs
weight: 10
url: /sv/net/data-formatting-in-charts/
---

I våra tidigare ämnen har vi redan tillhandahållit många exempel för att demonstrera hur man kan ställa in en datakälla för ditt diagram, men i det här ämnet kommer vi att tillhandahålla mer detaljer om vilka typer av data som kan anges för ett diagram.

## **Ställa in Diagramdata**

Det finns två typer av data att hantera när man arbetar med diagram med hjälp av Aspose.Cells som följer:

- Diagramdata.
- Kategoridata.

### **Diagramdata**

Diagramdata är den data som vi använder som datakälla för att bygga våra diagram. Vi kan lägga till ett intervall av celler (innehållande diagramdata) genom att ringa [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) objektets [**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add) metod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **Kategoridata**

Kategoridata används för märkning av diagramdata och kan läggas till i [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) genom att använda dess [**CategoryData**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata) egenskap. Ett komplett exempel ges nedan för att demonstrera användningen av diagram- och kategoridata. Efter att ha utfört ovanstående exempelkod läggs ett kolumn diagram till i arbetsbladet enligt nedan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **Fortsatta ämnen**
- [Ändra datakällan för diagrammet till destinationskalkylbladet samtidigt som du kopierar rader eller område](/cells/sv/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Skapa Dynamiska Diagram](/cells/sv/net/create-dynamic-charts/)
- [Enkel metod för diagraminställning med hjälp av Chart.SetChartDataRange-metoden](/cells/sv/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Hitta typ av X- och Y-värden för punkter i diagramserier](/cells/sv/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
