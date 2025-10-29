---
title: Применить заливку к чередующимся строкам и столбцам с помощью условного форматирования в C++
linktitle: Применить заливку к чередующимся строкам и столбцам
description: Как использовать библиотеку Aspose.Cells в C++ для применения теней к условному форматированию для чередующихся строк и столбцов. Настраивая эти критерии, вы получаете больший контроль над внешним видом ячеек.
keywords: Aspose.Cells, Условное форматирование, C++, Чередующиеся строки, Чередующиеся столбцы, Тени
type: docs
weight: 30
url: /ru/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

API Aspose.Cells предоставляет средства для добавления и управления правилами условного форматирования для объекта [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Эти правила могут быть настроены различными способами для достижения желаемого форматирования в зависимости от условий или правил. В этой статье продемонстрируется использование API Aspose.Cells for C++ для применения теней к чередующимся строкам и столбцам с помощью правил условного форматирования и встроенных функций Excel.

{{% /alert %}}

В этой статье используются встроенные функции Excel, такие как ROW, COLUMN & MOD. Вот некоторые подробности об этих функциях для лучшего понимания предоставленного фрагмента кода.

- Функция **ROW()** возвращает номер строки ссылочной ячейки. Если параметр ссылки опущен, то предполагается, что ссылка - это адрес ячейки, в которой была введена функция ROW().
- Функция **COLUMN()** возвращает номер столбца для ссылочной ячейки. Если параметр ссылки опущен, то предполагается, что ссылка - это адрес ячейки, в которой была введена функция COLUMN().
- **Функция MOD()** возвращает остаток после деления числа на делитель, где первый параметр функции - это числовое значение, для которого вы хотите найти остаток, и второй параметр - это число, используемое для деления числа. Если делитель равен 0, то она вернет ошибку #DIV/0!.

Давайте начнем писать код для достижения этой цели с помощью API Aspose.Cells for C++.

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

    // Create an instance of Workbook
    Workbook book;

    // Access the Worksheet on which desired rule has to be applied
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add FormatConditions to the instance of Worksheet
    int idx = sheet.GetConditionalFormattings().Add();

    // Access the newly added FormatConditions via its index
    auto conditionCollection = sheet.GetConditionalFormattings().Get(idx);

    // Define a CellsArea on which conditional formatting will be applicable
    // The code creates a CellArea ranging from A1 to I20
    CellArea area = CellArea::CreateCellArea(u"A1", u"I20");

    // Add area to the instance of FormatConditions
    conditionCollection.AddArea(area);

    // Add a condition to the instance of FormatConditions
    // For this case, the condition type is expression, which is based on some formula
    idx = conditionCollection.AddCondition(FormatConditionType::Expression);

    // Access the newly added FormatCondition via its index
    FormatCondition formatCondition = conditionCollection.Get(idx);

    // Set the formula for the FormatCondition
    // Formula uses the Excel's built-in functions as discussed earlier in this article
    formatCondition.SetFormula1(u"=MOD(ROW(),2)=0");

    // Set the background color and pattern for the FormatCondition's Style
    formatCondition.GetStyle().SetBackgroundColor(Color::Blue());
    formatCondition.GetStyle().SetPattern(BackgroundType::Solid);

    // Save the result on disk
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

В следующем снимке экрана показан полученный электронный лист, загруженный в приложение Excel.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Для применения засветки к альтернативным столбцам вам нужно изменить формулу **=MOD(ROW(),2)=0** на **=MOD(COLUMN(),2)=0**, то есть вместо получения индекса строки измените формулу для получения индекса столбца. 
Результирующая электронная таблица в этом случае будет выглядеть следующим образом.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="cpp" >}}
