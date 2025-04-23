---
title: Dataformatering i Diagram
linktitle: Datakälla
type: docs
weight: 50
url: /sv/java/data-formatting-in-charts/
---

{{% alert color="primary" %}}

I våra tidigare ämnen har vi redan tillhandahållit många exempel för att demonstrera hur man kan ställa in en datakälla för ditt diagram, men i det här ämnet kommer vi att tillhandahålla mer detaljer om vilka typer av data som kan anges för ett diagram.

{{% /alert %}}

## **Ställa in Diagramdata**

Det finns två typer av data att hantera när man arbetar med diagram med hjälp av Aspose.Cells som följer:

- [Diagramdata](/cells/sv/java/dataformatering-i-diagram/#diagramdata).
- [Kategoridata](/cells/sv/java/dataformatering-i-diagram/#kategoridata).

### **Diagramdata**

Diagramdata är den data som används som datakälla för att bygga våra diagram. Vi kan lägga till ett intervall av celler (innehållande diagramdata) genom att använda objektets [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **Kategoridata**

Kategoridata används för etikettering av diagramdata och kan läggas till i [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) genom att använda dess [**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**Kolumn diagram med diagram & kategoridata** 

![todo:image_alt_text](data-formatting-in-charts_1.png)

## **Fortsatta ämnen**
- [Skapa Dynamiska Diagram](/cells/sv/java/create-dynamic-charts/)
- [Enkel väg för diagramuppställning genom att använda Chart.setChartDataRange metoden](/cells/sv/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Hitta typ av X- och Y-värden för punkter i diagramserier](/cells/sv/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [Ställ in värdenas formatkod för diagramserier](/cells/sv/java/set-the-values-format-code-of-chart-series/)
{{< app/cells/assistant language="java" >}}
