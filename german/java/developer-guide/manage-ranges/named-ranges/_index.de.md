---
title: Benannte Bereiche
type: docs
weight: 40
url: /de/java/named-ranges/
---

{{% alert color="primary" %}} 

Normalerweise werden Spalten- und Zeilenbeschriftungen verwendet, um einzelne Zellen zu referenzieren. Es ist möglich, beschreibende Namen zu erstellen, um Zellen, Zellenbereiche, Formeln oder Konstanten zu repräsentieren. Das Wort **Name** kann eine Zeichenfolge von Zeichen bezeichnen, die eine Zelle, einen Zellenbereich, eine Formel oder einen Konstantenwert darstellt. Durch das Zuweisen eines Namens zu einem Bereich kann auf diesen Bereich anhand seines Namens Bezug genommen werden. Verwenden Sie leicht verständliche Namen, wie zum Beispiel Produkte, um auf schwer verständliche Bereiche, wie z.B. Umsatz!C20:C30, zu verweisen. Beschriftungen können in Formeln verwendet werden, die sich auf Daten im selben Arbeitsblatt beziehen; wenn Sie einen Bereich auf einem anderen Arbeitsblatt darstellen möchten, können Sie einen Namen verwenden. *Benannte Bereiche zählen zu den leistungsstärksten Funktionen von Microsoft Excel, insbesondere wenn sie als Quellbereich für Listensteuerelemente, Pivot-Tabellen, Diagramme usw. verwendet werden.*

{{% /alert %}} 
## **Erstellen eines benannten Bereichs**
### **Verwendung von Microsoft Excel**
Die folgenden Schritte beschreiben, wie Sie mithilfe von Microsoft Excel eine Zelle oder einen Zellenbereich benennen. Diese Methode gilt für Microsoft Office Excel 2003, Microsoft Excel 97, 2000 und 2002.

1. Wählen Sie die Zelle oder den Zellenbereich aus, den Sie benennen möchten.
1. Klicken Sie auf das Namensfeld am linken Ende der Formelzeile.
1. Geben Sie den Namen für die Zellen ein.
1. Drücken Sie die EINGABETASTE.

{{% alert color="primary" %}} 

Sie können eine Zelle nicht benennen, während Sie den Inhalt der Zelle ändern.

{{% /alert %}} 
### **Verwendung von Aspose.Cells**
Hier verwenden wir die Aspose.Cells API, um die Aufgabe zu erledigen.

Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), die eine Microsoft Excel-Datei darstellt. Die [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält eine [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection), die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse repräsentiert. Die [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse bietet eine [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung.

Es ist möglich, einen benannten Bereich zu erstellen, indem die überladene Methode [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-java.lang.String-java.lang.String-) der [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung aufgerufen wird. Eine typische Version der Methode [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-java.lang.String-java.lang.String-) akzeptiert folgende Parameter:

- Name der oberen linken Zelle, Name der oberen linken Zelle im Bereich.
- Name der unteren rechten Zelle, Name der unteren rechten Zelle im Bereich.

Wenn die Methode [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-java.lang.String-java.lang.String-) aufgerufen wird, gibt sie den neu erstellten benannten Bereich als Instanz der Klasse [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) zurück.

Das folgende Beispiel zeigt, wie ein benannter Bereich von Zellen erstellt wird, der sich über B4:G14 erstreckt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **Zugriff auf alle benannten Bereiche in einer Tabelle**
Rufen Sie die Methode [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges--) der [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) auf, um alle benannten Bereiche in einem Arbeitsblatt zu erhalten. Die Methode [getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges--) gibt ein Array aller benannten Bereiche in der Sammlung zurück.

Das folgende Beispiel zeigt, wie auf alle benannten Bereiche in einer Arbeitsmappe zugegriffen wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **Auf einen bestimmten benannten Bereich zugreifen**
Rufen Sie die [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName-java.lang.String-) Methode der [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) auf, um einen bestimmten Bereich anhand seines Namens zu bekommen. Eine typische [getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName-java.lang.String-) Methode akzeptiert den Namen des benannten Bereichs und gibt den entsprechenden Bereich als Instanz der Klasse [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) zurück.

Das folgende Beispiel zeigt, wie auf einen bestimmten Bereich nach seinem Namen zugegriffen wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **Zellen in einem benannten Bereich identifizieren**
Mit Aspose.Cells können Sie Daten in die einzelnen Zellen eines Bereichs einfügen. Angenommen, Sie haben einen benannten Bereich von Zellen, d.h. A1:C4. Die Matrix würde also 4 * 3 = 12 Zellen ergeben, und die einzelnen Bereichszellen sind sequentiell angeordnet. Aspose.Cells bietet Ihnen einige nützliche Eigenschaften der [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)-Klasse, um auf die einzelnen Zellen im Bereich zuzugreifen. Sie können die folgenden Methoden verwenden, um die Zellen im Bereich zu identifizieren:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) gibt den Index der ersten Zeile im benannten Bereich zurück.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) gibt den Index der ersten Spalte im benannten Bereich zurück.

Das folgende Beispiel zeigt, wie einige Werte in die Zellen eines bestimmten Bereichs eingegeben werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **Daten in die Zellen des benannten Bereichs eingeben**
Mit Aspose.Cells können Sie Daten in die einzelnen Zellen eines Bereichs einfügen. Angenommen, Sie haben einen benannten Bereich von Zellen, also H1:J4. Die Matrix würde also 4 * 3 = 12 Zellen ergeben, und die einzelnen Bereichszellen sind sequentiell angeordnet. Aspose.Cells bietet Ihnen einige nützliche Eigenschaften der [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)-Klasse, um auf die einzelnen Zellen im Bereich zuzugreifen. Sie können die folgenden Eigenschaften verwenden, um die Zellen im Bereich zu identifizieren:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) gibt den Index der ersten Zeile im benannten Bereich zurück.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn) gibt den Index der ersten Spalte im benannten Bereich zurück.

