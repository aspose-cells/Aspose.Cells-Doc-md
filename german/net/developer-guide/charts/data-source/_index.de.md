---
title: Datensatz für das Diagramm festlegen
description: Erfahren Sie mehr über die verschiedenen Datenquellen, die von Aspose.Cells for .NET unterstützt werden. Unser Leitfaden führt Sie durch die verschiedenen Arten von Datenquellen, die verfügbar sind, und zeigt Ihnen, wie Sie sich mit ihnen verbinden und Daten abrufen können, um Ihre Tabellenblätter zu füllen.
keywords: Aspose.Cells for .NET, Diagrammerstellung, Datenformatierung, Beschriftungen, Farben, Schriftarten, Erscheinungsbild, Benutzerfreundlichkeit.
linktitle: Datenquelle
type: docs
weight: 10
url: /de/net/data-formatting-in-charts/
---

In unseren vorherigen Themen haben wir bereits viele Beispiele bereitgestellt, um zu zeigen, wie Sie eine Datenquelle für Ihr Diagramm festlegen können, aber in diesem Thema werden wir detailliertere Informationen über die Arten von Daten bereitstellen, die für ein Diagramm festgelegt werden können.

## **Festlegen von Diagrammdaten**

Es gibt zwei Arten von Daten, mit denen Sie beim Arbeiten an Diagrammen mit Aspose.Cells umgehen können:

- Diagrammdaten.
- Kategoriedaten.

### **Diagrammdaten**

Diagrammdaten sind die Daten, die wir als Datenquelle für unsere Diagramme verwenden. Wir können einen Bereich der Zellen (die Diagrammdaten enthalten) hinzufügen, indem wir die [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)-Methode des Objekts [**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add) aufrufen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **Kategoriedaten**

Kategoriedaten werden zur Beschriftung von Diagrammdaten verwendet und können [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) mithilfe seiner [**CategoryData**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)-Eigenschaft hinzugefügt werden. Ein vollständiges Beispiel ist unten gegeben, um die Verwendung von Diagramm- und Kategoriedaten zu demonstrieren. Nach Ausführung des obigen Beispielcodes wird ein Säulendiagramm zu dem Arbeitsblatt hinzugefügt, wie unten gezeigt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **Erweiterte Themen**
- [Ändern der Datenquelle des Diagramms zur Zieltabelle beim Kopieren von Zeilen oder Bereichen](/cells/de/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Dynamische Diagramme erstellen](/cells/de/net/create-dynamic-charts/)
- [Einfacher Weg zur Diagrammeinrichtung mit der Methode Chart.SetChartDataRange](/cells/de/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Typen von X- und Y-Werten von Punkten in Diagrammserien herausfinden](/cells/de/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
