---
title: Datenformatierung in Diagrammen
linktitle: Datenquelle
type: docs
weight: 50
url: /de/java/data-formatting-in-charts/
---
{{% alert color="primary" %}}

In unseren vorherigen Themen haben wir bereits viele Beispiele bereitgestellt, um zu demonstrieren, wie Sie eine Datenquelle für Ihr Diagramm festlegen können, aber in diesem Thema werden wir weitere Details zu den Datentypen bereitstellen, die für ein Diagramm festgelegt werden können.

{{% /alert %}}

## **Diagrammdaten einstellen**

Bei der Arbeit an Diagrammen mit Aspose.Cells müssen zwei Arten von Daten wie folgt behandelt werden:

- [Diagrammdaten](/cells/de/java/data-formatting-in-charts/#chart-data).
- [Kategoriedaten](/cells/de/java/data-formatting-in-charts/#category-data).

### **Diagrammdaten**

 Diagrammdaten sind die Daten, die wir als Datenquelle zum Erstellen unserer Diagramme verwenden. Wir können einen Bereich der Zellen (mit Diagrammdaten) hinzufügen, indem wir die aufrufen[**SerieSammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) Objekt[**Addieren**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add(java.lang.Object)) Methode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **Kategoriedaten**

 Kategoriedaten dienen der Beschriftung von Diagrammdaten und können ergänzt werden[**SerieSammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) durch die Verwendung seiner[**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData)Methode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**Säulendiagramm mit Diagramm- und Kategoriedaten** 

![todo: Bild_alt_Text](data-formatting-in-charts_1.png)

## **Themen vorantreiben**
- [Erstellen Sie dynamische Diagramme](/cells/de/java/create-dynamic-charts/)
- [Einfache Methode zum Einrichten von Diagrammen mit der Methode Chart.setChartDataRange](/cells/de/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Finden Sie den Typ von X- und Y-Werten von Punkten in Diagrammreihen](/cells/de/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [Legen Sie den Werteformatcode der Diagrammreihe fest](/cells/de/java/set-the-values-format-code-of-chart-series/)
