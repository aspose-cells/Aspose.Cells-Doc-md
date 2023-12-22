---
title: Legen Sie die Datenquelle für das Diagramm fest
description: Erfahren Sie mehr über die verschiedenen Datenquellen, die von Aspose.Cells for .NET unterstützt werden. Unser Leitfaden führt Sie durch die verschiedenen verfügbaren Datenquellentypen und zeigt Ihnen, wie Sie eine Verbindung herstellen und Daten daraus abrufen, um Ihre Arbeitsblätter zu füllen.
keywords: Aspose.Cells for .NET, charting, data formatting, labels, colors, fonts, appearance, usability.
linktitle: Datenquelle
type: docs
weight: 10
url: /de/net/data-formatting-in-charts/
---
In unseren vorherigen Themen haben wir bereits viele Beispiele bereitgestellt, um zu zeigen, wie Sie eine Datenquelle für Ihr Diagramm festlegen können. In diesem Thema werden wir jedoch weitere Einzelheiten zu den Datentypen bereitstellen, die für ein Diagramm festgelegt werden können.

##  **Festlegen von Diagrammdaten**

Bei der Arbeit an Diagrammen mit Aspose.Cells müssen zwei Arten von Daten wie folgt verarbeitet werden:

- Diagrammdaten.
- Kategoriedaten.

###  **Diagrammdaten**

 Diagrammdaten sind die Daten, die wir als Datenquelle zum Erstellen unserer Diagramme verwenden. Wir können einen Bereich von Zellen (die Diagrammdaten enthalten) hinzufügen, indem wir aufrufen[**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) Objekt[**Hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)Methode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

###  **Kategoriedaten**

 Kategoriedaten werden zur Beschriftung von Diagrammdaten verwendet und können ergänzt werden[**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) durch die Verwendung von it[**Kategoriedaten**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)Eigentum. Nachfolgend finden Sie ein vollständiges Beispiel, um die Verwendung von Diagramm- und Kategoriedaten zu veranschaulichen. Nach der Ausführung des obigen Beispielcodes wird dem Arbeitsblatt ein Säulendiagramm hinzugefügt, wie unten gezeigt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

##  **Vorabthemen**
- [Ändern Sie beim Kopieren von Zeilen oder Bereichen die Datenquelle des Diagramms in das Zielarbeitsblatt](/cells/de/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Erstellen Sie dynamische Diagramme](/cells/de/net/create-dynamic-charts/)
- [Einfache Möglichkeit zur Karteneinrichtung mit der Methode Chart.SetChartDataRange](/cells/de/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Finden Sie die Art der X- und Y-Werte von Punkten in Diagrammreihen](/cells/de/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
