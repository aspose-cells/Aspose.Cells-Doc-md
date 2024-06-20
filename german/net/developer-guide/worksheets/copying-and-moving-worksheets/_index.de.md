---
title: Arbeitsblätter kopieren und verschieben
type: docs
weight: 10
url: /de/net/copying-and-moving-worksheets/
description: Dieser Artikel enthält Beispielcode und beschreibt, wie Sie Arbeitsblätter programmgesteuert innerhalb einer Excel Arbeitsmappe und zwischen Excel Arbeitsmappen mit der C# API oder der .NET Bibliothek kopieren und verschieben können.
keywords: Arbeitsblatt kopieren c#, Arbeitsblatt verschieben c#
---

{{% alert color="primary" %}}

Manchmal benötigen Sie eine Reihe von Arbeitsblättern mit gemeinsamer Formatierung und Daten. Wenn Sie beispielsweise mit vierteljährlichen Budgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe erstellen, die Tabellenblätter mit denselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthält. Es gibt eine Möglichkeit, das zu tun: Indem Sie ein Blatt erstellen und es dann kopieren.

Aspose.Cells unterstützt das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter einschließlich Daten, Formatierung, Tabellen, Matrizen, Diagramme, Bilder und anderen Objekten werden mit höchster Präzision kopiert.

{{% /alert %}}

## **Verschieben oder Kopieren von Blättern mit Microsoft Excel**

Im Folgenden sind die Schritte für das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen in Microsoft Excel aufgeführt.

1. Um Blätter zu einem anderen Arbeitsmappen zu verschieben oder zu kopieren, öffnen Sie die Arbeitsmappe, die die Blätter empfangen wird.
1. Wechseln Sie zum Arbeitsmappe, die die Blätter enthält, die Sie verschieben oder kopieren möchten, und wählen Sie dann die Blätter aus.
1. Klicken Sie im **Bearbeiten** Menü auf **Blatt verschieben oder kopieren**.
1. Klicken Sie im Dialogfeld **Zu Arbeitsbuch** auf das Arbeitsbuch, um die Blätter zu empfangen.
1. Um die ausgewählten Blätter in ein neues Arbeitsbuch zu verschieben oder zu kopieren, klicken Sie auf **Neues Buch**.
1. Wählen Sie im Feld 'Vor Blatt' das Blatt aus, vor dem Sie die verschobenen oder kopierten Blätter einfügen möchten.
1. Um die Blätter zu kopieren anstatt sie zu verschieben, aktivieren Sie das Kontrollkästchen **Kopie erstellen**.

### **Arbeitsblätter innerhalb einer Arbeitsmappe mit Aspose.Cells kopieren**

Aspose.Cells stellt eine überladene Methode, [**Aspose.Cells.WorksheetCollection.AddCopy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/addcopy/index), bereit, die verwendet wird, um ein Arbeitsblatt zur Sammlung hinzuzufügen und Daten von einem vorhandenen Arbeitsblatt zu kopieren. Eine Version der Methode nimmt den Index des Quellarbeitsblatts als Parameter an. Die andere Version nimmt den Namen des Quellarbeitsblatts an.

Das folgende Beispiel zeigt, wie ein vorhandenes Arbeitsblatt innerhalb einer Arbeitsmappe kopiert wird.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWithinWorkbook-1.cs" >}}

### **Arbeitsblätter zwischen Arbeitsmappen kopieren**

Aspose.Cells stellt eine Methode bereit, [**Aspose.Cells.Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index), die zum Kopieren von Daten und Formatierung von einem Quellarbeitsblatt in ein anderes Arbeitsblatt innerhalb oder zwischen Arbeitsmappen verwendet wird. Die Methode nimmt das Quelldatenblattobjekt als Parameter.

Das folgende Beispiel zeigt, wie ein Arbeitsblatt von einer Arbeitsmappe in eine andere kopiert wird.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.cs" >}}

Das folgende Beispiel zeigt, wie ein Arbeitsblatt von einer Arbeitsmappe in eine andere kopiert wird.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.cs" >}}

### **Arbeitsblätter innerhalb einer Arbeitsmappe verschieben**

Aspose.Cells stellt eine Methode [**Aspose.Cells.Worksheet.MoveTo()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/moveto) bereit, die verwendet wird, um ein Arbeitsblatt an eine andere Stelle im selben Tabellenblatt zu verschieben. Die Methode nimmt den Index des Zielarbeitsblatts als Parameter.

Das folgende Beispiel zeigt, wie ein Arbeitsblatt an einen anderen Ort innerhalb der Arbeitsmappe verschoben wird.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Value-MoveWorksheet-1.cs" >}}