Das folgende Beispiel zeigt, wie einige Werte in die Zellen eines bestimmten Bereichs eingegeben werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **Formatbereiche... Hintergrundfarbe und Schriftattribute auf einen benannten Bereich einstellen**
Um die Formatierung anzuwenden, definieren Sie ein [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)-Objekt, um Stileinstellungen festzulegen und wenden Sie es auf das [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range)-Objekt an.

Im folgenden Beispiel wird gezeigt, wie eine feste Füllfarbe (Schattierungsfarbe) mit Schrifteinstellungen auf einen Bereich gesetzt wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **Formatbereiche... Hinzufügen von Rahmen zu einem benannten Bereich**
Es ist möglich, Grenzen zu einem Zellbereich hinzuzufügen, anstatt nur eine einzelne Zelle. Das [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) Objekt bietet die Methode [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders-int-com.aspose.cells.Color-) an, die die folgenden Parameter akzeptiert, um einen Rahmen zum Zellbereich hinzuzufügen:

- borderStyle: Der Typ des Rahmens, ausgewählt aus der [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)-Aufzählung.
- borderColor: Die Linienfarbe des Rahmens, ausgewählt aus der [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)-Aufzählung.

Im folgenden Beispiel wird gezeigt, wie einem Bereich ein Umrissrahmen gesetzt wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


Nach Ausführung des obigen Codes wird die folgende Ausgabe generiert: 

![todo:image_alt_text](named-ranges_1.png)
#### **Stil auf Zellen in einem Bereich anwenden**
Manchmal möchten Sie einen Stil auf die Zellen eines [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range) anwenden. Dafür können Sie die Zellen im Bereich durchlaufen und die Methode [Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) verwenden, um den Stil auf die Zelle anzuwenden.

Im folgenden Beispiel wird gezeigt, wie Stile auf Zellen in einem Bereich angewendet werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **Einen benannten Bereich entfernen**
Aspose.Cells stellt die Methode [NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt-int-) bereit, um den Namen des Bereichs zu löschen. Um die Inhalte des Bereichs zu löschen, verwenden Sie die Methode [Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange-com.aspose.cells.CellArea-)
Im folgenden Beispiel wird gezeigt, wie ein benannter Bereich mit seinem Inhalt entfernt wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


borderColors 
{{< app/cells/assistant language="java" >}}
