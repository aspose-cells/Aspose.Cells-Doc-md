---
title: Anpassen von Diagrammen
type: docs
weight: 15
url: /de/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---
##  **Diagramme erstellen**

Mit Aspose.Cells ist es möglich, eine Vielzahl von Diagrammen zu Tabellenkalkulationen hinzuzufügen. Aspose.Cells bietet viele flexible Diagrammobjekte. In diesem Thema werden Diagrammobjekte vom Typ Aspose.Cells erläutert.

###  **Einfach ein Diagramm erstellen**

Mit den folgenden Beispielcodes können Sie ganz einfach ein Diagramm mit Aspose.Cells erstellen:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


###  **Wissenswertes zum Erstellen eines Diagramms**

Bevor Sie Diagramme erstellen, ist es wichtig, einige grundlegende Konzepte zu verstehen, die beim Erstellen von Diagrammen mit Aspose.Cells hilfreich sind.

####  **Diagrammobjekte**

Aspose.Cells stellt einen speziellen Satz von Klassen bereit, mit denen alle Arten von Diagrammen erstellt werden können. Mit diesen Klassen werden *Diagrammobjekte** erstellt, die als Diagrammbausteine fungieren. Die Diagrammobjekte sind unten aufgeführt:

- [**Achse**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), die Achse eines Diagramms.
- [**Diagramm**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), ein einzelnes Excel-Diagramm.
- [**ChartArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), der Diagrammbereich im Arbeitsblatt.
- [**ChartDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), eine Diagrammdatentabelle.
- [**ChartFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), das Rahmenobjekt in einem Diagramm.
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), ein einzelner Punkt in einer Reihe in einem Diagramm.
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection), eine Sammlung, die alle Punkte einer Reihe enthält.
- [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) , eine Sammlung von[**Diagramm**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)Objekte.
-  DataLabels, DataLabels für die angegebenen[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**Trendlinie**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), usw.
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat), Füllformat für eine Form.
- [**Boden**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor), der Boden eines 3D-Diagramms.
- [**Legende**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend), die Diagrammlegende.
- [**Linie**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), die Diagrammlinie.
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) , eine Sammlung von[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)Objekte.
- [**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), stellt eine einzelne Datenreihe in einem Diagramm dar.
- [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels)die Teilstrichbeschriftungen, die Teilstrichen auf einer Diagrammachse zugeordnet sind.
- [**Titel**](https://reference.aspose.com/cells/java/com.aspose.cells/Title), der Titel eines Diagramms oder einer Achse.
- [**Trendlinie**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), eine Trendlinie in einem Diagramm.
- [**TrendlineCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection), eine Sammlung aller Trendlinienobjekte für die angegebene Datenreihe.
- [**Wände**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), die Wände eines 3D-Diagramms.

####  **Verwenden von Diagrammobjekten**

Wie oben erwähnt, sind alle Diagrammobjekte Instanzen ihrer jeweiligen Klassen und stellen spezifische Eigenschaften und Methoden zur Ausführung bestimmter Aufgaben bereit. Verwenden Sie Diagrammobjekte, um Diagramme zu erstellen.

 Fügen Sie einem Arbeitsblatt eine beliebige Art von Diagramm hinzu, indem Sie die verwenden[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) Sammlung. Jedes Element in der[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) Sammlung repräsentiert a[**Diagramm**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) Objekt. A[**Diagramm**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)Das Objekt kapselt alle Diagrammobjekte, die zum Anpassen des Erscheinungsbilds des Diagramms erforderlich sind. Im nächsten Abschnitt wird gezeigt, wie Sie mit einigen grundlegenden Diagrammobjekten ein einfaches Diagramm erstellen.

###  **Erstellen eines einfachen Diagramms**

Mit Aspose.Cells ist es möglich, viele verschiedene Arten von Diagrammen zu erstellen. Alle von Aspose.Cells unterstützten Standarddiagramme sind in einer Aufzählung mit dem Namen vordefiniert[**Diagramm Typ**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). Die vordefinierten Diagrammtypen sind:

|**Diagrammtypen**|**Beschreibung**|
| :- | :- |
|Spalte|Stellt das gruppierte Säulendiagramm dar|
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
|Streuen|Stellt das Streudiagramm dar|
|ScatterConnectedByCurvesWithDataMarker|Stellt das durch Kurven verbundene Streudiagramm mit Datenmarkierungen dar|
|ScatterConnectedByCurvesWithoutDataMarker|Stellt das durch Kurven verbundene Streudiagramm ohne Datenmarkierungen dar|
|ScatterConnectedByLinesWithDataMarker|Stellt das durch Linien verbundene Streudiagramm mit Datenmarkierungen dar|
|ScatterConnectedByLinesWithoutDataMarker|Stellt das durch Linien verbundene Streudiagramm ohne Datenmarkierungen dar|
|Bereich|Stellt ein Flächendiagramm dar|
|BereichGestapelt|Stellt ein gestapeltes Flächendiagramm dar|
|Fläche100PercentStacked|Stellt ein 100 % gestapeltes Flächendiagramm dar|
|Area3D|Stellt ein 3D-Flächendiagramm dar|
|Area3DStacked|Stellt ein gestapeltes 3D-Flächendiagramm dar|
|Area3D100PercentStacked|Stellt ein 3D-100 %-Stapelflächendiagramm dar|
|Krapfen|Stellt ein Donut-Diagramm dar|
|DonutExplodiert|Stellt ein explodiertes Donut-Diagramm dar|
|Radar|Stellt das Radardiagramm dar|
|RadarWithDataMarkers|Stellt das Radardiagramm mit Datenmarkierungen dar|
|Radargefüllt|Stellt ein gefülltes Radardiagramm dar|
|Surface3D|Stellt ein 3D-Oberflächendiagramm dar|
|OberflächeWireframe3D|Stellt das Wireframe-3D-Oberflächendiagramm dar|
|Oberflächenkontur|Stellt ein Konturdiagramm dar|
|SurfaceContourWireframe|Stellt ein Drahtmodell-Konturdiagramm dar|
|Blase|Stellt ein Blasendiagramm dar|
|Bubble3D|Stellt ein 3D-Blasendiagramm dar|
|Zylinder|Stellt ein Zylinderdiagramm dar|
|Zylindergestapelt|Stellt ein gestapeltes Zylinderdiagramm dar|
|Zylinder100PercentStacked|Stellt ein 100 % gestapeltes Zylinderdiagramm dar|
|Zylindrischer Balken|Stellt ein zylindrisches Balkendiagramm dar.|
|CylindricalBarStacked|Stellt ein gestapeltes zylindrisches Balkendiagramm dar|
|CylindricalBar100PercentStacked|Stellt ein zu 100 % gestapeltes zylindrisches Balkendiagramm dar|
|Zylindrische Spalte3D|Stellt ein zylindrisches 3D-Säulendiagramm dar|
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
|PyramidBar|Stellt das Pyramiden-Balkendiagramm dar|
|PyramidBarStacked|Stellt ein gestapeltes Pyramidenbalkendiagramm dar|
|PyramidBar100PercentStacked|Stellt ein 100 % gestapeltes Pyramidenbalkendiagramm dar|
|PyramidColumn3D|Stellt ein 3D-Pyramiden-Säulendiagramm dar|
So erstellen Sie ein Diagramm mit Aspose.Cells:

1. Fügen Sie mit dem einige Daten zu Arbeitsblattzellen hinzu[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) Objekt[**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)Methode.
 Dies wird als Datenquelle für das Diagramm verwendet.
1.  Fügen Sie dem Arbeitsblatt ein Diagramm hinzu, indem Sie das aufrufen[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) Sammlung[*hinzufügen*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int) )-Methode, gekapselt in der[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)Objekt.
1.  Geben Sie den Diagrammtyp mit an[**Diagramm Typ**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)Aufzählung.
 Das Beispiel verwendet beispielsweise die[**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)Wert als Diagrammtyp.
