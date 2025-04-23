---
title: Diagramme anpassen
type: docs
weight: 15
url: /de/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---

## **Erstellen von Diagrammen**

Es ist möglich, verschiedene Diagramme zu Tabellenkalkulationen mit Aspose.Cells hinzuzufügen. Aspose.Cells bietet viele flexible Diagrammobjekte. In diesem Themenbereich werden die Diagrammobjekte von Aspose.Cells diskutiert.

### **Einfaches Erstellen eines Diagramms**

Es ist einfach, mit Aspose.Cells ein Diagramm zu erstellen, mit den folgenden Beispielcodes:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **Dinge, die Sie für die Erstellung eines Diagramms wissen sollten**

Bevor Sie Diagramme erstellen, ist es wichtig, einige grundlegende Konzepte zu verstehen, die hilfreich sind, wenn Sie Diagramme mit Aspose.Cells erstellen.

#### **Diagrammobjekte**

Aspose.Cells bietet eine spezielle Reihe von Klassen zum Erstellen aller Arten von Diagrammen. Diese Klassen werden verwendet, um **Diagrammobjekte** zu erstellen, die als Bausteine für den Diagrammaufbau dienen. Die Diagrammobjekte sind unten aufgeführt:

- [**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), eine Achse des Diagramms.
- [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), ein einzelnes Excel-Diagramm.
- [**ChartArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), der Diagrammbereich im Arbeitsblatt.
- [**ChartDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), eine Diagrammdatentabelle.
- [**ChartFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), das Rahmenelement in einem Diagramm.
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), ein einzelner Punkt in einer Serie in einem Diagramm.
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection), eine Sammlung, die alle Punkte in einer Serie enthält.
- [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection), eine Sammlung von [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) Objekten.
- Datenbeschriftungen, Datenbeschriftungen für das angegebene [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), usw.
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat), Füllformat für eine Form.
- [**Floor**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor), die Basis eines 3D-Diagramms.
- [**Legend**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend), die Diagrammlegende.
- [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), die Diagrammlinie.
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection), eine Sammlung von [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) Objekten.
- [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), stellt eine einzelne Datenreihe in einem Diagramm dar.
- [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels), die Zeichenbeschriftungen, die mit den Zeichen an einer Diagrammachse verbunden sind.
- [**Title**](https://reference.aspose.com/cells/java/com.aspose.cells/Title), der Titel eines Diagramms oder einer Achse.
- [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), eine Trendlinie in einem Diagramm.
- [**TrendlineCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection), eine Sammlung aller Trendline-Objekte für die angegebene Datenreihe.
- [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), die Wände eines 3D-Diagramms.

#### **Verwendung von Diagrammobjekten**

Wie oben erwähnt, sind alle Diagrammobjekte Instanzen ihrer jeweiligen Klassen und bieten spezifische Eigenschaften und Methoden zur Ausführung bestimmter Aufgaben. Verwenden Sie Diagrammobjekte, um Diagramme zu erstellen.

Fügen Sie mithilfe der [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) Sammlung jeden beliebigen Diagrammtyp zu einem Arbeitsblatt hinzu. Jedes Element in der [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) Sammlung stellt ein [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) Objekt dar. Ein [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) Objekt umfasst alle Diagrammobjekte, die erforderlich sind, um das Erscheinungsbild des Diagramms anzupassen. Der nächste Abschnitt zeigt, wie einige grundlegende Diagrammobjekte verwendet werden, um ein einfaches Diagramm zu erstellen.

### **Erstellen eines einfachen Diagramms**

Es ist möglich, mit Aspose.Cells viele verschiedene Arten von Diagrammen zu erstellen. Alle von Aspose.Cells unterstützten Standarddiagramme sind in einer Aufzählung namens [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) vordefiniert. Die vordefinierten Diagrammtypen sind:

|**Diagrammtypen**|**Beschreibung**|
| :- | :- |
|Column|Stellt das gruppierte Balkendiagramm dar|
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
|Scatter|Stellt das Punktdiagramm dar|
|ScatterConnectedByCurvesWithDataMarker|Stellt das über Kurven verbundene Punktdiagramm mit Datenmarkierungen dar|
|ScatterConnectedByCurvesWithoutDataMarker|Stellt das über Kurven verbundene Punktdiagramm ohne Datenmarkierungen dar|
|ScatterConnectedByLinesWithDataMarker|Stellt das über Linien verbundene Punktdiagramm mit Datenmarkierungen dar|
|ScatterConnectedByLinesWithoutDataMarker|Stellt das über Linien verbundene Punktdiagramm ohne Datenmarkierungen dar|
|Area|Stellt ein Flächendiagramm dar|
|AreaStacked|Stellt ein gestapeltes Flächendiagramm dar|
|Area100PercentStacked|Stellt ein 100 % gestapeltes Flächendiagramm dar|
|Area3D|Stellt ein 3D-Flächendiagramm dar|
|Area3DStacked|Stellt ein 3D-gestapeltes Flächendiagramm dar|
|Area3D100PercentStacked|Stellt ein 3D-100 %-gestapeltes Flächendiagramm dar|
|Doughnut|Stellt ein Doughnut-Diagramm dar|
|DoughnutExploded|Stellt ein explodiertes Doughnut-Diagramm dar|
|Radar|Stellt das Radar-Diagramm dar|
|RadarWithDataMarkers|Stellt das Radar-Diagramm mit Datenmarkierungen dar|
|RadarFilled|Stellt ein gefülltes Radar-Diagramm dar|
|Surface3D|Stellt ein 3D-Oberflächendiagramm dar|
|SurfaceWireframe3D|Stellt das 3D-Netzflächendiagramm dar|
|SurfaceContour|Stellt Konturdiagramm dar|
|SurfaceContourWireframe|Stellt Drahtgitter-Konturdiagramm dar|
|Bubble|Stellt Blasendiagramm dar|
|Bubble3D|Stellt 3D-Blasendiagramm dar|
|Cylinder|Stellt Zylinderdiagramm dar|
|CylinderStacked|Stellt gestapeltes Zylinderdiagramm dar|
|Cylinder100PercentStacked|Stellt 100 % gestapeltes Zylinderdiagramm dar|
|CylindricalBar|Stellt ein zylindrisches Balkendiagramm dar|
|CylindricalBarStacked|Stellt ein gestapeltes zylindrisches Balkendiagramm dar|
|CylindricalBar100PercentStacked|Stellt ein zu 100 % gestapeltes zylindrisches Balkendiagramm dar|
|CylindricalColumn3D|Stellt ein 3D-zylindrisches Säulendiagramm dar|
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
|PyramidBar|Stellt das Pyramid-Balkendiagramm dar|
|PyramidBarStacked|Stellt gestapeltes Pyramidensäulendiagramm dar|
|PyramidBar100PercentStacked|Stellt 100% gestapeltes Pyramidensäulendiagramm dar|
|PyramidColumn3D|Stellt 3D-Pyramiden-Säulendiagramm dar|
Um ein Diagramm mit Aspose.Cells zu erstellen:

1. Fügen Sie einige Daten zu Arbeitsblattzellen mit der [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)-Methode des Objekts [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) hinzu.
   Dies wird als Datenquelle für das Diagramm verwendet.
1. Fügen Sie ein Diagramm zum Arbeitsblatt hinzu, indem Sie die [*add*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add-int-int-int-int-int-) Methode der [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) Sammlung aufrufen, die im [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Objekt eingebettet ist.
1. Geben Sie mit der [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)-Aufzählung den Diagrammtyp an.
   Beispielsweise verwendet das Beispiel den Wert [**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID) als Diagrammtyp.
1. Greifen Sie über die Indexübergabe auf das neue [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)-Objekt aus der [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)-Sammlung zu.
1. Verwenden Sie eines der im [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)-Objekt eingeschlossenen Diagrammobjekte, um das Diagramm zu verwalten.
   Das untenstehende Beispiel verwendet das [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)-Diagrammobjekt, um die Datenquelle des Diagramms anzugeben.

Beim Hinzufügen von Quelldaten zum Diagramm kann die Datenquelle ein Zellenbereich (z. B. "A1:C3") oder eine Sequenz von nicht zusammenhängenden Zellen (z. B. "A1, A3, A5") oder eine Sequenz von Werten (z. B. "1,2,3") sein.

{{% alert color="primary" %}}

Wenn Sie einen Zellenbereich als Datenquelle festlegen, können Sie nur den Bereich von oben links nach unten rechts festlegen. Zum Beispiel ist "A1:C3" gültig, während "C3:A1" ungültig ist.

{{% /alert %}}

Diese allgemeinen Schritte ermöglichen es Ihnen, beliebige Arten von Diagrammen zu erstellen. Verwenden Sie verschiedene Diagrammobjekte, um verschiedene Diagramme zu erstellen.

Wenn der Beispielcode ausgeführt wird, wird ein Pyramiden-Diagramm wie unten gezeigt zum Arbeitsblatt hinzugefügt.

**Pyramiden-Diagramm mit seiner Datenquelle**

![todo:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

Um ein Bubbel-Diagramm zu erstellen, muss das [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) auf [**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE) gesetzt werden, und einige zusätzliche Eigenschaften wie BubbleSizes, Values & XValues müssen entsprechend gesetzt werden. Nach Ausführung des folgenden Codes wird ein Bubbel-Diagramm wie unten gezeigt zum Arbeitsblatt hinzugefügt.

**Bubbel-Diagramm mit seiner Datenquelle**

![todo:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **Liniendiagramm mit Datenmarkierungen**

Um ein Linie mit Datenmarkern-Diagramm zu erstellen, muss das [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) auf [**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE-WITH-DATA-MARKERS) gesetzt werden und einige zusätzliche Eigenschaften wie Hintergrundbereich, Serienmarker, Werte & X-Werte entsprechend gesetzt werden. Nach Ausführung des folgenden Codes wird ein Linie mit Datenmarkern-Diagramm zum Arbeitsblatt hinzugefügt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **Erstellen von benutzerdefinierten Diagrammen**

Bisher haben wir, wenn wir über Diagramme gesprochen haben, Standarddiagramme betrachtet, die ihre eigenen Formatierungseinstellungen haben. Wir definieren nur die Datenquelle, setzen einige Eigenschaften und das Diagramm wird mit seinen Standardformatierungseinstellungen erstellt. Aber Aspose.Cells unterstützt auch die Erstellung benutzerdefinierter Diagramme, die es Entwicklern ermöglichen, Diagramme mit ihren eigenen Formatierungseinstellungen zu erstellen.

### **Erstellen von benutzerdefinierten Diagrammen**

Entwickler können mithilfe der einfachen Aspose.Cells-API benutzerdefinierte Diagramme zur Laufzeit erstellen.

Ein Diagramm besteht aus einer Datenreihe. Jede Datenreihe in Aspose.Cells wird durch ein [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)-Objekt repräsentiert, während das [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)-Objekt als Sammlung von [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)-Objekten dient. Bei der Erstellung eines benutzerdefinierten Diagramms haben Entwickler die Freiheit, verschiedene Arten von Diagrammen für verschiedene Datenreihen (gesammelt in einem Objekt) zu verwenden.

{{% alert color="primary" %}}

Derzeit unterstützt Aspose.Cells nur benutzerdefinierte Diagramme, die Kuchen-, Linien-, Säulen- und Säulenstapeldiagramme kombinieren, aber in zukünftigen Versionen werden weitere Diagrammtypen unterstützt. Detaillierte Liste der Standarddiagramme, die von Aspose.Cells unterstützt werden, finden Sie im Artikel [Diagrammtypen](/cells/de/java/chart-types/).

{{% /alert %}}

Der nachstehende Beispielcode zeigt, wie benutzerdefinierte Diagramme erstellt werden können. In diesem Beispiel verwenden wir ein Säulendiagramm für die erste Datenreihe und ein Liniendiagramm für die zweite Reihe. Das Ergebnis ist, dass wir ein Säulendiagramm, kombiniert mit einem Liniendiagramm, dem Arbeitsblatt hinzufügen.

**Benutzerdefiniertes Diagramm, das Säulen- und Liniendiagramme kombiniert**

![todo:image_alt_text](creating-and-customizing-charts_3.png)

**Programmierbeispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

Um eine Liste der unterstützten Diagrammtypen zu sehen, lesen Sie den Artikel [Diagrammtypen](/cells/de/java/chart-types/).

{{% /alert %}}

{{< app/cells/assistant language="java" >}}
