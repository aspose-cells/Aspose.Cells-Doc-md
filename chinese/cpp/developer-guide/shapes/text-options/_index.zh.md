---
title: 用C++管理Shape文本选项
linktitle: 管理形状文本选项
type: docs
weight: 200
url: /zh/cpp/managing-shape-text-options/
description: 学习如何使用 Aspose.Cells for C++ 编程管理Shape的文本选项。
---

{{% alert color="primary" %}}

Aspose.Cells 提供强大的功能，用于程序化管理Excel文件中的Shape文本选项。本指南介绍如何使用 Aspose.Cells for C++ 操纵文本属性，如对齐、方向和格式。

{{% /alert %}}

## **管理Shape文本选项**

Aspose.Cells 允许你自定义Excel文件中Shape内的文本。 [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) 类提供方法和属性，用于管理文本选项，如对齐、方向和格式。

### **设置文本对齐**
你可以使用 [**GetTextHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettexthorizontalalignment/) 和 [**GetTextVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextverticalalignment/) 属性设置Shape内文本的水平和垂直对齐。

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

void SetTextAlignment() {
    // Load the Excel file
    Workbook workbook("example.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the shape
    Shape shape = worksheet.GetShapes().Get(0);

    // Set text alignment
    shape.SetTextHorizontalAlignment(TextAlignmentType::Center);
    shape.SetTextVerticalAlignment(TextAlignmentType::Center);

    // Save the workbook
    workbook.Save("output.xlsx");
}
```

### **设置文本方向**
你还可以使用 [**TextOrientationType**](https://reference.aspose.com/cells/cpp/aspose.cells/textorientationtype/) 属性设置Shape内文本的方向。

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

void SetTextOrientation() {
    Workbook workbook("example.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    TextBox textbox = worksheet.GetTextBoxes().Get(0);
    textbox.SetTextOrientationType(TextOrientationType::ClockWise);

    workbook.Save("output.xlsx");
}
```

### **格式化文本**
你可以使用 [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) 类格式化Shape内部的文本，设置字体大小、颜色和样式。

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

void FormatText() {
    // Load the Excel file
    Workbook workbook("example.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the shape
    Shape shape = worksheet.GetShapes().Get(0);

    // Access the font of the shape's text
    Font font = shape.GetTextBody().GetParagraphEnumerator().GetCurrent().GetFont();

    // Set font properties
    font.SetSize(14);
    font.SetColor(Color::Red());
    font.SetIsBold(true);

    // Save the workbook
    workbook.Save("output.xlsx");
}
```

## **结论**
Aspose.Cells for C++ 提供了一套完整的工具，用于管理Excel文件中的Shape文本选项。通过使用 [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) 类，可轻松定制文本的对齐、方向和格式以满足您的具体需求。
