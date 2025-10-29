---
title: Отображение диапазона ячеек как метки данных с помощью C++
linktitle: Отображение диапазона ячеек в качестве меток данных
description: Узнайте, как отображать диапазон ячеек как метки данных в графиках с помощью Aspose.Cells for C++. Наше руководство продемонстрирует, как связать метки с источником данных и форматировать их для предоставления точной и значимой информации в ваших графиках.
keywords: Aspose.Cells for C++, построение графиков, метки данных, диапазон ячеек, источник данных, форматирование, точность, значимая информация.
type: docs
weight: 130
url: /ru/cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

В Microsoft Excel 2013 вы можете отображать диапазон ячеек в качестве меток данных. Aspose.Cells поддерживает эту функцию.

{{% /alert %}}

## **Флажок для отображения диапазона ячеек в качестве меток данных**

Чтобы показать диапазон ячеек в качестве меток данных в Microsoft Excel:

1. Выберите метки данных ряда и щелкните правой кнопкой мыши, чтобы открыть контекстное меню.
1. Выберите **Формат меток данных**. Опции меток отображаются.
1. Выберите или снимите флажок у опции **Метка содержит - значение из ячеек**.

В приведенном ниже образце кода доступ к меткам данных серии графика и устанавливает свойство [**DataLabels.GetShowCellRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/getshowcellrange/) в **true**, чтобы выбрать опцию **Метка содержит - значение из ячеек**.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook from the source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Check the "Label Contains - Value From Cells"
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();
    dataLabels.SetShowCellRange(true);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
