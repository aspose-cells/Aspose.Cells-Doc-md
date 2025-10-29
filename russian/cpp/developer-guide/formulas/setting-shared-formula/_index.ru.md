---
title: Настройка общей формулы с использованием C++
linktitle: Настройка общих формул
type: docs
weight: 10
url: /ru/cpp/setting-shared-formula/
description: Узнайте, как задавать общие формулы в Excel с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Если вы хотите добавить функцию в лист для выполнения расчетов, эта статья объясняет, как выполнить эту задачу с помощью Aspose.Cells.

{{% /alert %}}

## Установка общей формулы с использованием Aspose.Cells

Предположим, у вас есть лист с данными в формате, который выглядит как приведенный ниже образец листа.

|**Входной файл с одним столбцом данных**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Вы хотите добавить функцию в B2, которая будет вычислять налог с продаж для первой строки данных. Налог составляет **9%**. Формула, вычисляющая налог с продаж, такова: **"=A2*0.09"**. В этой статье объясняется, как применить эту формулу с помощью Aspose.Cells.

Aspose.Cells позволяет указывать формулу, используя свойство [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/). Для других ячеек (B3, B4, B5 и так далее) в столбце есть два варианта добавления формул.

Либо выполните то, что вы делали для первой ячейки, фактически устанавливая формулу для каждой ячейки, соответствующим образом обновляя ссылку на ячейку (A3*0.09, A4*0.09, A5*0.09 и так далее). Это требует обновления ссылок на ячейки для каждой строки. Также необходимо, чтобы Aspose.Cells анализировал каждую формулу отдельно, что может быть затратным по времени для больших таблиц и сложных формул. Кроме того, это требует дополнительных строк кода, хотя циклы могут немного сократить их.

Другой подход - использовать **общую формулу**. С общей формулой формулы автоматически обновляются для ссылок на ячейки в каждой строке, чтобы налог был рассчитан правильно. Метод [**SetSharedFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setsharedformula/) более эффективен, чем первый метод.

Приведенный ниже пример демонстрирует, как его использовать.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Instantiate a Workbook from existing file
    Workbook workbook(inputFilePath);

    // Get the cells collection in the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Apply the shared formula in the range i.e.., B2:B14
    cells.Get(u"B2").SetSharedFormula(u"=A2*0.09", 13, 1);

    // Save the excel file
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Shared formula applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
