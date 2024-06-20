---
title: Datenformatierung in Diagrammen
linktitle: Datenquelle
type: docs
weight: 50
url: /de/java/data-formatting-in-charts/
---

{{% alert color="primary" %}}

In unseren vorherigen Themen haben wir bereits viele Beispiele bereitgestellt, um zu zeigen, wie Sie eine Datenquelle für Ihr Diagramm festlegen können, aber in diesem Thema werden wir detailliertere Informationen über die Arten von Daten bereitstellen, die für ein Diagramm festgelegt werden können.

{{% /alert %}}

## **Festlegen von Diagrammdaten**

Es gibt zwei Arten von Daten, mit denen Sie beim Arbeiten an Diagrammen mit Aspose.Cells umgehen können:

- [Diagrammdaten](/cells/de/java/data-formatting-in-charts/#chart-data).
- [Kategoriendaten](/cells/de/java/data-formatting-in-charts/#category-data).

### **Diagrammdaten**

Diagrammdaten sind die Daten, die wir als Datenquelle für unsere Diagramme verwenden. Wir können einen Bereich der Zellen (die Diagrammdaten enthalten) hinzufügen, indem wir die Methode [**Add**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add(java.lang.Object)) des [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)-Objekts aufrufen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **Kategoriedaten**

Kategoriendaten werden zur Beschriftung von Diagrammdaten verwendet und können durch Verwendung der Methode [**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData) zum [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) hinzugefügt werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**Säulendiagramm mit Diagramm- und Kategoriendaten** 

![todo:image_alt_text](data-formatting-in-charts_1.png)

## **Erweiterte Themen**
- [Dynamische Diagramme erstellen](/cells/de/java/create-dynamic-charts/)
- [Einfacher Weg zur Einrichtung von Diagrammen mit der Methode Chart.setChartDataRange](/cells/de/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Typen von X- und Y-Werten von Punkten in Diagrammserien herausfinden](/cells/de/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [Setzen des Werteformatcodes der Diagrammserie](/cells/de/java/set-the-values-format-code-of-chart-series/)
