---
title: Arbeitsblätter kopieren und verschieben
type: docs
weight: 10
url: /de/net/copying-and-moving-worksheets/
description: Dieser Artikel enthält Beispielcode und beschreibt, wie Sie Arbeitsblätter mithilfe der Bibliothek C#, API oder .NET programmgesteuert sowohl innerhalb einer Excel-Arbeitsmappe als auch zwischen Excel-Arbeitsmappen kopieren und verschieben.
keywords: copy worksheet c#, move worksheet c#
---
{{% alert color="primary" %}}

Manchmal benötigen Sie mehrere Arbeitsblätter mit gemeinsamen Formatierungen und Daten. Wenn Sie beispielsweise mit vierteljährlichen Budgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe mit Blättern erstellen, die dieselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthalten. Es gibt eine Möglichkeit, dies zu tun: indem Sie ein Blatt erstellen und es dann kopieren.

Aspose.Cells unterstützt das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter mit Daten, Formatierungen, Tabellen, Matrizen, Diagrammen, Bildern und anderen Objekten werden mit höchster Präzision kopiert.

{{% /alert %}}

##  **Verschieben oder Kopieren von Blättern mit Microsoft Excel**

Im Folgenden finden Sie die Schritte zum Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen in Microsoft Excel.

1. Um Blätter in eine andere Arbeitsmappe zu verschieben oder zu kopieren, öffnen Sie die Arbeitsmappe, die die Blätter erhalten soll.
1. Wechseln Sie zu der Arbeitsmappe, die die Blätter enthält, die Sie verschieben oder kopieren möchten, und wählen Sie dann die Blätter aus.
1.  Auf der**Bearbeiten** Klicken Sie im Menü auf *Blatt verschieben oder kopieren**.
1.  Im**Buchen** Klicken Sie im Dialogfeld auf die Arbeitsmappe, um die Blätter zu erhalten.
1. Um die ausgewählten Blätter in eine neue Arbeitsmappe zu verschieben oder zu kopieren, klicken Sie auf *Neues Buch**.
1.  Im**Vor Blatt** Klicken Sie im Feld auf das Blatt, vor dem Sie die verschobenen oder kopierten Blätter einfügen möchten.
1.  Um die Blätter zu kopieren, anstatt sie zu verschieben, wählen Sie das aus**Erstellen Sie eine Kopie** Kontrollkästchen.

###  **Kopieren Sie Arbeitsblätter innerhalb einer Arbeitsmappe mit Aspose.Cells**

 Aspose.Cells bietet eine überladene Methode,[**Aspose.Cells.WorksheetCollection.AddCopy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/addcopy/index)das zum Hinzufügen eines Arbeitsblatts zur Sammlung und zum Kopieren von Daten aus einem vorhandenen Arbeitsblatt verwendet wird. Eine Version der Methode verwendet den Index des Quellarbeitsblatts als Parameter. Die andere Version übernimmt den Namen des Quellarbeitsblatts.

Das folgende Beispiel zeigt, wie ein vorhandenes Arbeitsblatt innerhalb einer Arbeitsmappe kopiert wird.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWithinWorkbook-1.cs" >}}

###  **Kopieren Sie Arbeitsblätter zwischen Arbeitsmappen**

 Aspose.Cells bietet eine Methode,[**Aspose.Cells.Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index)Wird zum Kopieren von Daten und Formatierungen von einem Quellarbeitsblatt in ein anderes Arbeitsblatt innerhalb oder zwischen Arbeitsmappen verwendet. Die Methode verwendet das Quellarbeitsblattobjekt als Parameter.

Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt von einer Arbeitsmappe in eine andere kopieren.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.cs" >}}

Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt von einer Arbeitsmappe in eine andere kopieren.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.cs" >}}

###  **Verschieben Sie Arbeitsblätter innerhalb der Arbeitsmappe**

 Aspose.Cells bietet eine Methode[**Aspose.Cells.Worksheet.MoveTo()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/moveto)mit dem ein Arbeitsblatt an eine andere Stelle in derselben Tabelle verschoben werden kann. Die Methode verwendet den Zielarbeitsblattindex als Parameter.

Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt an eine andere Stelle in der Arbeitsmappe verschieben.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-MoveWorksheet-1.cs" >}}
