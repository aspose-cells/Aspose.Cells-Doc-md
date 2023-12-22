---
title: Ausrichtungseinstellungen
description: In der Bibliothek Aspose.Cells können Sie Zellenausrichtungseinstellungen verwenden, um das Layout und die Anzeige von Text anzupassen. Durch Anpassen von Einstellungen wie horizontaler Ausrichtung, vertikaler Ausrichtung und Textumbruch haben Sie mehr Kontrolle darüber, wie Text in Zellen fließt. Dieses Dokument stellt Ihnen detaillierte Schritte und Beispielcode zur Verfügung, damit Sie schnell verstehen, wie Sie Aspose.Cells für Zellenausrichtungseinstellungen verwenden.
keywords: Aspose.Cells, cell alignment, horizontal alignment, vertical alignment, text wrapping
type: docs
weight: 20
url: /de/net/cells-alignment-settings/
---
##  **Ausrichtungseinstellungen konfigurieren**

###  **Ausrichtungseinstellungen in Microsoft Excel**

Jeder, der Microsoft Excel zum Formatieren von Zellen verwendet hat, ist mit den Ausrichtungseinstellungen in Microsoft Excel vertraut.

Wie Sie der obigen Abbildung entnehmen können, gibt es verschiedene Arten der Ausrichtung:

- Textausrichtung (horizontal und vertikal)
- Vertiefung.
- Orientierung.
- Textkontrolle.
- Textrichtung.

Alle diese Ausrichtungseinstellungen werden von Aspose.Cells vollständig unterstützt und werden im Folgenden ausführlicher erläutert.

