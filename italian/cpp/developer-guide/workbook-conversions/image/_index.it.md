---
title: Converti Excel in immagine con C++
linktitle: Convertire Excel in Immagine
type: docs
weight: 300
url: /it/cpp/convert-excel-to-image/
description: Impara come convertire fogli di lavoro Excel in immagini, tra cui formati TIFF e SVG, usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells ti consente di esportare un foglio di lavoro dalla cartella di lavoro e convertirlo in diversi formati. Questo articolo spiega come convertire un foglio di lavoro in formati diversi.

{{% /alert %}}

## Conversione del Workbook in TIFF

Un file Excel può contenere più fogli con più pagine. [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) ti permette di convertire Excel in TIFF con più pagine. Inoltre, puoi controllare molte opzioni per TIFF, come [Compression](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/), [GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/), Risoluzione ([GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/), [GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)).

Il seguente snippet di codice mostra come convertire Excel in TIFF con pagine multiple. Il [file Excel di origine](workbook-to-tiff-with-mulitiple-pages.xlsx) e l'[immagine TIFF generata](workbook-to-tiff-with-mulitiple-pages.tiff) sono allegati per il tuo riferimento.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main() {
    Aspose::Cells::Startup();

    // Load the workbook
    Workbook wb(u"workbook-to-tiff-with-mulitiple-pages.xlsx");

    // Create image options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Tiff);

    // Set resolution to 200 DPI
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetVerticalResolution(200);

    // Set TIFF compression to LZW
    imgOptions.SetTiffCompression(TiffCompression::CompressionLZW);

    // Render the workbook to TIFF
    WorkbookRender workbookRender(wb, imgOptions);
    workbookRender.ToImage(u"workbook-to-tiff-with-mulitiple-pages.tiff");

    std::cout << "Workbook rendered to TIFF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Conversione del foglio di lavoro in immagine**

I fogli di lavoro contengono dati che si desidera analizzare. Ad esempio, un foglio di lavoro può contenere parametri, totali, percentuali, eccezioni e calcoli.

Come sviluppatore, potresti aver bisogno di presentare i fogli di lavoro come immagini. Ad esempio, potresti aver bisogno di utilizzare un'immagine di un foglio di lavoro in un'applicazione o una pagina web. Potresti voler inserire un'immagine in un documento di Microsoft Word, un file PDF, una presentazione PowerPoint o qualche altro tipo di documento. In poche parole, desideri un foglio di lavoro reso come immagine in modo che tu possa usarlo altrove.

Aspose.Cells supporta la conversione di fogli di lavoro Excel in immagini. Per usare questa funzionalità, devi importare lo spazio dei nomi [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) nel tuo programma o progetto. Offre diverse classi utili per rendering e stampa, ad esempio [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/), e altri.

La classe [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) rappresenta un foglio di lavoro da rendere come immagine. Ha un metodo sovraccaricato, [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), che può convertire un foglio di lavoro in uno o più file immagine con attributi o opzioni diversi. Restituisce un oggetto `System.Drawing.Bitmap` e puoi salvare un’immagine su disco o in streaming. Sono supportati diversi formati di immagine, ad esempio BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Il seguente frammento di codice mostra come convertire un foglio di lavoro in un file immagine.

```cpp
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::wstring numStr = std::to_wstring(j + 1);
        U16String numU16Str(reinterpret_cast<const char16_t*>(numStr.c_str()));
        U16String outputPath = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + numU16Str + U16String(u".tif");
        sr.ToImage(j, outputPath);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Attualmente, l'API per la conversione dei fogli di lavoro in immagini non supporta i grafici a bolle 3D.

{{% /alert %}}

## **Conversione del foglio di lavoro in SVG**

SVG sta per Scalable Vector Graphics. SVG è una specifica basata su standard XML per grafica vettoriale bidimensionale. È uno standard aperto che è stato in fase di sviluppo da parte del World Wide Web Consortium (W3C) dal 1999.

Aspose.Cells for C++ è in grado di convertire i fogli di lavoro in immagini SVG dal versione 7.1.0. Il seguente esempio di codice mostra come convertire un foglio di lavoro in un file immagine SVG.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a workbook
    Workbook workbook;

    // Put sample text in the first cell of first worksheet in the newly created workbook
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET1");

    // Add second worksheet in the workbook
    workbook.GetWorksheets().Add(SheetType::Worksheet);

    // Set text in first cell of the second sheet
    workbook.GetWorksheets().Get(1).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET2");

    // Set currently active sheet index to 1 i.e. Sheet2
    workbook.GetWorksheets().SetActiveSheetIndex(1);

    // Save workbook to SVG. It shall render the active sheet only to SVG
    workbook.Save(outDir + u"ConvertWorksheetToSVG_out.svg");

    std::cout << "Worksheet converted to SVG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Converti un Grafico Excel in Immagine](/cells/it/cpp/convert-an-excel-chart-to-image/)
- [Conversione del grafico in Immagine in formato SVG](/cells/it/cpp/converting-chart-to-image-in-svg-format/)
- [Esportare il grafico in SVG con attributo viewBox](/cells/it/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [Monitora il progresso della conversione di Excel in TIFF](/cells/it/cpp/track-conversion-progress-of-excel-to-tiff/)
