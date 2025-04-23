---
title: Управление текстовыми опциями фигур с помощью C++
linktitle: Управление параметрами текста формы
type: docs
weight: 200
url: /ru/cpp/managing-shape-text-options/
description: Узнайте, как управлять текстовыми опциями фигур программным путем с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет мощные инструменты для управления текстовыми опциями фигур в файлах Excel программным способом. В этом руководстве объясняется, как изменять свойства текста фигур, такие как выравнивание, ориентация и форматирование, используя Aspose.Cells for C++.

{{% /alert %}}

## **Управление текстовыми опциями фигур**

Aspose.Cells позволяет вам настраивать текст внутри фигур в файлах Excel. Класс [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) предоставляет методы и свойства для управления опциями текста, такими как выравнивание, ориентация и форматирование.

### **Установка выравнивания текста**
Вы можете установить горизонтальное и вертикальное выравнивание текста внутри фигуры, используя свойства [**GetTextHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettexthorizontalalignment/) и [**GetTextVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextverticalalignment/).

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

### **Установка ориентации текста**
Также вы можете установить ориентацию текста внутри фигуры, используя свойство [**TextOrientationType**](https://reference.aspose.com/cells/cpp/aspose.cells/textorientationtype/).

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

### **Форматирование текста**
Вы можете форматировать текст внутри фигуры, используя класс [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/). Это позволяет установить свойства такие как размер шрифта, цвет и стиль.

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

## **Заключение**
Aspose.Cells for C++ предоставляет полный набор инструментов для управления текстовыми опциями фигур в файлах Excel. Используя класс [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/), вы легко настраиваете выравнивание, ориентацию и форматирование текста под свои требования.
