---
title: Как применить/установить выравнивание текста в текстовом поле с помощью C++
linktitle: Применить/установить выравнивание текста для текстового поля
type: docs
weight: 20
url: /ru/cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Как применить/установить выравнивание текста в текстовом поле в Aspose.Cells с C++.
keywords: применить/установить выравнивание текстового поля Лист Excel Aspose
---

Текстовые поля могут повысить выразительность наших документов и диаграмм, а применение разных выравниваний к разным частям TextBox может помочь выделить важные моменты для читателей. Но стандартное выравнивание TextBox не удовлетворяет все наши потребности. Для этого возможно потребуется настроить каждое TextBox под ваши требования. Если у вас немного объектов TextBox для настройки, это отлично. А если их много — это может стать проблемой. Не волнуйтесь, [Aspose.Cells](https://products.aspose.com/cells/) предоставляет API, который может помочь вам в этом.

Приведенный ниже образец кода применяет выравнивание текста к текстовому полю.

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

    // Get the shapes collection from the first worksheet
    ShapeCollection shapes = workbook.GetWorksheets().Get(0).GetShapes();

    // Add a TextBox to the worksheet
    Shape shape = shapes.AddTextBox(2, 0, 2, 0, 50, 120);

    // Set the text of the TextBox
    shape.SetText(u"This is a test.");

    // Set the horizontal and vertical alignment of the text
    shape.SetTextHorizontalAlignment(TextAlignmentType::Center);
    shape.SetTextVerticalAlignment(TextAlignmentType::Center);

    // Save the workbook to the output directory
    workbook.Save(outDir + u"result.xlsx");

    std::cout << "TextBox added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Вы также можете изменить выравнивание текста внутри некоторого текста в фигуре TextBox с помощью соответствующего HTML текста. Следующий пример демонстрирует применение выравнивания текста внутри части текста в TextBox.

[исходный файл](SampleTextboxExcel2016.xlsx)

```c++
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
    U16String inputFilePath = srcDir + u"SampleTextboxExcel2016.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Output.xlsx";

    // Initialize an object of the Workbook class to load template file
    Workbook sourceWb(inputFilePath);

    // Access the target textbox whose text is to be aligned
    auto sourceTextBox = sourceWb.GetWorksheets().Get(0).GetShapes().Get(0);

    // Create an object of the target workbook
    Workbook destWb;

    // Access first worksheet from the collection
    auto sheet = destWb.GetWorksheets().Get(0);

    // Create new textbox
    TextBox textBox = sheet.GetShapes().AddShape(MsoDrawingType::TextBox, 1, 0, 1, 0, 200, 200);

    // Alternatively text box can be added using following line as well
    // TextBox textBox = sheet.GetShapes().AddTextBox(1, 0, 1, 0, 200, 200);

    // Use Html string from a template file textbox
    textBox.SetHtmlText(sourceTextBox.GetHtmlText());

    // Save the workbook on disc
    destWb.Save(outputFilePath);

    std::cout << "Textbox copied and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
