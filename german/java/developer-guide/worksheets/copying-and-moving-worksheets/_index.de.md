---
title: Kopieren und Verschieben von Arbeitsblättern
type: docs
weight: 20
url: /de/java/copying-and-moving-worksheets/
---
{{% alert color="primary" %}}

Manchmal benötigen Sie eine Reihe von Arbeitsblättern mit gemeinsamen Formatierungen und Daten. Wenn Sie beispielsweise mit Quartalsbudgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe mit Blättern erstellen, die dieselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthalten. Es gibt eine Möglichkeit, dies zu tun: indem Sie ein Blatt erstellen und es dann kopieren.

Aspose.Cells unterstützt das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter mit Daten, Formatierungen, Tabellen, Matrizen, Diagrammen, Bildern und anderen Objekten werden mit höchster Präzision kopiert.

{{% /alert %}}

## **Verschieben oder Kopieren von Blättern mit Microsoft Excel**

Im Folgenden sind die Schritte zum Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen aufgeführt.

1. Um Blätter in eine andere Arbeitsmappe zu verschieben oder zu kopieren, öffnen Sie die Arbeitsmappe, die die Blätter erhalten soll.
1. Wechseln Sie zu der Arbeitsmappe, die die Blätter enthält, die Sie verschieben oder kopieren möchten, und wählen Sie dann die Blätter aus.
1.  Auf der**Bearbeiten** Menü, klicken**Blatt verschieben oder kopieren**.
1. Klicken Sie im Feld An Buch auf die Arbeitsmappe, um die Blätter zu erhalten.
1.  Um die ausgewählten Blätter in eine neue Arbeitsmappe zu verschieben oder zu kopieren, klicken Sie auf**neues Buch**.
1.  In dem**Vor Blatt** klicken Sie auf das Blatt, vor dem Sie die verschobenen oder kopierten Blätter einfügen möchten.
1.  Um die Blätter zu kopieren, anstatt sie zu verschieben, wählen Sie aus**Erstellen Sie eine Kopie** Kontrollkästchen.

## **Arbeitsblätter innerhalb einer Arbeitsmappe kopieren**

 Aspose.Cells bietet eine überladene Methode,[**WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#addCopy(int)), die zum Hinzufügen eines Arbeitsblatts zur Sammlung und zum Kopieren von Daten aus einem vorhandenen Arbeitsblatt verwendet wird. Eine Version der Methode nimmt den Index des Quellarbeitsblatts als Parameter. Die andere Version übernimmt den Namen des Quellarbeitsblatts.

Das folgende Beispiel zeigt, wie Sie ein vorhandenes Arbeitsblatt innerhalb einer Arbeitsmappe kopieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWithinWorkbook-CopyWithinWorkbook.java" >}}

## **Arbeitsblätter zwischen Arbeitsmappen kopieren**

 Aspose.Cells stellt eine Methode bereit,[**Arbeitsblatt.copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)zum Kopieren von Daten und Formatierungen aus einem Quellarbeitsblatt in ein anderes Arbeitsblatt innerhalb oder zwischen den Arbeitsmappen. Die Methode nimmt das Quellarbeitsblattobjekt als Parameter.

Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt von einer Arbeitsmappe in eine andere Arbeitsmappe kopieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetsBetweenWorkbooks-CopyWorksheetsBetweenWorkbooks.java" >}}

Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt von einer Arbeitsmappe in eine andere kopieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CopyWorksheetFromWorkbookToOther-CopyWorksheetFromWorkbookToOther.java" >}}

## **Arbeitsblätter innerhalb der Arbeitsmappe verschieben**

 Aspose.Cells stellt eine Methode bereit,[**Arbeitsblatt.moveTo()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#moveTo(int)), wird verwendet, um ein Arbeitsblatt an eine andere Stelle in derselben Tabelle zu verschieben.

Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt an eine andere Stelle innerhalb der Arbeitsmappe verschieben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-MoveWorksheet-MoveWorksheet.java" >}}
