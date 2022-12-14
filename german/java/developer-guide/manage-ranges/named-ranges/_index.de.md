---
title: Benannte Bereiche
type: docs
weight: 40
url: /de/java/named-ranges/
---
{{% alert color="primary" %}} 

Normalerweise werden Spalten- und Zeilenbeschriftungen verwendet, um auf einzelne Zellen zu verweisen. Es ist möglich, aussagekräftige Namen zu erstellen, um Zellen, Zellbereiche, Formeln oder konstante Werte darzustellen. Das Wort**Name** kann sich auf eine Zeichenfolge beziehen, die eine Zelle, einen Zellbereich, eine Formel oder einen konstanten Wert darstellt. Das Zuweisen eines Namens zu einem Bereich bedeutet, dass auf diesen Zellbereich mit seinem Namen verwiesen werden kann. Verwenden Sie leicht verständliche Namen, z. B. Produkte, um auf schwer verständliche Bereiche zu verweisen, z. B. Sales!C20:C30. Beschriftungen können in Formeln verwendet werden, die auf Daten auf demselben Arbeitsblatt verweisen; Wenn Sie einen Bereich auf einem anderen Arbeitsblatt darstellen möchten, können Sie einen Namen verwenden. *Benannte Bereiche gehören zu den leistungsstärksten Funktionen von Microsoft Excel, insbesondere wenn sie als Quellbereich für Listensteuerelemente, Pivot-Tabellen, Diagramme usw. verwendet werden.

{{% /alert %}} 
## **Erstellen eines benannten Bereichs**
### **Mit Microsoft Excel**
Die folgenden Schritte beschreiben, wie Sie eine Zelle oder einen Zellbereich mit Microsoft Excel benennen. Diese Methode gilt für Microsoft Office Excel 2003, Microsoft Excel 97, 2000 und 2002.

1. Wählen Sie die Zelle oder den Zellbereich aus, den Sie benennen möchten.
1. Klicken Sie auf das Namensfeld am linken Ende der Bearbeitungsleiste.
1. Geben Sie den Namen für die Zellen ein.
1. Drücken Sie Enter.

{{% alert color="primary" %}} 

Sie können eine Zelle nicht benennen, während Sie den Inhalt der Zelle ändern.

{{% /alert %}} 
### **Mit Aspose.Cells**
Hier verwenden wir die Aspose.Cells API, um die Aufgabe zu erledigen.

 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Klasse enthält a[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) die den Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse. Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) Klasse bietet a[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Sammlung.

 Es ist möglich, einen benannten Bereich zu erstellen, indem Sie die überladene aufrufen[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) ) Methode der[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung. Eine typische Version des[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\))-Methode nimmt die folgenden Parameter an:

- Name der Zelle oben links, der Name der Zelle oben links im Bereich.
- Name der unteren rechten Zelle, der Name der unteren rechten Zelle im Bereich.

 Wenn der[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(java.lang.String,%20java.lang.String\) )-Methode aufgerufen wird, gibt sie den neu erstellten benannten Bereich als Instanz von zurück[Bereich](https://reference.aspose.com/cells/java/com.aspose.cells/range) Klasse.

Das folgende Beispiel zeigt, wie Sie einen benannten Zellbereich erstellen, der sich über B4:G14 erstreckt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CreateNamedRangeofCells-CreateNamedRangeofCells.java" >}}
#### **Zugriff auf alle benannten Bereiche in einer Tabelle**
 Ruf den[getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) ) Methode der[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) um alle benannten Bereiche in einer Tabelle zu erhalten. Das[getNamedRanges](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getNamedRanges\(\) )-Methode gibt ein Array aller benannten Bereiche in der zurück[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection).

Das folgende Beispiel zeigt, wie auf alle benannten Bereiche in einer Arbeitsmappe zugegriffen wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessAllNamedRanges-AccessAllNamedRanges.java" >}}
#### **Greifen Sie auf einen bestimmten benannten Bereich zu**
 Ruf den[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) Sammlung[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) )-Methode, um einen bestimmten Bereich nach Namen abzurufen. Ein typisches[getRangeByName](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#getRangeByName\(java.lang.String\) )-Methode nimmt den Namen des benannten Bereichs und gibt den angegebenen benannten Bereich als Instanz von zurück[Bereich](https://reference.aspose.com/cells/java/com.aspose.cells/range)Klasse.

Das folgende Beispiel zeigt, wie auf einen angegebenen Bereich über seinen Namen zugegriffen wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AccessSpecificNamedRange-AccessSpecificNamedRange.java" >}}
#### **Identifizieren Sie Cells in einem benannten Bereich**
Mit Aspose.Cells können Sie Daten in die einzelnen Zellen eines Bereichs einfügen. Angenommen, Sie haben einen benannten Zellbereich, z. B. A1:C4. Die Matrix würde also 4 * 3 = 12 Zellen ergeben und die einzelnen Bereichszellen werden sequentiell angeordnet. Aspose.Cells bietet Ihnen einige nützliche Eigenschaften der Klasse [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range), um auf die einzelnen Zellen im Bereich zuzugreifen. Sie können die folgenden Methoden verwenden, um die Zellen im Bereich zu identifizieren:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow) gibt den Index der ersten Zeile im benannten Bereich zurück.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)gibt den Index der ersten Spalte im benannten Bereich zurück.

