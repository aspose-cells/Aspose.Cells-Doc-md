---
title: Поиск данных по исходным значениям с помощью C++
linktitle: Поиск данных с использованием исходных значений
type: docs
weight: 380
url: /ru/cpp/search-data-using-original-values/
description: Узнайте, как осуществлять поиск данных по исходным значениям через API Aspose.Cells for C++.
keywords: Поиск данных по исходным значениям, Поиск данных по исходным значениям, Поиск данных по исходным значениям, Поиск данных по исходным значениям
---

{{% alert color="primary" %}}

Иногда значение данных скрыто, потому что оно отформатировано каким-то образом. Например, предположим, что ячейка D4 имеет формулу =Сумма(A1:A2) и ее значение равно 20, но оно отформатировано как ---, то значение 20 скрыто и не может быть найдено с помощью функции поиска в Microsoft Excel. Однако вы можете найти его с помощью Aspose.Cells, используя [**LookInType.OriginalValues**](https://reference.aspose.com/cells/cpp/aspose.cells/lookintype/)

{{% /alert %}}

Приведенный ниже образец кода иллюстрирует вышеупомянутый момент. Он находит ячейку D4, которую нельзя найти с помощью опций поиска Microsoft Excel, но Aspose.Cells может найти ее с помощью [**LookInType.OriginalValues**](https://reference.aspose.com/cells/cpp/aspose.cells/lookintype/). Пожалуйста, прочтите комментарии внутри кода для получения дополнительной информации.

## Код C++ для поиска данных по исходным значениям

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

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add 10 in cell A1 and A2
    worksheet.GetCells().Get(u"A1").PutValue(10);
    worksheet.GetCells().Get(u"A2").PutValue(10);

    // Add Sum formula in cell D4 but customize it as ---
    Cell cell = worksheet.GetCells().Get(u"D4");

    Style style = cell.GetStyle();
    style.SetCustom(u"---", true);
    cell.SetStyle(style);

    // The result of formula will be 20 but 20 will not be visible because the cell is formatted as ---
    cell.SetFormula(u"=Sum(A1:A2)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Create find options, we will search 20 using original values otherwise 20 will never be found because it is formatted as ---
    FindOptions options;
    options.SetLookInType(LookInType::OriginalValues);
    options.SetLookAtType(LookAtType::EntireContent);

    Cell foundCell;
    int32_t obj = 20;

    // Find 20 which is Sum(A1:A2) and formatted as ---
    foundCell = worksheet.GetCells().Find(obj, foundCell, options);

    // Print the found cell
    std::cout << foundCell.ToString().ToUtf8() << std::endl;

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## Консольный вывод, сгенерированный образцовым кодом

Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
