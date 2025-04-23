---
title: Dateien zusammenführen
type: docs
weight: 20
url: /de/net/merge-files/
---

## **Einführung**

Aspose.Cells bietet verschiedene Möglichkeiten zum Zusammenführen von Dateien. Für einfache Dateien mit Daten, Formatierung und Formeln kann die Methode [**Workbook.Combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) verwendet werden, um mehrere Arbeitsmappen zu kombinieren, und die Methode [**Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index) kann verwendet werden, um Arbeitsblätter in eine neue Arbeitsmappe zu kopieren. Diese Methoden sind einfach zu verwenden und effektiv, aber wenn Sie viele Dateien zusammenführen müssen, könnte es sein, dass sie viele Systemressourcen in Anspruch nehmen. Um dies zu vermeiden, verwenden Sie die statische Methode [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles), um mehrere Dateien effizient zusammenzuführen.

## **Dateien mit Aspose.Cells zusammenführen**

Der folgende Beispielcode zeigt, wie man große Dateien mit der Methode [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles) zusammenführt. Es werden zwei einfache, aber große Dateien, Book1.xls und Book2.xls, verwendet. Die Dateien enthalten nur formatierte Daten und Formeln.

{{% alert color="primary" %}}

Die Methode [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles) unterstützt nur das Zusammenführen von Daten, Stilen, Formatierung und Formeln. Objekte wie Diagramme, Bilder, Kommentare oder andere Objekte werden möglicherweise nicht mit dieser Methode zusammengeführt. Darüber hinaus wird eine Zwischenspeicherdatei verwendet, um temporäre Daten für den Prozess zu speichern.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
