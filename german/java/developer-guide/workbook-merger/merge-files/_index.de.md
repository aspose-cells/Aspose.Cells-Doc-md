---
title: Dateien zusammenführen
type: docs
weight: 10
url: /de/java/merge-files/
---

## **Einführung**

Aspose.Cells bietet verschiedene Möglichkeiten, um Dateien zusammenzuführen. Für einfache Dateien mit Daten, Formatierungen und Formeln kann die Methode [**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook)) verwendet werden, um mehrere Arbeitsmappen zu kombinieren, und die Methode [**Worksheet.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)) kann verwendet werden, um Arbeitsblätter in eine neue Arbeitsmappe zu kopieren. Diese Methoden sind einfach zu verwenden und effektiv, aber wenn Sie viele Dateien zusammenführen müssen, könnte es sein, dass sie viele Systemressourcen verbrauchen. Verwenden Sie deshalb die statische Methode CellsHelper.mergeFiles, um mehrere Dateien effizient zusammenzuführen.

## **Dateien mit Aspose.Cells zusammenführen**

Der folgende Beispielcode veranschaulicht, wie große Dateien mithilfe der Methode CellsHelper.mergeFiles zusammengeführt werden. Es handelt sich um zwei einfache, aber große Dateien: MyBook1.xls und MyBook2.xls. Die Dateien enthalten nur formatierte Daten und Formeln.

{{% alert color="primary" %}}

Die CellsHelper.mergeFiles-Methode unterstützt nur das Zusammenführen von Daten, Stilen, Formatierungen und Formeln. Objekte wie Diagramme, Bilder, Kommentare oder andere Objekte können mit dieser Methode möglicherweise nicht zusammengeführt werden. Darüber hinaus wird eine zwischengespeicherte Datei verwendet, um temporäre Daten für den Vorgang zu speichern.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