1.  Greifen Sie auf das Neue zu[**Diagramm**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) Objekt aus dem[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)Sammlung durch Übergabe ihres Index.
1.  Verwenden Sie eines der im gekapselten Diagrammobjekte[**Diagramm**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)Objekt zum Verwalten des Diagramms.
 Das folgende Beispiel verwendet die[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)Diagrammobjekt, um die Datenquelle des Diagramms anzugeben.

Beim Hinzufügen von Quelldaten zu einem Diagramm kann die Datenquelle ein Zellbereich (z. B. „A1:C3“) oder eine Folge nicht zusammenhängender Zellen (z. B. „A1, A3, A5“) oder eine Folge von Zellen sein Werte (z. B. „1,2,3“).

{{% alert color="primary" %}}

Wenn Sie einen Zellbereich als Datenquelle zuweisen, können Sie nur den Bereich von links oben nach rechts unten festlegen. Beispielsweise ist „A1:C3“ gültig, während „C3:A1“ ungültig ist.

{{% /alert %}}

Mit diesen allgemeinen Schritten können Sie jede Art von Diagramm erstellen. Verwenden Sie unterschiedliche Diagrammobjekte, um unterschiedliche Diagramme zu erstellen.

Wenn der Beispielcode ausgeführt wird, wird dem Arbeitsblatt ein Pyramidendiagramm hinzugefügt, wie unten gezeigt.

