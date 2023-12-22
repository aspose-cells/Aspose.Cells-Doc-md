---
title: Diagramm erstellen und verwalten
description: Erfahren Sie, wie Sie mit Aspose.Cells for .NET Diagramme in Microsoft Excel erstellen. Unser Leitfaden zeigt die verschiedenen Arten von Diagrammen, die erstellt werden können, und zeigt, wie Sie deren Erscheinungsbild und Formatierung anpassen können.
keywords: Aspose.Cells for .NET, Chart Creation, Microsoft Excel, Chart Types, Customization, Appearance, Formatting.
linktitle: Diagramme
type: docs
weight: 130
url: /de/net/creating-charts/
description: Erstellen Sie ein Diagramm in CSharp für Excel- und ODS-Dateien.
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

Mit Aspose.Cells ist es möglich, eine Vielzahl von Diagrammen zu Tabellenkalkulationen hinzuzufügen. Aspose.Cells bietet viele flexible Diagrammobjekte. In diesem Thema werden Diagrammobjekte vom Typ Aspose.Cells erläutert.

{{% /alert %}}

##  **Diagramme erstellen**

###  **Einfach ein Diagramm erstellen**
Mit den folgenden Beispielcodes können Sie ganz einfach ein Diagramm mit Aspose.Cells erstellen:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

###  **Wissenswertes zum Erstellen eines Diagramms**

Bevor Sie Diagramme erstellen, ist es wichtig, einige grundlegende Konzepte zu verstehen, die beim Erstellen von Diagrammen mit Aspose.Cells hilfreich sind.

####  **Diagrammobjekte**

 Aspose.Cells bietet eine spezielle Reihe von Kursen im[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts)Namespace, der zum Erstellen der von Aspose.Cells unterstützten Diagramme verwendet wird. Diese Klassen werden zum Erstellen von *Diagrammobjekten** verwendet, die als Diagrammbausteine fungieren. Die Diagrammobjekte sind unten aufgeführt:

- Serie, eine einzelne Datenreihe in einem Diagramm.
- Achse, die Achse eines Diagramms.
- Diagramm, ein einzelnes Excel-Diagramm.
- ChartArea, der Diagrammbereich im Arbeitsblatt.
- ChartDataTable, eine Diagrammdatentabelle.
- ChartFrame, das Rahmenobjekt in einem Diagramm.
- ChartPoint, ein einzelner Punkt in einer Reihe in einem Diagramm.
- ChartPointCollection, eine Sammlung, die alle Punkte in einer Reihe enthält.
- Charts, eine Sammlung von Chart-Objekten.
- DataLabels, eine Sammlung aller DataLabel-Objekte für die angegebene Serie.
- FillFormat, Füllformat für eine Form.
- Boden, der Boden eines 3D-Diagramms.
- Legende, die Diagrammlegende.
- Linie, die Diagrammlinie.
- SeriesCollection, eine Sammlung von Series-Objekten.
- TickLabels, die Teilstrichbeschriftungen, die mit Teilstrichen auf einer Diagrammachse verknüpft sind.
- Titel, der Titel eines Diagramms oder einer Achse.
- Trendlinie, eine Trendlinie in einem Diagramm.
- TrendlineCollection, eine Sammlung aller Trendline-Objekte für die angegebene Datenreihe.
- Wände, die Wände eines 3D-Diagramms.

####  **Verwenden von Diagrammobjekten**

Wie oben erwähnt, sind alle Diagrammobjekte Instanzen ihrer jeweiligen Klassen und stellen spezifische Eigenschaften und Methoden zur Ausführung bestimmter Aufgaben bereit. Verwenden Sie Diagrammobjekte, um Diagramme zu erstellen.

 Fügen Sie einem Arbeitsblatt eine beliebige Art von Diagramm hinzu, indem Sie die verwenden[**Diagramme**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) Sammlung. Jedes Element in der[**Diagramme**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) Sammlung repräsentiert a[**Diagramm**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) Objekt. A[**Diagramm**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)Das Objekt kapselt alle anderen Diagrammobjekte, die zum Anpassen der Darstellung des Diagramms erforderlich sind. Im nächsten Abschnitt wird gezeigt, wie Sie mit einigen grundlegenden Diagrammobjekten ein einfaches Diagramm erstellen.

