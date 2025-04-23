---
title: Вычисление массивной формулы таблиц данных с помощью C++
linktitle: Вычисление массивной формулы таблиц данных
description: Как использовать библиотеку Aspose.Cells для вычисления массивных формул для таблицы данных в Microsoft Excel с C++. Загружая существующий файл Excel или создавая новый файл Excel, мы можем использовать предоставленный Aspose.Cells метод для вычисления массивной формулы таблицы данных и получения результата. В конце мы сохраняем изменённый файл Excel на диск.
keywords: Aspose.Cells, Excel, таблицы данных, массивные формулы, вычисления, C++
type: docs
weight: 70
url: /ru/cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Вы можете создать таблицу данных в Microsoft Excel, используя Данные > Анализ по сценариям > Таблица данных.... Теперь Aspose.Cells позволяет вычислять массивные формулы таблицы данных. Пожалуйста, используйте [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) так, как обычно, чтобы вычислить любой тип формул.

{{% /alert %}}

В следующем образце кода мы использовали [исходный файл Excel](5115535.xlsx). Если вы измените значение ячейки B1 на 100, значения Таблицы данных, заполненные желтым цветом, станут равными 120, как показано на следующих изображениях. Образец кода генерирует [выходной PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Вот образец кода, используемый для генерации [выходного PDF](5115538.pdf) из [исходного файла Excel](5115535.xlsx). Пожалуйста, прочитайте комментарии для получения дополнительной информации.

```cpp
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
    U16String inputFilePath = srcDir + u"DataTable.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
    worksheet.GetCells().Get(u"B1").PutValue(100);

    // Calculate formula, now it also calculates Data Table array formula
    workbook.CalculateFormula();

    // Save the workbook in pdf format
    workbook.Save(outDir + u"output_out.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
