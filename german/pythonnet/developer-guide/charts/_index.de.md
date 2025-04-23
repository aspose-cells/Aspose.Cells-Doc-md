---
title: Diagramm erstellen und verwalten
description: Erfahren Sie, wie Sie mit Aspose.Cells für Python via .NET Diagramme in Microsoft Excel erstellen. Unser Leitfaden zeigt die verschiedenen Arten von Diagrammen, die erstellt werden können, sowie wie man ihr Erscheinungsbild und ihre Formatierung anpasst.
keywords: Aspose.Cells für Python via .NET, Diagrammerstellung, Microsoft Excel, Diagrammtypen, Anpassung, Aussehen, Formatierung.
linktitle: Diagramme
type: docs
weight: 130
url: /de/python-net/creating-charts/
description: Erstellen Sie ein Diagramm in CSharp für Excel und ODS Dateien.
keywords: Erstellen Sie ein Diagramm, erstellen Sie ein Diagramm 
---

{{% alert color="primary" %}}

Es ist möglich, eine Vielzahl von Diagrammen in Tabellen mit Aspose.Cells für Python via .NET hinzuzufügen. Aspose.Cells für Python via .NET bietet viele flexible Diagrammobjekte. Dieser Abschnitt behandelt die Diagrammobjekte von Aspose.Cells.

{{% /alert %}}

## **Erstellen von Diagrammen**

### **Einfaches Erstellen eines Diagramms**
Es ist einfach, mit Aspose.Cells für Python via .NET ein Diagramm zu erstellen, mit den folgenden Beispielcodes:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateColumnChart-1.py" >}}

### **Dinge, die beim Erstellen eines Diagramms zu beachten sind**

Bevor Sie Diagramme erstellen, ist es wichtig, einige grundlegende Konzepte zu verstehen, die beim Erstellen von Diagrammen mit Aspose.Cells für Python via .NET hilfreich sind.

#### **Diagrammobjekte**

