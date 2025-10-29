---  
title: Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона с помощью C++  
description: Узнайте, как изменить источник данных диаграммы на целевой лист при копировании строк или диапазона в Aspose.Cells for C++. Наш практи guide покажет, как обновлять диапазон данных диаграммы и связывать его с целевым листом, обеспечивая точное отображение скопированных строк или диапазона в диаграмме.  
keywords: Aspose.Cells for C++, построение диаграмм, источник данных, целевой лист, строки, диапазон, копирование, обновление, диапазон данных, связывание.  
type: docs  
weight: 440  
url: /ru/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **Возможные сценарии использования**

Когда вы копируете строки или диапазон с диаграммами в новый лист, источник данных диаграммы не меняется. Например, если источник данных диаграммы =Sheet1!$A$1:$B$4, то после копирования строк или диапазона на новый лист источник данных останется прежним, то есть =Sheet1!$A$1:$B$4. Он по-прежнему ссылается на старый лист, то есть Sheet1. Это также поведение в Microsoft Excel. Но если вы хотите, чтобы он ссылался на новый лист назначения, используйте свойство [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/) и установите его в значение **true** при вызове метода [**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/). Тогда, если ваш лист назначения — DestSheet, источник данных для вашей диаграммы изменится с =Sheet1!$A$1:$B$4 на =DestSheet!$A$1:$B$4.

## **Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона**

Следующий пример кода объясняет использование свойства [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/) при копировании строк или диапазона с диаграммами на новый лист. Код использует [образец файла Excel](5113699.xlsx) и создает [выходной файл Excel](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access the first sheet which contains chart
    Worksheet source = wb.GetWorksheets().Get(0);

    // Add another sheet named DestSheet
    Worksheet destination = wb.GetWorksheets().Add(u"DestSheet");

    // Set CopyOptions.ReferToDestinationSheet to true
    CopyOptions options;
    options.SetReferToDestinationSheet(true);

    // Copy all the rows of source worksheet to destination worksheet which includes chart as well
    // The chart data source will now refer to DestSheet
    destination.GetCells().CopyRows(source.GetCells(), 0, 0, source.GetCells().GetMaxDisplayRange().GetRowCount(), options);

    // Save workbook in xlsx format
    wb.Save(srcDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
