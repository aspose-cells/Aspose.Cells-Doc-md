---
title: Imposta la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions con priorità usando C++
linktitle: Impostare la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions per avere la priorità
type: docs
weight: 30
url: /it/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Impara a dare priorità alle impostazioni del font durante il salvataggio di documenti con Aspose.Cells in C++.
---

## **Possibili Scenari di Utilizzo**

Mentre si imposta la proprietà **DefaultFont** di [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) e [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), potresti aspettarti che il salvataggio in PDF o immagine imposti quel DefaultFont a tutto il testo in un foglio di lavoro che ha un carattere mancante (non installato).

 Generalmente, quando si salva in PDF o immagine, Aspose.Cells tenterà prima di impostare il carattere predefinito del Workbook (cioè Workbook.DefaultStyle.Font). Se il carattere predefinito del workbook ancora non può mostrare/rendersi correttamente, Aspose.Cells proverà a rendere con il font indicato contro l'attributo DefaultFont in [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/).

Per soddisfare le tue aspettative, abbiamo una proprietà Booleana chiamata "**CheckWorkbookDefaultFont**" in [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/). Puoi impostarla su **false** per disabilitare il tentativo di utilizzare il font predefinito del workbook o lasciare che l'impostazione **DefaultFont** in [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) abbia priorità.

## **Impostare la proprietà DefaultFont di PdfSaveOptions/ImageOrPrintOptions**

Il seguente esempio di codice apre un file Excel. La cella A1 (nel primo foglio di lavoro) contiene il testo "Christmas Time Font text". Il nome del font è "Christmas Time Personal Use" che non è installato sulla macchina. Impostiamo l'attributo **DefaultFont** di [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) su "Times New Roman". Impostiamo anche la proprietà booleana **CheckWorkbookDefaultFont** su **"false"** che garantisce che il testo della cella A1 venga reso con il font "Times New Roman" e non utilizzi il font di default del workbook ("Calibri" in questo caso). Il codice rende il primo foglio di lavoro in formati immagine PNG e TIFF. Infine, viene esportato come file PDF.

{{% alert color="primary" %}}

Il valore predefinito dell'attributo **CheckWorkbookDefaultFont** è **true**.

{{% /alert %}}

Questa è la schermata del file di [modello](49446913.xlsx) utilizzato nel codice di esempio.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Questa è l'immagine PNG di output dopo aver impostato la proprietà [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) su "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Guarda l'immagine [TIFF](48496672.tiff) di output dopo aver impostato la proprietà [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) su "Times New Roman".

Vedi il file [PDF](48496673.pdf) di output dopo aver impostato la proprietà [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) a "Times New Roman".

## **Codice di Esempio**

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
