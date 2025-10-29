---
title: Показать и скрыть строки, столбцы и полосы прокрутки с помощью C++
linktitle: Показать и скрыть строки, столбцы и полосы прокрутки
type: docs
weight: 20
url: /ru/cpp/show-and-hide-rows-columns-and-scroll-bars/
description: В этой статье демонстрируется, как программным способом отображать и скрывать строки и столбцы листа Excel с помощью языка C++ и API Aspose.Cells. Можно регулировать отображение полос прокрутки, а также скрывать несколько строк и столбцов.
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет способы управления видимостью строк, столбцов и полос прокрутки листа.

{{% /alert %}}

## **Показ и скрытие строк и столбцов**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), представляющий файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), позволяющую разработчикам получать доступ к каждому листу Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) обеспечивает коллекцию [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), которая отображает все ячейки листа. Коллекция [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) предоставляет несколько методов для управления строками или столбцами листа. Некоторые из них обсуждены ниже.

### **Показать строки и столбцы**

Разработчики могут отображать любой скрытый ряд или столбец, вызвав методы [**UnhideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhiderow/) и [**UnhideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/unhidecolumn/) коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) соответственно. Оба метода требуют два параметра:

- **Индекс строки или столбца** - индекс строки или столбца, который используется для отображения конкретной строки или столбца.
- **Высота строки или ширина столбца** - высота строки или ширина столбца, назначенные строке или столбцу после отображения.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unhiding the 3rd row and setting its height to 13.5
    worksheet.GetCells().UnhideRow(2, 13.5);

    // Unhiding the 2nd column and setting its width to 8.5
    worksheet.GetCells().UnhideColumn(1, 8.5);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

При восстановлении скрытого столбца до его предыдущей или исходной ширины, пожалуйста, сделайте его видимым с отрицательной шириной. Например: `worksheet->GetCells()->UnhideColumn(5, -1)`.

{{% /alert %}}

### **Скрыть строки и столбцы**

Разработчики могут скрывать строки или столбцы, вызвав методы [**HideRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderow/) и [**HideColumn**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumn/) коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) соответственно. Оба метода требуют индекс строки или столбца, чтобы скрыть конкретный элемент.

```cpp
#include <iostream>
#include <memory>
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

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the 3rd row of the worksheet
    worksheet.GetCells().HideRow(2);

    // Hide the 2nd column of the worksheet
    worksheet.GetCells().HideColumn(1);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Также можно скрыть строку или столбец, установив высоту строки или ширину столбца равным 0 соответственно.

{{% /alert %}}

### **Скрыть несколько строк и столбцов**

Разработчики могут скрывать несколько строк или столбцов одновременно, вызвав методы [**HideRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hiderows/) и [**HideColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/hidecolumns/) коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) соответственно. Оба метода требуют начальный индекс строки или столбца и количество скрываемых строк или столбцов в качестве параметров.

```c++
#include <iostream>
#include <memory>
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

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide 3, 4, and 5 rows in the worksheet
    worksheet.GetCells().HideRows(2, 3);

    // Hide 2 and 3 columns in the worksheet
    worksheet.GetCells().HideColumns(1, 2);

    // Save the modified Excel file
    workbook.Save(outDir + u"outputxls");

    std::cout << "Rows and columns hidden successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Показывать и скрывать полосы прокрутки**

Полосы прокрутки используются для навигации по содержимому любого файла. Обычно существует два типа полос прокрутки:

- Вертикальные полосы прокрутки
- Горизонтальные полосы прокрутки

Microsoft Excel также предоставляет горизонтальные и вертикальные полосы прокрутки, чтобы пользователи могли пролистывать содержимое листа Excel. Используя Aspose.Cells, разработчики могут контролировать видимость обоих типов полос прокрутки в файлах Excel.

### **Управление видимостью полос прокрутки**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), представляющий файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) предлагает широкий набор свойств и методов для управления файлом Excel. Для управления видимостью полос прокрутки используйте свойства [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) и [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) класса [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) и [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) — логические свойства, которые могут принимать только значения **true** или **false**.

#### **Отображение полос прокрутки**

Делайте полосы прокрутки видимыми, устанавливая свойства [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) или [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) класса [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) в **true**.

#### **Скрытие полос прокрутки**

Скрыть полосы прокрутки, установив свойства [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/) или [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/) класса [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) в **false**.

**Пример кода**

Ниже приведен полный код, который открывает файл Excel, `book1.xls`, скрывает обе полосы прокрутки и сохраняет измененный файл как `output.xls`.

```c++
#include <iostream>
#include <fstream>
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
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Hide the vertical scroll bar of the Excel file
    workbook.GetSettings().SetIsVScrollBarVisible(false);

    // Hide the horizontal scroll bar of the Excel file
    workbook.GetSettings().SetIsHScrollBarVisible(false);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Scroll bars hidden successfully and file saved!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
