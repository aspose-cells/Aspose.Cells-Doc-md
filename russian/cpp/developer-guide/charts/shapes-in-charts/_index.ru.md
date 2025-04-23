---
title: Формы в диаграммах с C++
linktitle: Формы в диаграммах
description: Узнайте, как использовать Aspose.Cells for C++ для добавления элементов управления и настройки диаграмм в Microsoft Excel. Наше руководство продемонстрирует, как манипулировать элементами диаграммы, настраивать форматирование и улучшать внешний вид и удобство использования ваших графиков.
keywords: Aspose.Cells for C++, элементы управления диаграммой, настройка диаграмм, Microsoft Excel, элементы диаграммы, форматирование.
type: docs
weight: 70
url: /ru/cpp/controls-in-charts/
---

{{% alert color="primary" %}}

Иногда вам может потребоваться вставить объекты рисования, такие как метки, текстовые поля, изображения и т. д., в график. Aspose.Cells может добавлять элементы управления в график во время выполнения.

{{% /alert %}}

## **Добавление элемента управления метки в график**

Метки обеспечивают возможность предоставления пользователям информации о содержании листа.
Aspose.Cells позволяет добавлять и манипулировать метками даже в графиках.

Класс [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) предоставляет метод [**AddLabelInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabelinchart/), предназначенный для добавления метки к диаграмме. Ниже приведён список параметров, используемых для этого метода:

- **top** – вертикальное смещение метки от верхнего левого угла в единицах 1/4000 от области графика.
- **left** – горизонтальное смещение метки от верхнего левого угла в единицах 1/4000 от области графика.
- **height** – высота метки в единицах 1/4000 от области графика.
- **width** – ширина метки в единицах 1/4000 от области графика.

 Метод возвращает объект [**Aspose::Cells::Drawing::Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/). Класс [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) представляет собой метку на диаграмме. У него есть важные члены:

- [**Text**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) (свойство) — задаёт строку заголовка метки.
- [**Fill**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getfill/) (свойство) – указывает атрибуты цвета заливки.

В следующем примере показано, как добавить метку в график. В примере используется файл дизайнера (**exp_piechart.xls**), в котором есть график. Мы используем этот файл для вставки метки в график. Ниже приведен исходный код для добавления метки в график. При выполнении кода генерируется следующий вывод.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"chart.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the designer chart in the second sheet
    Worksheet sheet = workbook.GetWorksheets().Get(1);
    Aspose::Cells::Charts::Chart chart = sheet.GetCharts().Get(0);

    // Add a new label to the chart
    Label label = chart.GetShapes().AddLabelInChart(100, 100, 350, 900);

    // Set the caption of the label
    label.SetText(u"A Label In Chart");

    // Set the Placement Type, the way the Label is attached to the cells
    label.SetPlacement(PlacementType::FreeFloating);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Label added to chart successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Добавление элемента управления текстовым полем в график**

Один из способов выделить важную информацию в отчёте — использовать текстовое поле. Например, введите текст для выделения названия компании или указания географического региона с наибольшими продажами. Класс [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) предоставляет метод [**AddTextBoxInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addtextboxinchart/), который используется для добавления элемента управления текстовым полем к диаграмме. Ниже приведён список параметров метода:

- **top** – вертикальное смещение текстового поля от верхнего левого угла в единицах 1/4000 от области графика.
- **left** – горизонтальное смещение текстового поля от верхнего левого угла в единицах 1/4000 от области графика.
- **height** – высота текстового поля в единицах 1/4000 от области графика.
- **ширина** - ширина текстового блока в единицах 1/4000 от области диаграммы.

 Метод возвращает объект [**Aspose::Cells::Drawing::TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/). Класс [**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/) представляет текстовое поле на диаграмме.

В следующем примере показано, как добавить текстовое поле на диаграмму. В примере используется предыдущий файл дизайнера (**exp_piechart.xls**), в котором есть диаграмма. Мы используем этот файл, чтобы вставить текстовое поле на диаграмму для отображения заголовка диаграммы. Ниже приведен исходный код для добавления текстового поля на диаграмму.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"chart.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"chart.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the designer chart in the second sheet
    Worksheet sheet = workbook.GetWorksheets().Get(1);
    Aspose::Cells::Charts::Chart chart = sheet.GetCharts().Get(0);

    // Add a new textbox to the chart
    TextBox textbox0 = chart.GetShapes().AddTextBoxInChart(100, 1100, 350, 2550);

    // Fill the text
    textbox0.SetText(u"Sales By Region");

    // Set the font color
    textbox0.GetFont().SetColor(Color::Maroon());

    // Set the font to bold
    textbox0.GetFont().SetIsBold(true);

    // Set the font size
    textbox0.GetFont().SetSize(14);

    // Set font attribute to italic
    textbox0.GetFont().SetIsItalic(true);

    // Get the fill format of the textbox
    FillFormat fillformat = textbox0.GetFill();

    // Get the line format type of the textbox
    LineFormat lineformat = textbox0.GetLine();

    // Set the line weight
    lineformat.SetWeight(2);

    // Set the dash style to solid
    lineformat.SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Textbox added to chart successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Добавление изображения на диаграмму**

