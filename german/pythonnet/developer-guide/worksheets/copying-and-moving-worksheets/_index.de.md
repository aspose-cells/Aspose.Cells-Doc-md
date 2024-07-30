---
title: Arbeitsblätter kopieren und verschieben
type: docs
weight: 10
url: /de/python-net/copying-and-moving-worksheets/
description: Dieser Artikel enthält Beispielscode und beschreibt, wie Arbeitsblätter programmgesteuert sowohl innerhalb einer Excel Arbeitsmappe als auch zwischen Excel Arbeitsmappen mit der Aspose.Cells für Python via .NET API kopiert und verschoben werden können.
keywords: Python Excel Bibliothek, Python Arbeitsblatt kopieren, Python Arbeitsblatt verschieben, Python Arbeitsblätter zwischen Arbeitsmappen kopieren, Python Arbeitsblätter innerhalb einer Arbeitsmappe verschieben, Python Arbeitsblätter zwischen Arbeitsmappen kopieren, Python Arbeitsblätter innerhalb einer Arbeitsmappe kopieren.
---

{{% alert color="primary" %}}

Manchmal benötigen Sie eine Reihe von Arbeitsblättern mit gemeinsamer Formatierung und Daten. Wenn Sie beispielsweise mit vierteljährlichen Budgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe erstellen, die Tabellenblätter mit denselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthält. Es gibt eine Möglichkeit, das zu tun: Indem Sie ein Blatt erstellen und es dann kopieren.

Aspose.Cells für Python via .NET unterstützt das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter mit Daten, Formatierungen, Tabellen, Matrizen, Diagrammen, Bildern und anderen Objekten werden mit höchster Genauigkeit kopiert.

{{% /alert %}}

## **Wie man Blätter mit Microsoft Excel verschiebt oder kopiert**

Im Folgenden sind die Schritte für das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen in Microsoft Excel aufgeführt.

1. Um Blätter zu einem anderen Arbeitsmappen zu verschieben oder zu kopieren, öffnen Sie die Arbeitsmappe, die die Blätter empfangen wird.
1. Wechseln Sie zum Arbeitsmappe, die die Blätter enthält, die Sie verschieben oder kopieren möchten, und wählen Sie dann die Blätter aus.
1. Klicken Sie im **Bearbeiten** Menü auf **Blatt verschieben oder kopieren**.
1. Klicken Sie im Dialogfeld **Zu Arbeitsbuch** auf das Arbeitsbuch, um die Blätter zu empfangen.
1. Um die ausgewählten Blätter in ein neues Arbeitsbuch zu verschieben oder zu kopieren, klicken Sie auf **Neues Buch**.
1. Wählen Sie im Feld 'Vor Blatt' das Blatt aus, vor dem Sie die verschobenen oder kopierten Blätter einfügen möchten.
1. Um die Blätter zu kopieren anstatt sie zu verschieben, aktivieren Sie das Kontrollkästchen **Kopie erstellen**.

## **Wie man Arbeitsblätter innerhalb einer Arbeitsmappe mit der Aspose.Cells für die Python Excel-Bibliothek kopiert**

Aspose.Cells für Python via .NET stellt eine überladene Methode [**Aspose.Cells.WorksheetCollection.add_copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add_copy/#str) bereit, die zum Hinzufügen eines Arbeitsblatts zur Sammlung und zum Kopieren von Daten aus einem vorhandenen Arbeitsblatt verwendet wird. Eine Version der Methode übernimmt den Index des Quellarbeitsblatts als Parameter. Die andere Version übernimmt den Namen des Quellarbeitsblatts.

Das folgende Beispiel zeigt, wie ein vorhandenes Arbeitsblatt innerhalb einer Arbeitsmappe kopiert wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWithinWorkbook-1.py" >}}

## **Wie man Arbeitsblätter zwischen Arbeitsmappen kopiert**

Aspose.Cells für Python via .NET stellt eine Methode [**Aspose.Cells.Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy/#aspose.cells.Worksheet) bereit, die zum Kopieren von Daten und Formatierungen von einem Quellarbeitsblatt in ein anderes Arbeitsblatt innerhalb oder zwischen Arbeitsmappen verwendet wird. Die Methode übernimmt das Quellarbeitsblattobjekt als Parameter.

Das folgende Beispiel zeigt, wie ein Arbeitsblatt von einer Arbeitsmappe in eine andere kopiert wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.py" >}}

Das folgende Beispiel zeigt, wie ein Arbeitsblatt von einer Arbeitsmappe in eine andere kopiert wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.py" >}}

## **Wie man Arbeitsblätter innerhalb einer Arbeitsmappe verschiebt**

Aspose.Cells für Python via .NET stellt eine Methode [**Aspose.Cells.Worksheet.move_to()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/move_to/#int) bereit, die zum Verschieben eines Arbeitsblatts an einen anderen Ort in derselben Arbeitsmappe verwendet wird. Die Methode übernimmt den Index des Zielarbeitsblatts als Parameter.

Das folgende Beispiel zeigt, wie ein Arbeitsblatt an einen anderen Ort innerhalb der Arbeitsmappe verschoben wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-MoveWorksheet-1.py" >}}
