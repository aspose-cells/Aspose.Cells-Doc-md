---
title: Dataformatering i diagram
linktitle: Datakälla
type: docs
weight: 50
url: /sv/java/data-formatting-in-charts/
---
{{% alert color="primary" %}}

våra tidigare ämnen har vi redan gett många exempel för att visa hur du kan ställa in en datakälla för ditt diagram, men i det här ämnet kommer vi att ge mer information om vilka typer av data som kan ställas in för ett diagram.

{{% /alert %}}

## **Ställa in diagramdata**

Det finns två typer av data att hantera när du arbetar med diagram med Aspose.Cells enligt följande:

- [Diagramdata](/cells/sv/java/data-formatting-in-charts/#chart-data).
- [Kategoridata](/cells/sv/java/data-formatting-in-charts/#category-data).

### **Diagramdata**

 Diagramdata är den data som vi använder som datakälla för att bygga våra diagram. Vi kan lägga till ett intervall av cellerna (som innehåller diagramdata) genom att anropa[**Seriekollektion**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) objekt[**Lägg till**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add(java.lang.Object)) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **Kategoridata**

 Kategoridata används för märkning av sjökortsdata och kan läggas till[**Seriekollektion**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) genom att använda dess[**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData)metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**Kolumndiagram med diagram & kategoridata** 

![todo:image_alt_text](data-formatting-in-charts_1.png)

## **Förhandsämnen**
- [Skapa dynamiska diagram](/cells/sv/java/create-dynamic-charts/)
- [Enkelt sätt för diagraminställning med metoden Chart.setChartDataRange](/cells/sv/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Hitta typ av X- och Y-värden för poäng i diagramserier](/cells/sv/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [Ställ in värdeformatets kod för diagramserien](/cells/sv/java/set-the-values-format-code-of-chart-series/)
