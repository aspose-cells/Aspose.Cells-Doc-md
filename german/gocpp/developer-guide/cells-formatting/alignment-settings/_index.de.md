---
title: Ausrichtungseinstellungen mit Golang via C++
linktitle: Ausrichtungseinstellungen
description: In der Aspose.Cells Bibliothek können Sie Zellenausrichtungseinstellungen verwenden, um das Layout und die Anzeige von Text anzupassen. Durch die Anpassung von Einstellungen wie horizontale Ausrichtung, vertikale Ausrichtung und Textumbruch haben Sie mehr Kontrolle darüber, wie der Text in den Zellen fließt. Dieses Dokument bietet Ihnen detaillierte Schritte und Beispielcode, um schnell zu erfassen, wie Sie Aspose.Cells für Zellenausrichtungseinstellungen verwenden.
keywords: Aspose.Cells, Zellenausrichtung, horizontale Ausrichtung, vertikale Ausrichtung, Textumbruch
type: docs
weight: 20
url: /de/go-cpp/cells-alignment-settings/
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

Aspose.Cells bietet eine Klasse, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/), die eine Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) enthält eine [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) repräsentiert. Die Klasse [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) bietet eine [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-Sammlung. Jedes Element in der [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)-Sammlung stellt ein Objekt der Klasse [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) dar.

Aspose.Cells bietet Methoden zum [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) und [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/), um die Formatierung einer Zelle abzurufen und festzulegen. Die Klasse [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) stellt nützliche Eigenschaften zur Konfiguration von Ausrichtungseinstellungen bereit.

Wählen Sie einen beliebigen Textausrichtungstyp mithilfe der Aufzählung [**TextAlignmentType**](https://reference.aspose.com/cells/go-cpp/textalignmenttype/) aus. Die vordefinierten Textausrichtungstypen in der Aufzählung [**TextAlignmentType**](https://reference.aspose.com/cells/go-cpp/textalignmenttype/) lauten:

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

Sie können auch die Blocksatzverteilung mit der Eigenschaft [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/go-cpp/style/isjustifydistributed/) anwenden.

{{% /alert %}}

#### **Horizontale Ausrichtung**

Verwenden Sie die Eigenschaft [**GetHorizontalAlignment()**](https://reference.aspose.com/cells/go-cpp/style/gethorizontalalignment/) des Objekts [**Style**](https://reference.aspose.com/cells/go-cpp/style/), um den Text horizontal auszurichten.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings.go" >}}
#### **Vertikale Ausrichtung**

Ähnlich wie bei der horizontalen Ausrichtung verwenden Sie die Eigenschaft [**GetVerticalAlignment()**](https://reference.aspose.com/cells/go-cpp/style/getverticalalignment/) des Objekts [**Style**](https://reference.aspose.com/cells/go-cpp/style/), um den Text vertikal auszurichten.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-1.go" >}}
#### **Einrückung**

Es ist möglich, den Einrückungsgrad des Textes in einer Zelle mit der [**Style**](https://reference.aspose.com/cells/go-cpp/style/) -Objekteigenschaft [**GetIndentLevel()**](https://reference.aspose.com/cells/go-cpp/style/getindentlevel/) festzulegen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-2.go" >}}
#### **Ausrichtung**

Legen Sie die Ausrichtung (Rotation) des Textes in einer Zelle mit der [**Style**](https://reference.aspose.com/cells/go-cpp/style/) -Objekteigenschaft [**GetRotationAngle()**](https://reference.aspose.com/cells/go-cpp/style/getrotationangle/) fest.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-3.go" >}}
#### **Textsteuerung**

Im Folgenden wird erläutert, wie Sie Text steuern können, indem Sie Textrahmen, Anpassung an die Größe und andere Formatierungsoptionen festlegen.

##### **Textumschlag**

Das Umwickeln von Text in einer Zelle erleichtert das Lesen: Die Höhe der Zelle passt sich an, um den gesamten Text aufzunehmen, anstatt ihn abzuschneiden oder über benachbarte Zellen überlaufen zu lassen. Legen Sie das Textumwickeln mit der [**Style**](https://reference.aspose.com/cells/go-cpp/style/)-Objekteigenschaft [**IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/) ein oder aus.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-4.go" >}}
##### **Anpassen an Größe**

Eine Option zum Umwickeln von Text in einem Feld ist das Verkleinern der Textgröße, um sich an die Abmessungen einer Zelle anzupassen. Dies erfolgt durch Festlegen der [**Style**](https://reference.aspose.com/cells/go-cpp/style/)-Objekteigenschaft [**IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/) auf **true**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-5.go" >}}
##### **Zellen zusammenführen**

Wie Microsoft Excel unterstützt Aspose.Cells das Zusammenführen mehrerer Zellen. Aspose.Cells bietet zwei Ansätze für diese Aufgabe. Ein Weg besteht darin, die [**GetCells()**](https://reference.aspose.com/cells/go-cpp/worksheet/getcells/)-Sammlungsmethode [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) aufzurufen. Die [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/)-Methode akzeptiert die folgenden Parameter zum Zusammenführen der Zellen:

- Erste Zeile: Die erste Zeile, ab der das Zusammenführen beginnt.
- Erste Spalte: Die erste Spalte, ab der das Zusammenführen beginnt.
- Anzahl der Zeilen: Die Anzahl der zu zusammenführenden Zeilen.
- Anzahl der Spalten: Die Anzahl der zu zusammenführenden Spalten.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-6.go" >}}
Der andere Weg besteht darin, zuerst die [**GetCells()**](https://reference.aspose.com/cells/go-cpp/worksheet/getcells/)-Sammlungsmethode [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) aufzurufen, um einen Bereich der zu zusammenführenden Zellen zu erstellen. Die [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/)-Methode akzeptiert denselben Satz von Parametern wie die zuvor diskutierte [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/)-Methode und gibt ein [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)-Objekt zurück. Das [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)-Objekt bietet auch eine [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/)-Methode, die den im [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)-Objekt angegebenen Bereich zusammenführt.

##### **Textausrichtung**

Es ist möglich, die Lesereihenfolge von Text in Zellen festzulegen. Die Lesereihenfolge gibt die visuelle Reihenfolge an, in der Zeichen, Wörter usw. angezeigt werden. Zum Beispiel ist Englisch eine von links nach rechts lesbare Sprache, während Arabisch eine von rechts nach links lesbare Sprache ist.

Die Lesereihenfolge wird mit der [**Style**](https://reference.aspose.com/cells/go-cpp/style/)-Objekteigenschaft [**GetTextDirection()**](https://reference.aspose.com/cells/go-cpp/style/gettextdirection/) festgelegt. Aspose.Cells bietet vordefinierte Textausrichtungstypen in der [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/)-Enumeration.

|**Text Direction Types**|**Beschreibung**|
| :- | :- |
|Context|Die Lese-Reihenfolge, die mit der Sprache des ersten eingegebenen Zeichens übereinstimmt|
|LeftToRight|Lesereihenfolge von links nach rechts|
|RightToLeft|Lesereihenfolge von rechts nach links|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AlignmentSettings-7.go" >}}
## **Erweiterte Themen**
- [Zellenausrichtung ändern und vorhandenes Format beibehalten](/cells/de/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Zeilenumbrüche und Textumbrüche](/cells/de/cpp/line-breaks-and-text-wrapping/)
