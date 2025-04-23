---
title: Создать, получить доступ и копировать именованные диапазоны с помощью C++
linktitle: Создавайте, получайте доступ и копируйте именованные диапазоны
type: docs
weight: 200
url: /ru/cpp/create-access-and-copy-named-ranges/
description: Узнайте, как создавать, получать доступ и копировать именованные диапазоны в файлах Excel с помощью Aspose.Cells и C++.
---

## **Введение**

Обычно, метки столбцов и строк используются для ссылки на отдельные ячейки. Можно создавать описательные имена для представления ячеек, диапазонов ячеек, формул или постоянных значений. Слово **имя** может относиться к строке символов, которая представляет ячейку, диапазон ячеек, формулу или постоянное значение. Назначение имени диапазону означает, что этот диапазон ячеек можно будет использовать по имени. Используйте легко запоминающиеся имена, такие как Products, чтобы обозначать сложные для понимания диапазоны, например Sales!C20:C30. Метки могут использоваться в формулах, ссылающихся на данные на той же рабочей области; если вы хотите обозначить диапазон на другом листе, вы можете использовать имя. *Именованные диапазоны — одна из наиболее мощных функций Microsoft Excel, особенно при использовании их как исходных диапазонов для списков, сводных таблиц, диаграмм и т.д.

## **Работа с именованным диапазоном с помощью Microsoft Excel**

### **Создание именованных диапазонов**

Следующие шаги описывают, как назвать ячейку или диапазон ячеек с помощью **MS Excel**. Этот метод применяется к **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000** и **2002**.

1. Выберите ячейку или диапазон ячеек, которые хотите назвать.
1. Нажмите **Поле с именем** в левом конце строки формул.
1. Введите имя для ячеек.
1. Нажмите ENTER.

{{% alert color="primary" %}}

Вы не можете называть ячейку, когда вы изменяете содержимое ячейки.

{{% /alert %}}

## **Работа с именованным диапазоном с использованием Aspose.Cells**

Здесь мы используем API Aspose.Cells для выполнения этой задачи.
Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/).

### **Создание именованного диапазона**

