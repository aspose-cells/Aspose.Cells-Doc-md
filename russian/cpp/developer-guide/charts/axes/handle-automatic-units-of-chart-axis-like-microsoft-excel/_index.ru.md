---
title: Обработка автоматических единиц осей графика, как в Microsoft Excel с помощью C++
linktitle: Обработка автоматических единиц осей графика
description: Узнайте, как обрабатывать автоматические единицы на осях графика в Aspose.Cells for C++, аналогично Microsoft Excel. Наш гид покажет вам, как настраивать и модифицировать автоматические единицы на оси графика, включая отображение научной нотации и регулировку масштаба.
keywords: Aspose.Cells for C++, оси графика, автоматические единицы, Microsoft Excel, настройка, модификация, научная нотация, масштабирование.
type: docs
weight: 120
url: /ru/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **Возможные сценарии использования**
Прежние версии Aspose.Cells не могли правильно управлять автоматическими единицами оси диаграммы при рендеринге диаграммы в изображение или PDF. Теперь Aspose.Cells поддерживает управление автоматическими единицами оси диаграммы. Нет изменений в коде. Просто преобразуйте свою диаграмму в изображение или PDF, и она будет отображать ось диаграммы точно так же, как это делает Microsoft Excel.

## **Обработка автоматических единиц оси диаграммы, как в Microsoft Excel**
В следующем образце кода загружается [образец файла Excel](61767755.xlsx) и генерируется [выходная PDF-диаграмма](61767752.pdf). На скриншоте показаны автоматические единицы оси диаграммы в красных прямоугольниках, а также сравниваются образцовая диаграмма файла Excel и выходная PDF-диаграмма. Обе идентичны.

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)

## **Образец кода**
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

    // Load the sample Excel file
    U16String inputFilePath = srcDir + u"sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access first chart
    ChartCollection charts = ws.GetCharts();
    Chart ch = charts.Get(0);

    // Render chart to PDF
    U16String outputFilePath = outDir + u"outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf";
    ch.ToPdf(outputFilePath);

    std::cout << "Chart rendered to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