###  **Ausrichtungseinstellungen in Aspose.Cells**

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , das eine Excel-Datei darstellt. Der[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet a[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung. Jedes Element in der[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Die Sammlung stellt ein Objekt dar[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)Klasse.

 Aspose.Cells bietet[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) Und[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) Methoden für die[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) Klasse, die zum Abrufen und Festlegen der Formatierung einer Zelle verwendet wird. Der[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)Die Klasse bietet nützliche Eigenschaften zum Konfigurieren von Ausrichtungseinstellungen.

 Wählen Sie mithilfe von einen beliebigen Textausrichtungstyp aus[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype) Aufzählung. Die vordefinierten Textausrichtungstypen im[**TextAlignmentType**](https://reference.aspose.com/cells/net/aspose.cells/textalignmenttype)Aufzählung sind:

|**Textausrichtungstypen**|**Beschreibung**|
| :- | :- |
|Unten|Stellt die Textausrichtung unten dar|
|Center|Stellt die Textausrichtung in der Mitte dar|
|CenterAcross|Stellt die zentrierte Textausrichtung dar|
|Verteilt|Stellt die verteilte Textausrichtung dar|
|Füllen|Stellt die Ausrichtung des Fülltexts dar|
|Allgemein|Stellt die allgemeine Textausrichtung dar|
|Rechtfertigen|Stellt die Textausrichtung im Blocksatz dar|
|Links|Stellt die linke Textausrichtung dar|
|Rechts|Stellt die rechte Textausrichtung dar|
|Spitze|Stellt die Textausrichtung oben dar|
|BegründetNiedrig|Richtet den Text an einer angepassten Kashida-Länge für arabischen Text aus.|
|ThailändischDistributed|Verteilt insbesondere thailändischen Text, da jedes Zeichen als Wort behandelt wird.|

{{% alert color="primary" %}}

 Sie können die Einstellung „Verteilt ausrichten“ auch mithilfe von anwenden[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/isjustifydistributed) Eigentum.

{{% /alert %}}

####  **Horizontale Ausrichtung**

 Benutzen Sie die[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**HorizontaleAusrichtung**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/horizontalalignment)Eigenschaft, um den Text horizontal auszurichten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.cs" >}}

####  **Vertikale Ausrichtung**

 Verwenden Sie ähnlich wie bei der horizontalen Ausrichtung die[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**Vertikale Ausrichtung**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/verticalalignment)Eigenschaft, um den Text vertikal auszurichten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.cs" >}}

####  **Vertiefung**

 Es ist möglich, die Einrückungsstufe des Textes in einer Zelle mit festzulegen[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**Einzugsebene**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/indentlevel)Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Indentation-1.cs" >}}

####  **Orientierung**

 Legen Sie die Ausrichtung (Rotation) des Textes in einer Zelle mit fest[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**Drehwinkel**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/rotationangle)Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-Orientation-1.cs" >}}

####  **Textkontrolle**

Im folgenden Abschnitt wird erläutert, wie Sie Text steuern, indem Sie den Textumbruch, die Größe anpassen und andere Formatierungsoptionen festlegen.

#####  **Text umschließen**

 Das Umschließen von Text in einer Zelle erleichtert das Lesen: Die Höhe der Zelle wird so angepasst, dass sie in den gesamten Text passt, anstatt ihn abzuschneiden oder in benachbarte Zellen zu überlaufen. Aktivieren oder deaktivieren Sie den Textumbruch mit[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

#####  **Auf die richtige Größe schrumpfen**

 Eine Option zum Umbrechen von Text in einem Feld besteht darin, die Textgröße zu verkleinern, um sie an die Abmessungen einer Zelle anzupassen. Dies geschieht durch die Einstellung[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)Eigenschaft auf *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.cs" >}}

#####  **Zusammenführen von Cells**

 Wie Microsoft Excel unterstützt Aspose.Cells das Zusammenführen mehrerer Zellen zu einer. Aspose.Cells bietet zwei Ansätze für diese Aufgabe. Eine Möglichkeit besteht darin, die anzurufen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung[**Verschmelzen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) Methode. Der[**Verschmelzen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index)Die Methode benötigt die folgenden Parameter, um die Zellen zusammenzuführen:

- Erste Reihe: die erste Reihe, ab der mit dem Zusammenführen begonnen werden soll.
- Erste Spalte: die erste Spalte, ab der mit der Zusammenführung begonnen werden soll.
- Anzahl der Zeilen: Die Anzahl der zusammenzuführenden Zeilen.
- Anzahl der Spalten: Die Anzahl der zusammenzuführenden Spalten.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-Merging-MergingCellsInWorksheet.-1.cs" >}}

Die andere Möglichkeit besteht darin, zuerst die anzurufen[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) Sammlung[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) Methode zum Erstellen eines Bereichs der zusammenzuführenden Zellen. Der[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/createrange/index) Die Methode verwendet denselben Parametersatz wie die[**Verschmelzen**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/merge/index) Methode, die oben besprochen wurde, und gibt a zurück[**Reichweite**](https://reference.aspose.com/cells/net/aspose.cells/range) Objekt. Der[**Reichweite**](https://reference.aspose.com/cells/net/aspose.cells/range) Objekt bietet auch a[**Verschmelzen**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) Methode, die den in der angegebenen Bereich zusammenführt[**Reichweite**](https://reference.aspose.com/cells/net/aspose.cells/range)Objekt.

#####  **Textrichtung**

Es ist möglich, die Lesereihenfolge von Text in Zellen festzulegen. Die Lesereihenfolge ist die visuelle Reihenfolge, in der Zeichen, Wörter usw. angezeigt werden. Beispielsweise ist Englisch eine von links nach rechts verlaufende Sprache, während Arabisch eine von rechts nach links verlaufende Sprache ist.

 Die Lesereihenfolge wird mit festgelegt[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) Objekt[**Textrichtung**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/textdirection) Eigentum. Aspose.Cells bietet vordefinierte Textrichtungstypen im[**TextDirectionType**](https://reference.aspose.com/cells/net/aspose.cells/textdirectiontype)Aufzählung.

|**Textrichtungstypen**|**Beschreibung**|
| :- | :- |
|Kontext|Die Lesereihenfolge entspricht der Sprache des ersten eingegebenen Zeichens|
|Links nach rechts|Lesereihenfolge von links nach rechts|
|Rechts nach links|Lesereihenfolge von rechts nach links|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChangeTextDirection-1.cs" >}}

##  **Vorabthemen**
- [Ändern Sie die Ausrichtung Cells und behalten Sie die vorhandene Formatierung bei](/cells/de/net/change-cells-alignment-and-keep-existing-formatting/)
- [Zeilenumbrüche und Textumbruch](/cells/de/net/line-breaks-and-text-wrapping/)

