---
title: Anpassen von Diagrammen
type: docs
weight: 15
url: /de/java/creating-and-customizing-charts/
---
## **Erstellen von Diagrammen**

Mit Aspose.Cells können Tabellenkalkulationen eine Vielzahl von Diagrammen hinzugefügt werden. Aspose.Cells bietet viele flexible Diagrammobjekte. In diesem Thema werden Aspose.Cells-Diagrammobjekte behandelt.

### **Einfach ein Diagramm erstellen**

Es ist einfach, ein Diagramm mit Aspose.Cells mit den folgenden Beispielcodes zu erstellen:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **Wissenswertes zum Erstellen eines Diagramms**

Vor dem Erstellen von Diagrammen ist es wichtig, einige grundlegende Konzepte zu verstehen, die beim Erstellen von Diagrammen mit Aspose.Cells hilfreich sind.

#### **Diagrammobjekte**

 Aspose.Cells bietet einen speziellen Satz von Klassen, die zum Erstellen aller Arten von Diagrammen verwendet werden. Diese Klassen werden zum Erstellen verwendet**Diagrammobjekte**, die als Diagrammbausteine fungieren. Die Diagrammobjekte sind unten aufgeführt:

- [**Achse**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), die Achse eines Diagramms.
- [**Diagramm**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), ein einzelnes Excel-Diagramm.
- [**ChartArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), der Diagrammbereich im Arbeitsblatt.
- [**ChartDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), eine Diagrammdatentabelle.
- [**ChartFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), das Rahmenobjekt in einem Diagramm.
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), ein einzelner Punkt in einer Reihe in einem Diagramm.
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection), eine Sammlung, die alle Punkte in einer Reihe enthält.
- [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) , eine Sammlung von[**Diagramm**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)Objekte.
-  DataLabels, DataLabels für die angegebenen[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**Trendlinie**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), etc.
- [**Füllformat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat), Füllformat für eine Form.
- [**Boden**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor), der Boden eines 3D-Diagramms.
- [**Legende**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend), die Diagrammlegende.
- [**Linie**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), die Diagrammlinie.
- [**SerieSammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) , eine Sammlung von[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)Objekte.
- [**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), stellt eine einzelne Datenreihe in einem Diagramm dar.
- [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels), die Teilstrichbeschriftungen, die Teilstrichen auf einer Diagrammachse zugeordnet sind.
- [**Titel**](https://reference.aspose.com/cells/java/com.aspose.cells/Title), der Titel eines Diagramms oder einer Achse.
- [**Trendlinie**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), eine Trendlinie in einem Diagramm.
- [**TrendlineCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection), eine Sammlung aller Trendline-Objekte für die angegebene Datenreihe.
- [**Wände**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), die Wände eines 3D-Diagramms.

#### **Verwenden von Diagrammobjekten**

Wie oben erwähnt, sind alle Diagrammobjekte Instanzen ihrer jeweiligen Klassen und stellen spezifische Eigenschaften und Methoden bereit, um spezifische Aufgaben auszuführen. Verwenden Sie Diagrammobjekte, um Diagramme zu erstellen.

Fügen Sie einem Arbeitsblatt mithilfe von beliebige Diagrammtypen hinzu[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) Sammlung. Jeder Artikel in der[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) Sammlung repräsentiert a[**Diagramm**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) Objekt. EIN[**Diagramm**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)-Objekt kapselt alle Diagrammobjekte, die zum Anpassen des Aussehens des Diagramms erforderlich sind. Der nächste Abschnitt zeigt, wie Sie mit einigen grundlegenden Diagrammobjekten ein einfaches Diagramm erstellen.

### **Erstellen eines einfachen Diagramms**

 Mit Aspose.Cells können viele verschiedene Arten von Diagrammen erstellt werden. Alle von Aspose.Cells unterstützten Standarddiagramme sind in einer Enumeration mit dem Namen vordefiniert[**Diagramm Typ**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). Die vordefinierten Diagrammtypen sind:

|**Diagrammtypen**|**Beschreibung**|
|:- |:- |
|Spalte|Stellt das gruppierte Säulendiagramm dar|
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
|ScatterConnectedByCurvesWithDataMarker|Stellt das durch Kurven verbundene Streudiagramm mit Datenmarkierungen dar|
|ScatterConnectedByCurvesWithoutDataMarker|Stellt das durch Kurven verbundene Streudiagramm ohne Datenmarkierungen dar|
|ScatterConnectedByLinesWithDataMarker|Stellt das durch Linien verbundene Streudiagramm mit Datenmarkierungen dar|
|ScatterConnectedByLinesWithoutDataMarker|Stellt das durch Linien verbundene Streudiagramm dar, ohne Datenmarkierungen|
|Bereich|Stellt das Flächendiagramm dar|
|BereichStacked|Stellt ein gestapeltes Flächendiagramm dar|
|Area100ProcentStacked|Stellt ein 100 % gestapeltes Flächendiagramm dar|
|Bereich3D|Stellt ein 3D-Flächendiagramm dar|
|Area3DStacked|Stellt ein gestapeltes 3D-Flächendiagramm dar|
|Area3D100ProzentStacked|Stellt ein 100 % gestapeltes 3D-Flächendiagramm dar|
|Krapfen|Stellt das Donut-Diagramm dar|
|Donut Explodiert|Stellt das explodierte Donut-Diagramm dar|
|Radar|Stellt das Netzdiagramm dar|
|RadarWithDataMarkers|Stellt das Netzdiagramm mit Datenmarkierungen dar|
|Radargefüllt|Stellt ein gefülltes Netzdiagramm dar|
|Surface3D|Stellt ein 3D-Oberflächendiagramm dar|
|SurfaceWireframe3D|Stellt das Drahtgitter-3D-Oberflächendiagramm dar|
|Oberflächenkontur|Stellt das Konturdiagramm dar|
|SurfaceContourWireframe|Stellt das Drahtmodell-Konturdiagramm dar|
|Blase|Stellt das Blasendiagramm dar|
|Bubble3D|Stellt ein 3D-Blasendiagramm dar|
|Zylinder|Stellt das Zylinderdiagramm dar|
|Zylinder gestapelt|Stellt das gestapelte Zylinderdiagramm dar|
|Zylinder 100 Prozent gestapelt|Repräsentiert ein 100 % gestapeltes Zylinderdiagramm|
|Zylindrischer Stab|Stellt ein zylindrisches Balkendiagramm dar.|
|ZylindrischBarStacked|Stellt ein gestapeltes zylindrisches Balkendiagramm dar|
|ZylindrischBar100ProzentGestapelt|Stellt ein 100 % gestapeltes zylindrisches Balkendiagramm dar|
|ZylindrischeSäule3D|Stellt ein zylindrisches 3D-Säulendiagramm dar|
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
|PyramidBar|Stellt das Pyramiden-Balkendiagramm dar|
|PyramidBarStacked|Stellt ein gestapeltes Pyramiden-Balkendiagramm dar|
|PyramidBar100PercentStacked|Stellt ein 100 % gestapeltes Pyramiden-Balkendiagramm dar|
|PyramidColumn3D|Stellt ein 3D-Pyramiden-Säulendiagramm dar|
So erstellen Sie ein Diagramm mit Aspose.Cells:

1.  Fügen Sie einige Daten zu Arbeitsblattzellen mit hinzu[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) Objekt[**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)Methode.
 Dies wird als Datenquelle für das Diagramm verwendet.
1.  Fügen Sie dem Arbeitsblatt ein Diagramm hinzu, indem Sie die aufrufen[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) Sammlung[*hinzufügen*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int) )-Methode, gekapselt in der[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)Objekt.
1.  Geben Sie den Diagrammtyp mit an[**Diagramm Typ**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)Aufzählung.
 Beispielsweise verwendet das Beispiel die[**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)value als Diagrammtyp.
