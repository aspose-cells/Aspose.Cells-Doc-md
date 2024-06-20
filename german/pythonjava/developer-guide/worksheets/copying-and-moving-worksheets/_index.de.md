---
title: Arbeitsblätter kopieren und verschieben
type: docs
weight: 20
url: /de/python-java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}} 

Manchmal benötigen Sie eine Reihe von Arbeitsblättern mit gemeinsamer Formatierung und Daten. Wenn Sie beispielsweise mit vierteljährlichen Budgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe erstellen, die Tabellenblätter mit denselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthält. Es gibt eine Möglichkeit, das zu tun: Indem Sie ein Blatt erstellen und es dann kopieren.

Aspose.Cells unterstützt das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter, komplett mit Daten, Formatierungen, Tabellen, Matrizen, Diagrammen, Bildern und anderen Objekten, werden mit höchster Präzision kopiert.

{{% /alert %}} 
## **Verschieben oder Kopieren von Blättern mit Microsoft Excel**
Die folgenden Schritte sind beim Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen involviert.

1. Öffnen Sie die Arbeitsmappe, die die Blätter empfangen wird.
1. Wechseln Sie zum Arbeitsmappe, die die Blätter enthält, die Sie verschieben oder kopieren möchten, und wählen Sie dann die Blätter aus.
1. Klicken Sie im **Bearbeiten** Menü auf **Blatt verschieben oder kopieren**.
1. Wählen Sie im Feld 'Zur Arbeitsmappe' die Arbeitsmappe aus, in die die Blätter eingefügt werden sollen.
1. Um die ausgewählten Blätter in eine neue Arbeitsmappe zu verschieben oder zu kopieren, klicken Sie auf **neue Mappe**.
1. Klicken Sie im **Vor dem Blatt** Feld auf das Blatt, vor dem Sie die verschobenen oder kopierten Blätter einfügen möchten.
1. Wenn Sie die Blätter kopieren möchten, anstatt sie zu verschieben, aktivieren Sie das Kontrollkästchen **Kopie erstellen**.
### **Arbeitsblätter innerhalb einer Arbeitsmappe kopieren**
Aspose.Cells bietet eine überladene [WorksheetCollection.addCopy()](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#addCopy\(int\)) Methode, die zum Kopieren eines vorhandenen Arbeitsblatts verwendet wird. Eine Version der Methode nimmt den Index des Quellarbeitsblatts als Parameter. Die andere Version nimmt den Namen des Quellarbeitsblatts.

Das folgende Beispiel zeigt, wie ein vorhandenes Arbeitsblatt innerhalb einer Arbeitsmappe kopiert wird.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWithinWorkbook.py" >}}
### **Arbeitsblätter zwischen Arbeitsmappen kopieren**
Aspose.Cells bietet die [Worksheet.copy()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#copy\(com.aspose.cells.Worksheet\)) Methode zum Kopieren von Arbeitsblättern in andere Arbeitsmappen. Die Methode nimmt das Quellarbeitsblattobjekt als Parameter.

Das folgende Beispiel zeigt, wie ein Arbeitsblatt von einer Arbeitsmappe in eine andere kopiert wird.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CopyWorksheetsBetweenWorkbooks.py" >}}
### **Arbeitsblätter innerhalb einer Arbeitsmappe verschieben**
Aspose.Cells bietet die [Worksheet.moveTo()](https://reference.aspose.com/cells/python/asposecells.api/worksheet#moveTo\(int\)) Methode, um ein Arbeitsblatt an einen anderen Ort in der gleichen Arbeitsmappe zu verschieben.

Das folgende Beispiel zeigt, wie ein Arbeitsblatt an einen anderen Ort innerhalb der Arbeitsmappe verschoben wird.



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-MoveWorksheet.py" >}}
