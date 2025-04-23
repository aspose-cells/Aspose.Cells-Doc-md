---
title: Копирование и перемещение листов внутри и между рабочими книгами с помощью C++
linktitle: Копирование и перемещение листов
type: docs
weight: 80
url: /ru/cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: Узнайте, как копировать и перемещать листы внутри и между рабочими книгами Excel с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Иногда вам нужны несколько листов с одинаковым форматированием и вводом данных. Например, если вы работаете с квартальными бюджетами, вы можете создать рабочую книгу с листами, содержащими одинаковые заголовки столбцов, строк и формулы. Есть способ сделать это: создав один лист и затем копируя его несколько раз.

Aspose.Cells поддерживает копирование или перемещение листов внутри или между книгами. Листы включают данные, форматирование, таблицы, матрицы, диаграммы, изображения и другие объекты с наивысшей степенью точности.

{{% /alert %}}

## **Копирование и перемещение листов**

### **Копирование листа внутри книги**

Начальные шаги одинаковы для всех примеров:

1. Создайте две рабочие книги с некоторыми данными в Microsoft Excel. Для этого примера мы создали две новые рабочие книги в Excel и ввели некоторые данные в листы:
   - FirstWorkbook.xlsx (3 листа)
   - SecondWorkbook.xlsx (1 лист)

1. Скачайте и установите Aspose.Cells:
   1. [Скачать Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp)
   1. Установите его на ваш компьютер для разработки

1. Создайте проект:
   1. Создайте новый проект C++ в выбранной IDE

1. Добавьте ссылки:
   1. Добавьте библиотеку Aspose.Cells for C++ в проект

1. Скопируйте лист в книге.
   Первый пример копирует первый лист (Copy) внутри FirstWorkbook.xlsx.

При выполнении кода лист с именем Copy копируется внутри FirstWorkbook.xlsx с именем Последний лист.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from input file
    Workbook excelWorkbook1(srcDir + u"FirstWorkbook.xlsx");

    // Get worksheet collection reference
    WorksheetCollection worksheets = excelWorkbook1.GetWorksheets();

    // Copy third worksheet (index 2) within the workbook
    worksheets.AddCopy(worksheets.Get(2).GetName());

    // Save modified workbook
    excelWorkbook1.Save(outDir + u"FirstWorkbookCopied_out.xlsx");

    std::cout << "Worksheet copied successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Перемещение листа внутри книги**

Приведенный ниже код показывает, как переместить лист с одной позиции в книге на другую. При выполнении кода лист с именем Move из индекса 1 перемещается на индекс 2 внутри FirstWorkbook.xlsx.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create input and output file paths
    U16String inputFilePath = srcDir + u"FirstWorkbook.xlsx";
    U16String outputFilePath = outDir + u"FirstWorkbookMoved_out.xlsx";

    // Load source workbook
    Workbook excelWorkbook2(inputFilePath);

    // Access worksheet collection and move target sheet
    WorksheetCollection sheets = excelWorkbook2.GetWorksheets();
    sheets.Get(u"Move").MoveTo(2);

    // Save modified workbook
    excelWorkbook2.Save(outputFilePath);

    std::cout << "Worksheet moved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Копирование листа между книгами Excel**

Выполнение кода копирует лист с именем Copy в SecondWorkbook.xlsx с именем листа Sheet2.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open source workbooks
    Workbook excelWorkbook3(srcDir + u"FirstWorkbook.xlsx");
    Workbook excelWorkbook4(srcDir + u"SecondWorkbook.xlsx");

    // Access worksheets collection from second workbook
    WorksheetCollection sheets4 = excelWorkbook4.GetWorksheets();

    // Add new worksheet to destination workbook
    sheets4.Add();

    // Copy specified worksheet from source to destination
    Worksheet sourceSheet = excelWorkbook3.GetWorksheets().Get(u"Copy");
    sheets4.Get(1).Copy(sourceSheet);

    // Save modified workbook
    excelWorkbook4.Save(outDir + u"CopyWorksheetsBetweenWorkbooks_out.xlsx");

    std::cout << "Worksheets copied successfully between workbooks." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Перемещение листа между книгами Excel**

При выполнении кода лист с именем Move перемещается из FirstWorkbook.xlsx в SecondWorkbook.xlsx с именем Sheet3.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open first workbook
    Workbook excelWorkbook5(srcDir + u"FirstWorkbook.xlsx");

    // Open second workbook and add new worksheet
    Workbook excelWorkbook6(srcDir + u"SecondWorkbook.xlsx");
    excelWorkbook6.GetWorksheets().Add();

    // Copy third worksheet from first workbook to third position in second workbook
    WorksheetCollection sheets5 = excelWorkbook5.GetWorksheets();
    WorksheetCollection sheets6 = excelWorkbook6.GetWorksheets();
    sheets6.Get(2).Copy(sheets5.Get(2));

    // Remove copied worksheet from source workbook
    sheets5.RemoveAt(2);

    // Save modified workbooks
    excelWorkbook5.Save(outDir + u"FirstWorkbookWithMove_out.xlsx");
    excelWorkbook6.Save(outDir + u"SecondWorkbookWithMove_out.xlsx");

    std::cout << "Worksheets moved successfully between workbooks." << std::endl;

    Aspose::Cells::Cleanup();
}
```