1.  Greifen Sie auf das Neue zu[**Diagramm**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) Objekt aus der[**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)-Sammlung, indem ihr Index übergeben wird.
1.  Verwenden Sie eines der Diagrammobjekte, die in gekapselt sind[**Diagramm**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)Objekt, um das Diagramm zu verwalten.
 Das folgende Beispiel verwendet die[**SerieSammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)charting-Objekt, um die Datenquelle des Diagramms anzugeben.

Beim Hinzufügen von Quelldaten zum Diagramm kann die Datenquelle ein Zellbereich (z. B. „A1:C3“) oder eine Folge nicht zusammenhängender Zellen (z. B. „A1, A3, A5“) oder eine Folge von sein Werte (z. B. "1,2,3").

{{% alert color="primary" %}}

Wenn Sie einen Zellbereich als Datenquelle zuweisen, können Sie den Bereich nur von links oben nach rechts unten festlegen. Beispielsweise ist „A1:C3“ gültig, während „C3:A1“ ungültig ist.

{{% /alert %}}

Mit diesen allgemeinen Schritten können Sie jede Art von Diagramm erstellen. Verwenden Sie verschiedene Diagrammobjekte, um verschiedene Diagramme zu erstellen.

Wenn der Beispielcode ausgeführt wird, wird dem Arbeitsblatt wie unten gezeigt ein Pyramidendiagramm hinzugefügt.

