---
title: Arbeitsblätter kopieren und verschieben
type: docs
weight: 10
url: /de/python-net/copying-and-moving-worksheets/
description: Dieser Artikel enthält Beispielcode und beschreibt, wie Sie Arbeitsblätter programmatisch innerhalb einer Excel Arbeitsmappe und über mehrere Excel Arbeitsmappen hinweg mit der Aspose.Cells für Python via .NET API kopieren und verschieben.
keywords: Python Excel Bibliothek, Python Arbeitsblatt kopieren, Python Arbeitsblatt verschieben, Python Arbeitsblätter zwischen Arbeitsmappen kopieren, Python Arbeitsblätter innerhalb der Arbeitsmappe verschieben, Python Arbeitsblätter zwischen Arbeitsmappen kopieren, Python Arbeitsblätter innerhalb einer Arbeitsmappe kopieren.
---

{{% alert color="primary" %}}

Manchmal benötigen Sie eine Reihe von Arbeitsblättern mit gemeinsamer Formatierung und Daten. Wenn Sie beispielsweise mit vierteljährlichen Budgets arbeiten, möchten Sie möglicherweise eine Arbeitsmappe erstellen, die Tabellenblätter mit denselben Spaltenüberschriften, Zeilenüberschriften und Formeln enthält. Es gibt eine Möglichkeit, das zu tun: Indem Sie ein Blatt erstellen und es dann kopieren.

Aspose.Cells für Python via .NET unterstützt das Kopieren und Verschieben von Arbeitsblättern innerhalb oder zwischen Arbeitsmappen. Arbeitsblätter, vollständig mit Daten, Formatierungen, Tabellen, Matrizen, Diagrammen, Bildern und anderen Objekten, werden mit höchster Präzision kopiert.

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

## **So kopieren Sie Arbeitsblätter innerhalb einer Arbeitsmappe mit der Python-Excel-Bibliothek von Aspose.Cells**

Aspose.Cells für Python via .NET bietet eine überladene Methode, [**Aspose.Cells.WorksheetCollection.add_copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add_copy/#str), die verwendet wird, um ein Arbeitsblatt zur Sammlung hinzuzufügen und Daten von einem bestehenden Arbeitsblatt zu kopieren. Eine Version der Methode nimmt den Index des Quellarbeitsblatts als Parameter. Die andere Version nimmt den Namen des Quellarbeitsblatts.

Das folgende Beispiel zeigt, wie ein vorhandenes Arbeitsblatt innerhalb einer Arbeitsmappe kopiert wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWithinWorkbook-1.py" >}}

## **Wie man Arbeitsblätter zwischen Arbeitsmappen kopiert**

Aspose.Cells für Python via .NET bietet eine Methode, [**Aspose.Cells.Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy/#aspose.cells.Worksheet), um Daten und Formatierungen von einem Quellarbeitsblatt auf ein anderes innerhalb oder zwischen Arbeitsmappen zu kopieren. Die Methode nimmt das Quellarbeitsblatt-Objekt als Parameter.

Das folgende Beispiel zeigt, wie ein Arbeitsblatt von einer Arbeitsmappe in eine andere kopiert wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.py" >}}

Das folgende Beispiel zeigt, wie ein Arbeitsblatt von einer Arbeitsmappe in eine andere kopiert wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-CopyWorksheetFromWorkbookToOther-1.py" >}}

## **Wie man Arbeitsblätter innerhalb einer Arbeitsmappe verschiebt**

Aspose.Cells für Python via .NET stellt die Methode [**Aspose.Cells.Worksheet.move_to()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/move_to/#int) bereit, mit der ein Arbeitsblatt an einen anderen Ort im selben Spreadsheet verschoben werden kann. Die Methode nimmt den Zielarbeitsblatt-Index als Parameter.

Das folgende Beispiel zeigt, wie ein Arbeitsblatt an einen anderen Ort innerhalb der Arbeitsmappe verschoben wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Value-MoveWorksheet-1.py" >}}
