---
title: Setzen Sie die Eigenschaft DefaultFont von PdfSaveOptions und ImageOrPrintOptions, um Priorität mit C++ zu haben
linktitle: StandardFont Eigenschaft von PdfSaveOptions und ImageOrPrintOptions Priorität einräumen
type: docs
weight: 30
url: /de/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Lernen Sie, wie Sie Schriftarteinstellungen beim Speichern von Dokumenten mit Aspose.Cells in C++ priorisieren.
---

## **Mögliche Verwendungsszenarien**

Beim Setzen der **DefaultFont**-Eigenschaft von [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) könnten Sie erwarten, dass beim Speichern als PDF oder Bild dieser DefaultFont auf den gesamten Text in einer Arbeitsmappe angewendet wird, der eine fehlende (nicht installierte) Schriftart hat.

Beim Speichern in PDF oder Bild wird Aspose.Cells zuerst versuchen, die Standard-Schriftart der Arbeitsmappe zu setzen (d.h. Workbook.DefaultStyle.Font). Wenn die Standardschriftart der Arbeitsmappe immer noch nicht korrekt Text anzeigen/rendern kann, versucht Aspose.Cells, mit der unter [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) gegen die DefaultFont-Attributhinweis angegebenen Schriftart zu rendern.

Um Ihre Erwartungen zu erfüllen, haben wir eine boolesche Eigenschaft namens "**CheckWorkbookDefaultFont**" in [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/). Sie können sie auf **false** setzen, um das Testen der Standard-Schriftart der Arbeitsmappe zu deaktivieren oder die **DefaultFont**-Einstellung in [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) Priorität einzuräumen.

## **StandardFont-Eigenschaft von PdfSaveOptions/ImageOrPrintOptions festlegen**

Der folgende Beispielcode öffnet eine Excel-Datei. Die Zelle A1 (im ersten Arbeitsblatt) enthält den Text "Christmas Time Font text". Der Schriftartname ist "Christmas Time Personal Use", die auf dem Computer nicht installiert ist. Wir setzen das Attribut **DefaultFont** von [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) auf "Times New Roman". Wir setzen auch die boolesche Eigenschaft **CheckWorkbookDefaultFont** auf **"false"**, was sicherstellt, dass der Text der A1-Zelle mit der Schriftart "Times New Roman" gerendert wird und nicht die Standardschriftart des Arbeitsbuchs (in diesem Fall "Calibri") verwendet wird. Der Code rendert das erste Arbeitsblatt in die Formate PNG und TIFF. Schließlich wird in das PDF-Format gerendert.

{{% alert color="primary" %}}

Der Standardwert der Eigenschaft **CheckWorkbookDefaultFont** ist **true**.

{{% /alert %}}

Dies ist der Screenshot der im Beispielcode verwendeten [Vorlagendatei](49446913.xlsx).

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Dies ist das Ausgabe-PNG-Bild nach Setzen der [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)-Eigenschaft auf "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Siehe das Ausgabe-[TIFF](48496672.tiff)-Bild nach Setzen der [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)-Eigenschaft auf "Times New Roman".

Siehe die Ausgabedatei [PDF](48496673.pdf), nachdem die Eigenschaft [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) auf "Times New Roman" gesetzt wurde.

## **Beispielcode**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Input and output directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open an Excel file
    Workbook workbook(sourceDir + u"sampleSetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.xlsx");

    // Rendering to PNG file format while setting the CheckWorkbookDefaultFont attribute to false.
    // So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
    ImageOrPrintOptions imgOpt;
    imgOpt.SetImageType(ImageType::Png);
    imgOpt.SetCheckWorkbookDefaultFont(false);
    imgOpt.SetDefaultFont(u"Times New Roman");

    // Create a SheetRender instance for the first worksheet and render to PNG.
    SheetRender sr(workbook.GetWorksheets().Get(0), imgOpt);
    sr.ToImage(0, outputDir + u"out1_imagePNG.png");

    // Rendering to TIFF file format while setting the CheckWorkbookDefaultFont attribute to false.
    imgOpt.SetImageType(ImageType::Tiff);
    WorkbookRender wr(workbook, imgOpt);
    wr.ToImage(outputDir + u"out1_imageTIFF.tiff");

    // Rendering to PDF file format while setting the CheckWorkbookDefaultFont attribute to false.
    PdfSaveOptions saveOptions;
    saveOptions.SetDefaultFont(u"Times New Roman");
    saveOptions.SetCheckWorkbookDefaultFont(false);

    // Save the workbook as PDF
    workbook.Save(outputDir + u"out1_pdf.pdf", saveOptions);

    std::cout << "Files exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
