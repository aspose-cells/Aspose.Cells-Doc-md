---
title: إدارة خيارات نص الشكل باستخدام C++
linktitle: إدارة خيارات نص الشكل
type: docs
weight: 200
url: /ar/cpp/managing-shape-text-options/
description: تعلم كيفية إدارة خيارات نص الشكل برمجيًا باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

تقدم Aspose.Cells ميزات قوية لإدارة خيارات نص الشكل في ملفات إكسل برمجيًا. يشرح هذا الدليل كيف يتم التلاعب بخصائص نص الشكل مثل التمحور، والتوجيه، والتنسيق باستخدام Aspose.Cells for C++.

{{% /alert %}}

## **إدارة خيارات نص الشكل**

تسمح لك Aspose.Cells بتخصيص النص داخل الأشكال في ملفات إكسل. توفر فئة [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) طرق وخصائص لإدارة خيارات النص مثل المحاذاة، والتوجيه، والتنسيق.

### **تعيين محاذاة النص**
يمكنك تعيين المحاذاة الأفقية والعمودية للنص داخل شكل باستخدام خصائص [**GetTextHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettexthorizontalalignment/) و [**GetTextVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextverticalalignment/).

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

### **تعيين توجيه النص**
يمكنك أيضًا تعيين توجيه النص داخل الشكل باستخدام خاصية [**TextOrientationType**](https://reference.aspose.com/cells/cpp/aspose.cells/textorientationtype/).

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

### **تنسيق النص**
يمكنك تنسيق النص داخل شكل باستخدام فئة [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/). هذا يسمح لك بضبط خصائص مثل حجم الخط، اللون، والنمط.

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

## **الاستنتاج**
توفر Aspose.Cells for C++ مجموعة أدوات شاملة لإدارة خيارات نص الشكل في ملفات إكسل. باستخدام فئة [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/)، يمكنك بسهولة تخصيص محاذاة النص، والتوجيه، والتنسيق لتلبية متطلباتك الخاصة.
{{< app/cells/assistant language="cpp" >}}
