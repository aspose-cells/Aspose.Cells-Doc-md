---
title: Diagrammformatierung
type: docs
weight: 20
url: /de/java/chart-formatting/
---
## **Darstellung des Diagramms einstellen**

 Im[Diagrammtypen](/cells/de/java/chart-types/)gaben wir eine kurze Einführung in die Arten von Diagrammen und Diagrammobjekten, die von Aspose.Cells angeboten werden.

In diesem Artikel besprechen wir, wie Sie das Erscheinungsbild von Diagrammen anpassen können, indem Sie eine Reihe verschiedener Eigenschaften festlegen:

- [Einstellen des Diagrammbereichs](/cells/de/java/chart-formatting/#setting-chart-area).
- [Diagrammlinien setzen](/cells/de/java/chart-formatting/#setting-chart-lines).
- [Themen anwenden](/cells/de/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts).
- [Titel für Diagramme und Achsen festlegen](/cells/de/java/chart-formatting/#setting-the-titles-of-charts-or-axes).
- [Arbeiten mit Gitterlinien](/cells/de/java/chart-formatting/#setting-major-gridlines).
- [Randeinfassungen für Rück- und Seitenwände setzen](/cells/de/java/chart-formatting/#setting-borders-for-back-and-side-walls).

### **Diagrammbereich einstellen**

Es gibt verschiedene Arten von Bereichen in einem Diagramm und Aspose.Cells bietet die Flexibilität, das Erscheinungsbild jedes Bereichs zu ändern. Entwickler können verschiedene Formatierungseinstellungen auf einen Bereich anwenden, indem sie dessen Vordergrundfarbe, Hintergrundfarbe und Füllformat usw. ändern.

In dem unten angegebenen Beispiel haben wir verschiedene Formatierungseinstellungen auf verschiedene Arten von Bereichen eines Diagramms angewendet. Zu diesen Bereichen gehören:

- Grundstücksfläche
- Diagrammbereich
- [**SerieSammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) Bereich
- Die Fläche eines einzelnen Punktes in einer[**SerieSammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

Nach dem Ausführen des Beispielcodes wird dem Arbeitsblatt ein Säulendiagramm hinzugefügt, wie unten gezeigt:

**Ein Säulendiagramm mit gefüllten Bereichen** 

![todo: Bild_alt_Text](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **Diagrammlinien festlegen**

 Entwickler können auch verschiedene Arten von Stilen auf die Linien oder Datenmarkierungen des anwenden[**SerieSammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)wie unten im Beispiel gezeigt. Durch Ausführen des Beispielcodes wird dem Arbeitsblatt ein Säulendiagramm wie unten gezeigt hinzugefügt:

**Säulendiagramm nach dem Anwenden von Linienstilen** 

![todo: Bild_alt_Text](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **Anwenden von Microsoft Excel 2007/2010-Designs auf Diagramme**

 Entwickler können verschiedene Microsoft Excel-Designs und -Farben auf die anwenden[**SerieSammlung**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)oder andere Diagrammobjekte, wie im Beispiel unten gezeigt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **Festlegen der Titel von Diagrammen oder Achsen**

Sie können Microsoft Excel verwenden, um die Titel eines Diagramms und seine Achsen in einer WYSIWYG-Umgebung festzulegen, wie unten gezeigt.

**Festlegen von Titeln eines Diagramms und seiner Achsen mit Microsoft Excel** 

![todo: Bild_alt_Text](chart-formatting_3.png)

Aspose.Cells ermöglicht es Entwicklern auch, die Titel eines Diagramms und seiner Achsen zur Laufzeit festzulegen. Alle Diagramme und ihre Achsen enthalten a[**Titel.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text)Methode, die verwendet werden kann, um ihre Titel festzulegen, wie unten in einem Beispiel gezeigt. Nach dem Ausführen des Beispielcodes wird dem Arbeitsblatt ein Säulendiagramm hinzugefügt, wie unten gezeigt:

**Säulendiagramm nach dem Festlegen von Titeln** 

![todo: Bild_alt_Text](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **Festlegen von Hauptrasterlinien**

#### **Ausblenden wichtiger Gitternetzlinien**

 Entwickler können die Sichtbarkeit wichtiger Gitternetzlinien mithilfe von steuern[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible) Methode der[**Linie**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)Objekt. Nach dem Ausblenden der Hauptgitterlinien sieht ein dem Arbeitsblatt hinzugefügtes Säulendiagramm wie folgt aus:

**Ein Säulendiagramm mit ausgeblendeten Hauptgitterlinien** 

![todo: Bild_alt_Text](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **Ändern der Einstellungen für Hauptgitterlinien**

Entwickler können nicht nur die Sichtbarkeit der Hauptgitterlinien steuern, sondern auch andere Eigenschaften, einschließlich ihrer Farbe usw. Nach dem Festlegen der Farbe der Hauptgitterlinien sieht ein dem Arbeitsblatt hinzugefügtes Säulendiagramm wie folgt aus:

**Säulendiagramm mit farbigen Hauptgitterlinien** 

![todo: Bild_alt_Text](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **Rahmen für Rück- und Seitenwände festlegen**

 Seit der Veröffentlichung von Microsoft Excel 2007 sind die Wände eines 3D-Diagramms in zwei Teile geteilt: Seitenwand und Rückwand, also müssen wir zwei verwenden[**Wände**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls) Objekte, um sie separat darzustellen, und Sie können auf sie zugreifen, indem Sie verwenden[**Chart.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall) und[**Chart.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall).

Das folgende Beispiel zeigt, wie Sie den Rand der Seitenwand mithilfe verschiedener Attribute festlegen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **Ändern Sie die Position und Größe des Diagramms**

 Manchmal möchten Sie die Position oder Größe des neuen oder vorhandenen Diagramms innerhalb des Arbeitsblatts ändern. Aspose.Cells bietet die[**Chart.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject) Eigenschaft, dies zu erreichen. Sie können die Untereigenschaften verwenden, um die Größe des Diagramms mit neu zu ändern**Höhe** und**Breite** oder mit new neu positionieren** X** und**Y**-Koordinaten.

### **Position und Größe des Diagramms ändern**

Um die Position (X-, Y-Koordinaten) und die Größe (Höhe, Breite) des Diagramms zu ändern, verwenden Sie diese Eigenschaften:

1. [**Chart.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Chart.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Chart.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Chart.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

Das folgende Beispiel erläutert die Verwendung der oben genannten Eigenschaften. Es lädt die vorhandene Arbeitsmappe, die ein Diagramm in ihrem ersten Arbeitsblatt enthält. Dann ändert es die Größe und Position des Diagramms und speichert die Arbeitsmappe.

Vor der Ausführung des Beispielcodes sieht die Quelldatei so aus:

**Diagrammgröße und -position vor der Ausführung des Beispielcodes** 

![todo: Bild_alt_Text](chart-formatting_7.png)

Nach der Ausführung sieht die Ausgabedatei so aus:

**Diagrammgröße und Position nach der Ausführung des Beispielcodes** 

![todo: Bild_alt_Text](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **Bearbeiten von Designer-Diagrammen**

Es kann vorkommen, dass Sie die Diagramme in Ihren Designer-Vorlagendateien bearbeiten oder ändern müssen. Aspose.Cells unterstützt vollständig die Bearbeitung von Designer-Diagrammen mit ihren Inhalten und Elementen. Die Daten, Diagramminhalte, Hintergrundbilder und Formatierungen können genau beibehalten werden.

### **Bearbeiten von Designer-Diagrammen in den Vorlagendateien**

 Verwenden Sie zum Bearbeiten von Designerdiagrammen in einer Vorlagendatei alle diagrammbezogenen API-Aufrufe. Verwenden Sie zum Beispiel[**Arbeitsblatt.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts) -Eigenschaft, um die vorhandene Diagrammsammlung in der Vorlagendatei abzurufen.

#### **Erstellen eines Diagramms**

Das folgende Beispiel zeigt, wie Sie ein Kreisdiagramm erstellen. Wir werden dieses Diagramm später manipulieren. Die folgende Ausgabe wird vom Code generiert.

**Das Eingabe-Kreisdiagramm** 

![todo: Bild_alt_Text](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **Manipulation des Diagramms**

Das folgende Beispiel zeigt, wie das vorhandene Diagramm bearbeitet wird. In diesem Beispiel ändern wir das oben erstellte Diagramm. Die folgende Ausgabe wird vom Code generiert. Beachten Sie, dass sich die Farbe des Diagrammtitels von Blau zu Schwarz geändert hat und „England 30000“ in „Vereinigtes Königreich, 30K“ geändert wurde.

**Das Tortendiagramm wurde geändert** 

![todo: Bild_alt_Text](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **Bearbeiten eines Liniendiagramms in der Designer-Vorlage**

In diesem Beispiel bearbeiten wir ein Liniendiagramm. Wir werden dem bestehenden Diagramm einige Datenreihen hinzufügen und ihre Linienfarben ändern.

Werfen Sie zunächst einen Blick auf das Designer-Liniendiagramm.

**Das Eingabeliniendiagramm** 

![todo: Bild_alt_Text](chart-formatting_11.png)

 Nun manipulieren wir das Liniendiagramm (das in der**Liniendiagramm.xls** Datei) mit dem folgenden Code. Die folgende Ausgabe wird vom Code generiert.

**Das manipulierte Liniendiagramm** 

![todo: Bild_alt_Text](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **Verwendung von Sparklines**

Microsoft Excel 2010 kann Informationen auf mehr Arten als je zuvor analysieren. Es ermöglicht Benutzern, wichtige Datentrends mit neuen Datenanalyse- und Visualisierungstools zu verfolgen und hervorzuheben. Sparklines sind Minidiagramme, die Sie in Zellen platzieren können, sodass Sie Daten und Diagramme in derselben Tabelle anzeigen können. Wenn Sparklines richtig eingesetzt werden, ist die Datenanalyse schneller und präziser. Sie bieten auch eine einfache Ansicht von Informationen und vermeiden überfüllte Arbeitsblätter mit vielen geschäftigen Diagrammen.

Aspose.Cells bietet ein API zum Bearbeiten von Sparklines in Tabellenkalkulationen.

### **Sparklines in Microsoft Excel**

So fügen Sie Sparklines in Microsoft Excel 2010 ein:

1. Wählen Sie die Zellen aus, in denen die Sparklines erscheinen sollen. Um sie einfacher anzuzeigen, wählen Sie Zellen neben den Daten aus.
1.  Klicken**Einfügung** auf dem Band und wählen Sie dann**Säule** in dem**Sparklines** Gruppe.

![todo: Bild_alt_Text](chart-formatting_13.png)

1. Wählen Sie den Zellbereich im Arbeitsblatt aus, der die Quelldaten enthält, oder geben Sie ihn ein.
 Die Diagramme werden angezeigt.

Sparklines helfen Ihnen beispielsweise dabei, Trends oder die Gewinn- oder Verlustbilanz einer Softball-Liga zu erkennen. Sparklines kann sogar die gesamte Saison jedes Teams in der Liga zusammenfassen.

![todo: Bild_alt_Text](chart-formatting_14.png)

### **Sparklines mit Aspose.Cells**

Entwickler können Sparklines (in der Vorlagendatei) mit dem von Aspose.Cells bereitgestellten API erstellen, löschen oder lesen. Durch Hinzufügen benutzerdefinierter Grafiken für einen bestimmten Datenbereich haben Entwickler die Freiheit, verschiedene Arten von winzigen Diagrammen zu ausgewählten Zellbereichen hinzuzufügen.

Das folgende Beispiel zeigt die Sparklines-Funktion. Das Beispiel zeigt, wie Sie:

1. Öffnen Sie eine einfache Vorlagendatei.
1. Sparklines-Informationen für ein Arbeitsblatt lesen.
1. Fügen Sie einem Zellbereich neue Sparklines für einen bestimmten Datenbereich hinzu.
1. Speichert die Excel-Datei auf der Festplatte.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **Anwenden des 3D-Formats auf das Diagramm**

Möglicherweise benötigen Sie 3D-Diagrammstile, damit Sie genau die Ergebnisse für Ihr Szenario erhalten. Aspose.Cells-APIs stellen die relevanten API bereit, um die Microsoft Excel 2007-3D-Formatierung anzuwenden, wie in diesem Artikel gezeigt.

### **Einstellen des 3D-Formats auf Diagramm**

Nachfolgend finden Sie ein vollständiges Beispiel, um zu demonstrieren, wie Sie ein Diagramm erstellen und die Microsoft Excel 2007 3D-Formatierung anwenden. Nach dem Ausführen des obigen Beispielcodes wird dem Arbeitsblatt ein Säulendiagramm (mit 3D-Effekten) hinzugefügt, wie unten gezeigt.

**Ein Säulendiagramm mit 3D-Formatierung**

![todo: Bild_alt_Text](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

 Eine vollständige Liste der unterstützten 2D- und 3D-Diagramme finden Sie unter[Unterstützte Diagrammtypen für das Rendern](/cells/de/java/chart-rendering/#supported-chart-types-for-rendering).

{{% /alert %}}

## **Themen vorantreiben**
- [Bild als Hintergrund festlegen Füllen Sie das Diagramm aus](/cells/de/java/set-picture-as-background-fill-in-the-chart/)