###  **Erstellen Sie ein Diagramm mit Aspose.Cells**

**Schritte:**

1. Fügen Sie mit dem einige Daten zu Arbeitsblattzellen hinzu[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Objekt[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)Methode.
 Dies wird als Datenquelle für das Diagramm verwendet.
1.  Fügen Sie dem Arbeitsblatt ein Diagramm hinzu, indem Sie das aufrufen[**Diagramme**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) Sammlung[**Hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) Methode, gekapselt in der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Objekt.
1.  Geben Sie den Diagrammtyp mit an[**Diagramm Typ**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)Aufzählung.
 Im folgenden Beispiel wird beispielsweise verwendet[**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)Wert als Diagrammtyp.
1.  Greifen Sie auf das Neue zu[**Diagramm**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) Objekt aus dem[**Diagramme**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)Sammlung durch Übergabe ihres Index.
1.  Verwenden Sie eines der im gekapselten Diagrammobjekte[**Diagramm**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)Objekt zum Verwalten des Diagramms.
 Das folgende Beispiel verwendet die[**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)Diagrammobjekt, um die Datenquelle des Diagramms anzugeben.

Beim Hinzufügen von Quelldaten zu einem Diagramm kann die Datenquelle ein Zellbereich (z. B. „A1:C3“) oder eine Folge nicht zusammenhängender Zellen (z. B. „A1, A3, A5“) oder eine Folge von Zellen sein Werte (z. B. „1,2,3“).

Mit diesen allgemeinen Schritten können Sie jede Art von Diagramm erstellen. Verwenden Sie unterschiedliche Diagrammobjekte, um unterschiedliche Diagramme zu erstellen.

Mit Aspose.Cells ist es möglich, viele verschiedene Arten von Diagrammen zu erstellen. Alle von Aspose.Cells unterstützten Standarddiagramme sind in einer Aufzählung mit dem Namen vordefiniert[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

Die vordefinierten Diagrammtypen sind:

|**Diagrammtypen**|**Beschreibung**|
| :- | :- |
|Spalte|Stellt ein gruppiertes Säulendiagramm dar|
|ColumnStacked|Stellt ein gestapeltes Säulendiagramm dar|
|Column100PercentStacked|Stellt ein 100 % gestapeltes Säulendiagramm dar|
|Column3DClustered|Stellt ein gruppiertes 3D-Säulendiagramm dar|
|Column3DStacked|Stellt ein gestapeltes 3D-Säulendiagramm dar|
|Column3D100PercentStacked|Stellt ein zu 100 % gestapeltes 3D-Säulendiagramm dar|
|Column3D|Stellt ein 3D-Säulendiagramm dar|
|Bar|Stellt ein gruppiertes Balkendiagramm dar|
|BarStacked|Stellt ein gestapeltes Balkendiagramm dar|
|Bar100PercentStacked|Stellt ein 100 % gestapeltes Balkendiagramm dar|
|Bar3DClustered|Stellt ein gruppiertes 3D-Balkendiagramm dar|
|Bar3DStacked|Stellt ein gestapeltes 3D-Balkendiagramm dar|
|Bar3D100PercentStacked|Stellt ein zu 100 % gestapeltes 3D-Balkendiagramm dar|
|Linie|Stellt ein Liniendiagramm dar|
|LineStacked|Stellt ein gestapeltes Liniendiagramm dar|
|Line100PercentStacked|Stellt ein 100 % gestapeltes Liniendiagramm dar|
|LineWithDataMarkers|Stellt ein Liniendiagramm mit Datenmarkierungen dar|
|LineStackedWithDataMarkers|Stellt ein gestapeltes Liniendiagramm mit Datenmarkierungen dar|
|Line100PercentStackedWithDataMarkers|Stellt ein 100 % gestapeltes Liniendiagramm mit Datenmarkierungen dar|
|Line3D|Stellt ein 3D-Liniendiagramm dar|
|Kuchen|Stellt ein Kreisdiagramm dar|
|Pie3D|Stellt ein 3D-Kreisdiagramm dar|
|PiePie|Stellt einen Kreis des Kreisdiagramms dar|
|PieExploded|Stellt ein explodiertes Kreisdiagramm dar|
|Pie3DEExploded|Stellt ein 3D-Explosions-Kreisdiagramm dar|
|PieBar|Stellt einen Balken eines Kreisdiagramms dar|
|Streuen|Stellt ein Streudiagramm dar|
|ScatterConnectedByCurvesWithDataMarker|Stellt ein durch Kurven verbundenes Streudiagramm mit Datenmarkierungen dar|
|ScatterConnectedByCurvesWithoutDataMarker|Stellt ein durch Kurven verbundenes Streudiagramm ohne Datenmarkierungen dar|
|ScatterConnectedByLinesWithDataMarker|Stellt ein durch Linien verbundenes Streudiagramm mit Datenmarkierungen dar|
|ScatterConnectedByLinesWithoutDataMarker|Stellt ein durch Linien verbundenes Streudiagramm ohne Datenmarkierungen dar|
|Bereich|Stellt ein Flächendiagramm dar|
|BereichGestapelt|Stellt ein gestapeltes Flächendiagramm dar|
|Fläche100PercentStacked|Stellt ein 100 % gestapeltes Flächendiagramm dar|
|Area3D|Stellt ein 3D-Flächendiagramm dar|
|Area3DStacked|Stellt ein gestapeltes 3D-Flächendiagramm dar|
|Area3D100PercentStacked|Stellt ein 3D-100 %-Stapelflächendiagramm dar|
|Krapfen|Stellt ein Donut-Diagramm dar|
|DonutExplodiert|Stellt ein explodiertes Donut-Diagramm dar|
|Radar|Stellt ein Radardiagramm dar|
|RadarWithDataMarkers|Stellt ein Radardiagramm mit Datenmarkierungen dar|
|Radargefüllt|Stellt ein gefülltes Radardiagramm dar|
|Surface3D|Stellt ein 3D-Oberflächendiagramm dar|
|OberflächeWireframe3D|Stellt ein Wireframe-3D-Oberflächendiagramm dar|
|Oberflächenkontur|Stellt ein Konturdiagramm dar|
|SurfaceContourWireframe|Stellt ein Drahtmodell-Konturdiagramm dar|
|Blase|Stellt ein Blasendiagramm dar|
|Bubble3D|Stellt ein 3D-Blasendiagramm dar|
|Zylinder|Stellt ein Zylinderdiagramm dar|
|Zylindergestapelt|Stellt ein gestapeltes Zylinderdiagramm dar|
|Zylinder100PercentStacked|Stellt ein 100 % gestapeltes Zylinderdiagramm dar|
|Zylinderischer Balken|Stellt ein zylindrisches Balkendiagramm dar.|
|ZylinderischerBarStacked|Stellt ein gestapeltes zylindrisches Balkendiagramm dar|
|Zylinderischer Balken100PercentStacked|Stellt ein zu 100 % gestapeltes zylindrisches Balkendiagramm dar|
|Zylinderische Spalte3D|Stellt ein zylindrisches 3D-Säulendiagramm dar|
|Kegel|Stellt ein Kegeldiagramm dar|
|Kegelgestapelt|Stellt ein gestapeltes Kegeldiagramm dar|
|Cone100PercentStacked|Stellt ein 100 % gestapeltes Kegeldiagramm dar|
|ConicalBar|Stellt ein konisches Balkendiagramm dar|
|ConicalBarStacked|Stellt ein gestapeltes konisches Balkendiagramm dar|
|ConicalBar100PercentStacked|Stellt ein zu 100 % gestapeltes konisches Balkendiagramm dar|
|ConicalColumn3D|Stellt ein konisches 3D-Säulendiagramm dar|
|Pyramide|Stellt ein Pyramidendiagramm dar|
|PyramidStacked|Stellt ein gestapeltes Pyramidendiagramm dar|
|Pyramid100PercentStacked|Stellt ein 100 % gestapeltes Pyramidendiagramm dar|
|PyramidBar|Stellt ein Pyramidenbalkendiagramm dar|
|PyramidBarStacked|Stellt ein gestapeltes Pyramidenbalkendiagramm dar|
|PyramidBar100PercentStacked|Stellt ein 100 % gestapeltes Pyramidenbalkendiagramm dar|
|PyramidColumn3D|Stellt ein 3D-Pyramiden-Säulendiagramm dar|
{{% alert color="primary" %}}

Wenn Sie einen Zellbereich als Datenquelle zuweisen, können Sie nur den Bereich von links oben nach rechts unten festlegen. Beispielsweise ist „A1:C3“ gültig, während „C3:A1“ ungültig ist.

{{% /alert %}}

####  **Pyramidendiagramm**

Wenn der Beispielcode ausgeführt wird, wird dem Arbeitsblatt ein Pyramidendiagramm hinzugefügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

####  **Liniendiagramm**

 Im obigen Beispiel einfach die ändern[**Diagramm Typ**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) Zu*Linie*erstellt ein Liniendiagramm. Die vollständige Quelle finden Sie unten. Wenn der Code ausgeführt wird, wird dem Arbeitsblatt ein Liniendiagramm hinzugefügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

####  **Blasendiagramm**

 Um ein Blasendiagramm zu erstellen, muss das[**Diagramm Typ**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) muss eingestellt werden[**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)und einige zusätzliche Eigenschaften wie BubbleSizes, Values und XValues müssen entsprechend festgelegt werden. Beim Ausführen des folgenden Codes wird dem Arbeitsblatt ein Blasendiagramm hinzugefügt.

####  **Linie mit Datenmarkierungsdiagramm**

 Um eine Linie mit dem Datenmarkierungsdiagramm zu erstellen,[**Diagramm Typ**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)muss eingestellt werden*ChartType.LineWithDataMarkers*und einige zusätzliche Eigenschaften wie Hintergrundbereich, Serienmarkierungen, Werte und X-Werte müssen entsprechend eingestellt werden. Beim Ausführen des folgenden Codes wird dem Arbeitsblatt eine Zeile mit dem Datenmarkierungsdiagramm hinzugefügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

##  **Vorabthemen**
- [Lesen und Bearbeiten von Excel 2016-Diagrammen](/cells/de/net/read-and-manipulate-excel-2016-charts/)
- [Verwalten Sie die Achsen von Excel-Diagrammen](/cells/de/net/chart-axes/)
- [Festlegen der Darstellung des Diagramms](/cells/de/net/setting-chart-appearance/)
- [Diagrammtypen](/cells/de/net/chart-types/)
- [Anpassen von Diagrammen](/cells/de/net/customizing-charts/)
- [Legen Sie die Datenquelle für das Diagramm fest](/cells/de/net/data-formatting-in-charts/)
- [Verwalten Sie Datenbeschriftungen von Excel-Diagrammen](/cells/de/net/insert-datalabels-to-chart/)
- [Generieren Sie ein Diagramm durch die Verarbeitung intelligenter Markierungen](/cells/de/net/generate-chart-by-processing-smart-markers/)
- [Holen Sie sich das Arbeitsblatt des Diagramms](/cells/de/net/get-worksheet-of-the-chart/)
- [Verwalten Sie die Legende von Excel-Diagrammen](/cells/de/net/chart-legend/)
- [Positionsgröße und Designer-Diagramm manipulieren](/cells/de/net/manipulate-position-size-and-designer-chart/)
- [Kreisdiagramm mit Führungslinien erstellen](/cells/de/net/creating-pie-chart-with-leader-lines/)
- [Formen in Diagrammen](/cells/de/net/controls-in-charts/)
- [Titel von Excel-Diagrammen verwalten](/cells/de/net/chart-and-axis-titles/)
- [Diagrammdarstellung](/cells/de/net/chart-rendering/)
- [Gleichungstext der Diagrammtrendlinie abrufen](/cells/de/net/get-equation-text-of-chart-trendline/)
