---
title: Jede Arbeitsblatt in eine separate PDF Datei speichern
type: docs
weight: 50
url: /de/java/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Konvertierung von Tabellenkalkulationsdateien (die Bilder, Diagramme usw. enthalten) in PDF-Dokumente. Aspose.Cells for Java kann unabhängig arbeiten, um eine Tabellenkalkulation in ein PDF-Dokument umzuwandeln, und Sie müssen Aspose.PDF für Java nicht mehr für die Konvertierung verwenden. Der Vorgang erfordert auch nicht, temporäre Dateien zu erstellen oder zu verwenden, da der gesamte Prozess im Speicher durchgeführt werden kann.

{{% /alert %}}

Wenn Sie jedes Arbeitsblatt in Ihrer Vorlagen-Excel-Datei speichern müssen, um verschiedene PDF-Dateien zu erstellen, kann dies leicht erreicht werden. Sie können jeweils einen Blattindex zur [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setSheetSet-com.aspose.cells.SheetSet-)-Option festlegen, um es als PDF zu rendern.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

Wenn die Tabellenkalkulation Formeln enthält, ist es am besten, die Methode [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) kurz vor dem Rendern der Tabelle in PDF aufzurufen. Dies stellt sicher, dass formelabhängige Werte neu berechnet werden und die korrekten Werte im PDF angezeigt werden.

{{% /alert %}}
