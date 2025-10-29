---
title: Сортировка данных с помощью C++
linktitle: Сортировка данных
type: docs
weight: 130
url: /ru/cpp/sort-data-of-excel/
description: Узнайте, как сортировать данные, используя API Aspose.Cells for C++.
keywords: Сортировка данных в порядке возрастания или убывания, сортировка данных на основе цвета фона
---

{{% alert color="primary" %}}

Сортировка данных - одна из многих полезных функций в Microsoft Excel. Она позволяет пользователям упорядочить данные для удобного просмотра. Aspose.Cells позволяет разработчикам сортировать данные на листе таблицы по алфавиту или числовому значению, что работает так же, как в Microsoft Excel.

{{% /alert %}}

## **Сортировка данных в Microsoft Excel**

Чтобы отсортировать данные в Microsoft Excel:

1. Выберите **Данные** в меню **Сортировка**. В диалоговом окне сортировки будет отображаться.
1. Выберите вариант сортировки.

Обычно сортировка выполняется в списке - это непрерывная группа данных, отображаемых в столбцах.

## **Сортировка данных с помощью Aspose.Cells**

Aspose.Cells предоставляет класс [**DataSorter**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/), используемый для сортировки данных в порядке возрастания или убывания. В классе есть некоторые важные члены, например, свойства, такие как Key1 … Key3 и Order1 … Order3. Эти члены используются для определения отсортированных ключей и указания порядка сортировки ключей.

Перед реализацией сортировки данных необходимо определить ключи и установить порядок сортировки. В классе предоставляется метод [**Sort**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/sort/), используемый для выполнения сортировки данных на основе данных ячейки на листе таблицы.

Метод [**Sort**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/sort/) принимает следующие параметры:

- [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), ячейки для основного листа таблицы.
- [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/), диапазон ячеек. Определите область ячеек перед применением сортировки данных.

В этом примере используется шаблонный файл "Book1.xls", созданный в Microsoft Excel. После выполнения приведенного ниже кода данные сортируются правильно.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the workbook datasorter object
    DataSorter sorter = workbook.GetDataSorter();

    // Set the first order for datasorter object
    sorter.SetOrder1(SortOrder::Descending);

    // Define the first key
    sorter.SetKey1(0);

    // Set the second order for datasorter object
    sorter.SetOrder2(SortOrder::Ascending);

    // Define the second key
    sorter.SetKey2(1);

    // Create a cells area (range)
    CellArea ca = CellArea::CreateCellArea(0, 0, 13, 1);

    // Sort data in the specified data range (A1:B14)
    sorter.Sort(workbook.GetWorksheets().Get(0).GetCells(), ca);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Data sorted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Если вы хотите выполнить сортировку *СлеваНаправо*, используйте атрибут [**DataSorter.GetSortLeftToRight()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/getsortlefttoright/).

{{% /alert %}}

### **Сортировка данных с цветом фона**

Excel предоставляет функции для сортировки данных на основе цвета фона. Та же функция предоставляется с использованием Aspose.Cells с помощью DataSorter, где [**SortOnType**](https://reference.aspose.com/cells/cpp/aspose.cells/sortontype/).CellColor может быть использован в [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/) для сортировки данных на основе цвета фона. Все ячейки, которые содержат указанный цвет в [**AddKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/datasorter/addkey/), функции размещаются в начале или в конце в зависимости от установок SortOrder, и порядок остальных ячеек вообще не изменяется.

Ниже приведены образцовые файлы, которые можно загрузить для тестирования этой функции:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

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
    U16String inputFilePath = srcDir + u"CellsNet46500.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"outputSortData_CustomSortList.xlsx";

    // Create a workbook object and load template file
    Workbook workbook(inputFilePath);

    // Instantiate data sorter object
    DataSorter sorter = workbook.GetDataSorter();

    // Add key for second column for red color
    sorter.AddColorKey(1, SortOnType::CellColor, SortOrder::Descending, Color::Red());

    // Sort the data based on the key
    sorter.Sort(workbook.GetWorksheets().Get(0).GetCells(), CellArea::CreateCellArea(u"A2", u"C6"));

    // Save the output file
    workbook.Save(outputFilePath);

    std::cout << "Data sorted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Продвинутые темы**
- [Сортировка данных в столбце с пользовательским списком](/cells/ru/cpp/sort-data-in-column-with-custom-sort-list/)
- [Указание предупреждения при сортировке данных](/cells/ru/cpp/specifying-sort-warning-while-sorting-data/)
{{< app/cells/assistant language="cpp" >}}
