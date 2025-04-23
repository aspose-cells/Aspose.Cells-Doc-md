---
title: Применение условного форматирования в рабочих листах с помощью C++
linktitle: Применить условное форматирование
description: Как использовать библиотеку Aspose.Cells в C++ для применения условного форматирования в рабочих листах. Настраивая эти критерии, вы получаете больший контроль над внешним видом ячеек.
keywords: Aspose.Cells, Условное форматирование, C++, Рабочий лист, Форматирование
type: docs
weight: 130
url: /ru/cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Эта статья предназначена для подробного понимания того, как добавить условное форматирование к диапазону ячеек на рабочем листе.

Условное форматирование - это расширенная функция в Microsoft Excel, которая позволяет применять форматы к диапазону ячеек и менять этот формат в зависимости от значения ячейки или значения формулы. Например, фон ячейки может быть красным, чтобы выделить отрицательное значение, или цвет текста может быть зеленым для положительного значения. Когда значение ячейки соответствует условию форматирования, формат применяется. Если значение ячейки не соответствует условию форматирования, используется форматирование по умолчанию для ячейки.

Возможно применить условное форматирование с помощью автоматизации Microsoft Office, но это имеет свои недостатки. В этом участвует несколько причин и проблем: например, безопасность, стабильность, масштабируемость и скорость. Основной причиной поиска другого решения является то, что сама Microsoft настоятельно рекомендует не использовать автоматизацию Office для программных решений.

Эта статья показывает, как создать консольное приложение, добавить условное форматирование в ячейки с помощью нескольких простейших строк кода с использованием API Aspose.Cells.

{{% /alert %}}

## **Использование Aspose.Cells для применения условного форматирования на основе значения ячейки**

1. **Загрузите и установите Aspose.Cells**.
   1. Скачать Aspose.Cells for C++.
1. Установите его на вашем компьютере для разработки.
   Все компоненты Aspose, установленные, работают в режиме оценки. Режим оценки не имеет ограничения по времени и только внедряет водные знаки в созданные документы.
1. **Создайте проект**.
   Запустите свое окружение для разработки C++ и создайте новое консольное приложение.
1. **Добавьте ссылки**.
   Добавьте ссылку на Aspose.Cells в свой проект, например, добавьте ссылку на ….\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. **Примените условное форматирование на основе значения ячейки**.
   Ниже приведен код, используемый для выполнения задачи. Он применяет условное форматирование к ячейке.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the FormatConditionCollection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(0, 0, 0, 0);

    // Add the cell area to the format condition collection
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Sets the background color
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

При выполнении приведенного выше кода условное форматирование применяется к ячейке «A1» в первом рабочем листе выходного файла (output.xls). В зависимости от значения ячейки A1, фон ячейки становится красным, если значение находится между 50 и 100, из-за примененного условного форматирования.

## **Использование Aspose.Cells для применения условного форматирования на основе формулы**

1. **Применение условного форматирования в зависимости от формулы (пример кода)**
   Ниже приведен код для выполнения задачи. Он применяет условное форматирование к B3.

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

    // Create workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the conditional formatting collection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(2, 1, 2, 1);

    // Add the area to the conditional formatting
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::Expression);

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Set the formula for the condition
    fc.SetFormula1(u"=IF(SUM(B1:B2)>100,TRUE,FALSE)");

    // Set the background color
    Style style = fc.GetStyle();
    style.SetBackgroundColor(Color::Red());
    fc.SetStyle(style);

    // Set the formula for cell B3
    sheet.GetCells().Get(u"B3").SetFormula(u"=SUM(B1:B2)");

    // Set the value for cell C4
    sheet.GetCells().Get(u"C4").PutValue(u"If Sum of B1:B2 is greater than 100, B3 will have RED background");

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

При выполнении этого кода в первую очередь условное форматирование применяется к ячейке «B3» в первом рабочем листе выходного файла (output.xls). Оно зависит от формулы, которая рассчитывает значение «B3» как сумму B1 и B2.
