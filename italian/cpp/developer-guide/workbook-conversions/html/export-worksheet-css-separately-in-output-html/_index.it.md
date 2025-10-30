---
title: Esporta CSS del foglio di lavoro separatamente nel output HTML con C++
linktitle: Esporta il foglio di lavoro CSS separatamente in HTML di output
type: docs
weight: 80
url: /it/cpp/export-worksheet-css-separately-in-output/
description: Impara come esportare il CSS del foglio di lavoro separatamente quando converti file Excel in HTML usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells offre la funzione di esportare il CSS del foglio di lavoro separatamente durante la conversione del file Excel in HTML. Per questo scopo, usa la proprietà [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/) e impostala su **true** durante il salvataggio del file Excel in formato HTML.

## **Esportare il Foglio di Stile CSS Separatamente nell'HTML di Output**

Il seguente codice di esempio crea un file Excel, aggiunge del testo nella cella **B5** di colore **Rosso** e poi lo salva nel formato HTML utilizzando la proprietà [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/). Si prega di vedere l'HTML di output nel [HTML generato](60489766.zip) dal codice per riferimento. All'interno si troverà **stylesheet.css** come risultato del codice di esempio.

## **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and put value inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This is some text.");

    // Set the style of the cell - font color is Red
    Style st = cell.GetStyle();
    st.GetFont().SetColor(Color::Red());
    cell.SetStyle(st);

    // Specify html save options - export worksheet css separately
    HtmlSaveOptions opts;
    opts.SetExportWorksheetCSSSeparately(true);

    // Save the workbook in html
    wb.Save(u"outputExportWorksheetCSSSeparately.html", opts);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Esporta Workbook a singolo foglio in HTML**

Quando si converte un workbook con più fogli in HTML usando Aspose.Cells, viene creato un file HTML insieme a una cartella contenente CSS e più file HTML. Quando si apre questo file HTML nel browser, sono visibili le schede. Lo stesso comportamento è richiesto per un workbook con un solo foglio di lavoro quando viene convertito in HTML. In passato, non veniva creata una cartella separata per i workbook a foglio singolo, e veniva creato solo un file HTML. Tale file HTML non mostra una scheda quando viene aperto nel browser. Anche MS Excel crea una cartella e un HTML corretti per un singolo foglio, e per questo motivo il comportamento identico è stato implementato usando le API di Aspose.Cells. Il file esempio può essere scaricato dal link seguente da utilizzare nel codice esempio sottostante:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleSingleSheet.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputSampleSingleSheet.htm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify HTML save options
    HtmlSaveOptions options;

    // Set optional settings
    options.SetEncoding(EncodingType::UTF8);
    options.SetExportImagesAsBase64(true);
    options.SetExportGridLines(true);
    options.SetExportSimilarBorderStyle(true);
    options.SetExportBogusRowData(true);
    options.SetExcludeUnusedStyles(true);
    options.SetExportHiddenWorksheet(true);

    // Save the workbook in HTML format with specified HTML save options
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
