---
title: Diagramm erstellen und verwalten
description: Erfahren Sie, wie Sie Aspose.Cells for .NET verwenden, um Diagramme in Microsoft Excel zu erstellen. Unser Leitfaden demonstriert die verschiedenen Arten von Diagrammen, die erstellt werden können, sowie deren Anpassung und Formatierung.
keywords: Aspose.Cells for .NET, Diagrammerstellung, Microsoft Excel, Diagrammtypen, Anpassung, Erscheinungsbild, Formatierung.
linktitle: Diagramme
type: docs
weight: 130
url: /de/net/creating-charts/
description: Erstellen Sie ein Diagramm in CSharp für Excel und ODS Dateien.
keywords: Erstellen Sie ein Diagramm, erstellen Sie ein Diagramm 
---

{{% alert color="primary" %}}

Es ist möglich, verschiedene Diagramme zu Tabellenkalkulationen mit Aspose.Cells hinzuzufügen. Aspose.Cells bietet viele flexible Diagrammobjekte. In diesem Themenbereich werden die Diagrammobjekte von Aspose.Cells diskutiert.

{{% /alert %}}

## **Erstellen von Diagrammen**

### **Einfaches Erstellen eines Diagramms**
Das Erstellen eines Diagramms mit Aspose.Cells ist mit den folgenden Beispielcodes einfach:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **Dinge, die beim Erstellen eines Diagramms zu beachten sind**

Bevor Sie Diagramme erstellen, ist es wichtig, einige grundlegende Konzepte zu verstehen, die hilfreich sind, wenn Sie Diagramme mit Aspose.Cells erstellen.

#### **Diagrammobjekte**

Aspose.Cells bietet eine spezielle Reihe von Klassen im [**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts)-Namespace, die verwendet werden, um die von Aspose.Cells unterstützten Diagramme zu erstellen. Diese Klassen werden verwendet, um **Diagrammobjekte** zu erstellen, die als die Bausteine für den Diagrammaufbau dienen. Die Diagrammobjekte werden unten aufgeführt:

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

Fügen Sie mit der [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts)-Sammlung eine beliebige Art von Diagramm zu einem Arbeitsblatt hinzu. Jedes Element in der [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts)-Sammlung stellt ein [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)-Objekt dar. Ein [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)-Objekt umschließt alle anderen Diagrammobjekte, die erforderlich sind, um das Aussehen des Diagramms anzupassen. Im nächsten Abschnitt wird gezeigt, wie man einige grundlegende Diagrammobjekte verwendet, um ein einfaches Diagramm zu erstellen.

### **Diagramm mit Aspose.Cells erstellen**

**Schritte:**

1. Fügen Sie einige Daten zu Arbeitsblattzellen mit der [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)-Methode des Objekts [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) hinzu.
   Dies wird als Datenquelle für das Diagramm verwendet.
1. Fügen Sie ein Diagramm zu Arbeitsblatt hinzu, indem Sie die [**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)-Methode der Sammlung aufrufen, die im [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Objekt eingeschlossen ist.
1. Geben Sie mit der [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)-Aufzählung den Diagrammtyp an.
   Beispielsweise verwendet das untenstehende Beispiel den Wert [**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) als Diagrammtyp.
1. Greifen Sie über die Indexübergabe auf das neue [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)-Objekt aus der [**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)-Sammlung zu.
1. Verwenden Sie eines der im [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)-Objekt eingeschlossenen Diagrammobjekte, um das Diagramm zu verwalten.
   Das untenstehende Beispiel verwendet das [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)-Diagrammobjekt, um die Datenquelle des Diagramms anzugeben.

Beim Hinzufügen von Quelldaten zum Diagramm kann die Datenquelle ein Zellenbereich (z. B. "A1:C3") oder eine Sequenz von nicht zusammenhängenden Zellen (z. B. "A1, A3, A5") oder eine Sequenz von Werten (z. B. "1,2,3") sein.

Diese allgemeinen Schritte ermöglichen es Ihnen, beliebige Arten von Diagrammen zu erstellen. Verwenden Sie verschiedene Diagrammobjekte, um verschiedene Diagramme zu erstellen.

Es ist möglich, mit Aspose.Cells viele verschiedene Arten von Diagrammen zu erstellen. Alle von Aspose.Cells unterstützten Standarddiagramme sind in einer Aufzählung namens [**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) vordefiniert.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **Linien-Diagramm**

Im obigen Beispiel wird durch einfaches Ändern von [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) in *Line* ein Liniendiagramm erstellt. Der vollständige Quellcode wird unten bereitgestellt. Wenn der Code ausgeführt wird, wird dem Arbeitsblatt ein Liniendiagramm hinzugefügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **Bubble-Diagramm**

Um ein Bubble-Diagramm zu erstellen, muss [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) auf [**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) gesetzt und einige zusätzliche Eigenschaften wie BubbleSizes, Values & XValues entsprechend festgelegt werden. Nach Ausführung des folgenden Codes wird dem Arbeitsblatt ein Bubble-Diagramm hinzugefügt.

#### **Liniendiagramm mit Datenmarkierungen**

Um ein Liniendiagramm mit Datenmarkierungen zu erstellen, muss [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) auf *ChartType.LineWithDataMarkers* gesetzt und einige zusätzliche Eigenschaften wie Hintergrundbereich, Series Markers, Values & XValues entsprechend festgelegt werden. Nach Ausführung des folgenden Codes wird dem Arbeitsblatt ein Liniendiagramm mit Datenmarkierungen hinzugefügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **Erweiterte Themen**
- [Excel 2016 Diagramme lesen und bearbeiten](/cells/de/net/read-and-manipulate-excel-2016-charts/)
- [Achsen von Excel-Diagrammen verwalten](/cells/de/net/chart-axes/)
- [Diagrammaussehen festlegen](/cells/de/net/setting-chart-appearance/)
- [Diagrammtypen](/cells/de/net/chart-types/)
- [Diagramme anpassen](/cells/de/net/customizing-charts/)
- [Datenquelle für das Diagramm festlegen](/cells/de/net/data-formatting-in-charts/)
- [Datenbeschriftungen von Excel-Diagrammen verwalten](/cells/de/net/insert-datalabels-to-chart/)
- [Diagramm durch Verarbeitung von Smart Markern generieren](/cells/de/net/generate-chart-by-processing-smart-markers/)
- [Arbeitsblatt des Diagramms erhalten](/cells/de/net/get-worksheet-of-the-chart/)
- [Legende von Excel-Diagrammen verwalten](/cells/de/net/chart-legend/)
- [Position Size und Gestaltung von Diagrammen bearbeiten](/cells/de/net/manipulate-position-size-and-designer-chart/)
- [Erstellen eines Tortendiagramms mit Führungslinien](/cells/de/net/creating-pie-chart-with-leader-lines/)
- [Formen in Diagrammen](/cells/de/net/controls-in-charts/)
- [Titel von Excel-Diagrammen verwalten](/cells/de/net/chart-and-axis-titles/)
- [Diagrammrendering](/cells/de/net/chart-rendering/)
- [Gleichungstext der Trendlinie des Diagramms abrufen](/cells/de/net/get-equation-text-of-chart-trendline/)
{{< app/cells/assistant language="csharp" >}}
