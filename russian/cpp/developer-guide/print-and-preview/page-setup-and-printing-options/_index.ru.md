---
title: Настройка страницы и параметры печати с C++
linktitle: Настройка страницы и параметры печати
type: docs
weight: 60
url: /ru/cpp/page-setup-and-printing-options/
description: Настройте параметры страницы и печати для контроля процесса печати с использованием Aspose.Cells с C++.
---

{{% alert color="primary" %}}

Иногда разработчики нуждаются в настройке страницы и параметров печати для управления процессом печати. Настройки страницы и параметры печати предлагают различные варианты и полностью поддерживаются в Aspose.Cells.

Эта статья показывает, как создать консольное приложение в Visual Studio и применить настройки страницы и параметры печати к листу с помощью API Aspose.Cells.

{{% /alert %}}

## **Работа с настройками страницы и печати**

Для этого примера мы создали книгу в Microsoft Excel и использовали Aspose.Cells для установки настроек страницы и параметров печати.

### **Использование Aspose.Cells для установки параметров настройки страницы**

Сначала создайте простой лист в Microsoft Excel. Затем примените к нему настройки страницы. При выполнении кода настройки страницы изменяются, как показано на скриншоте ниже.

|**Выходной файл.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. Создайте лист с данными в Microsoft Excel:
   1. Откройте новую книгу в Microsoft Excel.
   1. Добавьте некоторые данные.
1. Установите параметры настройки страницы:
   Примените параметры настройки страницы к файлу. Ниже приведено скриншоты параметров по умолчанию, до применения новых параметров.

|**Параметры настройки страницы по умолчанию.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|

1. Скачайте и установите Aspose.Cells:
   1. [Скачать](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++.
   1. Установите его на вашем компьютере для разработки.
      Все компоненты Aspose, установленные, работают в режиме оценки. Режим оценки не имеет ограничения по времени и только внедряет водные знаки в созданные документы.
1. Создайте проект:
   1. Запустите Visual Studio.
   1. Создайте новое консольное приложение.
      Этот пример покажет консольное приложение на C++.
1. Добавьте ссылки:
   1. В этом примере используется Aspose.Cells, поэтому добавьте ссылку на этот компонент в проект. Например:
      …\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Напишите приложение, которое вызывает API:

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
    U16String inputFilePath = srcDir + u"CustomerReport.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Setting the orientation to Portrait
    worksheet.GetPageSetup().SetOrientation(PageOrientationType::Portrait);

    // Setting the number of pages to which the length of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesTall(1);

    // Setting the number of pages to which the width of the worksheet will be spanned
    worksheet.GetPageSetup().SetFitToPagesWide(1);

    // Setting the paper size to A4
    worksheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);

    // Setting the print quality of the worksheet to 1200 dpi
    worksheet.GetPageSetup().SetPrintQuality(1200);

    // Setting the first page number of the worksheet pages
    worksheet.GetPageSetup().SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Настройка параметров печати**

Настройки настройки страницы также предоставляют несколько параметров печати (также называемых параметрами листа), которые позволяют пользователям контролировать печать страниц листа. Они позволяют пользователям:

- Выбирать конкретную область печати листа.
- Напечатать заголовки.
- Напечатать сетку.
- Печать верхних заголовков строк / столбцов.
- Достичь чернового качества.
- Напечатать примечания.
- Напечатать ошибки ячеек.
- Определить порядок страниц.

Приведенный ниже пример применяет параметры печати к файлу, созданному в приведенном выше примере (PageSetup.xls). Снимок экрана ниже показывает параметры печати по умолчанию до применения новых параметров.

|**Входной документ**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
Выполнение кода изменяет параметры печати.

|**Выходной файл**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

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
    U16String inputFilePath = srcDir + u"PageSetup.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"PageSetup_Print_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get PageSetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specifying the cells range (from A1 cell to E30 cell) of the print area
    pageSetup.SetPrintArea(u"A1:E30");

    // Defining column numbers A & E as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$E");

    // Defining row numbers 1 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Allowing to print gridlines
    pageSetup.SetPrintGridlines(true);

    // Allowing to print row/column headings
    pageSetup.SetPrintHeadings(true);

    // Allowing to print worksheet in black & white mode
    pageSetup.SetBlackAndWhite(true);

    // Allowing to print comments as displayed on worksheet
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);

    // Allowing to print worksheet with draft quality
    pageSetup.SetPrintDraft(true);

    // Allowing to print cell errors as N/A
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);

    // Setting the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Page setup applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
