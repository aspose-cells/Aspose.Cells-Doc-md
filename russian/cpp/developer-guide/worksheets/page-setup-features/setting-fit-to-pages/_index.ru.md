---
title: Как напечатать Excel в масштабированных страницах по ширине и высоте с помощью C++
linktitle: Как напечатать Excel так, чтобы страницы были шириной и высотой, подогнанными под страницу
type: docs
weight: 200
url: /ru/cpp/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: В этой статье представлен пример кода, объясняющий, как установить параметры FitToPagesWide и FitToPagesTall с помощью библиотеки Aspose.Cells на C++.
keywords: Как установить FitToPagesWide и FitToPagesTall в C++, как добавить FitToPagesWide и FitToPagesTall в C++, как установить FitToPagesWide и FitToPagesTall в Excel, как очистить FitToPagesWide и FitToPagesTall в Excel, как напечатать Excel в масштабированных страницах по ширине и высоте, как распечатать лист как одну страницу, как распечатать все столбцы листа на одной странице.
---

## **Введение**

Настройки FitToPagesWide и FitToPagesTall используются в приложениях для работы с таблицами (таких как Microsoft Excel), чтобы контролировать масштабирование при печати. Эти настройки помогают обеспечить, чтобы напечатанный результат поместился на указанное количество страниц, как по горизонтали, так и по вертикали. Вот разъяснение каждого из параметров:

1. FitToPagesWide: Эта настройка задает количество страниц по ширине, в которые должна поместиться распечатка. Например, установка значения в 1 означает, что содержимое масштабируется для размещения на одной странице по ширине, независимо от ширины таблицы.
1. FitToPagesTall: Эта настройка задает количество страниц по высоте, в которые должна поместиться распечатка. Например, установка значения в 1 означает, что содержимое масштабируется для размещения на одной странице по высоте, независимо от количества строк.

## **Зачем использовать FitToPagesWide и FitToPagesTall**
Вот некоторые причины установки FitToPagesWide и FitToPagesTall:
1. Контроль над размещением при печати: задавая количество страниц по ширине и высоте, вы можете убедиться, что ваш печатный документ легко читаем и хорошо отформатирован, без нежелательного переноса столбцов или строк между страницами.
1. Последовательность: если вы печатаете несколько листов или отчетов, использование этих настроек помогает сохранить одинаковый формат, что облегчает сравнение и анализ распечатанных документов.
1. Профессиональная презентация: правильное масштабирование и размещение содержимого на заданное число страниц создаст более профессиональный и аккуратный вид ваших данных.

## **Как распечатать файл по страницам по ширине и высоте в Excel**

Чтобы установить параметры FitToPagesWide и FitToPagesTall в Microsoft Excel, выполните следующие шаги:

1. Откройте рабочую книгу Excel и перейдите к листу, который хотите распечатать.
1. Перейдите на вкладку Макет страницы на ленте.
1. В группе Настройка страницы нажмите на маленькую стрелку в правом нижнем углу, чтобы открыть диалоговое окно Настройка страницы.
1. В диалоговом окне Настройка страницы перейдите на вкладку Страница.
1. В разделе Масштабирование выберите опцию "Подогнать" и укажите количество страниц по ширине и высоте, которые вы хотите: введите желаемое количество страниц по ширине в первый блок (Подогнать x страниц по ширине). Введите желаемое количество страниц по высоте во второй блок (Подогнать y страниц по высоте).
<br>
<img src="2.png" width=60% />

1. Нажмите OK, чтобы применить настройки.

## **Как распечатать Excel как страницы по ширине и высоте, используя Aspose.Cells**

Чтобы установить FitToPagesWide и FitToPagesTall для указанного листа: сначала откройте [пример файла](input.xlsx), затем необходимо изменить свойства [**Worksheet.GetFitToPagesTall()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfittopagestall/) и [**Worksheet.GetFitToPagesWide()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfittopageswide/) объекта [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) для нужного листа. Вот пример на C++:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook(U16String(u"input.xlsx"));

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the number of pages to which the length of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesTall(1);

    // Set the number of pages to which the width of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Save the workbook
    workbook.Save(U16String(u"out_net.pdf"));

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Результат вывода:
<br>
<img src="1.png" width=60% />

## **Как напечатать лист как одну страницу, используя Aspose.Cells**

Чтобы распечатать лист как одну страницу: сначала откройте [пример файла](sample.xlsx), затем нужно установить свойство [**PdfSaveOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getonepagepersheet/) объекта [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/). Вот пример на C++:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook(u"sample.xlsx");

    // Create PdfSaveOptions object
    PdfSaveOptions options;

    // Set options for exporting PDF
    options.SetOnePagePerSheet(true);

    // Save the workbook to a PDF file
    workbook.Save(u"OnePagePerSheet.pdf", options);

    std::cout << "Workbook saved as OnePagePerSheet.pdf!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Результат вывода:
<br>
<img src="3.png" width=60% />

## **Как распечатать все столбцы листа на одной странице, используя Aspose.Cells**

Чтобы распечатать все столбцы листа на одной странице: сначала откройте [пример файла](sample.xlsx), затем нужно установить свойство [**PdfSaveOptions.GetAllColumnsInOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getallcolumnsinonepagepersheet/) объекта [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/). Вот пример на C++:

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object with the specified file.
    Workbook workbook(u"sample.xlsx");

    // Create PdfSaveOptions instance.
    PdfSaveOptions options;

    // Set options for saving the workbook as a PDF.
    options.SetAllColumnsInOnePagePerSheet(true);

    // Save the workbook as a PDF file with the specified options.
    workbook.Save(u"AllColumnsInOnePagePerSheet.pdf", options);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Результат вывода:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="cpp" >}}
