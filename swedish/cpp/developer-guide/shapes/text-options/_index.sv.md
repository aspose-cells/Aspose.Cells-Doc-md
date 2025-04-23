---
title: Hantera formtextalternativ med C++
linktitle: Hantera textalternativ för form
type: docs
weight: 200
url: /sv/cpp/managing-shape-text-options/
description: Lär dig att hantera formtextalternativ programmatiskt med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells erbjuder kraftfulla funktioner för att hantera formtextalternativ i Excel-filer programmatiskt. Denna guide förklarar hur man manipulerar formtext egenskaper som justering, orientering och formatering med Aspose.Cells for C++.

{{% /alert %}}

## **Hantera formtextalternativ**

Aspose.Cells tillåter dig att anpassa texten inom former i Excel-filer. Klassen [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) tillhandahåller metoder och egenskaper för att hantera textalternativ som justering, orientering och formatering.

### **Ställa in textjustering**
Du kan ställa in den horisontella och vertikala justeringen av text i en form med hjälp av egenskaperna [**GetTextHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettexthorizontalalignment/) och [**GetTextVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextverticalalignment/).

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

### **Ställa in textorientering**
Du kan också ställa in orienteringen av texten i en form med hjälp av egenskapen [**TextOrientationType**](https://reference.aspose.com/cells/cpp/aspose.cells/textorientationtype/).

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

### **Formatering av text**
Du kan formatera texten inom en form med hjälp av [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/)-klassen. Detta gör att du kan ange egenskaper såsom teckenstorlek, färg och stil.

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

## **Slutsats**
Aspose.Cells for C++ erbjuder ett omfattande verktygssätt för att hantera formtextalternativ i Excel-filer. Genom att använda [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/)-klassen kan du enkelt anpassa textjustering, orientering och formatering för att möta dina specifika krav.
