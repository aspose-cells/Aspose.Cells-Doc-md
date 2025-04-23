---
title: Преобразование диаграммы в PDF с помощью C++
linktitle: Диаграмма в PDF
description: Узнайте, как использовать Aspose.Cells for C++ для преобразования диаграммы в PDF документ. Наше руководство продемонстрирует, как экспортировать диаграмму из Microsoft Excel и сохранить её как PDF для дальнейшего распространения и архивации.
keywords: Aspose.Cells for C++, Диаграмма в PDF, Microsoft Excel, Преобразование в PDF, Экспорт, Распространение, Архивация.
type: docs
weight: 47
url: /ru/cpp/chart-to-pdf/
---

## **Отображение диаграммы в формат PDF**

Чтобы рендерить диаграмму в формат PDF, API Aspose.Cells предоставляют метод [**Chart::ToPdf**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/topdf/) с возможностью сохранять итоговый PDF на диске или в поток.

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

## **Создание PDF-файла диаграммы с выбранным размером страницы**
Вы можете создавать PDF диаграммы с желаемым размером страницы, используя Aspose.Cells, и задавать, как вы хотите выравнивать диаграмму внутри страницы — сверху, снизу, по центру, слева, справа и т. д. Кроме того, результирующая диаграмма может быть создана в потоке или на диск. Ниже приведён пример кода, который загружает [образец файла Excel](64716906.xlsx), получает первую диаграмму внутри листа и затем преобразует её в [выходной PDF](64716907.pdf) с нужным размером страницы. Следующий скриншот показывает, что размер страницы в выходящем PDF — 7x7, как указано в коде, а диаграмма выравнена по центру как по горизонтали, так и по вертикали.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)

## **Образец кода**
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
