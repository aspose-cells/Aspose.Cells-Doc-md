---
title: Jede Arbeitsblatt in eine separate PDF Datei speichern
type: docs
weight: 130
url: /de/net/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}} 

Aspose.Cells unterstützt die Konvertierung von XLS-Dateien (die Bilder, Diagramme usw. enthalten) in PDF-Dokumente. Aspose.Cells for .NET kann unabhängig voneinander arbeiten, um eine Tabelle in PDF zu konvertieren, und Sie müssen nicht Aspose.PDF für die Konvertierung verwenden. Für die Konvertierung sind keine temporären Dateien erforderlich, da der gesamte Vorgang im Speicher durchgeführt werden kann.

{{% /alert %}} 
## **Jedes Arbeitsblatt in eine separate PDF-Datei speichern**
Wenn Sie jedes Arbeitsblatt in Ihrer Vorlagen-Excel-Datei speichern möchten, um verschiedene PDF-Dateien zu generieren, können Sie dies einfach erreichen. Sie können versuchen, eine Blattindexierungsoption auf [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) festzulegen, um es einzeln in PDF zu rendern.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
