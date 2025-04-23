---
title: Filtrare il tipo di dati durante il caricamento del workbook da file modello con C++
linktitle: Filtrare i dati durante il caricamento del workbook
type: docs
weight: 400
url: /it/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: Impara come filtrare tipi di dati specifici durante il caricamento di un workbook da un file modello usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A volte, si vuole specificare quale tipo di dati deve essere caricato quando si costruisce il workbook dal file modello. Il filtraggio dei dati caricati può migliorare le prestazioni per uno scopo particolare, specialmente quando si usano le API [LightCells](/cells/it/cpp/using-lightcells-api/). Si prega di utilizzare la proprietà [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) a questo scopo.

{{% /alert %}}

Il codice di esempio seguente carica solo gli oggetti di forma durante il caricamento della cartella di lavoro dal [file di modello](5115552.xlsx) che è possibile scaricare dal link fornito. Lo screenshot seguente mostra i contenuti del [file di modello](5115552.xlsx) e spiega anche che i dati di colore rosso e sfondo giallo non saranno caricati perché la proprietà [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) è stata impostata su [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Lo screenshot seguente mostra il [PDF di output](5115555.pdf) che è possibile scaricare dal link fornito. Qui si può vedere che i dati di colore rosso e sfondo giallo non sono presenti ma ci sono tutte le forme.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

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

    // Set the load options, we only want to load shapes and do not want to load data
    LoadOptions loadOptions(LoadFormat::Xlsx);
    loadOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Create workbook object from sample excel file using load options
    Workbook workbook(srcDir + u"sampleFilterChars.xlsx", loadOptions);

    // Save the output in pdf format
    workbook.Save(outDir + u"sampleFilterChars_out.pdf", SaveFormat::Pdf);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