**Pyramidendiagramm mit seiner Datenquelle**

![todo:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

 Um ein Blasendiagramm zu erstellen, müssen Sie Folgendes tun:[**Diagramm Typ**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)muss eingestellt werden[**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)und einige zusätzliche Eigenschaften wie BubbleSizes, Values und XValues müssen entsprechend festgelegt werden. Beim Ausführen des folgenden Codes wird dem Arbeitsblatt ein Blasendiagramm hinzugefügt, wie unten gezeigt.

**Blasendiagramm mit seiner Datenquelle**

![todo:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

####  **Linie mit Datenmarkierungsdiagramm**

Um eine Linie mit einem Datenmarkierungsdiagramm zu erstellen, müssen Sie Folgendes tun:[**Diagramm Typ**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)muss eingestellt werden[**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS) und einige zusätzliche Eigenschaften wie Hintergrundbereich, Serienmarkierungen, Werte und X-Werte müssen entsprechend festgelegt werden. Beim Ausführen des folgenden Codes wird dem Arbeitsblatt eine Zeile mit einem Datenmarkierungsdiagramm hinzugefügt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

##  **Erstellen benutzerdefinierter Diagramme**

Bisher haben wir uns bei der Besprechung von Diagrammen mit Standarddiagrammen befasst, die über ihre Standardformatierungseinstellungen verfügen. Wir definieren nur die Datenquelle, legen einige Eigenschaften fest und das Diagramm wird mit seinen Standardformateinstellungen erstellt. Aber Aspose.Cells unterstützt auch die Erstellung benutzerdefinierter Diagramme, die es Entwicklern ermöglichen, Diagramme mit ihren eigenen Formateinstellungen zu erstellen.

###  **Erstellen benutzerdefinierter Diagramme**

Entwickler können zur Laufzeit benutzerdefinierte Diagramme erstellen, indem sie Aspose.Cells einfach API verwenden.

 Ein Diagramm besteht aus einer Datenreihe. Jede Datenreihe in Aspose.Cells wird durch a dargestellt[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) Objekt, während die[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) Das Objekt dient als Sammlung von[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)Objekte. Beim Erstellen eines benutzerdefinierten Diagramms haben Entwickler die Freiheit, verschiedene Diagrammtypen für unterschiedliche Datenreihen (gesammelt in einem) zu verwenden[**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)Objekt).

{{% alert color="primary" %}}

Derzeit unterstützt Aspose.Cells nur benutzerdefinierte Diagramme, die Kreis-, Linien-, Säulen- und Säulenstapeldiagramme kombinieren. In zukünftigen Versionen werden jedoch weitere Diagramme unterstützt. Eine vollständige Liste der von Aspose.Cells unterstützten Standarddiagramme finden Sie im[Diagrammtypen](/cells/de/java/chart-types/) Artikel.

{{% /alert %}}

Der folgende Beispielcode zeigt, wie Sie benutzerdefinierte Diagramme erstellen. In diesem Beispiel verwenden wir ein Säulendiagramm für die erste Datenreihe und ein Liniendiagramm für die zweite Reihe. Das Ergebnis ist, dass wir dem Arbeitsblatt ein Säulendiagramm in Kombination mit einem Liniendiagramm hinzufügen.

**Benutzerdefiniertes Diagramm, das Säulen- und Liniendiagramme kombiniert**

![todo:image_alt_text](creating-and-customizing-charts_3.png)

**Programmierbeispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

Um eine Liste der unterstützten Diagrammtypen anzuzeigen, lesen Sie die[Diagrammtypen](/cells/de/java/chart-types/) Artikel.

{{% /alert %}}

