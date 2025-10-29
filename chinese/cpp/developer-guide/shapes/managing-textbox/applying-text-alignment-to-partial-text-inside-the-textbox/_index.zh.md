---
title: 如何用 C++ 为文本框应用/设置文本对齐
linktitle: 应用/设置文本框的文本对齐
type: docs
weight: 20
url: /zh/cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: 如何用 C++ 在 Aspose.Cells 中为文本框应用/设置文本对齐。
keywords: 应用/设置文本框工作表的 Excel Aspose 对齐文本框。
---

文本框可以提升我们文档和图表的表现力，对文本框不同部分应用不同的对齐方式，可以帮助突出重点。但默认的文本框对齐方式不能满足所有需求。对此，你可能需要调整每个文本框以满足目标要求。如果你没有大量的文本框需要调整，你很幸运。如果有很多文本框需要调整，我想你会遇到麻烦。别担心，[Aspose.Cells](https://products.aspose.com/cells/) 提供了相关API接口帮你实现这一点。

以下示例代码将文本对齐应用于文本框。

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

你还可以用适当的HTML文本改变文本框内某些文本的对齐方式。以下示例代码将对文本框内部的部分文本应用对齐方式。

[源文件](SampleTextboxExcel2016.xlsx)

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
