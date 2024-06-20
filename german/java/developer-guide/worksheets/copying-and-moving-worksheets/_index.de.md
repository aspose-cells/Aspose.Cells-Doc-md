---
title: Arbeitsblätter kopieren und verschieben
type: docs
weight: 20
url: /de/java/copying-and-moving-worksheets/
---

{{% alert color="primary" %}}

Manchmal benötigen Sie eine Reihe von Arbeitsblättern mit gemeinsamer Formatierung und Daten. Wenn Sie beispielsweise mit vierteljährlichen Budgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe erstellen, die Tabellenblätter mit denselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthält. Es gibt eine Möglichkeit, das zu tun: Indem Sie ein Blatt erstellen und es dann kopieren.

Aspose.Cells unterstützt das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter einschließlich Daten, Formatierung, Tabellen, Matrizen, Diagramme, Bilder und anderen Objekten werden mit höchster Präzision kopiert.

{{% /alert %}}

## **Verschieben oder Kopieren von Blättern mit Microsoft Excel**

Im Folgenden sind die Schritte aufgeführt, die für das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen erforderlich sind.

1. Um Blätter zu einem anderen Arbeitsmappen zu verschieben oder zu kopieren, öffnen Sie die Arbeitsmappe, die die Blätter empfangen wird.
1. Wechseln Sie zum Arbeitsmappe, die die Blätter enthält, die Sie verschieben oder kopieren möchten, und wählen Sie dann die Blätter aus.
1. Klicken Sie im **Bearbeiten** Menü auf **Blatt verschieben oder kopieren**.
1. Wählen Sie im Feld 'Zur Arbeitsmappe' die Arbeitsmappe aus, in die die Blätter eingefügt werden sollen.
1. Um die ausgewählten Blätter in eine neue Arbeitsmappe zu verschieben oder zu kopieren, klicken Sie auf **Neue Arbeitsmappe**.
1. Wählen Sie im Feld 'Vor Blatt' das Blatt aus, vor dem Sie die verschobenen oder kopierten Blätter einfügen möchten.
1. Um die Blätter zu kopieren anstatt sie zu verschieben, aktivieren Sie das Kontrollkästchen **Kopie erstellen**.

## **Arbeitsblätter innerhalb einer Arbeitsmappe kopieren**

Aspose.Cells stellt eine überladene Methode, [**WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#addCopy(int)), bereit, die verwendet wird, um ein Arbeitsblatt zur Sammlung hinzuzufügen und Daten von einem vorhandenen Arbeitsblatt zu kopieren. Eine Version der Methode nimmt den Index des Quellarbeitsblatts als Parameter an. Die andere Version nimmt den Namen des Quellarbeitsblatts an.

Das folgende Beispiel zeigt, wie ein vorhandenes Arbeitsblatt innerhalb einer Arbeitsmappe kopiert wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWithinWorkbook-CopyWithinWorkbook.java" >}}

## **Arbeitsblätter zwischen Arbeitsmappen kopieren**

Aspose.Cells stellt eine Methode, [**Worksheet.copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)), bereit, um Daten und Formatierungen von einem Quellarbeitsblatt auf ein anderes Arbeitsblatt innerhalb oder zwischen den Arbeitsmappen zu kopieren. Die Methode nimmt das Quellarbeitsblattobjekt als Parameter an.

Das folgende Beispiel zeigt, wie ein Arbeitsblatt von einer Arbeitsmappe in eine andere kopiert wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetsBetweenWorkbooks-CopyWorksheetsBetweenWorkbooks.java" >}}

Das folgende Beispiel zeigt, wie ein Arbeitsblatt von einer Arbeitsmappe in eine andere kopiert wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetFromWorkbookToOther-CopyWorksheetFromWorkbookToOther.java" >}}

## **Arbeitsblätter innerhalb einer Arbeitsmappe verschieben**

Aspose.Cells stellt eine Methode, [**Worksheet.moveTo()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#moveTo(int)), bereit, um ein Arbeitsblatt an einen anderen Ort im selben Tabellenblatt zu verschieben.

Das folgende Beispiel zeigt, wie ein Arbeitsblatt an einen anderen Ort innerhalb der Arbeitsmappe verschoben wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-MoveWorksheet-MoveWorksheet.java" >}}
