---
title: Filtra Oggetti durante il caricamento del Workbook o del Foglio di lavoro con C++
linktitle: Filtra gli Oggetti durante il caricamento del Workbook o del Foglio di Lavoro
type: docs
weight: 330
url: /it/cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Impara come filtrare oggetti come grafici, forme e formattazione condizionale durante il caricamento di workbooks o fogli di lavoro usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**
 Si prega di usare la proprietà [LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) durante il filtraggio dei dati dal workbook. Ma se si desidera filtrare i dati da fogli di lavoro individuali, sarà necessario sovrascrivere il metodo [LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/). Si prega di fornire il valore appropriato dall'enumerazione [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) durante la creazione o la gestione di [LoadFilter](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/).

L'enumerazione [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) ha i seguenti valori possibili.

- Tutti
- Impostazioni del libro
- Cellavuota
- Cella booleana
- Dati cella
- Errore cella
- Numerico cella
- Stringa cella
- Valore cella
- Chart
- Formattazione condizionale
- Convalida dati
- Nomi definiti
- Proprietà documento
- Formula
- Collegamenti ipertestuali
- Area unita
- Tabella pivot
- Impostazioni
- Forma
- Dati del Foglio
- Impostazioni del Foglio
- Struttura
- Stile
- Tabella
- VBA
- XmlMap

## **Filtra oggetti durante il caricamento della cartella di lavoro**
Il codice di esempio seguente illustra come filtrare i grafici dalla cartella di lavoro. Si prega di controllare il [file excel di esempio](5115258.xlsx) utilizzato in questo codice e il [PDF di output](5115257.pdf) generato da esso. Come si può vedere nel PDF di output, tutti i grafici sono stati filtrati fuori dalla cartella di lavoro.

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

    // Filter charts from the workbook
    LoadOptions lOptions;
    lOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Load the workbook with the above filter
    U16String inputFilePath = srcDir + u"sampleFilterCharts.xlsx";
    Workbook workbook(inputFilePath, lOptions);

    // Save worksheet to a single PDF page
    PdfSaveOptions pOptions;
    pOptions.SetOnePagePerSheet(true);

    // Save the workbook in PDF format
    U16String outputFilePath = outDir + u"sampleFilterCharts.pdf";
    workbook.Save(outputFilePath, pOptions);

    std::cout << "Workbook saved successfully with filtered charts!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Filtra oggetti durante il caricamento del foglio di lavoro**
Il codice di esempio seguente carica il [file Excel di origine](5115255.xlsx) e filtra i seguenti dati dai suoi fogli di lavoro utilizzando un filtro personalizzato.

- Filtra i Grafici dalla cartella di lavoro denominata NoCharts.
- Filtra le Forme dalla cartella di lavoro denominata NoShapes.
- Filtra la formattazione condizionale dalla cartella di lavoro denominata NoConditionalFormatting.

Una volta caricato il [file Excel di origine](5115255.xlsx) con un filtro personalizzato, si prendono le immagini di tutti i fogli di lavoro uno per uno. Ecco le immagini di output per il riferimento. Come si può vedere, la prima immagine non contiene grafici, la seconda immagine non ha forme e la terza immagine non ha formattazione condizionale.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoadFilter : public LoadFilter
{
public:
    void StartSheet(Worksheet& sheet) override
    {
        U16String sheetName = sheet.GetName();

        if (sheetName == u"NoCharts")
        {
            // Load everything and filter charts
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::Chart)));
        }

        if (sheetName == u"NoShapes")
        {
            // Load everything and filter shapes
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::Drawing)));
        }

        if (sheetName == u"NoConditionalFormatting")
        {
            // Load everything and filter conditional formatting
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::ConditionalFormatting)));
        }
    }
};

// Add main function to serve as entry point
int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Cleanup();
    return 0;

}
```

Così si utilizza la classe CustomLoadFilter come per i nomi dei fogli di lavoro.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoadFilter : public LoadFilter
{
public:
    CustomLoadFilter() : LoadFilter(LoadDataFilterOptions::All) {}
};

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Filter worksheets using CustomLoadFilter class
    LoadOptions loadOpts;
    CustomLoadFilter customLoadFilter;
    loadOpts.SetLoadFilter(&customLoadFilter);

    // Load the workbook with filter defined in CustomLoadFilter class
    Workbook workbook(srcDir + u"sampleCustomFilteringPerWorksheet.xlsx", loadOpts);

    // Take the image of all worksheets one by one
    WorksheetCollection sheets = workbook.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        // Access worksheet at index i
        Worksheet worksheet = sheets.Get(i);

        // Create an instance of ImageOrPrintOptions
        // Render entire worksheet to image
        ImageOrPrintOptions imageOpts;
        imageOpts.SetOnePagePerSheet(true);
        imageOpts.SetImageType(Aspose::Cells::Drawing::ImageType::Png);

        // Convert worksheet to image
        SheetRender render(worksheet, imageOpts);
        render.ToImage(0, outDir + u"outputCustomFilteringPerWorksheet_" + worksheet.GetName() + u".png");
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
