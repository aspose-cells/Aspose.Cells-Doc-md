---
title: Datensatz für das Diagramm festlegen
description: Erfahren Sie mehr über die verschiedenen Datenquellen, die von Aspose.Cells für Python via .NET unterstützt werden. Unser Leitfaden zeigt Ihnen die verfügbaren Datentypen und wie Sie sich mit ihnen verbinden und Daten abrufen, um Ihre Arbeitsblätter zu füllen.
keywords: Aspose.Cells für Python via .NET, Diagrammerstellung, Datenformatierung, Labels, Farben, Schriften, Erscheinungsbild, Benutzerfreundlichkeit.
linktitle: Datenquelle
type: docs
weight: 10
url: /de/python-net/data-formatting-in-charts/
---

In unseren vorherigen Themen haben wir bereits viele Beispiele bereitgestellt, um zu zeigen, wie Sie eine Datenquelle für Ihr Diagramm festlegen können, aber in diesem Thema werden wir detailliertere Informationen über die Arten von Daten bereitstellen, die für ein Diagramm festgelegt werden können.

## **Festlegen von Diagrammdaten**

Beim Arbeiten mit Diagrammen in Aspose.Cells für Python via .NET gibt es zwei Arten von Daten, die verarbeitet werden:

- Diagrammdaten.
- Kategoriedaten.

### **Diagrammdaten**

Diagrammdaten sind die Daten, die wir als Datenquelle für unsere Diagramme verwenden. Wir können einen Bereich der Zellen (die Diagrammdaten enthalten) hinzufügen, indem wir die [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)-Methode des Objekts [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/add) aufrufen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsData-1.py" >}}

### **Kategoriedaten**

Kategoriedaten werden zur Beschriftung von Diagrammdaten verwendet und können [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) mithilfe seiner [**category_data**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/category_data)-Eigenschaft hinzugefügt werden. Ein vollständiges Beispiel ist unten gegeben, um die Verwendung von Diagramm- und Kategoriedaten zu demonstrieren. Nach Ausführung des obigen Beispielcodes wird ein Säulendiagramm zu dem Arbeitsblatt hinzugefügt, wie unten gezeigt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingCategoryData-1.py" >}}

## **Erweiterte Themen**
- [Ändern der Datenquelle des Diagramms zur Zieltabelle beim Kopieren von Zeilen oder Bereichen](/cells/de/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Dynamische Diagramme erstellen](/cells/de/python-net/create-dynamic-charts/)
- [Einfacher Weg zur Diagrammeinrichtung mit der Methode Chart.SetChartDataRange](/cells/de/python-net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Typen von X- und Y-Werten von Punkten in Diagrammserien herausfinden](/cells/de/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/)
{{< app/cells/assistant language="python-net" >}}
