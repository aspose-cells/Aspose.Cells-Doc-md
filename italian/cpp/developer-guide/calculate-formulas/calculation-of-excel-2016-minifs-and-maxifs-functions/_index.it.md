---
title: Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016 con C++
description: Questo articolo introduce come usare la libreria Aspose.Cells per calcolare le funzioni MINIFS e MAXIFS in Microsoft Excel 2016 usando C++.
keywords: Aspose.Cells, Excel, 2016, funzione MINIFS, funzione MAXIFS, calcolo
type: docs
weight: 300
url: /it/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Possibili Scenari di Utilizzo**
Microsoft Excel 2016 supporta le funzioni MINIFS e MAXIFS. Queste funzioni non sono supportate in Excel 2013 o versioni precedenti. Aspose.Cells supporta anche il calcolo di queste funzioni. Lo screenshot seguente illustra l'uso di queste funzioni. Si prega di leggere i commenti in rosso all'interno dello screenshot per capire come funzionano queste funzioni.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016**
Il seguente esempio di codice carica il [file Excel di esempio](5115149.xlsx) e chiama il metodo [Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) per eseguire il calcolo delle formule tramite Aspose.Cells e poi salva i risultati in un [file PDF di output](5115154.pdf).

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source workbook containing MINIFS and MAXIFS functions
    Workbook workbook(srcDir + u"sampleMINIFSAndMAXIFS.xlsx");

    // Perform Aspose.Cells formula calculation
    workbook.CalculateFormula();

    // Save the calculations result in pdf format
    PdfSaveOptions options;
    options.SetOnePagePerSheet(true);
    workbook.Save(outDir + u"outputMINIFSAndMAXIFS.pdf", options);

    std::cout << "PDF saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
