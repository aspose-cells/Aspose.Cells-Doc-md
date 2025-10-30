---
title: Carica un immagine web da un URL in un foglio Excel con C++
linktitle: Carica un immagine web da un URL in un foglio di calcolo di Excel
type: docs
weight: 30
url: /it/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: Impara come convertire un immagine da URL in immagine incorporata in Excel usando C++ e API Aspose.Cells for C++.
keywords: Excel mostra immagine da URL, URL di excel a immagine, mostra immagine in excel da URL, excel inserisci immagine da URL, converti URL in immagine in excel, immagine excel da URL, carica immagine da URL in excel, C++, Excel
---

## Caricare un'immagine da un URL in un foglio di lavoro di Excel

L'API Aspose.Cells for C++ fornisce un metodo semplice per caricare immagini da URL nei fogli Excel. Questo articolo spiega come scaricare i dati dell'immagine in un flusso di memoria e inserirli nel foglio usando Aspose.Cells. L'immagine diventa incorporata nel file Excel e non richiede download esterni quando viene aperto.

## Codice di esempio

```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    try
    {
        // Create a new workbook
        Workbook wb;

        // Get the first worksheet
        WorksheetCollection worksheets = wb.GetWorksheets();
        Worksheet sheet = worksheets.Get(0);

        // Get the pictures collection
        PictureCollection pictures = sheet.GetPictures();

        // Insert the picture from local file to B2 cell (row 1, column 1)
        // Note: Image file should be pre-downloaded to source directory
        U16String imagePath = srcDir + u"aspose-logo.jpg";
        pictures.Add(1, 1, imagePath);

        // Save the Excel file
        wb.Save(outDir + u"webimagebook.out.xlsx");
        std::cout << "Image added successfully." << std::endl;
    }
    catch (const std::exception& ex)
    {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Per scenari che richiedono immagini sempre aggiornate da un URL, usa il metodo descritto in [Inserisci un'immagine collegata da indirizzo web](/cells/it/cpp/insert-a-linked-picture-from-web-address/). Questo approccio carica l'immagine dall'URL ogni volta che si apre il foglio.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
