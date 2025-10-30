---
title: Grafico in PDF con C++
linktitle: Grafico in PDF
description: Impara come usare Aspose.Cells for C++ per convertire un grafico in un documento PDF. La nostra guida dimostrerà come esportare un grafico da Microsoft Excel e salvarlo come PDF per ulteriore distribuzione e archiviazione.
keywords: Aspose.Cells for C++, Grafico in PDF, Microsoft Excel, Conversione in PDF, Esportazione, Distribuzione, Archiviazione.
type: docs
weight: 47
url: /it/cpp/chart-to-pdf/
---

## **Rendering del grafico in PDF**

Per rendere il grafico in formato PDF, le API Aspose.Cells hanno esposto il metodo [**Chart::ToPdf**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/topdf/) con la possibilità di memorizzare il PDF risultante sul percorso del disco o su Stream.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its index to WorksheetCollection
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(4);
    worksheet.GetCells().Get(u"B2").PutValue(20);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add Series Collection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Convert chart to PDF
    chart.ToPdf(outDir + u"chartPDF_out.pdf");

    std::cout << "Chart converted to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Crea Grafico PDF con Dimensione Pagina Desiderata**
Puoi creare un PDF del grafico con la dimensione della pagina desiderata utilizzando Aspose.Cells e specificare come allineare il grafico all'interno della pagina, ad esempio in alto, in basso, al centro, a sinistra, a destra, ecc. Inoltre, il grafico di output può essere creato in uno stream o su disco. Si prega di vedere il seguente esempio di codice che carica il [file Excel di esempio](64716906.xlsx), accede al primo grafico all’interno del foglio di lavoro e lo converte in [PDF di output](64716907.pdf) con la dimensione della pagina desiderata. Lo screenshot seguente mostra che la dimensione della pagina nel PDF di output è 7x7 come specificato nel codice, e il grafico è allineato al centro sia orizzontalmente che verticalmente.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)

## **Codice di Esempio**
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

    // Load sample Excel file containing the chart
    Workbook wb(srcDir + u"sampleCreateChartPDFWithDesiredPageSize.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart ch = ws.GetCharts().Get(0);

    // Create chart pdf with desired page size
    ch.ToPdf(outDir + u"outputCreateChartPDFWithDesiredPageSize.pdf", 7, 7, PageLayoutAlignmentType::Center, PageLayoutAlignmentType::Center);

    std::cout << "Chart PDF created successfully with desired page size!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
