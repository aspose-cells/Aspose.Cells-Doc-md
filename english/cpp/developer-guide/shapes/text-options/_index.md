---
title: Manage Shape Text Options with C++
linktitle: Manage Shape Text Options
type: docs
weight: 200
url: /cpp/managing-shape-text-options/
description: Learn how to manage shape text options programmatically using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells provides powerful features to manage shape text options in Excel files programmatically. This guide explains how to manipulate shape text properties such as alignment, orientation, and formatting using Aspose.Cells for C++.

{{% /alert %}}

## **Managing Shape Text Options**

Aspose.Cells allows you to customize the text within shapes in Excel files. The [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) class provides methods and properties to manage text options such as alignment, orientation, and formatting.

### **Setting Text Alignment**
You can set the horizontal and vertical alignment of text within a shape using the [**GetTextHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettexthorizontalalignment/) and [**GetTextVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextverticalalignment/) **methods**.

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

### **Setting Text Orientation**
You can also set the orientation of the text within a shape using the **SetTextOrientationType** method with the [**TextOrientationType**](https://reference.aspose.com/cells/cpp/aspose.cells/textorientationtype/) enumeration.

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

void SetTextOrientation() {
    Workbook workbook("example.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    TextBox textbox = worksheet.GetTextBoxes().Get(0);
    textbox.SetTextOrientationType(TextOrientationType::Clockwise);

    workbook.Save("output.xlsx");
}
```

### **Formatting Text**
You can format the text within a shape using the [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) class. This allows you to set properties such as font size, color, and style.

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

## **Conclusion**
Aspose.Cells for C++ provides a comprehensive set of tools to manage shape text options in Excel files. By using the [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) class, you can easily customize text alignment, orientation, and formatting to meet your specific requirements.
{{< app/cells/assistant language="cpp" >}}
