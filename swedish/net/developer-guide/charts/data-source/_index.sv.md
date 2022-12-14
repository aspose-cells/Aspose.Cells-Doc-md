---
title: Ställ in datakälla för diagrammet
linktitle: Datakälla
type: docs
weight: 10
url: /sv/net/data-formatting-in-charts/
---
våra tidigare ämnen har vi redan gett många exempel för att visa hur du kan ställa in en datakälla för ditt diagram, men i det här ämnet kommer vi att ge mer information om vilka typer av data som kan ställas in för ett diagram.

## **Ställa in diagramdata**

Det finns två typer av data att hantera när du arbetar med diagram med Aspose.Cells enligt följande:

- Diagramdata.
- Kategoridata.

### **Diagramdata**

Diagramdata är den data som vi använder som datakälla för att bygga våra diagram. Vi kan lägga till ett intervall av cellerna (som innehåller diagramdata) genom att anropa[**Seriekollektion**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) objekt[**Lägg till**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)metod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **Kategoridata**

 Kategoridata används för märkning av sjökortsdata och kan läggas till[**Seriekollektion**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) genom att använda dess[**CategoryData**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)fast egendom. Ett komplett exempel ges nedan för att demonstrera användningen av diagram- och kategoridata. Efter exekvering av ovanstående exempelkod kommer ett kolumndiagram att läggas till i kalkylbladet som visas nedan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **Förhandsämnen**
- [Ändra datakälla för diagrammet till målarbetsblad medan du kopierar rader eller intervall](/cells/sv/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Skapa dynamiska diagram](/cells/sv/net/create-dynamic-charts/)
- [Enkelt sätt för diagraminställning med metoden Chart.SetChartDataRange](/cells/sv/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Hitta typ av X- och Y-värden för poäng i diagramserier](/cells/sv/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
