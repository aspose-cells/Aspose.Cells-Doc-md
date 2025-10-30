---
title: Dateien mit Golang via C++ zusammenführen
linktitle: Dateien zusammenführen
type: docs
weight: 20
url: /de/go-cpp/merge-files/
description: Lernen Sie, wie Sie Excel Dateien effizient mit Aspose.Cells for C++ zusammenführen.
---

## **Einführung**

Aspose.Cells bietet verschiedene Möglichkeiten zum Zusammenführen von Dateien. Für einfache Dateien mit Daten, Formatierungen und Formeln kann die [**Workbook.Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/)-Methode verwendet werden, um mehrere Arbeitsmappen zu kombinieren, und die [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/)-Methode, um Arbeitsblätter in eine neue Arbeitsmappe zu kopieren. Diese Methoden sind einfach und effektiv, aber wenn Sie viele Dateien zusammenführen müssen, könnten sie systemintensiv sein. Um dies zu vermeiden, verwenden Sie die statische Methode [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/), die effizienter ist, um mehrere Dateien zu zusammenzuführen.

## **Dateien mit Aspose.Cells zusammenführen**

Der folgende Beispielcode zeigt, wie große Dateien mit der [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/)-Methode zusammengeführt werden. Es nimmt zwei einfache, aber große Dateien, Book1.xls und Book2.xls. Die Dateien enthalten formatierten Daten und Formeln.

{{% alert color="primary" %}}

Die [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/)-Methode unterstützt nur das Zusammenführen von Daten, Styles, Formatierungen und Formeln. Objekte wie Diagramme, Bilder, Kommentare oder andere Objekte werden möglicherweise nicht mit dieser Methode zusammengeführt. Außerdem wird eine zwischengespeicherte Datei verwendet, um temporäre Daten für den Vorgang zu speichern.

{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeFiles.go" >}}