Aspose.Cells für Python via .NET stellt eine spezielle Gruppe von Klassen im namespace [**Aspose.Cells.Charts**](https://reference.aspose.com/cells/python-net/aspose.cells.charts) bereit, die zum Erstellen der von Aspose.Cells für Python via .NET unterstützten Diagramme verwendet werden. Diese Klassen dienen zur Erstellung von **Diagramm-Objekten**, die die Bausteine des Diagramms sind. Die Diagramm-Objekte sind unten aufgeführt:

- Serie, eine einzelne Datenreihe in einem Diagramm.
- Achse, die Achse eines Diagramms.
- Diagramm, ein einzelnes Excel-Diagramm.
- Diagrammbereich, der Diagrammbereich im Arbeitsblatt.
- Diagrammdaten Tabelle, eine Diagrammdatentabelle.
- Diagrammrahmen, das Rahmenobjekt in einem Diagramm.
- Diagrammpunkt, ein einzelner Punkt in einer Serie in einem Diagramm.
- Diagrammpunktsammlung, eine Sammlung, die alle Punkte in einer Serie enthält.
- Diagramme, eine Sammlung von Diagrammobjekten.
- Datenbeschriftungen, eine Sammlung aller Datenbeschriftungsobjekte für die angegebene Serie.
- Füllformat, Füllformat für eine Form.
- Boden, der Boden eines 3D-Diagramms.
- Legende, die Diagrammlegende.
- Linie, die Diagrammlinie.
- Seriensammlung, eine Sammlung von Serienobjekten.
- Achsenbeschriftungen, die Achsenbeschriftungen, die mit den Achsenmarkierungen auf einer Diagrammachse verbunden sind.
- Titel, der Titel eines Diagramms oder einer Achse.
- Trendlinie, eine Trendlinie in einem Diagramm.
- Trendliniensammlung, eine Sammlung aller Trendlinienobjekte für die angegebene Datenserie.
- Wände, die Wände eines 3D-Diagramms.

#### **Verwendung von Diagrammobjekten**

Wie oben erwähnt, sind alle Diagrammobjekte Instanzen ihrer jeweiligen Klassen und bieten spezifische Eigenschaften und Methoden zur Ausführung bestimmter Aufgaben. Verwenden Sie Diagrammobjekte, um Diagramme zu erstellen.

Fügen Sie mit der [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/charts)-Sammlung eine beliebige Art von Diagramm zu einem Arbeitsblatt hinzu. Jedes Element in der [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/charts)-Sammlung stellt ein [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart)-Objekt dar. Ein [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart)-Objekt umschließt alle anderen Diagrammobjekte, die erforderlich sind, um das Aussehen des Diagramms anzupassen. Im nächsten Abschnitt wird gezeigt, wie man einige grundlegende Diagrammobjekte verwendet, um ein einfaches Diagramm zu erstellen.

### **Diagramm mit Aspose.Cells für Python via .NET erstellen**

**Schritte:**

1. Fügen Sie einige Daten zu Arbeitsblattzellen mit der [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell)-Methode des Objekts [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value) hinzu.
   Dies wird als Datenquelle für das Diagramm verwendet.
1. Fügen Sie ein Diagramm zu Arbeitsblatt hinzu, indem Sie die [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartcollection)-Methode der Sammlung aufrufen, die im [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Objekt eingeschlossen ist.
1. Geben Sie mit der [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype)-Aufzählung den Diagrammtyp an.
   Beispielsweise verwendet das untenstehende Beispiel den Wert [**ChartType.PYRAMID**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype/) als Diagrammtyp.
1. Greifen Sie über die Indexübergabe auf das neue [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart)-Objekt aus der [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartcollection)-Sammlung zu.
1. Verwenden Sie eines der im [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart)-Objekt eingeschlossenen Diagrammobjekte, um das Diagramm zu verwalten.
   Das untenstehende Beispiel verwendet das [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)-Diagrammobjekt, um die Datenquelle des Diagramms anzugeben.

Beim Hinzufügen von Quelldaten zum Diagramm kann die Datenquelle ein Zellenbereich (z. B. "A1:C3") oder eine Sequenz von nicht zusammenhängenden Zellen (z. B. "A1, A3, A5") oder eine Sequenz von Werten (z. B. "1,2,3") sein.

Diese allgemeinen Schritte ermöglichen es Ihnen, beliebige Arten von Diagrammen zu erstellen. Verwenden Sie verschiedene Diagrammobjekte, um verschiedene Diagramme zu erstellen.

Es ist möglich, viele verschiedene Diagrammtypen mit Aspose.Cells für Python via .NET zu erstellen. Alle von Aspose.Cells für Python via .NET unterstützten Standarddiagramme sind in einer Enumeration namens [**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) vordefiniert.

Die vordefinierten Diagrammtypen sind:

|**Diagrammtypen**|**Beschreibung**|
| :- | :- |
|Column|Stellt gruppiertes Säulendiagramm dar|
|ColumnStacked|Stellt gestapeltes Säulendiagramm dar|
|Column100PercentStacked|Stellt zu 100 % gestapeltes Säulendiagramm dar|
|Column3DClustered|Stellt 3D-gruppiertes Säulendiagramm dar|
|Column3DStacked|Stellt 3D-gestapeltes Säulendiagramm dar|
|Column3D100PercentStacked|Stellt 3D-100%-gestapeltes Säulendiagramm dar|
|Column3D|Stellt 3D-Säulendiagramm dar|
|Bar|Stellt gestapeltes Balkendiagramm dar|
|BarStacked|Stellt gestapeltes Balkendiagramm dar|
|Bar100PercentStacked|Stellt 100%-gestapeltes Balkendiagramm dar|
|Bar3DClustered|Stellt 3D-gruppiertes Balkendiagramm dar|
|Bar3DStacked|Stellt 3D-gestapeltes Balkendiagramm dar|
|Bar3D100PercentStacked|Stellt 3D-100%-gestapeltes Balkendiagramm dar|
|Line|Stellt Liniendiagramm dar|
|LineStacked|Stellt gestapeltes Liniendiagramm dar|
|Line100PercentStacked|Stellt 100%-gestapeltes Liniendiagramm dar|
|LineWithDataMarkers|Stellt Liniendiagramm mit Datenmarkierungen dar|
|LineStackedWithDataMarkers|Stellt gestapeltes Liniendiagramm mit Datenmarkierungen dar|
|Line100PercentStackedWithDataMarkers|Stellt 100%-gestapeltes Liniendiagramm mit Datenmarkierungen dar|
|Line3D|Stellt 3D-Liniendiagramm dar|
|Pie|Stellt Tortendiagramm dar|
|Pie3D|Stellt 3D-Tortendiagramm dar|
|PiePie|Stellt Tortendiagramm von Tortendiagramm dar|
|PieExploded|Stellt explodiertes Tortendiagramm dar|
|Pie3DExploded|Stellt ein 3D-Sprengkuchendiagramm dar|
|PieBar|Stellt Balken eines Kuchendiagramms dar|
|Scatter|Stellt ein Scatter-Diagramm dar|
|ScatterConnectedByCurvesWithDataMarker|Stellt ein Scatter-Diagramm dar, das durch Kurven verbunden ist, mit Datenmarkierungen|
|ScatterConnectedByCurvesWithoutDataMarker|Stellt ein Scatter-Diagramm dar, das durch Kurven verbunden ist, ohne Datenmarkierungen|
|ScatterConnectedByLinesWithDataMarker|Stellt ein Scatter-Diagramm dar, das durch Linien verbunden ist, mit Datenmarkierungen|
|ScatterConnectedByLinesWithoutDataMarker|Stellt ein Scatter-Diagramm dar, das durch Linien verbunden ist, ohne Datenmarkierungen|
|Area|Stellt ein Flächendiagramm dar|
|AreaStacked|Stellt ein gestapeltes Flächendiagramm dar|
|Area100PercentStacked|Stellt ein 100 % gestapeltes Flächendiagramm dar|
|Area3D|Stellt ein 3D-Flächendiagramm dar|
|Area3DStacked|Stellt ein 3D-gestapeltes Flächendiagramm dar|
|Area3D100PercentStacked|Stellt ein 3D-100 %-gestapeltes Flächendiagramm dar|
|Doughnut|Stellt ein Doughnut-Diagramm dar|
|DoughnutExploded|Stellt ein explodiertes Doughnut-Diagramm dar|
|Radar|Stellt ein Radar-Diagramm dar|
|RadarWithDataMarkers|Stellt ein Radar-Diagramm mit Datenmarkierungen dar|
|RadarFilled|Stellt ein gefülltes Radar-Diagramm dar|
|Surface3D|Stellt ein 3D-Oberflächendiagramm dar|
|SurfaceWireframe3D|Stellt ein drahtgerahmtes 3D-Oberflächendiagramm dar|
|SurfaceContour|Stellt Konturdiagramm dar|
|SurfaceContourWireframe|Stellt Drahtgitter-Konturdiagramm dar|
|Bubble|Stellt Blasendiagramm dar|
|Bubble3D|Stellt 3D-Blasendiagramm dar|
|Cylinder|Stellt Zylinderdiagramm dar|
|CylinderStacked|Stellt gestapeltes Zylinderdiagramm dar|
|Cylinder100PercentStacked|Stellt 100 % gestapeltes Zylinderdiagramm dar|
|CylindericalBar|Stellt zylindrisches Balkendiagramm dar|
|CylindericalBarStacked|Stellt gestapeltes zylindrisches Balkendiagramm dar|
|CylindericalBar100PercentStacked|Stellt 100 % gestapeltes zylindrisches Balkendiagramm dar|
|CylindericalColumn3D|Stellt 3D-Säulendiagramm dar|
|Cone|Stellt Kegeldiagramm dar|
|ConeStacked|Stellt gestapeltes Kegeldiagramm dar|
|Cone100PercentStacked|Stellt 100 % gestapeltes Kegeldiagramm dar|
|ConicalBar|Stellt konisches Balkendiagramm dar|
|ConicalBarStacked|Stellt gestapeltes konisches Balkendiagramm dar|
|ConicalBar100PercentStacked|Stellt 100 % gestapeltes konisches Balkendiagramm dar|
|ConicalColumn3D|Stellt 3D-konisches Säulendiagramm dar|
|Pyramid|Stellt Pyramiden-Diagramm dar|
|PyramidStacked|Stellt gestapeltes Pyramiden-Diagramm dar|
|Pyramid100PercentStacked|Stellt 100% gestapeltes Pyramidendiagramm dar|
|PyramidBar|Stellt Pyramidensäulendiagramm dar|
|PyramidBarStacked|Stellt gestapeltes Pyramidensäulendiagramm dar|
|PyramidBar100PercentStacked|Stellt 100% gestapeltes Pyramidensäulendiagramm dar|
|PyramidColumn3D|Stellt 3D-Pyramiden-Säulendiagramm dar|
{{% alert color="primary" %}}

Wenn Sie einen Zellbereich als Datenquelle zuweisen, können Sie den Bereich nur von oben links nach unten rechts festlegen. Zum Beispiel ist "A1:C3" gültig, während "C3:A1" ungültig ist.

{{% /alert %}}

#### **Pyramiden-Diagramm**

Wenn der Beispielcode ausgeführt wird, wird ein Pyramiden-Diagramm dem Arbeitsblatt hinzugefügt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreatePyramidChart-1.py" >}}

#### **Linien-Diagramm**

Im obigen Beispiel wird durch einfaches Ändern von [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) in *Line* ein Liniendiagramm erstellt. Der vollständige Quellcode wird unten bereitgestellt. Wenn der Code ausgeführt wird, wird dem Arbeitsblatt ein Liniendiagramm hinzugefügt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateLineChart-1.py" >}}

#### **Bubble-Diagramm**

Um ein Bubble-Diagramm zu erstellen, muss [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) auf [**ChartType.BUBBLE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) gesetzt und einige zusätzliche Eigenschaften wie BubbleSizes, Values & XValues entsprechend festgelegt werden. Nach Ausführung des folgenden Codes wird dem Arbeitsblatt ein Bubble-Diagramm hinzugefügt.

#### **Liniendiagramm mit Datenmarkierungen**

Um ein Liniendiagramm mit Datenmarkierungen zu erstellen, muss [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) auf *ChartType.LineWithDataMarkers* gesetzt und einige zusätzliche Eigenschaften wie Hintergrundbereich, Series Markers, Values & XValues entsprechend festgelegt werden. Nach Ausführung des folgenden Codes wird dem Arbeitsblatt ein Liniendiagramm mit Datenmarkierungen hinzugefügt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateLineWithDataMarkerChart-1.py" >}}

## **Erweiterte Themen**
- [Excel 2016 Diagramme lesen und bearbeiten](/cells/de/python-net/read-and-manipulate-excel-2016-charts/)
- [Achsen von Excel-Diagrammen verwalten](/cells/de/python-net/chart-axes/)
- [Diagrammaussehen festlegen](/cells/de/python-net/setting-chart-appearance/)
- [Diagrammtypen](/cells/de/python-net/chart-types/)
- [Diagramme anpassen](/cells/de/python-net/customizing-charts/)
- [Datenquelle für das Diagramm festlegen](/cells/de/python-net/data-formatting-in-charts/)
- [Datenbeschriftungen von Excel-Diagrammen verwalten](/cells/de/python-net/insert-datalabels-to-chart/)
- [Diagramm durch Verarbeitung von Smart Markern generieren](/cells/de/python-net/generate-chart-by-processing-smart-markers/)
- [Arbeitsblatt des Diagramms erhalten](/cells/de/python-net/get-worksheet-of-the-chart/)
- [Legende von Excel-Diagrammen verwalten](/cells/de/python-net/chart-legend/)
- [Position Size und Gestaltung von Diagrammen bearbeiten](/cells/de/python-net/manipulate-position-size-and-designer-chart/)
- [Erstellen eines Tortendiagramms mit Führungslinien](/cells/de/python-net/creating-pie-chart-with-leader-lines/)
- [Formen in Diagrammen](/cells/de/python-net/controls-in-charts/)
- [Titel von Excel-Diagrammen verwalten](/cells/de/python-net/chart-and-axis-titles/)
- [Diagrammrendering](/cells/de/python-net/chart-rendering/)
- [Gleichungstext der Trendlinie des Diagramms abrufen](/cells/de/python-net/get-equation-text-of-chart-trendline/)
