---
title: Verwalten von Shape Textoptionen mit C++
linktitle: Formtextoptionen verwalten
type: docs
weight: 200
url: /de/cpp/managing-shape-text-options/
description: Erfahren Sie, wie Sie Shape Textoptionen programmatisch mit Aspose.Cells for C++ verwalten.
---

{{% alert color="primary" %}}

Aspose.Cells bietet leistungsstarke Funktionen zum programmatischen Verwalten von Shape-Textoptionen in Excel-Dateien. Diese Anleitung erklärt, wie Sie Shape-Text-Eigenschaften wie Ausrichtung, Orientierung und Formatierung mit Aspose.Cells for C++ manipulieren.

{{% /alert %}}

## **Verwalten von Shape-Textoptionen**

Aspose.Cells ermöglicht es Ihnen, den Text innerhalb von Formen in Excel-Dateien anzupassen. Die Klasse [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) stellt Methoden und Eigenschaften zur Verwaltung von Texteinstellungen wie Ausrichtung, Orientierung und Formatierung bereit.

### **Textausrichtung festlegen**
Sie können die horizontale und vertikale Ausrichtung des Textes innerhalb einer Form mit den Eigenschaften [**GetTextHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettexthorizontalalignment/) und [**GetTextVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextverticalalignment/) einstellen.

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

### **Textrichtung festlegen**
Sie können auch die Orientierung des Textes innerhalb einer Form mit der Eigenschaft [**TextOrientationType**](https://reference.aspose.com/cells/cpp/aspose.cells/textorientationtype/) einstellen.

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

### **Formatierung des Textes**
Sie können den Text innerhalb einer Form mit der Klasse [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) formatieren. Damit lassen sich Eigenschaften wie Schriftgröße, Farbe und Stil festlegen.

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

## **Fazit**
Aspose.Cells for C++ bietet eine umfassende Palette an Werkzeugen zur Verwaltung von Shape-Textoptionen in Excel-Dateien. Durch die Verwendung der Klasse [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) können Sie Textausrichtung, Orientierung und Formatierung einfach an Ihre Anforderungen anpassen.
