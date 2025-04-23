---
title: Ausrichtungseinstellungen
linktitle: Ausrichtungseinstellungen
description: In der Aspose.Cells Bibliothek können Sie die Einstellungen der Zellen Ausrichtung verwenden, um das Layout und die Anzeige von Text mit Node.js via C++ anzupassen. Dieses Dokument bietet detaillierte Schritte und Beispielcode für die Verwendung von Aspose.Cells für die Zell Ausrichtungseinstellungen.
keywords: Aspose.Cells, Zellen Ausrichtung, Horizontale Ausrichtung, Vertikale Ausrichtung, Textumbruch Node.js via C++
type: docs
weight: 20
url: /de/nodejs-cpp/cells-alignment-settings/
---

## **Konfigurieren von Ausrichtungseinstellungen**

### **Ausrichtungseinstellungen in Microsoft Excel**

Jeder, der Microsoft Excel verwendet hat, um Zellen zu formatieren, wird mit den Ausrichtungseinstellungen in Microsoft Excel vertraut sein.

Wie Sie aus der obigen Abbildung sehen können, gibt es verschiedene Arten von Ausrichtungsoptionen:

- Textausrichtung (horizontal & vertikal)
- Einrückung
- Orientierung
- Textkontrolle
- Textrichtung

Alle diese Ausrichtungseinstellungen werden vollständig von Aspose.Cells unterstützt und werden im Folgenden näher erläutert.

### **Ausrichtungseinstellungen in Aspose.Cells**

Aspose.Cells stellt die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) bereit, die eine Excel-Datei repräsentiert. Die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) bietet eine [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung. Jedes Element in der Sammlung [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) stellt ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) dar.

Aspose.Cells stellt die Methoden [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) und [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) für die Klasse [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) bereit, um die Formatierung einer Zelle abzurufen und zu setzen. Die Klasse [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) bietet nützliche Eigenschaften zur Konfiguration der Ausrichtungsoptionen.

Wählen Sie einen beliebigen Text-Ausrichtungstyp mit dem [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype)-Enum. Die vordefinierten Text-Ausrichtungstypen im [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype)-Enum sind:

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

Sie können auch die justify-verteilte Einstellung mit der [**Style.setIsJustifyDistributed(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsJustifyDistributed-boolean-)-Methode anwenden.

{{% /alert %}}

#### **Horizontale Ausrichtung**

Verwenden Sie die [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-[**setHorizontalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setHorizontalAlignment-textalignmenttype-)-Methode des Objekts [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style), um den Text horizontal auszurichten.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-HorizontalAlignment.js" >}}



#### **Vertikale Ausrichtung**

Ähnlich wie bei der horizontalen Ausrichtung verwenden Sie die [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-[**setVerticalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setVerticalAlignment-textalignmenttype-)-Methode des Objekts [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style), um den Text vertikal auszurichten.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-VerticalAlignment.js" >}}


#### **Einrückung**

Es ist möglich, die Einrückungsebene des Textes in einer Zelle mit der [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-[**setIndentLevel**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIndentLevel-number-)-Methode des Objekts [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) zu setzen.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Indentation.js" >}}



#### **Ausrichtung**

Setzen Sie die Orientierung (Drehung) des Textes in einer Zelle mit der [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-[**setRotationAngle**](https://reference.aspose.com/cells/nodejs-cpp/style/#setRotationAngle-number-)-Methode des Objekts [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Orientation.js" >}}

#### **Textsteuerung**

Im Folgenden wird erläutert, wie Sie Text steuern können, indem Sie Textrahmen, Anpassung an die Größe und andere Formatierungsoptionen festlegen.

##### **Textumschlag**

Das Textumbruch-Feature in einer Zelle erleichtert das Lesen: Die Höhe der Zelle passt sich an, um den gesamten Text aufzunehmen, anstatt ihn abzuschneiden oder in angrenzende Zellen auslaufen zu lassen. Aktivieren oder deaktivieren Sie den Textumbruch mit der [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-[**setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-)-Methode des Objekts [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapText.js" >}}


##### **Anpassen an Größe**

Eine Option zum Textumbruch in einem Feld ist, die Textgröße so zu verkleinern, dass sie in die Zelle passt. Das erfolgt durch Setzen der [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-[**setShrinkToFit(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setShrinkToFit-boolean-)-Methode des Objekts [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) auf **wahr**.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ShrinkToFit.js" >}}


##### **Zellen zusammenführen**

Wie Microsoft Excel unterstützt Aspose.Cells das Zusammenfassen mehrerer Zellen zu einer. Aspose.Cells bietet zwei Ansätze hierfür. Eine Möglichkeit ist, die [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-[**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-)-Methode der [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-Sammlung aufzurufen. Die [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-)-Methode nimmt die folgenden Parameter, um die Zellen zu verbinden:

- Erste Zeile: Die erste Zeile, ab der das Zusammenführen beginnt.
- Erste Spalte: Die erste Spalte, ab der das Zusammenführen beginnt.
- Anzahl der Zeilen: Die Anzahl der zu zusammenführenden Zeilen.
- Anzahl der Spalten: Die Anzahl der zu zusammenführenden Spalten.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-MergeCells.js" >}}


Der andere Weg ist, zuerst die [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)-[**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-)-Methode der Sammlung [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) aufzurufen, um einen Bereich der zu verbindenden Zellen zu erstellen. Die [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-)-Methode nimmt denselben Parameter wie die oben diskutierte [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-)-Methode und gibt ein [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)-Objekt zurück. Das [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)-Objekt bietet außerdem eine [**merge**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--)-Methode, die den Bereich, der im [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)-Objekt angegeben ist, verbindet.

##### **Textausrichtung**

Es ist möglich, die Lesereihenfolge von Text in Zellen festzulegen. Die Lesereihenfolge gibt die visuelle Reihenfolge an, in der Zeichen, Wörter usw. angezeigt werden. Zum Beispiel ist Englisch eine von links nach rechts lesbare Sprache, während Arabisch eine von rechts nach links lesbare Sprache ist.

Die Lese-Reihenfolge wird mit der [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-[**TextDirection**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTextDirection-textdirectiontype-)-Eigenschaft des Objekts [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) gesetzt. Aspose.Cells bietet vordefinierte Textrichtungsarten im [**TextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/textdirectiontype)-Enum.

|**Text Direction Types**|**Beschreibung**|
| :- | :- |
|Context|Die Lese-Reihenfolge, die mit der Sprache des ersten eingegebenen Zeichens übereinstimmt|
|LeftToRight|Lesereihenfolge von links nach rechts|
|RightToLeft|Lesereihenfolge von rechts nach links|

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-TextDirection.js" >}}


## **Erweiterte Themen**
- [Zellenausrichtung ändern und vorhandenes Format beibehalten](/cells/de/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Zeilenumbrüche und Textumbrüche](/cells/de/nodejs-cpp/line-breaks-and-text-wrapping/)

