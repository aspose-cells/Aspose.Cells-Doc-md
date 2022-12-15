---
title: Diagramm erstellen und verwalten
linktitle: Diagramme
type: docs
weight: 130
url: /de/net/creating-charts/
description: Erstellen Sie ein Diagramm in CSharp für Excel- und ODS-Dateien.
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

Mit Aspose.Cells können Tabellenkalkulationen eine Vielzahl von Diagrammen hinzugefügt werden. Aspose.Cells bietet viele flexible Diagrammobjekte. In diesem Thema werden Aspose.Cells-Diagrammobjekte behandelt.

{{% /alert %}}

## **Erstellen von Diagrammen**

### **Einfach ein Diagramm erstellen**
Es ist einfach, ein Diagramm mit Aspose.Cells mit den folgenden Beispielcodes zu erstellen:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **Wissenswertes zum Erstellen eines Diagramms**

Vor dem Erstellen von Diagrammen ist es wichtig, einige grundlegende Konzepte zu verstehen, die beim Erstellen von Diagrammen mit Aspose.Cells hilfreich sind.

#### **Diagrammobjekte**

Aspose.Cells bietet eine spezielle Reihe von Klassen in der[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts) Namespace, der zum Erstellen der von Aspose.Cells unterstützten Diagramme verwendet wird. Diese Klassen werden zum Erstellen verwendet**Diagrammobjekte**, die als Diagrammbausteine fungieren. Die Diagrammobjekte sind unten aufgeführt:

- Serie, eine einzelne Datenreihe in einem Diagramm.
- Axis, die Achse eines Diagramms.
- Diagramm, ein einzelnes Excel-Diagramm.
- ChartArea, der Diagrammbereich im Arbeitsblatt.
- ChartDataTable, eine Diagrammdatentabelle.
- ChartFrame, das Rahmenobjekt in einem Diagramm.
- ChartPoint, ein einzelner Punkt in einer Reihe in einem Diagramm.
- ChartPointCollection, eine Auflistung, die alle Punkte in einer Reihe enthält.
- Charts, eine Sammlung von Chart-Objekten.
- DataLabels, eine Auflistung aller DataLabel-Objekte für die angegebene Reihe.
- FillFormat, Füllformat für eine Form.
- Boden, der Boden eines 3D-Diagramms.
- Legende, die Diagrammlegende.
- Linie, die Diagrammlinie.
- SeriesCollection, eine Sammlung von Series-Objekten.
- TickLabels, die Teilstrichbeschriftungen, die Teilstrichen auf einer Diagrammachse zugeordnet sind.
- Titel, der Titel eines Diagramms oder einer Achse.
- Trendlinie, eine Trendlinie in einem Diagramm.
- TrendlineCollection, eine Sammlung aller Trendline-Objekte für die angegebene Datenreihe.
- Wände, die Wände eines 3D-Diagramms.

#### **Verwenden von Diagrammobjekten**

Wie oben erwähnt, sind alle Diagrammobjekte Instanzen ihrer jeweiligen Klassen und stellen spezifische Eigenschaften und Methoden bereit, um spezifische Aufgaben auszuführen. Verwenden Sie Diagrammobjekte, um Diagramme zu erstellen.

Fügen Sie einem Arbeitsblatt mithilfe von beliebige Diagrammtypen hinzu[**Diagramme**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) Sammlung. Jeder Artikel in der[**Diagramme**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) Sammlung repräsentiert a[**Diagramm**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) Objekt. EIN[**Diagramm**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)-Objekt kapselt alle anderen Diagrammobjekte, die zum Anpassen der Darstellung des Diagramms erforderlich sind. Der nächste Abschnitt zeigt, wie Sie mit einigen grundlegenden Diagrammobjekten ein einfaches Diagramm erstellen.

### **Erstellen Sie ein Diagramm mit Aspose.Cells**

**Schritte:**

