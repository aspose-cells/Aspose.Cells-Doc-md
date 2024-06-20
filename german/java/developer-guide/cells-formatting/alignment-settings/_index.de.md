---
title: Ausrichtungseinstellungen
type: docs
weight: 20
url: /de/java/cells-alignment-settings/
---

## **Konfigurieren von Ausrichtungseinstellungen**

## **Ausrichtungseinstellungen in Microsoft Excel**

Jeder, der Microsoft Excel verwendet hat, um Zellen zu formatieren, wird mit den Ausrichtungseinstellungen in Microsoft Excel vertraut sein.

Wie Sie aus der obigen Abbildung sehen können, gibt es verschiedene Arten von Ausrichtungsoptionen:

- Textausrichtung (horizontal & vertikal)
- Einrückung
- Orientierung
- Textkontrolle
- Textrichtung

Alle diese Ausrichtungseinstellungen werden vollständig von Aspose.Cells unterstützt und werden im Folgenden näher erläutert.

## **Ausrichtungseinstellungen in Aspose.Cells**

Aspose.Cells bietet Methoden zum [**GetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getStyle) und [**SetStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle), um die Formatierung einer Zelle abzurufen und festzulegen. Die Klasse [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) stellt nützliche Eigenschaften zur Konfiguration von Ausrichtungseinstellungen bereit.

Wählen Sie einen beliebigen Textausrichtungstyp mithilfe der Aufzählung [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) aus. Die vordefinierten Textausrichtungstypen in der Aufzählung [**TextAlignmentType**](https://reference.aspose.com/cells/java/com.aspose.cells/textalignmenttype) lauten:

|**Textausrichtungstypen**|**Beschreibung**|
| :- | :- |
|Bottom|Stellt die untere Textausrichtung dar
|Center|Stellt die zentrale Textausrichtung dar
|CenterAcross|Stellt die zentrale überkreuzte Textausrichtung dar
|Distributed|Stellt die verteilte Textausrichtung dar
|Fill|Stellt die Fülltextausrichtung dar
|General|Stellt die allgemeine Textausrichtung dar
|Justify|Stellt die Textausrichtung als blocksatz dar
|Left|Stellt die linksbündige Textausrichtung dar
|Right|Stellt die rechtsbündige Textausrichtung dar
|Top|Stellt die obere Textausrichtung dar
|JustifiedLow|Richtet den Text mit einer angepassten Kachidalänge für arabischen Text aus.
|ThaiDistributed|Verteilt insbesondere thailändischen Text, da jeder Buchstabe als Wort behandelt wird.

{{% alert color="primary" %}}

Sie können auch die Blocksatzverteilung mit der Eigenschaft [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsJustifyDistributed) anwenden.

{{% /alert %}}

## **Horizontale, vertikale Ausrichtung und Einrückung**

Verwenden Sie die [**HorizontalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#horizontalalignment) Eigenschaft, um den Text horizontal auszurichten, und die [**VerticalAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/style#verticalalignment) Eigenschaft, um den Text vertikal auszurichten.
Es ist möglich, den Einzugslevel des Textes in einer Zelle mit der [**IndentLevel**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IndentLevel) Eigenschaft festzulegen 
und tt wirkt sich nur aus, wenn die horizontale Ausrichtung links oder rechts ist.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-1.java" >}}


## **Ausrichtung**

Legen Sie die Ausrichtung (Rotation) des Textes in einer Zelle mit der [**RotationAngle**](https://reference.aspose.com/cells/java/com.aspose.cells/style#RotationAngle) Eigenschaft fest.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ConfiguringAlignmentSettings-Orientation-1.java" >}}

## **Textsteuerung**

Im Folgenden wird erläutert, wie Sie Text steuern können, indem Sie Textrahmen, Anpassung an die Größe und andere Formatierungsoptionen festlegen.

### **Textumschlag**

Wenn Text in einer Zelle umgebrochen wird, wird es einfacher zu lesen: Die Höhe der Zelle passt sich an, um den gesamten Text unterzubringen, anstatt ihn abzuschneiden oder in benachbarte Zellen auslaufen zu lassen. Legen Sie den Textumbruch mit der [**IsTextWrapped**](https://reference.aspose.com/cells/java/com.aspose.cells/style#IsTextWrapped) Eigenschaft ein oder aus.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LineBreakTextWrapping-WrapText-1.java" >}}

### **Anpassen an Größe**

Eine Option zum Umbruch von Text in einem Feld besteht darin, die Textgröße anzupassen, um in die Abmessungen einer Zelle zu passen. Dies wird durch Einstellen der [**ShrinkToFit**](https://reference.aspose.com/cells/java/com.aspose.cells/style#ShrinkToFit) Eigenschaft auf **true** erreicht.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ShrinkingToFit-1.java" >}}

### **Zellen zusammenführen**

Wie Microsoft Excel unterstützt auch Aspose.Cells das Zusammenführen mehrerer Zellen in eine. Aspose.Cells bietet zwei Ansätze für diese Aufgabe. Eine Möglichkeit besteht darin, die [**Merge**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) Methode aufzurufen. Die Methode nimmt die folgenden Parameter an, um die Zellen zusammenzuführen:

- Erste Zeile: Die erste Zeile, ab der das Zusammenführen beginnt.
- Erste Spalte: Die erste Spalte, ab der das Zusammenführen beginnt.
- Anzahl der Zeilen: Die Anzahl der zu zusammenführenden Zeilen.
- Anzahl der Spalten: Die Anzahl der zu zusammenführenden Spalten.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "MergingCellsInWorksheet.-1.java" >}}


### **Textausrichtung**

Es ist möglich, die Lesereihenfolge von Text in Zellen festzulegen. Die Lesereihenfolge gibt die visuelle Reihenfolge an, in der Zeichen, Wörter usw. angezeigt werden. Zum Beispiel ist Englisch eine von links nach rechts lesbare Sprache, während Arabisch eine von rechts nach links lesbare Sprache ist.

Die Lesereihenfolge wird mit der [**TextDirection**](https://reference.aspose.com/cells/java/com.aspose.cells/style#TextDirection) Eigenschaft festgelegt. Aspose.Cells bietet vordefinierte Textausrichtungstypen in der [**TextDirectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextDirection) Aufzählung an.

|**Text Direction Types**|**Beschreibung**|
| :- | :- |
|Context|Die Lese-Reihenfolge, die mit der Sprache des ersten eingegebenen Zeichens übereinstimmt|
|LeftToRight|Lesereihenfolge von links nach rechts|
|RightToLeft|Lesereihenfolge von rechts nach links|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ChangeTextDirection-1.java" >}}

## **Erweiterte Themen**
- [Zellenausrichtung ändern und vorhandenes Format beibehalten](/cells/de/java/change-cells-alignment-and-keep-existing-formatting/)
- [Zeilenumbrüche und Textumbrüche](/cells/de/java/line-breaks-and-text-wrapping/)
