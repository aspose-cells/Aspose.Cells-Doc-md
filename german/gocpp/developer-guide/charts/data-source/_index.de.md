---
title: Datenquelle für das Diagramm mit Golang über C++ festlegen
linktitle: Datenquelle
type: docs
weight: 10
url: /de/go-cpp/data-formatting-in-charts/
description: Erfahren Sie mehr über die verschiedenen Datenquellen, die von Aspose.Cells for C++ unterstützt werden. Unser Leitfaden führt Sie durch die verfügbaren Datentypen und zeigt, wie Sie eine Verbindung herstellen und Daten daraus abrufen, um Ihre Arbeitsblätter zu füllen.
keywords: Aspose.Cells for C++, Diagrammerstellung, Datenformatierung, Labels, Farben, Schriftarten, Erscheinungsbild, Benutzerfreundlichkeit.
---

In unseren vorherigen Themen haben wir bereits viele Beispiele gezeigt, um zu demonstrieren, wie Sie eine Datenquelle für Ihr Diagramm festlegen können. In diesem Thema werden wir weitere Details zu den Arten von Daten bereitstellen, die für ein Diagramm festgelegt werden können.

## **Festlegen von Diagrammdaten**

Es gibt zwei Arten von Daten, mit denen Sie beim Arbeiten an Diagrammen mit Aspose.Cells umgehen können:

- Diagrammdaten.
- Kategoriedaten.

### **Diagrammdaten**

Diagrammdaten sind die Daten, die wir als Datenquelle für unsere Diagramme verwenden. Wir können einen Bereich der Zellen (die Diagrammdaten enthalten) hinzufügen, indem wir die [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/)-Methode des Objekts [**Add**](https://reference.aspose.com/cells/go-cpp/seriescollection/add/) aufrufen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource.go" >}}
### **Kategoriedaten**

Kategoriedaten werden zur Beschriftung von Diagrammdaten verwendet und können [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/) mithilfe seiner [**GetCategoryData()**](https://reference.aspose.com/cells/go-cpp/seriescollection/getcategorydata/)-Eigenschaft hinzugefügt werden. Ein vollständiges Beispiel ist unten gegeben, um die Verwendung von Diagramm- und Kategoriedaten zu demonstrieren. Nach Ausführung des obigen Beispielcodes wird ein Säulendiagramm zu dem Arbeitsblatt hinzugefügt, wie unten gezeigt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource-1.go" >}}
## **Fortgeschrittene Themen**
- [Ändern der Datenquelle des Diagramms zur Zieltabelle beim Kopieren von Zeilen oder Bereichen](/cells/de/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Dynamische Diagramme erstellen](/cells/de/cpp/create-dynamic-charts/)
- [Einfacher Weg zur Diagrammeinrichtung mit der Methode Chart.SetChartDataRange](/cells/de/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Typen von X- und Y-Werten von Punkten in Diagrammserien herausfinden](/cells/de/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
