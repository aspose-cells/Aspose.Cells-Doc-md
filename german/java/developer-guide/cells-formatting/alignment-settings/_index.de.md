---
title: Ausrichtungseinstellungen
type: docs
weight: 20
url: /de/java/cells-alignment-settings/
---
## **Ausrichtungseinstellungen konfigurieren**

## **Ausrichtungseinstellungen in Microsoft Excel**

Jeder, der Microsoft Excel zum Formatieren von Zellen verwendet hat, ist mit den Ausrichtungseinstellungen in Microsoft Excel vertraut.

Wie Sie der obigen Abbildung entnehmen können, gibt es verschiedene Ausrichtungsoptionen:

- Textausrichtung (horizontal & vertikal)
- Vertiefung.
- Orientierung.
- Textsteuerung.
- Textrichtung.

Alle diese Ausrichtungseinstellungen werden von Aspose.Cells vollständig unterstützt und unten ausführlicher erläutert.

## **Ausrichtungseinstellungen in Aspose.Cells**

 Aspose.Cells bietet[**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) und[**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle) Methoden für die[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) Klasse, die zum Abrufen und Festlegen der Formatierung einer Zelle verwendet werden. Das[**Stil**](https://reference.aspose.com/cells/java/com.aspose.cells/style)-Klasse bietet nützliche Eigenschaften zum Konfigurieren von Ausrichtungseinstellungen.

 Wählen Sie mithilfe von einen beliebigen Textausrichtungstyp aus[**Textausrichtungstyp**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) Aufzählung. Die vordefinierten Textausrichtungstypen in der[**Textausrichtungstyp**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype)Aufzählung sind:

|**Textausrichtungstypen**|**Beschreibung**|
|:- |:- |
|Unterseite|Stellt die untere Textausrichtung dar|
|Center|Stellt die zentrierte Textausrichtung dar|
|CenterAcross|Stellt die Mitte über der Textausrichtung dar|
|Verteilt|Stellt die verteilte Textausrichtung dar|
|Füllen|Stellt die Fülltextausrichtung dar|
|Allgemein|Stellt die allgemeine Textausrichtung dar|
|Rechtfertigen|Stellt die Textausrichtung im Blocksatz dar|
|Links|Stellt die linke Textausrichtung dar|
|Recht|Stellt die rechte Textausrichtung dar|
|oben|Stellt die obere Textausrichtung dar|
|GerechtfertigtNiedrig|Richtet den Text mit einer angepassten Kashida-Länge für arabischen Text aus.|
|ThaiDistributed|Verteilt besonders thailändischen Text, da jedes Zeichen als Wort behandelt wird.|

{{% alert color="primary" %}}

 Sie können die Justify-Distributed-Einstellung auch mithilfe von anwenden[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed) Eigentum.

{{% /alert %}}

## **Horizontale, vertikale Ausrichtung und Einrückung**

 Verwenden Sie die[**Horizontale Ausrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) -Eigenschaft, um den Text horizontal auszurichten und[**Vertikale Ausrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment)-Eigenschaft, um den Text vertikal auszurichten.
 Es ist möglich, die Einzugsebene des Textes in einer Zelle mit einzustellen[**Einzugsebene**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel) Eigentum
und tt wirken sich nur aus, wenn die horizontale Ausrichtung links oder rechts ist.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **Orientierung**

 Stellen Sie die Ausrichtung (Drehung) des Textes in einer Zelle mit ein[**Drehwinkel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle)Eigentum.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **Textsteuerung**

Im folgenden Abschnitt wird erläutert, wie Sie Text steuern, indem Sie Textumbruch, Anpassen verkleinern und andere Formatierungsoptionen festlegen.

### **Textumbruch**

 Das Umbrechen von Text in einer Zelle erleichtert das Lesen: Die Höhe der Zelle passt sich an den gesamten Text an, anstatt ihn abzuschneiden oder in benachbarte Zellen zu überlaufen. Stellen Sie den Textumbruch mit ein oder aus[**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped)Eigentum.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **Schrumpfen, um zu passen**

 Eine Option zum Umbrechen von Text in einem Feld besteht darin, die Textgröße zu verkleinern, um sie an die Abmessungen einer Zelle anzupassen. Dies geschieht durch die Einstellung von[**Schrumpfen bis es passt**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit) Eigentum. zu**Stimmt**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **Cells zusammenführen**

 Wie Microsoft Excel unterstützt Aspose.Cells das Zusammenführen mehrerer Zellen zu einer. Aspose.Cells bietet zwei Ansätze für diese Aufgabe. Eine Möglichkeit ist, die anzurufen[**Verschmelzen**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) Methode. Die Methode benötigt die folgenden Parameter, um die Zellen zusammenzuführen:

- Erste Reihe: Die erste Reihe, ab der mit dem Zusammenführen begonnen werden soll.
- Erste Spalte: Die erste Spalte, ab der mit dem Zusammenführen begonnen werden soll.
- Anzahl der Zeilen: Die Anzahl der zusammenzuführenden Zeilen.
- Anzahl der Spalten: Die Anzahl der zusammenzuführenden Spalten.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **Textrichtung**

Es ist möglich, die Lesereihenfolge von Text in Zellen festzulegen. Die Lesereihenfolge ist die visuelle Reihenfolge, in der Zeichen, Wörter usw. angezeigt werden. Zum Beispiel ist Englisch eine Sprache von links nach rechts, während Arabisch eine Sprache von rechts nach links ist.

 Die Lesereihenfolge wird mit eingestellt[**Textrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection) Eigentum. Aspose.Cells bietet vordefinierte Textrichtungstypen in der[**Textrichtungstyp**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection)Aufzählung.

|**Textrichtungstypen**|**Beschreibung**|
|:- |:- |
|Kontext|Die Lesereihenfolge in Übereinstimmung mit der Sprache des ersten eingegebenen Zeichens|
|Links nach rechts|Lesereihenfolge von links nach rechts|
|Rechts nach links|Lesereihenfolge von rechts nach links|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **Themen vorantreiben**
- [Ändern Sie die Cells-Ausrichtung und behalten Sie die vorhandene Formatierung bei](/cells/de/java/change-cells-alignment-and-keep-existing-formatting/)
- [Zeilenumbrüche und Textumbruch](/cells/de/java/line-breaks-and-text-wrapping/)
