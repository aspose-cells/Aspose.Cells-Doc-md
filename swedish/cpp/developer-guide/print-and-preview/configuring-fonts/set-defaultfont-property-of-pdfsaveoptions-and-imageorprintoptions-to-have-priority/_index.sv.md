---
title: Ställ in egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions för att ha företräde med C++
linktitle: Ange egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions för att prioritera den
type: docs
weight: 30
url: /sv/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Lär dig att prioritera teckensnittinställningar vid sparning av dokument med Aspose.Cells i C++.
---

## **Möjliga användningsscenario**

När du ställer in **DefaultFont**-egenskapen för [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) kan du förvänta dig att vid sparande till PDF eller bild kommer den inställda StandardFonten att gälla för all text i en arbetsbok som har en saknad (ej installerad) font.

Generellt, när man sparar till PDF eller bild, försöker Aspose.Cells först att sätta kalkylbladets standardteckensnitt (dvs. Workbook.DefaultStyle.Font). Om kalkylbladets standardteckensnitt fortfarande inte kan visa/rita text ordentligt, kommer Aspose.Cells att försöka med det teckensnitt som nämns mot DefaultFont-attributet i [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/).

För att möta dina förväntningar har vi en Boolean egenskap kallad "**CheckWorkbookDefaultFont**" i [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/). Du kan ställa in den på **falsk** för att inaktivera försök med kalkylbladets standardteckensnitt eller låta **DefaultFont**-inställningen i [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) ha företräde.

## **Ange egenskapen DefaultFont för PdfSaveOptions/ImageOrPrintOptions**

Följande exempel kod öppnar en Excel-fil. A1-cellen (i det första kalkylbladet) har satt texten "Jul Tid Teckensnitt". Teckensnittsnamnet är "Christmas Time Personal Use" som inte är installerat på maskinen. Vi ställer in **DefaultFont**-attributet för [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) till "Times New Roman". Vi sätter också den booleska egenskapen **CheckWorkbookDefaultFont** till **"falsk"** vilket säkerställer att texten i A1-cellen renderas med "Times New Roman" teckensnitt och inte använder kalkylbladets standardteckensnitt ("Calibri" i detta fall). Koden renderar det första kalkylbladet till PNG och TIFF bildeformat. Slutligen renderas det till en PDF-fil.

{{% alert color="primary" %}}

Standardvärdet för egenskapen **CheckWorkbookDefaultFont** är **sant**.

{{% /alert %}}

Detta är skärmbilden av [mallfilen](49446913.xlsx) som används i exempelkoden.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Detta är utdata PNG-bild efter att ha ställt in egenskapen [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) till "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Se utdata [TIFF](48496672.tiff) bild efter att ha ställt in egenskapen [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) till "Times New Roman".

Se utdata [PDF](48496673.pdf) fil efter att ha ställt in egenskapen [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) till "Times New Roman".

## **Exempelkod**

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
