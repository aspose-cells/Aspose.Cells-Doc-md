---
title: Calcolare il fattore di scalatura della configurazione della pagina con C++
linktitle: Calcola il fattore di scala della pagina di impostazione
type: docs
weight: 300
url: /it/cpp/calculate-page-setup-scaling-factor/
description: Questo articolo fornisce codice di esempio che spiega come usare l API o libreria C++ per calcolare il fattore di scalatura della configurazione della pagina usando l opzione adatta a n pagine di larghezza per m di altezza di un foglio Excel in modo programmatico.
keywords: Adatta a n pagine di larghezza per m di altezza in Excel C++, calcola il fattore di scalatura della configurazione della pagina C++
---

{{% alert color="primary" %}}

Quando si imposta il fattore di scala dell'impostazione della pagina utilizzando l'opzione **Fit to n page(s) wide by m tall**, Microsoft Excel calcola il Fattore di scala dell'impostazione della pagina. È possibile calcolare la stessa cosa utilizzando la proprietà [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/). Questa proprietà restituisce un valore double che può essere convertito in valore percentuale. Ad esempio, se restituisce 0.5 significa che il fattore di scala è del 50%.

{{% /alert %}}

Il seguente codice di esempio illustra come calcolare il fattore di scala dell'impostazione della pagina utilizzando la proprietà [**SheetRender.GetPageScale()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/getpagescale/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some data in these cells
    worksheet.GetCells().Get(u"A4").PutValue(u"Test");
    worksheet.GetCells().Get(u"S4").PutValue(u"Test");

    // Set paper size
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Set fit to pages wide as 1
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Calculate page scale via sheet render
    ImageOrPrintOptions options;
    SheetRender sr(worksheet, options);

    // Convert page scale double value to percentage
    double pageScale = sr.GetPageScale();
    std::wstring strPageScale = std::to_wstring(pageScale * 100) + L"%";

    // Write the page scale value
    std::wcout << strPageScale << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