Можно создать именованный диапазон, вызвав перегруженный метод [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Обычная версия метода [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) принимает следующие параметры:

- Имя верхней левой ячейки, имя верхней левой ячейки в диапазоне.
- Имя нижней правой ячейки, имя нижней правой ячейки в диапазоне.

Когда вызывается метод [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/), он возвращает только что созданный диапазон в виде экземпляра класса [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). Используйте этот объект [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/), чтобы настроить именованный диапазон. Например, установите имя диапазона, используя свойство [**GetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getname/). В следующем примере показано, как создать именованный диапазон ячеек, который простирается от B4:G14.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Creating a named range
    Range range = worksheet.GetCells().CreateRange(u"B4", u"G14");

    // Setting the name of the named range
    range.SetName(u"TestRange");

    // Saving the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Named range created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Ввод данных в ячейки именованного диапазона**

Вы можете вставить данные в отдельные ячейки диапазона, следуя шаблону:

- **C++**: Range(строка, столбец)

Допустим, у вас есть именованный диапазон ячеек, охватывающий A1:C4. Матрица содержит 4 * 3 = 12 ячеек. Отдельные ячейки диапазона расположены последовательно: Range(0, 0), Range(0, 1), Range(0, 2), Range(1, 0), Range(1, 1), Range(1, 2), Range(2, 0), Range(2, 1), Range(2, 2), Range(3, 0), Range(3, 1), Range(3, 2).

Используйте следующие свойства для определения ячеек в диапазоне:

- FirstRow возвращает индекс первой строки в именованном диапазоне.
- FirstColumn возвращает индекс первого столбца в именованном диапазоне.
- RowCount возвращает общее количество строк в именованном диапазоне.
- ColumnCount возвращает общее количество столбцов в именованном диапазоне.

В следующем примере показано, как ввести некоторые значения в ячейки указанного диапазона.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet worksheet1 = workbook.GetWorksheets().Get(0);

    // Create a range of cells based on H1:J4
    Range range = worksheet1.GetCells().CreateRange(u"H1", u"J4");

    // Name the range
    range.SetName(u"MyRange");

    // Input some data into cells in the range
    range.Get(0, 0).PutValue(u"USA");
    range.Get(0, 1).PutValue(u"SA");
    range.Get(0, 2).PutValue(u"Israel");
    range.Get(1, 0).PutValue(u"UK");
    range.Get(1, 1).PutValue(u"AUS");
    range.Get(1, 2).PutValue(u"Canada");
    range.Get(2, 0).PutValue(u"France");
    range.Get(2, 1).PutValue(u"India");
    range.Get(2, 2).PutValue(u"Egypt");
    range.Get(3, 0).PutValue(u"China");
    range.Get(3, 1).PutValue(u"Philipine");
    range.Get(3, 2).PutValue(u"Brazil");

    // Save the excel file
    workbook.Save(outDir + u"rangecells.out.xls");

    std::cout << "Range cells created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Определение ячеек в именованном диапазоне**

Вы можете вставить данные в отдельные ячейки диапазона, следуя шаблону:

- **C++**: Range(строка, столбец)

Если у вас есть именованный диапазон, охватывающий A1:C4. Матрица содержит 4 * 3 = 12 ячеек. Отдельные ячейки расположены последовательно: Range(0, 0), Range(0, 1), Range(0, 2), Range(1, 0), Range(1, 1), Range(1, 2), Range(2, 0), Range(2, 1), Range(2, 2), Range(3, 0), Range(3, 1), Range(3, 2).

Используйте следующие свойства для определения ячеек в диапазоне:

- FirstRow возвращает индекс первой строки в именованном диапазоне.
- FirstColumn возвращает индекс первого столбца в именованном диапазоне.
- RowCount возвращает общее количество строк в именованном диапазоне.
- ColumnCount возвращает общее количество столбцов в именованном диапазоне.

В следующем примере показано, как ввести некоторые значения в ячейки указанного диапазона.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    // Identify range cells
    std::cout << "First Row : " << range.GetFirstRow() << std::endl;
    std::cout << "First Column : " << range.GetFirstColumn() << std::endl;
    std::cout << "Row Count : " << range.GetRowCount() << std::endl;
    std::cout << "Column Count : " << range.GetColumnCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Доступ к именованным диапазонам**

#### **Доступ к конкретному именованному диапазону**

Вызовите метод [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) коллекции [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), чтобы получить диапазон по указанному имени. Типичный метод [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) принимает имя именованного диапазона и возвращает указанный именованный диапазон как экземпляр класса [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/). В следующем примере показано, как получить доступ к указанному диапазону по его имени.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Getting the specified named range
    Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");

    if (range)
    {
        std::cout << "Named Range : " << range.GetRefersTo().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

#### **Доступ ко всем именованным диапазонам в электронной таблице**

Вызовите метод [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) коллекции [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), чтобы получить все именованные диапазоны в электронной таблице. Метод [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) возвращает массив всех именованных диапазонов в коллекции [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).

В следующем примере показано, как получить доступ ко всем именованным диапазонам в книге.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    WorksheetCollection sheets = workbook.GetWorksheets();
    Vector<Range> ranges = sheets.GetNamedRanges();

    std::cout << "Total Number of Named Ranges: " << ranges.GetLength() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Копировать именованные диапазоны**

Aspose.Cells предоставляет метод [**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/) для копирования диапазона ячеек с форматированием в другой диапазон.

В следующем примере показано, как скопировать исходный диапазон ячеек в другой именованный диапазон.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Range range1 = worksheet.GetCells().CreateRange(u"E12", u"I12");
    range1.SetName(u"MyRange");

	Color borderColor = Color{ 0,0, 0, 128 };
    range1.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Medium, borderColor);
    range1.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Medium, borderColor);

    range1.Get(0, 0).PutValue(u"Test");
    range1.Get(0, 4).PutValue(u"123");

    Range range2 = worksheet.GetCells().CreateRange(u"B3", u"F3");
    range2.SetName(u"testrange");
    range2.Copy(range1);

    workbook.Save(outDir + u"copyranges.out.xls");

    std::cout << "Ranges copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
