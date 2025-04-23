---
title: Настройки заливки с C++
linktitle: Настройки заливки
description: Aspose.Cells — это библиотека C++ для работы с файлами таблиц. Она поддерживает установку настроек заливки ячеек, позволяя пользователям настраивать фон и стиль ячеек. Эта статья расскажет, как использовать библиотеку Aspose.Cells для настройки заливки ячеек.
keywords: Aspose.Cells, Ячейки, Настройки заливки, Фон, Стиль
type: docs
weight: 50
url: /ru/cpp/cells-fill-settings/
---

## **Цвета и фоновые узоры**

Microsoft Excel может устанавливать передний (контур) и задний (заливка) цвета ячеек и фоновые узоры.

Aspose.Cells также поддерживает эти функции гибким образом. В этой теме мы узнаем, как использовать эти функции с использованием Aspose.Cells.

### **Настройка цветов и фоновых узоров**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет получить доступ к каждому листу Excel-файла. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Каждый элемент в коллекции [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) представляет объект класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

У класса [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) есть методы [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) и [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/), которые используются для получения и установки форматирования ячейки. Класс [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) предоставляет свойства для установки переднего и заднего цветов ячеек. Aspose.Cells предоставляет перечисление [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/), которое содержит набор предопределенных типов фоновых узоров, приведенных ниже.

|**Фоновые узоры**|**Описание**|
| :- | :- |
|DiagonalCrosshatch|Представляет диагональный рисунок косой крест|
|DiagonalStripe|Представляет диагональную полосу|
|Gray6|Представляет 6,25% серый узор|
|Gray12|Представляет 12,5% серый узор|
|Gray25|Представляет 25% серый узор|
|Gray50|Представляет 50% серый узор|
|Gray75|Представляет 75% серый узор|
|HorizontalStripe|Представляет горизонтальный узор полосы|
|None|Представляет отсутствие фона|
|ReverseDiagonalStripe|Представляет обратный диагональный узор полосы|
|Solid|Представляет сплошной узор|
|ThickDiagonalCrosshatch|Представляет толстый диагональный крестовый узор|
|ThinDiagonalCrosshatch|Представляет тонкий диагональный крестовый узор|
|ThinDiagonalStripe|Представляет тонкий диагональный узор полосы|
|ThinHorizontalCrosshatch|Представляет тонкий горизонтальный крестовый узор|
|ThinHorizontalStripe|Представляет тонкий горизонтальный узор полосы|
|ThinReverseDiagonalStripe|Представляет тонкий обратный диагональный узор полосы|
|ThinVerticalStripe|Представляет тонкий вертикальный узор полосы|
|VerticalStripe|Представляет вертикальный узор полосы|

В приведенном ниже примере цвет переднего плана ячейки A1 установлен, но ячейка A2 настроена иметь как передний, так и фоновый цвета с фоновым узором вертикальных полос.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Define a Style and get the A1 cell style
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    // Setting the foreground color to yellow
    style.SetForegroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A1 cell
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    // Get the A2 cell style
    style = worksheet.GetCells().Get(u"A2").GetStyle();

    // Setting the foreground color to blue
    style.SetForegroundColor(Color::Blue());

    // Setting the background color to yellow
    style.SetBackgroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A2 cell
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Важно знать**

{{% alert color="primary" %}}

- Чтобы установить передний или фоновый цвет ячейки, используйте свойства объекта [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) или [**GetBackgroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundcolor/). Оба свойства вступят в силу только в том случае, если свойство [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) объекта [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) будет настроено.
- Свойство [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) задает цвет тени ячейки.
  Свойство [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) указывает тип используемого фонового узора для переднего или фонового цвета. Aspose.Cells предоставляет перечисление [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) содержащее набор предопределенных типов фоновых узоров.
- Если вы выберете значение *BackgroundType.None* из перечисления [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/), то передний цвет не будет применен.
  Аналогично, фоновый цвет не будет применен, если вы выберете значения *BackgroundType.None* или *BackgroundType.Solid*.
- При извлечении цвета тени ячейки, если [**Style.GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) равно *BackgroundType.None*, [**Style.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) вернет *Color.Empty*.

{{% /alert %}}

### **Применение эффектов градиентного заливки**

Чтобы применить желаемые эффекты градиентного заливки к ячейке, используйте метод [**SetTwoColorGradient**](https://reference.aspose.com/cells/cpp/aspose.cells/style/settwocolorgradient/) объекта [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) соответственно.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::System;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(2, 1).PutValue(u"test");

    Cell cell = worksheet.GetCells().Get(u"B3");
    Style style = cell.GetStyle();
    style.SetIsGradient(true);
    style.SetTwoColorGradient(
        Color{ 0xFF, 0xFF, 0xFF, 0xFF },
        Color{ 0xFF, 0x4F, 0x81, 0xBD },
        GradientStyleType::Horizontal,
        1
    );

    style.GetFont().SetColor(Color::Red());
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    worksheet.GetCells().SetRowHeightPixel(2, 53);
    worksheet.GetCells().Merge(2, 1, 1, 2);

    workbook.Save(outDir + u"output.xlsx");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Цвета и палитра**

Палитра - это количество цветов, доступных для использования при создании изображения. Использование стандартной палитры в презентации позволяет пользователю создавать однородный вид. Каждый файл Microsoft Excel (97-2003) имеет палитру из 56 цветов, которые могут быть применены к ячейкам, шрифтам, сеткам, графическим объектам, заливкам и линиям в диаграмме.

С помощью Aspose.Cells можно использовать не только существующие цвета палитры, но и пользовательские цвета. Прежде чем использовать пользовательский цвет, сначала добавьте его в палитру.

Эта тема обсуждает, как добавить пользовательские цвета в палитру.

### **Добавление пользовательских цветов в палитру**

Aspose.Cells поддерживает 56-цветную палитру Microsoft Excel. Для использования пользовательского цвета, который не определен в палитре, добавьте цвет в палитру.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит метод [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/), который принимает следующие параметры для добавления пользовательского цвета для изменения палитры:

- Пользовательский цвет, пользовательский цвет, который будет добавлен.
- Индекс, индекс цвета в палитре, который будет заменен пользовательским цветом. Должен быть от 0 до 55.

Приведенный ниже пример добавляет пользовательский цвет (Орхидея) в палитру перед его применением к шрифту.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Check if Orchid color is in the palette
    std::cout << "Is Orchid in palette: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add Orchid color to the palette at index 55
    workbook.ChangePalette(Color::Orchid(), 55);

    // Verify if Orchid color is now in the palette
    std::cout << "Is Orchid in palette after change: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add a new worksheet
    int i = workbook.GetWorksheets().Add();

    // Get the reference to the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"Hello Aspose!");

    // Create a new style
    Style styleObject = workbook.CreateStyle();

    // Set the custom color (Orchid) to the font
    styleObject.GetFont().SetColor(workbook.GetColors()[55]);

    // Apply the style to the cell
    cell.SetStyle(styleObject);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Палитра может содержать только 56 цветов. Когда вы добавляете пользовательский цвет в палитру, палитра изменяется, и любой элемент в файле, отформатированный предыдущим цветом, изменяется. Поэтому при изменении палитры, пожалуйста, будьте очень осторожны. Более того, это ограничение только для формата файла XLS (Excel 97-2003), так как нет такого ограничения для форматов файлов XLSX или других более продвинутых форматов файлов MS Excel (2007/2010 или 2013).

{{% /alert %}}
