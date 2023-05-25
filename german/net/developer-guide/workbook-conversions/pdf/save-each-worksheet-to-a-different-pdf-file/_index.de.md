---
title: Speichern Sie jedes Arbeitsblatt in einer anderen PDF-Datei
type: docs
weight: 130
url: /de/net/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}} 

Aspose.Cells unterstützt die Konvertierung von XLS-Dateien (die Bilder, Diagramme usw. enthalten) in PDF-Dokumente. Aspose.Cells for .NET kann unabhängig arbeiten, um eine Tabelle in PDF zu konvertieren, und Sie müssen Aspose.PDF for .NET nicht für die Konvertierung verwenden. Für die Konvertierung ist es nicht erforderlich, dass die Software temporäre Dateien erstellt oder verwendet, da der gesamte Vorgang im Speicher durchgeführt werden kann.

{{% /alert %}} 
##  **Speichern Sie jedes Arbeitsblatt in einer anderen PDF-Datei**
 Wenn Sie jedes Arbeitsblatt in Ihrer Excel-Vorlagedatei speichern müssen, um verschiedene PDF-Dateien zu generieren, können Sie dies problemlos erreichen. Sie können versuchen, einen Blattindex auf festzulegen**[`PdfSaveOptions.SheetSet`](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** Option nacheinander zum Rendern auf PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

 Wenn Ihre Tabelle Formeln enthält, rufen Sie am besten an[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) kurz vor dem Rendern der Tabelle in das Format PDF. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet werden und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
