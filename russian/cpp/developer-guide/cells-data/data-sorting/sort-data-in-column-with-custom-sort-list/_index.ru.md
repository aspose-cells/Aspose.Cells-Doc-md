---
title: Сортировка данных в столбце с пользовательским списком сортировки с помощью C++
linktitle: Сортировка данных в столбце с пользовательским списком сортировки
type: docs
weight: 290
url: /ru/cpp/sort-data-in-column-with-custom-sort-list/
description: Узнайте, как отсортировать данные в столбце с использованием пользовательского списка, применяя API Aspose.Cells for C++.
keywords: Сортировка данных в столбце с помощью пользовательского списка, Сортировка данных по пользовательскому списку.
---

## **Возможные сценарии использования**

Вы можете отсортировать данные в столбце, используя пользовательский список. Это можно сделать с помощью метода [**DataSorter::AddKey(int key, SortOrder order, String customList)**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/). Однако этот метод работает только в случае, если элементы в пользовательском списке не содержат запятых. Если там есть запятые, как в "USA,US", "China,CN" и т.д., тогда необходимо использовать метод [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/). Здесь последний параметр — не строка, а массив строк.

## **Сортировка данных в столбце с пользовательским списком**

Следующий пример кода показывает, как использовать метод [**DataSorter::AddKey Method (Int32, SortOrder, String[])**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) для сортировки данных с помощью пользовательского списка сортировки. Пожалуйста, посмотрите на [пример файла Excel](50528327.xlsx), используемый в этом коде, и [сгенерированный выходной файл Excel](50528328.xlsx). Следующий скриншот показывает эффект работы кода на примере файла Excel при выполнении.

![todo:image_alt_text](sort-data-in-column-with-custom-sort-list_1.png)

## **Образец кода**

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

    // Load the source Excel file
    Workbook wb(srcDir + u"sampleSortData_CustomSortList.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify cell area - sort from A1 to A40
    CellArea ca = CellArea::CreateCellArea(u"A1", u"A40");

    // Create Custom Sort list
    Vector<U16String> customSortList = { u"USA,US", u"Brazil,BR", u"China,CN", u"Russia,RU", u"Canada,CA" };

    // Add Key for Column A, Sort it in Ascending Order with Custom Sort List
    wb.GetDataSorter().AddKey(0, SortOrder::Ascending, customSortList);
    wb.GetDataSorter().Sort(ws.GetCells(), ca);

    // Save the output Excel file
    wb.Save(outDir + u"outputSortData_CustomSortList.xlsx");

    std::cout << "Data sorted successfully with custom sort list!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
