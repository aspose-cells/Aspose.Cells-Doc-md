---
title: Dateien zusammenführen
type: docs
weight: 10
url: /de/java/merge-files/
---
## **Einführung**

 Aspose.Cells bietet verschiedene Möglichkeiten zum Zusammenführen von Dateien. Für einfache Dateien mit Daten, Formatierungen und Formeln ist die[**Arbeitsmappe.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook))-Methode kann verwendet werden, um mehrere Arbeitsmappen zu kombinieren, und die[**Arbeitsblatt.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet))-Methode kann verwendet werden, um Arbeitsblätter in eine neue Arbeitsmappe zu kopieren. Diese Methoden sind einfach zu verwenden und effektiv, aber wenn Sie viele Dateien zusammenführen müssen, werden Sie möglicherweise feststellen, dass sie viele Systemressourcen beanspruchen. Um dies zu vermeiden, verwenden Sie die statische Methode CellsHelper.mergeFiles, eine effizientere Methode zum Zusammenführen mehrerer Dateien.

## **Dateien mit Aspose.Cells zusammenführen**

Der folgende Beispielcode veranschaulicht, wie große Dateien mit der CellsHelper.mergeFiles-Methode zusammengeführt werden. Es werden zwei einfache, aber große Dateien benötigt, MyBook1.xls und MyBook2.xls. Die Dateien enthalten nur formatierte Daten und Formeln.

{{% alert color="primary" %}}

Die CellsHelper.mergeFiles-Methode unterstützt nur das Zusammenführen von Daten, Stilen, Formatierungen und Formeln. Objekte wie Diagramme, Bilder, Kommentare oder andere Objekte werden mit dieser Methode möglicherweise nicht zusammengeführt. Darüber hinaus wird eine zwischengespeicherte Datei verwendet, um temporäre Daten für den Prozess zu speichern.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
