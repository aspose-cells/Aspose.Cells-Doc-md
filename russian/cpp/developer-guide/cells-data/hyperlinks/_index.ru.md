---
title: Вставка гиперссылок в Excel или OpenOffice с помощью C++
linktitle: Управление гиперссылками
type: docs
weight: 45
url: /ru/cpp/insert-hyperlinks-to-excel/
description: Как вставить гиперссылки в файл Excel с помощью библиотеки Aspose.Cells без MS Excel на C++.
keywords: Вставить гиперссылки в Excel, Добавить или вставить гиперссылки, Добавить или вставить ссылку на URL, Добавить или вставить ссылку в ячейку, Добавить ссылку на внешний файл
---

{{% alert color="primary" %}} 

Гиперссылка используется для создания связи между двумя сущностями. Каждый знаком с использованием гиперссылок, особенно на веб-сайтах.
Используя Aspose.Cells, разработчики могут создавать различные виды гиперссылок в файлах Microsoft Excel. В этой теме обсуждается, какие типы гиперссылок поддерживает Aspose.Cells и как они могут быть использованы в наших файлах Excel.

{{% /alert %}} 

## **Добавление гиперссылок**
 Aspose.Cells позволяет разработчикам добавлять гиперссылки в файлы Excel либо с помощью API, либо через дизайнерские таблицы (таблицы, в которых гиперссылки создаются вручную, а Aspose.Cells используется для их импорта в другие таблицы).

 Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), который обеспечивает доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет различные методы для добавления различных гиперссылок в файлы Excel.

## **Добавление ссылки на URL**
Класс [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) содержит коллекцию [GetHyperlinks()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/). Каждый элемент в коллекции [GetHyperlinks()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/) представляет [Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/). Для добавления гиперссылок на URL вызывайте метод [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) коллекции [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). Метод [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL-адрес, адрес URL.

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

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a hyperlink to cell "A1"
    worksheet.GetHyperlinks().Add(u"A1", 1, 1, u"http://www.aspose.com");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

В приведенном выше примере гиперссылка добавляется в URL в пустую ячейку **A1**. В таких случаях, если ячейка пустая, то адрес URL также добавляется в эту пустую ячейку в качестве ее значения. Если ячейка не пустая и в нее добавляется гиперссылка, значение ячейки выглядит как обычный текст. Чтобы сделать его похожим на гиперссылку, примените соответствующие настройки форматирования к этой ячейке.

{{% /alert %}} 

## **Добавление ссылки на ячейку в том же файле**
Можно добавлять гиперссылки в ячейки того же файла Excel, вызывая метод [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) коллекции [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). Метод [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) работает как для внутренних, так и для внешних гиперссылок. Одна из версий перегруженного метода принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес целевой ячейки.

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

    // Adding a new worksheet to the Workbook object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the first (default) worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in
    // The same Excel file
    worksheet.GetHyperlinks().Add(u"B3", 1, 1, u"Sheet2!B9");

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Добавление ссылки на внешний файл**
Можно добавлять гиперссылки в внешние файлы Excel, вызывая метод [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) коллекции [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/). Метод [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) принимает следующие параметры:

- Имя ячейки, в которую будет добавлена гиперссылка.
- Количество строк, количество строк в этом диапазоне гиперссылок.
- Количество столбцов, количество столбцов в этом диапазоне гиперссылок.
- URL, адрес цели, внешний файл Excel.

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Add an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
    worksheet.GetHyperlinks().Add(U16String(u"A5"), 1, 1, srcDir + U16String(u"book1.xls"));

    // Save the Excel file
    workbook.Save(outDir + U16String(u"output.out.xls"));

    std::cout << "Hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Продвинутые темы**
- [Добавление гиперссылок на изображения](/cells/ru/cpp/add-image-hyperlinks/)
- [Определение типа гиперссылки](/cells/ru/cpp/detect-hyperlink-type/)
- [Редактирование гиперссылок в рабочем листе](/cells/ru/cpp/editing-hyperlinks-of-worksheet/)
- [Получение гиперссылок в диапазоне](/cells/ru/cpp/get-hyperlinks-in-range/)