Das folgende Beispiel zeigt, wie einige Werte in die Zellen eines bestimmten Bereichs eingegeben werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-IdentifyCellsinNamedRange-IdentifyCellsinNamedRange.java" >}}
#### **Geben Sie Daten in Cells im benannten Bereich ein**
Mit Aspose.Cells können Sie Daten in die einzelnen Zellen eines Bereichs einfügen. Angenommen, Sie haben einen benannten Zellbereich, z. B. H1:J4. Die Matrix würde also 4 * 3 = 12 Zellen ergeben und die einzelnen Bereichszellen werden sequentiell angeordnet. Aspose.Cells bietet Ihnen einige nützliche Eigenschaften der Klasse [Range](https://reference.aspose.com/cells/java/com.aspose.cells/range), um auf die einzelnen Zellen im Bereich zuzugreifen. Sie können die folgenden Eigenschaften verwenden, um die Zellen im Bereich zu identifizieren:

- [getFirstRow](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstRow)gibt den Index der ersten Zeile im benannten Bereich zurück.
- [getFirstColumn](https://reference.aspose.com/cells/java/com.aspose.cells/range#FirstColumn)gibt den Index der ersten Spalte im benannten Bereich zurück.

Das folgende Beispiel zeigt, wie einige Werte in die Zellen eines bestimmten Bereichs eingegeben werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-InputDataInCellsInRange-InputDataInCellsInRange.java" >}}
#### **Bereiche formatieren ... Hintergrundfarbe und Schriftattribute auf einen benannten Bereich festlegen**
 Um eine Formatierung anzuwenden, definieren Sie a[Stil](https://reference.aspose.com/cells/java/com.aspose.cells/style) Objekt, um Stileinstellungen anzugeben und auf die anzuwenden[Bereich](https://reference.aspose.com/cells/java/com.aspose.cells/range)Objekt.

Das folgende Beispiel zeigt, wie Sie eine solide Füllfarbe (Schattierungsfarbe) mit Schriftarteinstellungen auf einen Bereich festlegen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges1-FormatRanges1.java" >}}
#### **Formatbereiche...Hinzufügen von Rahmen zu einem benannten Bereich**
 Es ist möglich, statt nur einer einzelnen Zelle Rahmen zu einem Bereich von Zellen hinzuzufügen. Das[Bereich](https://reference.aspose.com/cells/java/com.aspose.cells/range) Objekt bietet a[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\))-Methode, die die folgenden Parameter verwendet, um dem Zellbereich einen Rahmen hinzuzufügen:

-  borderStyle: die Art des Rahmens, ausgewählt aus der[CellRandType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)Aufzählung.
-  borderColor: die Linienfarbe des Rahmens, ausgewählt aus der[Farbe](https://reference.aspose.com/cells/java/com.aspose.cells/Color) Aufzählung.

Das folgende Beispiel zeigt, wie Sie einen Gliederungsrahmen für einen Bereich festlegen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormatRanges2-FormatRanges2.java" >}}


 Die folgende Ausgabe würde nach der Ausführung des obigen Codes generiert werden:

![todo: Bild_alt_Text](named-ranges_1.png)
#### **Stil auf Zellen in einem Bereich anwenden**
Manchmal möchten Sie einen Stil auf die Zellen in a anwenden[Bereich](https://reference.aspose.com/cells/java/com.aspose.cells/range) . Dazu können Sie über die Zellen im Bereich iterieren und die verwenden[Cell.setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\))-Methode, um den Stil auf die Zelle anzuwenden.

Das folgende Beispiel zeigt, wie Stile auf Zellen in einem Bereich angewendet werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConvertCellsAddresstoRangeorCellArea-ConvertCellsAddresstoRangeorCellArea.java" >}}
#### **Entfernen Sie einen benannten Bereich**
 Aspose.Cells bietet die[NameCollection.RemoveAt()](https://reference.aspose.com/cells/java/com.aspose.cells/namecollection#removeAt\(int\) )-Methode, um den Namen des Bereichs zu löschen. Um den Inhalt des Bereichs zu löschen, verwenden Sie[Cells.ClearRange()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#clearRange\(com.aspose.cells.CellArea\)) Methode.
Das folgende Beispiel zeigt, wie ein benannter Bereich mit seinem Inhalt entfernt wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-RemoveANamedRange-RemoveANamedRange.java" >}}


RandFarben
