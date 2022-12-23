---
title: Kopieren und Verschieben von Arbeitsblättern
type: docs
weight: 20
url: /de/python-java/copying-and-moving-worksheets/
---
{{% alert color="primary" %}} 

Manchmal benötigen Sie eine Reihe von Arbeitsblättern mit gemeinsamen Formatierungen und Daten. Wenn Sie beispielsweise mit Quartalsbudgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe mit Blättern erstellen, die dieselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthalten. Es gibt eine Möglichkeit, dies zu tun: indem Sie ein Blatt erstellen und es dann kopieren.

Aspose.Cells unterstützt das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter mit Daten, Formatierungen, Tabellen, Matrizen, Diagrammen, Bildern und anderen Objekten werden mit höchster Präzision kopiert.

{{% /alert %}} 
## **Verschieben oder Kopieren von Blättern mit Microsoft Excel**
Im Folgenden sind die Schritte zum Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen aufgeführt.

1. Öffnen Sie die Arbeitsmappe, die die Blätter erhalten soll.
1. Wechseln Sie zu der Arbeitsmappe, die die Blätter enthält, die Sie verschieben oder kopieren möchten, und wählen Sie dann die Blätter aus.
1. Auf der**Bearbeiten**Menü, klicken**Blatt verschieben oder kopieren**.
1. Klicken Sie im Feld An Buch auf die Arbeitsmappe, um die Blätter zu erhalten.
1. Um die ausgewählten Blätter in eine neue Arbeitsmappe zu verschieben oder zu kopieren, klicken Sie auf**neues Buch**.
1. Im**Vor Blatt**klicken Sie auf das Blatt, vor dem Sie die verschobenen oder kopierten Blätter einfügen möchten.
1. Um die Blätter zu kopieren, anstatt sie zu verschieben, wählen Sie aus**Erstellen Sie eine Kopie**Kontrollkästchen.
### **Arbeitsblätter innerhalb einer Arbeitsmappe kopieren**
Aspose.Cells liefert eine überladene[WorksheetCollection.addCopy()](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#addCopy\(int\))-Methode, die zum Kopieren eines vorhandenen Arbeitsblatts verwendet wird. Eine Version der Methode nimmt den Index des Quellarbeitsblatts als Parameter. Die andere Version übernimmt den Namen des Quellarbeitsblatts.

Das folgende Beispiel zeigt, wie Sie ein vorhandenes Arbeitsblatt innerhalb einer Arbeitsmappe kopieren.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWithinWorkbook.py" >}}
### **Arbeitsblätter zwischen Arbeitsmappen kopieren**
Aspose.Cells bietet die[Arbeitsblatt.copy()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#copy\(com.aspose.cells.Worksheet\)) Methode zum Kopieren von Arbeitsblättern in andere Arbeitsmappen. Die Methode nimmt das Quellarbeitsblattobjekt als Parameter.

Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt von einer Arbeitsmappe in eine andere Arbeitsmappe kopieren.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWorksheetsBetweenWorkbooks.py" >}}
### **Arbeitsblätter innerhalb der Arbeitsmappe verschieben**
Aspose.Cells bietet die[Arbeitsblatt.moveTo()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#moveTo\(int\)) Methode zum Verschieben eines Arbeitsblatts an eine andere Stelle in derselben Tabelle.

Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt an eine andere Stelle innerhalb der Arbeitsmappe verschieben.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-MoveWorksheet.py" >}}
