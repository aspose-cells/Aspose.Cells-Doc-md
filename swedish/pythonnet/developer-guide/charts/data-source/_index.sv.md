---
title: Ange datakälla för diagrammet
description: Lär dig om de olika datakällor som stöds av Aspose.Cells för Python via .NET. Vår guide går igenom de olika typer av datakällor som finns och visar hur du ansluter och hämtar data från dem för att fylla i dina kalkylblad.
keywords: Aspose.Cells för Python via .NET, diagram, datformatering, etiketter, färger, teckensnitt, utseende, användbarhet.
linktitle: Datakälla
type: docs
weight: 10
url: /sv/python-net/data-formatting-in-charts/
---

I våra tidigare ämnen har vi redan tillhandahållit många exempel för att demonstrera hur man kan ställa in en datakälla för ditt diagram, men i det här ämnet kommer vi att tillhandahålla mer detaljer om vilka typer av data som kan anges för ett diagram.

## **Ställa in Diagramdata**

Det finns två typer av data att hantera när man arbetar med diagram med Aspose.Cells för Python via .NET, enligt följande:

- Diagramdata.
- Kategoridata.

### **Diagramdata**

Diagramdata är den data som vi använder som datakälla för att bygga våra diagram. Vi kan lägga till ett intervall av celler (innehållande diagramdata) genom att ringa [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) objektets [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/add) metod.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsData-1.py" >}}

### **Kategoridata**

Kategoridata används för märkning av diagramdata och kan läggas till i [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) genom att använda dess [**category_data**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/category_data) egenskap. Ett komplett exempel ges nedan för att demonstrera användningen av diagram- och kategoridata. Efter att ha utfört ovanstående exempelkod läggs ett kolumn diagram till i arbetsbladet enligt nedan.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingCategoryData-1.py" >}}

## **Fortsatta ämnen**
- [Ändra datakällan för diagrammet till destinationskalkylbladet samtidigt som du kopierar rader eller område](/cells/sv/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Skapa Dynamiska Diagram](/cells/sv/python-net/create-dynamic-charts/)
- [Enkel metod för diagraminställning med hjälp av Chart.SetChartDataRange-metoden](/cells/sv/python-net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Hitta typ av X- och Y-värden för punkter i diagramserier](/cells/sv/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/)
{{< app/cells/assistant language="python-net" >}}