1.  Fügen Sie einige Daten zu Arbeitsblattzellen mit hinzu[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Objekt[**PutWert**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)Methode.
 Dies wird als Datenquelle für das Diagramm verwendet.
1.  Fügen Sie dem Arbeitsblatt ein Diagramm hinzu, indem Sie die aufrufen[**Diagramme**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) Sammlung[**Hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) Methode, gekapselt in der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Objekt.
1.  Geben Sie den Diagrammtyp mit an[**Diagramm Typ**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)Aufzählung.
 Im folgenden Beispiel wird z. B. die verwendet[**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)value als Diagrammtyp.
1.  Greifen Sie auf das Neue zu[**Diagramm**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) Objekt aus der[**Diagramme**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)-Sammlung, indem ihr Index übergeben wird.
1.  Verwenden Sie eines der Diagrammobjekte, die in gekapselt sind[**Diagramm**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)Objekt, um das Diagramm zu verwalten.
 Das folgende Beispiel verwendet die[**SerieSammlung**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)charting-Objekt, um die Datenquelle des Diagramms anzugeben.

Beim Hinzufügen von Quelldaten zum Diagramm kann die Datenquelle ein Zellbereich (z. B. „A1:C3“) oder eine Folge nicht zusammenhängender Zellen (z. B. „A1, A3, A5“) oder eine Folge von sein Werte (z. B. "1,2,3").

Mit diesen allgemeinen Schritten können Sie jede Art von Diagramm erstellen. Verwenden Sie verschiedene Diagrammobjekte, um verschiedene Diagramme zu erstellen.

 Mit Aspose.Cells können viele verschiedene Arten von Diagrammen erstellt werden. Alle von Aspose.Cells unterstützten Standarddiagramme sind in einer Enumeration mit dem Namen vordefiniert[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

Die vordefinierten Diagrammtypen sind:

|**Diagrammtypen**|**Beschreibung**|
|:- |:- |
|Spalte|Stellt ein gruppiertes Säulendiagramm dar|
|Spalte gestapelt|Stellt ein gestapeltes Säulendiagramm dar|
|Spalte 100 Prozent gestapelt|Stellt ein 100 % gestapeltes Säulendiagramm dar|
|Column3DClustered|Stellt ein gruppiertes 3D-Säulendiagramm dar|
|Column3DStacked|Stellt ein gestapeltes 3D-Säulendiagramm dar|
|Column3D100PercentStacked|Stellt ein gestapeltes 3D-Säulendiagramm mit 100 % dar|
|Spalte3D|Stellt ein 3D-Säulendiagramm dar|
|Bar|Stellt gruppiertes Balkendiagramm dar|
|BarStacked|Stellt ein gestapeltes Balkendiagramm dar|
|Balken 100 Prozent gestapelt|Stellt ein 100 % gestapeltes Balkendiagramm dar|
|Bar3DClustered|Stellt ein gruppiertes 3D-Balkendiagramm dar|
|Bar3DStacked|Stellt ein gestapeltes 3D-Balkendiagramm dar|
|Bar3D100PercentStacked|Stellt ein 100 % gestapeltes 3D-Balkendiagramm dar|
|Linie|Stellt Liniendiagramm dar|
|LineStacked|Stellt ein gestapeltes Liniendiagramm dar|
|Zeile 100 Prozent gestapelt|Stellt ein 100 % gestapeltes Liniendiagramm dar|
|LineWithDataMarkers|Stellt Liniendiagramm mit Datenmarkierungen dar|
|LineStackedWithDataMarkers|Stellt ein gestapeltes Liniendiagramm mit Datenmarkierungen dar|
|Line100PercentStackedWithDataMarkers|Stellt ein 100 % gestapeltes Liniendiagramm mit Datenmarkierungen dar|
|Line3D|Stellt ein 3D-Liniendiagramm dar|
|Kuchen|Stellt Kreisdiagramm dar|
|Pie3D|Stellt ein 3D-Kreisdiagramm dar|
|PiePie|Stellt ein Kreisdiagramm dar|
|Kuchenexplodiert|Stellt ein explodiertes Kreisdiagramm dar|
|Pie3D Explodiert|Stellt ein explodiertes 3D-Kreisdiagramm dar|
|PieBar|Stellt den Balken des Kreisdiagramms dar|
|Streuen|Stellt das Streudiagramm dar|
|ScatterConnectedByCurvesWithDataMarker|Stellt ein Streudiagramm dar, das durch Kurven verbunden ist, mit Datenmarkierungen|
|ScatterConnectedByCurvesWithoutDataMarker|Stellt ein Streudiagramm dar, das durch Kurven verbunden ist, ohne Datenmarkierungen|
|ScatterConnectedByLinesWithDataMarker|Stellt ein Streudiagramm dar, das durch Linien verbunden ist, mit Datenmarkierungen|
|ScatterConnectedByLinesWithoutDataMarker|Stellt ein Streudiagramm dar, das durch Linien verbunden ist, ohne Datenmarkierungen|
|Bereich|Stellt das Flächendiagramm dar|
|BereichStacked|Stellt ein gestapeltes Flächendiagramm dar|
|Area100ProcentStacked|Stellt ein 100 % gestapeltes Flächendiagramm dar|
|Bereich3D|Stellt ein 3D-Flächendiagramm dar|
|Area3DStacked|Stellt ein gestapeltes 3D-Flächendiagramm dar|
|Area3D100ProzentStacked|Stellt ein 100 % gestapeltes 3D-Flächendiagramm dar|
|Krapfen|Stellt das Donut-Diagramm dar|
|Donut Explodiert|Stellt das explodierte Donut-Diagramm dar|
|Radar|Stellt Radardiagramm dar|
|RadarWithDataMarkers|Stellt Netzdiagramm mit Datenmarkierungen dar|
|Radargefüllt|Stellt ein gefülltes Netzdiagramm dar|
|Surface3D|Stellt ein 3D-Oberflächendiagramm dar|
|SurfaceWireframe3D|Stellt ein Drahtgitter-3D-Oberflächendiagramm dar|
|Oberflächenkontur|Stellt das Konturdiagramm dar|
|SurfaceContourWireframe|Stellt das Drahtmodell-Konturdiagramm dar|
|Blase|Stellt das Blasendiagramm dar|
|Bubble3D|Stellt ein 3D-Blasendiagramm dar|
|Zylinder|Stellt das Zylinderdiagramm dar|
|Zylinder gestapelt|Stellt das gestapelte Zylinderdiagramm dar|
|Zylinder 100 Prozent gestapelt|Repräsentiert ein 100 % gestapeltes Zylinderdiagramm|
|Zylinderbar|Stellt ein zylindrisches Balkendiagramm dar.|
|CylindericalBarStacked|Stellt ein gestapeltes zylindrisches Balkendiagramm dar|
|ZylinderförmigBar100Prozentgestapelt|Stellt ein 100 % gestapeltes zylindrisches Balkendiagramm dar|
|ZylinderförmigeSäule3D|Stellt ein zylindrisches 3D-Säulendiagramm dar|
|Kegel|Stellt das Kegeldiagramm dar|
|Kegelgestapelt|Stellt das gestapelte Kegeldiagramm dar|
|Kegel 100 Prozent gestapelt|Stellt ein 100 % gestapeltes Kegeldiagramm dar|
|Konische Stange|Stellt ein konisches Balkendiagramm dar|
|ConicalBarStacked|Stellt ein gestapeltes konisches Balkendiagramm dar|
|ConicalBar100ProcentStacked|Stellt ein 100 % gestapeltes konisches Balkendiagramm dar|
|KonischeSäule3D|Stellt ein konisches 3D-Säulendiagramm dar|
|Pyramide|Stellt Pyramidendiagramm dar|
|PyramidStacked|Stellt ein gestapeltes Pyramidendiagramm dar|
|Pyramid100Prozent gestapelt|Stellt ein 100 % gestapeltes Pyramidendiagramm dar|
|PyramidBar|Stellt ein Pyramiden-Balkendiagramm dar|
|PyramidBarStacked|Stellt ein gestapeltes Pyramiden-Balkendiagramm dar|
|PyramidBar100PercentStacked|Stellt ein 100 % gestapeltes Pyramiden-Balkendiagramm dar|
|PyramidColumn3D|Stellt ein 3D-Pyramiden-Säulendiagramm dar|
{{% alert color="primary" %}}

Wenn Sie als Datenquelle einen Zellbereich zuweisen, können Sie den Bereich nur von links oben nach rechts unten festlegen. Beispielsweise ist „A1:C3“ gültig, während „C3:A1“ ungültig ist.

{{% /alert %}}

#### **Pyramidendiagramm**

Wenn der Beispielcode ausgeführt wird, wird dem Arbeitsblatt ein Pyramidendiagramm hinzugefügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **Liniendiagramm**

 Im obigen Beispiel ändert man einfach die[**Diagramm Typ**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) zu*Linie*erstellt ein Liniendiagramm. Die vollständige Quelle ist unten angegeben. Wenn der Code ausgeführt wird, wird dem Arbeitsblatt ein Liniendiagramm hinzugefügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **Blasendiagramm**

 Um ein Blasendiagramm zu erstellen, muss die[**Diagramm Typ**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) muss eingestellt werden[**ChartType.Blase**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)und einige zusätzliche Eigenschaften wie BubbleSizes, Values & XValues müssen entsprechend eingestellt werden. Beim Ausführen des folgenden Codes wird dem Arbeitsblatt ein Blasendiagramm hinzugefügt.

#### **Linie mit Datenmarkierungsdiagramm**

 Um eine Linie mit dem Datenmarkierungsdiagramm zu erstellen,[**Diagramm Typ**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)muss eingestellt werden*ChartType.LineWithDataMarkers*und einige zusätzliche Eigenschaften wie Hintergrundbereich, Serienmarkierungen, Werte und X-Werte müssen entsprechend festgelegt werden. Beim Ausführen des folgenden Codes wird dem Arbeitsblatt eine Zeile mit dem Datenmarkierungsdiagramm hinzugefügt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **Themen vorantreiben**
- [Lesen und bearbeiten Sie Excel 2016-Diagramme](/cells/de/net/read-and-manipulate-excel-2016-charts/)
- [Achsen von Excel-Diagrammen verwalten](/cells/de/net/chart-axes/)
- [Darstellung des Diagramms einstellen](/cells/de/net/setting-chart-appearance/)
- [Diagrammtypen](/cells/de/net/chart-types/)
- [Anpassen von Diagrammen](/cells/de/net/customizing-charts/)
- [Legen Sie die Datenquelle für das Diagramm fest](/cells/de/net/data-formatting-in-charts/)
- [Verwalten Sie DataLabels von Excel-Diagrammen](/cells/de/net/insert-datalabels-to-chart/)
- [Erstellen Sie ein Diagramm, indem Sie Smart-Marker verarbeiten](/cells/de/net/generate-chart-by-processing-smart-markers/)
- [Holen Sie sich das Arbeitsblatt des Diagramms](/cells/de/net/get-worksheet-of-the-chart/)
- [Legende von Excel-Diagrammen verwalten](/cells/de/net/chart-legend/)
- [Manipulieren Sie die Positionsgröße und das Designer-Diagramm](/cells/de/net/manipulate-position-size-and-designer-chart/)
- [Kreisdiagramm mit Führungslinien erstellen](/cells/de/net/creating-pie-chart-with-leader-lines/)
- [Formen in Diagrammen](/cells/de/net/controls-in-charts/)
- [Titel von Excel-Diagrammen verwalten](/cells/de/net/chart-and-axis-titles/)
- [Diagrammdarstellung](/cells/de/net/chart-rendering/)
- [Holen Sie sich den Gleichungstext der Trendlinie des Diagramms](/cells/de/net/get-equation-text-of-chart-trendline/)
