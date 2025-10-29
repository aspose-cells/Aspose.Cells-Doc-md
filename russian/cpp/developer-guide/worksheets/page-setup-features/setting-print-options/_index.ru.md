---
title: Настройка параметров печати с помощью C++
linktitle: Настройка параметров печати
type: docs
weight: 40
url: /ru/cpp/setting-print-options/
description: В этой статье показано, как программно установить параметры печати функции настройки страницы листа Excel с помощью API и библиотеки C++. Можно установить область печати, заголовки печати и порядок страниц.
keywords: установка области печати Excel C++, установка заголовков печати Excel C++, установка порядка страниц Excel C++
---

{{% alert color="primary" %}}

Настройки страницы установки Microsoft Excel предоставляют несколько параметров печати (также называемых параметрами листа), которые позволяют пользователям контролировать порядок печати листов рабочей книги.

{{% /alert %}}

## **Установка параметров печати**

Эти параметры печати позволяют пользователям:

- Выбрать конкретную область печати на рабочем листе.
- Напечатать заголовки.
- Напечатать сетку.
- Печать верхних заголовков строк / столбцов.
- Достичь чернового качества.
- Напечатать примечания.
- Напечатать ошибки ячеек.
- Определить порядок страниц.

Aspose.Cells поддерживает все параметры печати, предлагаемые Microsoft Excel, и разработчики могут легко настроить эти параметры для листов с помощью свойств класса [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/). Подробное описание использования этих свойств приведено ниже.

### **Установка области печати**

По умолчанию область печати включает все области листа, содержащие данные. Разработчики могут установить конкретную область печати листа.

Чтобы выбрать конкретную область печати, используйте свойство [**GetPrintArea()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintarea/) класса [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/). Назначьте этому свойству диапазон ячеек, определяющий область печати.

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set the print area to the range A1:T35
    pageSetup.SetPrintArea(u"A1:T35");

    // Save the workbook
    workbook.Save(outDir + u"SetPrintArea_out.xls");

    std::cout << "Print area set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Установка заголовков для печати**

Aspose.Cells позволяет определить повторение заголовков строк и столбцов на всех страницах напечатанного листа. Для этого используйте свойства [**GetPrintTitleColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlecolumns/) и [**GetPrintTitleRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinttitlerows/) класса [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/).

Строки или столбцы, которые будут повторяться, определяются путем передачи их номеров строки или столбца. Например, строки определяются как $1:$2, а столбцы определяются как $A:$B.

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

    // Path of output excel file
    U16String outputFilePath = outDir + u"SetPrintTitle_out.xls";

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Define column numbers A & B as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$B");

    // Define row numbers 1 & 2 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Настройка Других Опций Печати**

Класс [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) также предоставляет несколько других свойств для установки общих параметров печати:

- [**GetPrintGridlines()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintgridlines/): логическое свойство, определяющее, нужно ли печатать сетку.
- [**GetPrintHeadings()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintheadings/): булевое свойство, определяющее, печатать заголовки строк и столбцов или нет.
- [**GetBlackAndWhite()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getblackandwhite/): булево свойство, определяющее, печатать лист в черно-белом режиме или нет.
- [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/): определяет, отображать ли примечания к печати на листе или в конце листа.
- [**GetPrintDraft()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintdraft/): логическое свойство, определяющее, нужно ли печатать лист без графики.
- [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/): определяет, нужно ли печатать ошибки ячеек как отображается, пустыми, тире или N/A.

Для установки свойств [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) и [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/) Aspose.Cells также предоставляет две перечислительные структуры, [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) и [**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/), содержащие предопределенные значения, которые присваиваются свойствам [**GetPrintComments()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprintcomments/) и [**GetPrintErrors()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getprinterrors/) соответственно.

Заранее определенные значения в перечислении [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) перечислены ниже вместе с их описаниями.

|**Типы Примечаний к Печати**|**Описание**|
| :- | :- |
|PrintInPlace|Указывает на печать комментариев как отображаемых в таблице.|
|PrintNoComments|Указывает, что комментарии не нужно печатать.|
|PrintSheetEnd|Указывает на печать комментариев в конце таблицы.|

Заранее определенные значения перечисления [**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) перечислены ниже вместе с их описаниями.

|**Типы Ошибок Печати**|**Описание**|
| :- | :- |
|PrintErrorsBlank|Указывает, что ошибки не нужно печатать.|
|PrintErrorsDash|Указывает на печать ошибок как "--".|
|PrintErrorsDisplayed|Указывает на печать ошибок как отображаемых.|
|PrintErrorsNA|Указывает на печать ошибок как "#N/A".|

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set print options
    pageSetup.SetPrintGridlines(true);  // Allow printing gridlines
    pageSetup.SetPrintHeadings(true);   // Allow printing row/column headings
    pageSetup.SetBlackAndWhite(true);   // Allow printing in black & white mode
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);  // Print comments as displayed
    pageSetup.SetPrintDraft(true);      // Print with draft quality
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);  // Print cell errors as N/A

    // Save the workbook
    U16String outputPath = outDir + u"OtherPrintOptions_out.xls";
    workbook.Save(outputPath);

    std::cout << "Workbook saved with print options successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Установить порядок страниц**

Класс [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) предоставляет свойство [**GetOrder()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getorder/), которое используется для упорядочивания печати нескольких страниц вашей таблицы. Есть две возможности упорядочить страницы следующим образом:

- **Сначала вниз, затем вправо:** печатает все страницы вниз до печати любых страниц вправо.
- **Сначала вправо, затем вниз:** печатает страницы слева направо до печати страниц ниже.

Aspose.Cells предоставляет перечисление [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/), содержащее все заранее определенные типы порядка.

Заранее определенные значения перечисления [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) перечислены ниже.

|**Типы порядка печати**|**Описание**|
| :- | :- |
|DownThenOver|Представляет порядок печати как сначала вниз, затем вправо.|
|OverThenDown|Представляет порядок печати как сначала вправо, затем вниз.|

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

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

    // Set the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outDir + u"SetPageOrder_out.xls");

    std::cout << "Page order set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
