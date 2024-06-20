---
title: Diagrammformatierung
type: docs
weight: 20
url: /de/java/chart-formatting/
---

## **Diagrammaussehen festlegen**

In den [Diagrammtypen](/cells/de/java/chart-types/) haben wir eine kurze Einführung in die Arten von Diagrammen und Diagrammobjekten von Aspose.Cells gegeben.

In diesem Artikel diskutieren wir, wie man das Aussehen von Diagrammen anpasst, indem man eine Reihe unterschiedlicher Eigenschaften setzt:

- [Festlegen des Diagrammbereichs](/cells/de/java/chart-formatting/#setting-chart-area).
- [Festlegen der Diagrammlinien](/cells/de/java/chart-formatting/#setting-chart-lines).
- [Themen anwenden](/cells/de/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts).
- [Titel für Diagramme und Achsen festlegen](/cells/de/java/chart-formatting/#titel-von-diagrammen-oder-achsen-festlegen).
- [Arbeiten mit Gitterlinien](/cells/de/java/chart-formatting/#festlegen-der-hauptgitterlinien).
- [Rahmen für Hinter- und Seitenwände festlegen](/cells/de/java/chart-formatting/#festlegen-von-rahmen-für-hinter-und-seitenwände).

### **Diagrammbereich einstellen**

Es gibt verschiedene Arten von Bereichen in einem Diagramm und Aspose.Cells bietet die Flexibilität, das Erscheinungsbild jedes Bereichs zu ändern. Entwickler können verschiedene Formatierungseinstellungen auf einen Bereich anwenden, indem sie die Vordergrundfarbe, Hintergrundfarbe und Füllformat usw. ändern.

Im untenstehenden Beispiel haben wir verschiedene Formatierungseinstellungen auf verschiedene Arten von Bereichen eines Diagramms angewendet. Diese Bereiche umfassen:

- Plot-Bereich
- Diagrammbereich
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) Bereich
- Der Bereich eines einzigen Punktes in einem [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

Nach dem Ausführen des Beispielcodes wird ein Säulendiagramm wie unten gezeigt zum Arbeitsblatt hinzugefügt:

**Ein Säulendiagramm mit gefüllten Bereichen** 

![todo:image_alt_text](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **Einstellen von Diagramm Linien**

Entwickler können auch verschiedene Stile auf die Linien oder Datenmarkierungen des [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) anwenden, wie im untenstehenden Beispiel gezeigt. Durch Ausführen des Beispielcodes wird ein Säulendiagramm wie unten gezeigt zum Arbeitsblatt hinzugefügt:

**Säulendiagramm nach Anwendung von Linienstilen** 

![todo:image_alt_text](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **Anwendung von Microsoft Excel 2007/2010-Themen auf Diagramme**

Entwickler können verschiedene Microsoft Excel-Themen und -Farben auf das [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) oder andere Diagrammobjekte anwenden, wie im folgenden Beispiel gezeigt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **Einstellen der Titel von Diagrammen oder Achsen**

Sie können Microsoft Excel verwenden, um die Titel eines Diagramms und seiner Achsen in einer WYSIWYG-Umgebung festzulegen, wie unten gezeigt.

**Titel eines Diagramms & seiner Achsen mit Microsoft Excel festlegen** 

![todo:image_alt_text](chart-formatting_3.png)

Aspose.Cells ermöglicht Entwicklern auch, die Titel eines Diagramms und seiner Achsen zur Laufzeit festzulegen. Alle Diagramme und ihre Achsen enthalten eine [**Title.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text)-Methode, die verwendet werden kann, um ihre Titel wie unten in einem Beispiel gezeigt festzulegen. Nach Ausführung des Beispielcodes wird ein Säulendiagramm wie unten auf dem Arbeitsblatt hinzugefügt:

**Säulendiagramm nach Festlegung der Titel** 

![todo:image_alt_text](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **Festlegen von Hauptgitterlinien**

#### **Ausblenden von Haupt-Gitterlinien**

Entwickler können die Sichtbarkeit der Hauptgitterlinien mithilfe der [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible)-Methode des [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)-Objekts steuern. Nach dem Verstecken der Hauptgitterlinien hat ein dem Arbeitsblatt hinzugefügtes Säulendiagramm das folgende Aussehen:

**Ein Säulendiagramm mit versteckten Hauptgitterlinien** 

![todo:image_alt_text](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **Ändern der Einstellungen für Haupt-Gitterlinien**

Entwickler können nicht nur die Sichtbarkeit der Hauptgitterlinien steuern, sondern auch andere Eigenschaften wie deren Farbe usw. festlegen. Nach Festlegen der Farbe der Hauptgitterlinien hat ein dem Arbeitsblatt hinzugefügtes Säulendiagramm das folgende Aussehen:

**Säulendiagramm mit farbigen Hauptgitterlinien** 

![todo:image_alt_text](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **Festlegen von Rahmen für Rück- und Seitenwände**

Seit der Veröffentlichung von Microsoft Excel 2007 wurden die Wände eines 3D-Diagramms in zwei Teile unterteilt: Seitenwand und Rückwand, sodass wir zwei [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls)-Objekte verwenden müssen, um sie separat darzustellen, und Sie können darauf zugreifen, indem Sie [**Chart.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall) und [**Chart.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall) verwenden.

Das unten gezeigte Beispiel zeigt, wie der Rahmen der Seitenwand mithilfe verschiedener Attribute festgelegt wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **Ändern der Diagrammposition und -größe**

Manchmal möchten Sie die Position oder Größe des neuen oder vorhandenen Diagramms innerhalb des Arbeitsblatts ändern. Aspose.Cells bietet die [**Chart.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject)-Eigenschaft, um dies zu erreichen. Sie können ihre Unterattribute verwenden, um das Diagramm mit neuer **Höhe** und **Breite** neu zu skalieren oder mit neuen **X**- und **Y**-Koordinaten neu zu positionieren.

### **Ändern von Position und Größe des Diagramms**

Um die Position (X,Y-Koordinaten) und Größe (Höhe, Breite) des Diagramms zu ändern, verwenden Sie diese Eigenschaften:

1. [**Chart.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Chart.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Chart.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Chart.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

Das folgende Beispiel erläutert die Verwendung der obigen Eigenschaften. Es lädt die vorhandene Arbeitsmappe, die ein Diagramm in ihrem ersten Arbeitsblatt enthält. Dann ändert es die Größe und Position des Diagramms und speichert die Arbeitsmappe.

Vor der Ausführung des Beispielcodes sieht die Quelldatei so aus:

**Diagrammgröße und -position vor der Ausführung des Beispielcodes** 

![todo:image_alt_text](chart-formatting_7.png)

Nach der Ausführung sieht die Ausgabedatei so aus:

**Diagrammgröße und -position nach der Ausführung des Beispielcodes** 

![todo:image_alt_text](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **Manipulation von Designer-Diagrammen**

Es gibt Momente, in denen Sie möglicherweise die Diagramme in Ihren Designer-Vorlagendateien manipulieren oder ändern müssen. Aspose.Cells unterstützt vollständig das Manipulieren von Designer-Diagrammen mit ihren Inhalten und Elementen. Die Daten, Diagramminhalte, Hintergrundbild und Formatierung können mit Genauigkeit beibehalten werden.

### **Manipulation von Designer-Diagrammen in den Vorlagendateien**

Verwenden Sie zum Manipulieren von Designer-Diagrammen in einer Vorlagendatei alle diagrammspezifischen API-Aufrufe. Verwenden Sie beispielsweise die [**Worksheet.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts)-Eigenschaft, um die vorhandene Diagrammsammlung in der Vorlagendatei zu erhalten.

#### **Erstellen eines Diagramms**

Das folgende Beispiel zeigt, wie man ein Tortendiagramm erstellt. Später werden wir dieses Diagramm manipulieren. Die folgende Ausgabe wird vom Code generiert.

**Das Eingabe-Tortendiagramm** 

![todo:image_alt_text](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **Manipulation des Diagramms**

Das folgende Beispiel zeigt, wie man das vorhandene Diagramm manipuliert. In diesem Beispiel modifizieren wir das oben erstellte Diagramm. Die folgende Ausgabe wird vom Code generiert. Beachten Sie, dass die Farbe des Diagrammtitels von blau auf schwarz geändert wurde und 'England 30000' zu 'Vereinigtes Königreich, 30K' geändert wurde.

**Das Tortendiagramm wurde geändert** 

![todo:image_alt_text](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **Manipulation eines Liniendiagramms in der Designer-Vorlage**

In diesem Beispiel werden wir ein Liniendiagramm manipulieren. Wir werden einige Datenreihen zu dem vorhandenen Diagramm hinzufügen und deren Linienfarben ändern.

Sehen Sie sich zunächst das Designer-Liniendiagramm an.

**Das Eingabe-Liniendiagramm** 

![todo:image_alt_text](chart-formatting_11.png)

Nun manipulieren wir das Liniendiagramm (das in der Datei **linechart.xls** enthalten ist) mit dem folgenden Code. Die folgende Ausgabe wird vom Code generiert.

**Die manipulierte Liniendiagramm** 

![todo:image_alt_text](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **Verwendung von Sparklines**

Microsoft Excel 2010 kann Informationen auf vielfältige Weise analysieren. Es ermöglicht Benutzern, wichtige Datentrends mit neuen Datenanalyse- und Visualisierungstools nachzuverfolgen und hervorzuheben. Sparklines sind Mini-Diagramme, die Sie innerhalb von Zellen platzieren können, um Daten und Diagramme in derselben Tabelle anzuzeigen. Wenn Sparklines richtig verwendet werden, ist die Datenanalyse schneller und präziser. Sie bieten auch einen einfachen Überblick über Informationen, vermeiden überfüllte Arbeitsblätter mit vielen belebten Diagrammen.

Aspose.Cells bietet eine API zur Manipulation von Sparklines in Tabellenkalkulationen.

### **Sparklines in Microsoft Excel**

Um Sparklines in Microsoft Excel 2010 einzufügen:

1. Wählen Sie die Zellen aus, in denen die Sparklines erscheinen sollen. Um sie leicht zu sehen, wählen Sie Zellen neben den Daten aus.
1. Klicken Sie auf **Einfügen** im Menüband und wählen Sie dann **Spalte** in der Gruppe **Sparklines** aus.

![todo:image_alt_text](chart-formatting_13.png)

1. Wählen Sie den Bereich von Zellen im Arbeitsblatt aus, der die Datenquelle enthält.
   Die Diagramme erscheinen.

Sparklines helfen dabei, Trends zu erkennen, beispielsweise den Sieg oder die Niederlage eines Softball-Teams. Sparklines können sogar die gesamte Saison jedes Teams in der Liga zusammenfassen.

![todo:image_alt_text](chart-formatting_14.png)

### **Sparklines mit Aspose.Cells verwenden**

Entwickler können mithilfe der bereitgestellten API von Aspose.Cells Sparklines in Tabellenkalkulationen erstellen, löschen oder lesen. Indem benutzerdefinierte Grafiken für einen bestimmten Datenbereich hinzugefügt werden, haben Entwickler die Möglichkeit, verschiedene Arten von Mini-Diagrammen in ausgewählten Zellbereichen hinzuzufügen.

Das folgende Beispiel zeigt die Sparklines-Funktion. Das Beispiel zeigt, wie man:

1. Eine einfache Vorlagendatei öffnen.
1. Sparklines-Informationen für ein Arbeitsblatt lesen.
1. Neue Sparklines für einen bestimmten Datenbereich zu einem Zellbereich hinzufügen.
1. Speichert die Excel-Datei auf der Festplatte.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **Anwendung von 3D-Format auf Diagramm**

Es können 3D-Diagrammstile erforderlich sein, um genau die Ergebnisse für Ihr Szenario zu erhalten. Aspose.Cells APIs bieten die entsprechende API zur Anwendung von Microsoft Excel 2007 3D-Formatierung, wie in diesem Artikel gezeigt.

### **Einstellung 3D-Format für Diagramm**

Ein vollständiges Beispiel ist unten gegeben, um zu zeigen, wie man ein Diagramm erstellt und das 3D-Format von Microsoft Excel 2007 anwendet. Nach Ausführen des obigen Beispielcodes wird ein Säulendiagramm (mit 3D-Effekten) wie unten gezeigt zum Arbeitsblatt hinzugefügt.

**Ein Säulendiagramm mit 3D-Formatierung**

![todo:image_alt_text](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

Für eine vollständige Liste der unterstützten 2D- und 3D-Diagramme siehe [Unterstützte Diagrammtypen für die Darstellung](/cells/de/java/chart-rendering/#supported-chart-types-for-rendering).

{{% /alert %}}

## **Erweiterte Themen**
- [Bild als Hintergrundfüllung im Diagramm festlegen](/cells/de/java/set-picture-as-background-fill-in-the-chart/)
