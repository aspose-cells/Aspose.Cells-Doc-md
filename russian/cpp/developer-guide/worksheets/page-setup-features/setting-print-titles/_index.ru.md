---
title: Как установить заголовки печати с помощью C++
linktitle: Как установить заголовки печати
type: docs
weight: 200
url: /ru/cpp/how-to-set-print-titles/
description: В этой статье показан код, объясняющий, как установить заголовки печати с помощью библиотеки Aspose.Cells на C++.
keywords: Повторяющаяся печать строк и колонок, Как установить заголовки печати в C++, установка и очистка заголовков печати с помощью C++, как очистить заголовки печати в C++, как добавить заголовки печати с помощью C++, как удалить заголовки печати с помощью C++, установка заголовков печати в Excel, очистка заголовков печати в Excel.
---

## **Возможные сценарии использования**

Установка заголовков печати в Excel обеспечивает повторение определенных строк или столбцов на каждой странице печати, что особенно полезно для больших таблиц, занимающих несколько страниц. Вот причины, почему стоит устанавливать заголовки печати:

1. Повышенная читаемость: Заголовки печати помогают читателям понять данные, оставляя заголовки видимыми на всех страницах, облегчая интерпретацию информации без необходимости возвращения к первой странице.

1. Профессиональный внешний вид: Постоянное отображение заголовков или меток на каждой странице создает более аккуратный и профессиональный вид печатных документов.

1. Улучшенная навигация: для документов с обширными данными повторение заголовков на каждой странице позволяет быстрее находить нужную информацию и сокращает необходимость перелистывать страницы.

1. Меньше ошибок: при наличии заголовков на каждой странице снижается риск неправильного восприятия или ошибок при вводе данных, так как пользователи легко могут понять контекст данных.

1. Последовательность: обеспечение постоянного отображения важной информации, такой как заголовки столбцов или метки строк, поддерживает последовательность и ясность во всем документе.

## **Как установить заголовки печати в Excel**

Чтобы установить заголовки печати в Excel, выполните следующие шаги:

1. Откройте вкладку Макет страницы: нажмите на вкладку "Макет страницы" в ленте в верхней части окна Excel.
1. Получить доступ к заголовкам печати: в группе "Настройка страницы" нажмите "Заголовки печати".
1. Установите строки для повторения: В диалоговом окне "Параметры страницы" перейдите на вкладку "Лист". В разделе "Заголовки печати" укажите строки для повторения в верхней части, щелкнув по полю рядом с "Строки для повторения вверху" и выбрав нужные строки.
1. Установите столбцы для повторения (если необходимо): Аналогичным образом вы можете указать столбцы для повторения слева, щелкнув по полю рядом с "Столбцы для повторения слева" и выбрав нужные столбцы.
<br>
<img src="3.png" width=60% />

1. Подтвердить и распечатать: нажмите "ОК", чтобы применить настройки. При печати листа, указанные строки или столбцы будут отображаться на каждой странице.

## **Как удалить заголовки печати в Excel**

Чтобы удалить заголовки печати в Excel, нужно удалить строки или столбцы, установленные для повторения на каждой странице. Вот как это сделать:

1. Откройте вкладку Макет страницы: нажмите на вкладку "Макет страницы" в ленте в верхней части окна Excel.
1. Получить доступ к заголовкам печати: в группе "Настройка страницы" нажмите "Заголовки печати".
1. Удалить заголовки печати: в диалоговом окне "Настройка страницы" перейдите на вкладку "Лист". Очистите текстовые поля "Строки для повторения сверху" и "Столбцы для повторения слева", удаляя любой содержимое внутри них.
<br>
<img src="4.png" width=60% />

1. Подтвердить и закрыть: нажмите "ОК" для применения изменений.

## **Как установить заголовки печати с помощью Aspose.Cells**

Чтобы установить заголовки печати в указанном листе: сначала загрузите [образец файла](input.xlsx), затем необходимо изменить свойства [**Worksheet.GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) и [**Worksheet.GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) объекта [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) для нужного листа. Установка этих свойств в строку диапазона установит заголовки печати.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    Workbook workbook(u"input.xlsx");

    // Access the desired worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set rows to repeat at the top (e.g., rows 1 and 2)
    worksheet.GetPageSetup().SetPrintTitleRows(u"$1:$2");

    // Set columns to repeat at the left (e.g., columns A and B)
    worksheet.GetPageSetup().SetPrintTitleColumns(u"$A:$B");

    // Save the workbook
    workbook.Save(u"set_print_titles.pdf");

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Результат вывода:
<br>
<img src="1.png" width=60% />

## **Как удалить заголовки печати с помощью Aspose.Cells**

Чтобы удалить заголовки печати в указанном листе: сначала загрузите [образец файла](input.xlsx), затем необходимо изменить свойства [**Worksheet.GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) и [**Worksheet.GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) объекта [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) для нужного листа. Установка этих свойств в пустую строку очистит заголовки печати.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the workbook
    U16String inputFilePath = u"input.xlsx";
    Workbook workbook(inputFilePath);

    // Access the desired worksheet
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet worksheet = sheets.Get(0);

    // Clear the rows and columns set to repeat
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintTitleRows(u"");
    pageSetup.SetPrintTitleColumns(u"");

    // Save the workbook
    U16String outputFilePath = u"clear_print_titles.pdf";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();
}
```

Результат вывода:
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="cpp" >}}