Aspose.Cells позволяет вставлять изображения в диаграмму. Например, добавьте изображение, чтобы подчеркнуть или придать больший смысл диаграмме или ее содержимому, или вставьте файл изображения бренда.

Класс [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) предоставляет метод [**AddPictureInChart**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpictureinchart/), используемый для добавления объекта изображения на диаграмму. Ниже приведён список параметров этого метода:

- **верх** - вертикальное смещение изображения от верхнего левого угла в единицах 1/4000 от области диаграммы.
- **слева** - горизонтальное смещение изображения от верхнего левого угла в единицах 1/4000 от области диаграммы.
- **поток** - объект потока, содержащий данные изображения.
- **масштабШирины** - масштаб ширины изображения, значение в процентах.
- **масштабВысоты** - масштаб высоты изображения, значение в процентах.

 Метод возвращает объект [**Aspose::Cells::Drawing::Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/). Класс [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) представляет объект изображения на диаграмме.

В следующем примере показано, как добавить изображение на диаграмму. Пример использует предыдущий файл дизайнера (**exp_piechart.xls**), в котором есть диаграмма. Мы используем этот файл, чтобы вставить изображение на диаграмму. Ниже приведен исходный код для добавления изображения на диаграмму.

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

std::vector<uint8_t> ReadFileData(const U16String& filePath) {
    std::ifstream file(filePath.ToUtf8(), std::ios::binary | std::ios::ate);
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);

    std::vector<uint8_t> buffer(size);
    if (!file.read(reinterpret_cast<char*>(buffer.data()), size)) {
        throw std::runtime_error("Error reading file");
    }
    return buffer;
}

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"chart.xls");
    std::vector<uint8_t> imageData = ReadFileData(srcDir + u"logo.jpg");

    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Chart chart = sheet.GetCharts().Get(0);
    Vector<uint8_t> data(imageData.data(), static_cast<int32_t>(imageData.size()));
    Picture pic0 = chart.GetShapes().AddPictureInChart(50, 50, data, 40, 40);
    LineFormat lineFormat = pic0.GetLine();

    lineFormat.SetDashStyle(MsoLineDashStyle::Solid);
    lineFormat.SetWeight(4);

    workbook.Save(outDir + u"chart.out.xls");
    std::cout << "Chart modified successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Добавление флажка на диаграмму**

Aspose.Cells позволяет вставлять флажки на лист диаграммы, используя перечисление [**MsoDrawingType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msodrawingtype/). В следующем примере показано добавление флажка на лист диаграммы.

На следующем изображении показан лист диаграммы с флажком в выходном файле.

![todo:image_alt_text](controls-in-charts_1.jpg)

Ссылка на [выходной файл](101089316.xlsx), сгенерированный следующим фрагментом кода, прикреплена для вашего ознакомления.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a chart sheet to the workbook
    int32_t index = workbook.GetWorksheets().Add(SheetType::Chart);

    // Get the newly added chart sheet
    Worksheet sheet = workbook.GetWorksheets().Get(index);

    // Add a floating chart to the sheet
    sheet.GetCharts().AddFloatingChart(ChartType::Column, 0, 0, 1024, 960);

    // Add data series to the chart
    sheet.GetCharts().Get(0).GetNSeries().Add(U16String(u"{1,2,3}"), false);

    // Add a checkbox to the chart
    sheet.GetCharts().Get(0).GetShapes().AddShapeInChart(MsoDrawingType::CheckBox, PlacementType::Move, 400, 400, 1000, 600);

    // Set text for the checkbox
    sheet.GetCharts().Get(0).GetShapes().Get(0).SetText(U16String(u"CheckBox 1"));

    // Save the workbook
    workbook.Save(outDir + u"InsertCheckboxInChartSheet_out.xlsx");

    std::cout << "Checkbox added to chart sheet successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Продвинутые темы**
- [Добавить водяной знак WordArt на диаграмму](/cells/ru/cpp/add-wordart-watermark-to-chart/)
