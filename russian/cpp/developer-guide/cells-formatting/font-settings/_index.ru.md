---
title: Настройки шрифта с C++
linktitle: Настройки шрифта
type: docs
weight: 30
url: /ru/cpp/cells-font-settings/
description: Aspose.Cells — это библиотека C++ для работы с файлами таблиц. Она поддерживает установку настроек шрифта ячеек, позволяя пользователям настраивать стиль и свойства шрифта. В этой статье рассказывается, как использовать библиотеку Aspose.Cells для установки настроек шрифта ячеек.
keywords: Aspose.Cells, Ячейки, Настройки шрифта, Стили, Свойства
---

{{% alert color="primary" %}}

 Внешний вид текста можно контролировать, изменяя настройки шрифта. Настройки могут включать имя, стиль, размер, цвет и другие эффекты шрифта. Так же как в Microsoft Excel, Aspose.Cells поддерживает настройку шрифтов ячеек.

{{% /alert %}}

## **Настройка настроек шрифта**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/). Каждый элемент в коллекции [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) представляет объект класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells предоставляет методы класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) для получения и установки стиля форматирования ячейки. Класс [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) предоставляет свойства для настройки настроек шрифта.

### **Установка названия шрифта**

 Разработчики могут применять любой шрифт к тексту внутри ячейки, используя свойство [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) объекта [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/).

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font name to "Times New Roman"
    style.GetFont().SetName(u"Times New Roman");

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Установка стиля шрифта на жирный**

Разработчики могут сделать текст жирным, установив свойство [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) объекта [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) в **true**.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font weight to bold
    style.GetFont().SetIsBold(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Установка размера шрифта**

Установите размер шрифта с помощью свойства [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/) объекта [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font size to 14
    style.GetFont().SetSize(14);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Установка цвета шрифта**

 Используйте свойство [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) объекта [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) для установки цвета шрифта. Выберите любой цвет из перечисления Color (часть C++ фреймворка) и присвойте его свойству [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font color to blue
    style.GetFont().SetColor(Color::Blue());

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```

### **Установка типа подчеркивания шрифта**

Используйте свойство [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) объекта [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) для подчеркивания текста. Aspose.Cells предлагает различные предопределенные типы шрифтов в перечислении [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/).

|**Типы подчеркивания шрифта**|**Описание**|
| :- | :- |
|Accounting| Одиночная линия подчеркивания для учета
|Double| Двойное подчеркивание
|DoubleAccounting| Двойная линия подчеркивания для учета
|None| Без подчеркивания
|Single| Одиночная линия подчеркивания

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

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font to be underlined
    style.GetFont().SetUnderline(FontUnderlineType::Single);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Установка эффекта зачеркивания**

Примените зачеркивание, установив свойство [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) объекта [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) в **true**.

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

    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Hello Aspose!");

    Style style = cell.GetStyle();
    style.GetFont().SetIsStrikeout(true);
    cell.SetStyle(style);

    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Установка эффекта нижнего индекса**

Примените нижний индекс, установив свойство [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) объекта [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) в **true**.

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

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set subscript effect
    style.GetFont().SetIsSubscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Установка верхнего индекса на шрифт**

Разработчики могут применить эффект верхнего индекса к шрифту, установив свойство [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) объекта [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) в **true**.

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

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Obtain the style of the cell
    Style style = cell.GetStyle();

    // Set superscript effect
    style.GetFont().SetIsSuperscript(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Продвинутые темы**
- [Применить эффект верхнего и нижнего индекса к шрифтам](/cells/ru/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [Получение списка используемых шрифтов в электронной таблице или книге](/cells/ru/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
{{< app/cells/assistant language="cpp" >}}
