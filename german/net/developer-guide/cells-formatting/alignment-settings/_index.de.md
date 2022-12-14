---
title: Ausrichtungseinstellungen
type: docs
weight: 20
url: /de/net/cells-alignment-settings/
---
## **Ausrichtungseinstellungen konfigurieren**

### **Ausrichtungseinstellungen in Microsoft Excel**

Jeder, der Microsoft Excel zum Formatieren von Zellen verwendet hat, ist mit den Ausrichtungseinstellungen in Microsoft Excel vertraut.

Wie Sie der obigen Abbildung entnehmen können, gibt es verschiedene Ausrichtungsoptionen:

- Textausrichtung (horizontal & vertikal)
- Vertiefung.
- Orientierung.
- Textkontrolle.
- Textrichtung.

Alle diese Ausrichtungseinstellungen werden von Aspose.Cells vollständig unterstützt und unten ausführlicher erläutert.

### **Ausrichtungseinstellungen in Aspose.Cells**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Jeder Artikel in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung stellt ein Objekt der[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse.

 Aspose.Cells bietet[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) und[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) Methoden für die[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse, die zum Abrufen und Festlegen der Formatierung einer Zelle verwendet werden. Das[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)-Klasse bietet nützliche Eigenschaften zum Konfigurieren von Ausrichtungseinstellungen.

 Wählen Sie mithilfe von einen beliebigen Textausrichtungstyp aus[**Textausrichtungstyp**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) Aufzählung. Die vordefinierten Textausrichtungstypen in der[**Textausrichtungstyp**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)Aufzählung sind:

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

 Sie können die Justify-Distributed-Einstellung auch mithilfe von anwenden[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed) Eigentum.

{{% /alert %}}

#### **Horizontale Ausrichtung**

 Verwenden Sie die[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**Horizontale Ausrichtung**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)-Eigenschaft, um den Text horizontal auszurichten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

#### **Vertikale Ausrichtung**

 Verwenden Sie ähnlich wie bei der horizontalen Ausrichtung die[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**Vertikale Ausrichtung**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)-Eigenschaft, um den Text vertikal auszurichten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

#### **Vertiefung**

 Es ist möglich, die Einzugsebene des Textes in einer Zelle mit einzustellen[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**Einzugsebene**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

#### **Orientierung**

 Stellen Sie die Ausrichtung (Drehung) des Textes in einer Zelle mit ein[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**Drehwinkel**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle)Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

#### **Textkontrolle**

Im folgenden Abschnitt wird erläutert, wie Sie Text steuern, indem Sie Textumbruch, Anpassen verkleinern und andere Formatierungsoptionen festlegen.

##### **Textumbruch**

 Das Umbrechen von Text in einer Zelle erleichtert das Lesen: Die Höhe der Zelle passt sich an den gesamten Text an, anstatt ihn abzuschneiden oder in benachbarte Zellen zu überlaufen. Stellen Sie den Textumbruch mit ein oder aus[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##### **Schrumpfen, um zu passen**

 Eine Option zum Umbrechen von Text in einem Feld besteht darin, die Textgröße zu verkleinern, um sie an die Abmessungen einer Zelle anzupassen. Dies geschieht durch die Einstellung von[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped) Eigentum zu**Stimmt**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

##### **Cells zusammenführen**

 Wie Microsoft Excel unterstützt Aspose.Cells das Zusammenführen mehrerer Zellen zu einer. Aspose.Cells bietet zwei Ansätze für diese Aufgabe. Eine Möglichkeit ist, die anzurufen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung[**Verschmelzen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) Methode. Das[**Verschmelzen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)Die Methode benötigt die folgenden Parameter, um die Zellen zusammenzuführen:

- Erste Reihe: Die erste Reihe, ab der mit dem Zusammenführen begonnen werden soll.
- Erste Spalte: Die erste Spalte, ab der mit dem Zusammenführen begonnen werden soll.
- Anzahl der Zeilen: Die Anzahl der zusammenzuführenden Zeilen.
- Anzahl der Spalten: Die Anzahl der zusammenzuführenden Spalten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

 Der andere Weg ist, zuerst die anzurufen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung[**Bereich erstellen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) -Methode, um einen Bereich der zu verbindenden Zellen zu erstellen. Das[**Bereich erstellen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) -Methode verwendet denselben Satz von Parametern wie die der[**Verschmelzen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) oben diskutierte Methode und gibt a zurück[**Bereich**](https://reference.aspose.com/cells/net/aspose.cells/range) Objekt. Das[**Bereich**](https://reference.aspose.com/cells/net/aspose.cells/range) Objekt bietet auch a[**Verschmelzen**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) Methode, die den in der angegebenen Bereich zusammenführt[**Bereich**](https://reference.aspose.com/cells/net/aspose.cells/range)Objekt.

##### **Textrichtung**

Es ist möglich, die Lesereihenfolge von Text in Zellen festzulegen. Die Lesereihenfolge ist die visuelle Reihenfolge, in der Zeichen, Wörter usw. angezeigt werden. Zum Beispiel ist Englisch eine Sprache von links nach rechts, während Arabisch eine Sprache von rechts nach links ist.

 Die Lesereihenfolge wird mit eingestellt[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**Textrichtung**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) Eigentum. Aspose.Cells bietet vordefinierte Textrichtungstypen in der[**Textrichtungstyp**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)Aufzählung.

|**Textrichtungstypen**|**Beschreibung**|
|:- |:- |
|Kontext|Die Lesereihenfolge in Übereinstimmung mit der Sprache des ersten eingegebenen Zeichens|
|Links nach rechts|Lesereihenfolge von links nach rechts|
|Rechts nach links|Lesereihenfolge von rechts nach links|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

## **Themen vorantreiben**
- [Ändern Sie die Cells-Ausrichtung und behalten Sie die vorhandene Formatierung bei](/cells/de/net/change-cells-alignment-and-keep-existing-formatting/)
- [Zeilenumbrüche und Textumbruch](/cells/de/net/line-breaks-and-text-wrapping/)

