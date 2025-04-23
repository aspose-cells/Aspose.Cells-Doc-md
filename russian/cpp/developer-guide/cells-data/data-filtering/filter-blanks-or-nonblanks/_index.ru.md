---
title: Как фильтровать пустые и не пустые ячейки с помощью C++
linktitle: Как фильтровать пустые или непустые ячейки
type: docs
weight: 85
url: /ru/cpp/how-to-filter-blanks-and-non-blanks/
description: Узнайте, как фильтровать пустые и непустые ячейки, используя API Aspose.Cells for C++.
keywords: Отфильтровать пустые, отфильтровать непустые, отфильтровать пустые в листе, отфильтровать непустые в листе, отфильтровать пустые в Excel, отфильтровать непустые в Excel, отфильтровать пустые и непустые в Excel
---

## **Возможные сценарии использования**
Фильтрация данных в Excel – это ценный инструмент, который улучшает анализ, исследование и презентацию данных, позволяя пользователям сосредоточиться на конкретных подмножествах данных в соответствии с их критериями, что делает общий процесс манипулирования данными и их интерпретации более эффективным и эффективным.

## **Как фильтровать пустые или непустые ячейки в Excel**
В Excel вы можете легко фильтровать пустые или непустые ячейки с помощью опций фильтрации. Вот как это можно сделать:

### **Как фильтровать пустые ячейки в Excel**
1. Выберите диапазон: Щелкните на букве заголовка столбца, чтобы выбрать весь столбец или выберите диапазон, в котором хотите отфильтровать пустые ячейки.
1. Откройте меню Фильтр: перейдите на вкладку "Данные" на ленте.
<br>
<image src="1.png" width="70%" />
1. Варианты фильтра: нажмите кнопку "Фильтр". Это добавит стрелки фильтрации к выбранному диапазону.
1. Отфильтруйте пустые ячейки: Щелкните на стрелке фильтра в столбце, который вы хотите отфильтровать пустыми. Снимите все параметры, кроме «Пустые», и нажмите OK. Это отобразит только пустые ячейки в этом столбце.
<br>
<image src="2.png" width="70%" />
1. Результат следующий:
<br>
<image src="3.png" width="70%" />

### **Как фильтровать непустые ячейки в Excel**
1. Выберите диапазон: нажмите на букву заголовка столбца, чтобы выбрать весь столбец, или выберите диапазон, в котором хотите отфильтровать непустые ячейки.
1. Откройте меню Фильтр: перейдите на вкладку "Данные" на ленте.
<br>
<image src="1.png" width="70%" />
1. Варианты фильтра: нажмите кнопку "Фильтр". Это добавит стрелки фильтрации к выбранному диапазону.
1. Фильтрация непустых ячеек: нажмите на стрелку фильтра в столбце, который хотите отфильтровать по непустоте. Снимите выбор со всех вариантов, кроме "Непустые" или "Пользовательский", и установите условия соответственно. Нажмите ОК. Это отобразит только ячейки, которые не пустые в этом столбце.
<br>
<image src="4.png" width="70%" />
1. Результат следующий:
<br>
<image src="5.png" width="70%" />

## **Как фильтровать пустые ячейки с помощью Aspose.Cells**
Если в столбце содержится текст, такой что несколько ячеек пусты, и требуется фильтрация для выбора только тех строк, где присутствуют пустые ячейки, функции [AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchblanks/) и [AutoFilter.AddFilter(int fieldIndex, string criteria)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/addfilter/) могут быть использованы, как показано ниже. 

Пожалуйста, ознакомьтесь с примерным кодом, загружающим [образец Excel-файла](sample.xlsx), который содержит некоторые фиктивные данные. Примерный код использует три метода для фильтрации пустот. Затем он сохраняет книгу как [выходной Excel-файл](FilteredBlanks.xlsx). 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Method 1: Call MatchBlanks function to apply the filter
    // worksheet.GetAutoFilter().MatchBlanks(1);

    // Method 2: Call AddFilter function and set criteria to ""
    // worksheet.GetAutoFilter().AddFilter(1, u"");

    // Method 3: Call AddFilter function and set criteria to nullptr
    worksheet.GetAutoFilter().AddFilter(1, nullptr);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(u"FilteredBlanks.xlsx");

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Как фильтровать непустые ячейки с помощью Aspose.Cells**

Пожалуйста, посмотрите следующий пример кода, который загружает [пример файла Excel](sample.xlsx), содержащего некоторые фиктивные данные. После загрузки файла вызовите функцию [AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchnonblanks/) для фильтрации данных без пустых ячеек, и, наконец, сохраните рабочую книгу как [выходной файл Excel](FilteredNonBlanks.xlsx). 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook by opening an existing Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter on the second column (index 1)
    worksheet.GetAutoFilter().MatchNonBlanks(1);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(u"FilteredNonBlanks.xlsx");

    std::cout << "Filtered non-blanks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```


