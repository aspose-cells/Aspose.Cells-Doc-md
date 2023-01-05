---
title: Dateien zusammenführen
type: docs
weight: 20
url: /de/net/merge-files/
---
## **Einführung**

 Aspose.Cells bietet verschiedene Möglichkeiten zum Zusammenführen von Dateien. Für einfache Dateien mit Daten, Formatierungen und Formeln ist die[**Workbook.Combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) Methode kann verwendet werden, um mehrere Arbeitsmappen zu kombinieren, und die[**Arbeitsblatt.Kopieren()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index)Methode kann verwendet werden, um Arbeitsblätter in eine neue Arbeitsmappe zu kopieren. Diese Methoden sind einfach zu verwenden und effektiv, aber wenn Sie viele Dateien zusammenführen müssen, werden Sie möglicherweise feststellen, dass sie viele Systemressourcen beanspruchen. Um dies zu vermeiden, verwenden Sie die[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)statische Methode, eine effizientere Methode zum Zusammenführen mehrerer Dateien.

## **Dateien mit Aspose.Cells zusammenführen**

 Der folgende Beispielcode veranschaulicht, wie große Dateien mithilfe von zusammengeführt werden[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)Methode. Es braucht zwei einfache, aber große Dateien, Book1.xls und Book2.xls. Die Dateien enthalten nur formatierte Daten und Formeln.

{{% alert color="primary" %}}

 Das[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles) -Methode unterstützt nur das Zusammenführen von Daten, Stilen, Formatierungen und Formeln. Objekte wie Diagramme, Bilder, Kommentare oder andere Objekte werden mit dieser Methode möglicherweise nicht zusammengeführt. Darüber hinaus wird eine zwischengespeicherte Datei verwendet, um temporäre Daten für den Prozess zu speichern.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