**Pyramidendiagramm mit seiner Datenquelle**

![todo: Bild_alt_Text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

 Um ein Blasendiagramm zu erstellen, die[**Diagramm Typ**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)muss eingestellt werden[**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)und einige zusätzliche Eigenschaften wie BubbleSizes, Values & XValues müssen entsprechend eingestellt werden. Beim Ausführen des folgenden Codes wird dem Arbeitsblatt ein Blasendiagramm hinzugefügt, wie unten gezeigt.

**Blasendiagramm mit seiner Datenquelle**

![todo: Bild_alt_Text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **Linie mit Datenmarkierungsdiagramm**

Um eine Linie mit einem Datenmarkierungsdiagramm zu erstellen, müssen Sie die[**Diagramm Typ**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)muss eingestellt werden[**Diagrammtyp.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS) und einige zusätzliche Eigenschaften wie Hintergrundbereich, Serienmarkierungen, Werte und XWerte müssen entsprechend festgelegt werden. Beim Ausführen des folgenden Codes wird dem Arbeitsblatt eine Zeile mit einem Datenmarkierungsdiagramm hinzugefügt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **Erstellen von benutzerdefinierten Diagrammen**

Bisher haben wir uns bei der Erörterung von Diagrammen mit Standarddiagrammen befasst, die über ihre Standardformatierungseinstellungen verfügen. Wir definieren nur die Datenquelle, legen ein paar Eigenschaften fest und das Diagramm wird mit seinen Standardformateinstellungen erstellt. Aber Aspose.Cells unterstützt auch das Erstellen benutzerdefinierter Diagramme, mit denen Entwickler Diagramme mit ihren eigenen Formateinstellungen erstellen können.

### **Erstellen von benutzerdefinierten Diagrammen**

Entwickler können benutzerdefinierte Diagramme zur Laufzeit mit Aspose.Cells einfach API erstellen.

 Ein Diagramm besteht aus einer Datenreihe. Jede Datenreihe in Aspose.Cells wird durch a dargestellt[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) Objekt, während die[**SerieSammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) Objekt dient als Sammlung von[**Serie**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)Objekte. Beim Erstellen eines benutzerdefinierten Diagramms haben Entwickler die Freiheit, verschiedene Arten von Diagrammen für verschiedene Datenreihen (gesammelt in einer[**SerieSammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)Objekt).

{{% alert color="primary" %}}

 Derzeit unterstützt Aspose.Cells nur benutzerdefinierte Diagramme, die Torten-, Linien-, Säulen- und Säulenstapeldiagramme kombinieren, aber in zukünftigen Versionen werden weitere Diagramme unterstützt. Eine vollständige Liste der von Aspose.Cells unterstützten Standarddiagramme finden Sie unter[Diagrammtypen](/cells/de/java/chart-types/) Artikel.

{{% /alert %}}

Der folgende Beispielcode zeigt, wie benutzerdefinierte Diagramme erstellt werden. In diesem Beispiel verwenden wir ein Säulendiagramm für die erste Datenreihe und ein Liniendiagramm für die zweite Reihe. Das Ergebnis ist, dass wir dem Arbeitsblatt ein Säulendiagramm in Kombination mit einem Liniendiagramm hinzufügen.

**Benutzerdefiniertes Diagramm, das Säulen- und Liniendiagramme kombiniert**

![todo: Bild_alt_Text](creating-and-customizing-charts_3.png)

**Programmierbeispiel**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

Um eine Liste der unterstützten Diagrammtypen anzuzeigen, lesen Sie die[Diagrammtypen](/cells/de/java/chart-types/) Artikel.

{{% /alert %}}

