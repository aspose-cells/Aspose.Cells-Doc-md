---
title: Dateien zusammenführen
type: docs
weight: 20
url: /de/python-net/merge-files/
---

## **Einführung**

Aspose.Cells für Python via .NET bietet verschiedene Möglichkeiten zum Zusammenführen von Dateien. Für einfache Dateien mit Daten, Formatierungen und Formeln kann die [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine)-Methode verwendet werden, um mehrere Arbeitsmappen zu kombinieren, und die [**Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy)-Methode, um Arbeitsblätter in eine neue Arbeitsmappe zu kopieren. Diese Methoden sind einfach und effektiv, aber wenn Sie viele Dateien zusammenführen müssen, stellen Sie fest, dass sie viele Systemressourcen beanspruchen können. Um dies zu vermeiden, verwenden Sie die [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files)-statische Methode, eine effizientere Möglichkeit, mehrere Dateien zusammenzuführen.

## **Dateien mit Aspose.Cells for Python via .NET zusammenführen**

Der folgende Beispielcode zeigt, wie man große Dateien mit der Methode [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files) zusammenführt. Es werden zwei einfache, aber große Dateien, Book1.xls und Book2.xls, verwendet. Die Dateien enthalten nur formatierte Daten und Formeln.

{{% alert color="primary" %}}

Die Methode [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files) unterstützt nur das Zusammenführen von Daten, Stilen, Formatierung und Formeln. Objekte wie Diagramme, Bilder, Kommentare oder andere Objekte werden möglicherweise nicht mit dieser Methode zusammengeführt. Darüber hinaus wird eine Zwischenspeicherdatei verwendet, um temporäre Daten für den Prozess zu speichern.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CellsHelperClass-MergeFiles-1.py" >}}

