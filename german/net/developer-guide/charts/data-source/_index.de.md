---
title: Legen Sie die Datenquelle für das Diagramm fest
linktitle: Datenquelle
type: docs
weight: 10
url: /de/net/data-formatting-in-charts/
---
In unseren vorherigen Themen haben wir bereits viele Beispiele bereitgestellt, um zu demonstrieren, wie Sie eine Datenquelle für Ihr Diagramm festlegen können, aber in diesem Thema werden wir weitere Details zu den Datentypen bereitstellen, die für ein Diagramm festgelegt werden können.

## **Diagrammdaten einstellen**

Bei der Arbeit an Diagrammen mit Aspose.Cells müssen zwei Arten von Daten wie folgt behandelt werden:

- Diagrammdaten.
- Kategoriedaten.

### **Diagrammdaten**

Diagrammdaten sind die Daten, die wir als Datenquelle zum Erstellen unserer Diagramme verwenden. Wir können einen Bereich der Zellen (mit Diagrammdaten) hinzufügen, indem wir die aufrufen[**SerieSammlung**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) Objekt[**Hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)Methode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **Kategoriedaten**

 Kategoriedaten dienen der Beschriftung von Diagrammdaten und können ergänzt werden[**SerieSammlung**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) durch die Verwendung seiner[**KategorieDaten**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)Eigentum. Ein vollständiges Beispiel ist unten angegeben, um die Verwendung von Diagramm- und Kategoriedaten zu demonstrieren. Nach dem Ausführen des obigen Beispielcodes wird dem Arbeitsblatt ein Säulendiagramm hinzugefügt, wie unten gezeigt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **Themen vorantreiben**
- [Ändern Sie die Datenquelle des Diagramms in das Zielarbeitsblatt, während Sie Zeilen oder einen Bereich kopieren](/cells/de/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Erstellen Sie dynamische Diagramme](/cells/de/net/create-dynamic-charts/)
- [Einfache Methode zum Einrichten von Diagrammen mit der Methode Chart.SetChartDataRange](/cells/de/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Finden Sie den Typ von X- und Y-Werten von Punkten in Diagrammreihen](/cells/de/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
