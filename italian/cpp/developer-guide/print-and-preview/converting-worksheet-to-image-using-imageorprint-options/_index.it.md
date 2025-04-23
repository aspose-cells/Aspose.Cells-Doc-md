---
title: Conversione di Foglio di Lavoro in Immagine utilizzando le Opzioni Immagine o Stampa con C++
linktitle: Conversione di Foglio di Lavoro in Immagine
type: docs
weight: 90
url: /it/cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Impara come convertire un foglio di lavoro in un file immagine e applicare diverse opzioni di immagine e stampa usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Questo documento è progettato per offrire una comprensione dettagliata di come convertire un foglio di lavoro in un file immagine e applicare diverse opzioni di immagine e stampa per l'immagine, come risoluzione, compressione TIFF, formato immagine e qualità della pagina.

{{% /alert %}}

## **Salvataggio Fogli di lavoro in Immagini - Diverse Approcci**

A volte potrebbe essere necessario presentare i tuoi fogli di lavoro come rappresentazione illustrata. Potresti aver bisogno di inserire le immagini dei fogli di lavoro nelle tue applicazioni o pagine web, inserirle in un documento Word, un file PDF, una presentazione PowerPoint o utilizzarle in qualche altro scenario. In breve, vuoi un foglio di lavoro renderizzato come immagine in modo da poterlo usare altrove. Aspose.Cells supporta la conversione dei fogli di lavoro nei file Excel in immagini. Inoltre, Aspose.Cells supporta la configurazione di diverse opzioni come formato immagine, risoluzione (sia verticale che orizzontale), qualità dell'immagine e altre opzioni di stampa e immagine.

Potresti considerare l'automazione di Office, ma presenta i suoi svantaggi. Ci sono diverse ragioni e problematiche coinvolte, come sicurezza, stabilità, scalabilità, velocità, prezzo e funzioni. In breve, ci sono molte ragioni, con la principale che Microsoft stessa raccomanda vivamente di evitare l'automazione di Office da soluzioni software.

Quest'articolo mostra come creare un'applicazione console in Visual Studio, eseguire la conversione di un foglio di lavoro in immagine utilizzando diverse opzioni di immagine e stampa con poche e semplici righe di codice usando l'API Aspose.Cells.

È necessario includere lo spazio dei nomi [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) nel proprio programma/progetto. Ha diverse classi utili, ad esempio, [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/), ecc.

La classe [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) rappresenta un foglio di lavoro per il quale si vogliono creare immagini. Ha un metodo sovraccaricato [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) che può convertire direttamente un foglio di lavoro in uno o più file immagine specificati con le proprie caratteristiche o opzioni desiderate. Può restituire un oggetto bitmap e puoi salvare un file immagine sul disco/stream. Supporta diversi formati immagine, come BMP, PNG, GIF, JPEG, TIFF, EMF, e altri.

## **Utilizzo di Aspose.Cells per convertire un foglio di lavoro in immagine utilizzando opzioni ImageOrPrint**

### **Creazione di un workbook modello in Microsoft Excel**

Ho creato un nuovo workbook in MS Excel e aggiunto alcuni dati nel primo foglio di lavoro. Ora convertirò il foglio “Sheet1” del file modello in un’immagine “SheetImage.tiff” e applicherò diverse opzioni di immagine come risoluzioni orizzontali e verticali, TiffCompression, ecc.

### **Scarica e installa Aspose.Cells**

Per prima cosa, è necessario [scaricare](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++. Installarlo sul computer di sviluppo. Tutti i componenti [Aspose](http://www.aspose.com/), una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.

### **Crea un Progetto**

Avvia Visual Studio e crea una nuova applicazione console. Questo esempio mostrerà un'applicazione console in C++.

### **Aggiungi Riferimenti**

Questo progetto utilizzerà Aspose.Cells. Quindi, devi aggiungere un riferimento al componente Aspose.Cells nel tuo progetto. Ad esempio, aggiungi un riferimento a `...\Program Files\Aspose\Aspose.Cells for C++\Bin\Aspose.Cells.lib`.

### **Convertire foglio di lavoro in un file immagine**

```c++
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

    Workbook book(srcDir + u"sampleWorksheetToAnImage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(300);
    options.SetVerticalResolution(300);
    options.SetTiffCompression(TiffCompression::CompressionLZW);
    options.SetImageType(ImageType::Tiff);
    options.SetPrintingPage(PrintingPageType::Default);

    SheetRender sr(sheet, options);

    int pageIndex = 3;
    int pageNumber = pageIndex + 1;
    std::wstring pageStr = std::to_wstring(pageNumber);
    U16String pageNumberStr(reinterpret_cast<const char16_t*>(pageStr.c_str()));
    U16String outputPath = outDir + U16String(u"outputWorksheetToAnImage_") + pageNumberStr + U16String(u".tiff");
    sr.ToImage(pageIndex, outputPath);

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Opzioni di conversione**

È possibile salvare pagine specifiche come immagine. Il seguente codice converte i primi due fogli di lavoro di un workbook in immagini JPG.

```c++
#include <iostream>
#include <fstream>
#include <sstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"sampleSpecificPagesToImages.xlsx";
    Workbook workbook(inputPath);

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);

    SheetRender sr(worksheet, imgOptions);

    int32_t pageIndex = 3;

    Vector<uint8_t> imageData = sr.ToImage(pageIndex);

    std::wstringstream ws;
    ws << (pageIndex + 1);
    U16String pageNumStr(reinterpret_cast<const char16_t*>(ws.str().c_str()));

    U16String outputPath = outDir + u"outputSpecificPagesToImage_" + pageNumStr + u".jpg";
    std::ofstream outputFile(outputPath.ToUtf8(), std::ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Page rendered successfully to: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Conversione di immagine utilizzando WorkbookRender**

Un'immagine TIFF può contenere più di un frame. È possibile salvare l'intero workbook in un’unica immagine TIFF con più frame o pagine:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook wb(srcDir + u"sampleUseWorkbookRenderForImageConversion.xlsx");

    // Set image options
    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Tiff);

    // Render workbook to image
    WorkbookRender wr(wb, opts);
    wr.ToImage(outDir + u"outputUseWorkbookRenderForImageConversion.tiff");

    std::cout << "Workbook rendered to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
