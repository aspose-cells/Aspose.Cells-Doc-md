---
title: Gestionar Opciones de Texto de Forma con C++
linktitle: Gestionar opciones de texto de formas
type: docs
weight: 200
url: /es/cpp/managing-shape-text-options/
description: Aprende cómo gestionar las opciones de texto en formas programáticamente usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells proporciona funciones potentes para gestionar las opciones de texto de formas en archivos de Excel de manera programática. Esta guía explica cómo manipular propiedades de texto de forma como alineación, orientación y formato usando Aspose.Cells for C++.

{{% /alert %}}

## **Gestión de Opciones de Texto en Forma**

Aspose.Cells te permite personalizar el texto dentro de las formas en archivos de Excel. La clase [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) proporciona métodos y propiedades para gestionar opciones de texto como alineación, orientación y formato.

### **Establecer alineación del texto**
Puedes configurar la alineación horizontal y vertical del texto dentro de una forma usando las propiedades [**GetTextHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettexthorizontalalignment/) y [**GetTextVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextverticalalignment/).

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

### **Establecer orientación del texto**
También puedes configurar la orientación del texto dentro de una forma usando la propiedad [**TextOrientationType**](https://reference.aspose.com/cells/cpp/aspose.cells/textorientationtype/).

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

### **Formatear Texto**
Puedes formatear el texto dentro de una forma usando la clase [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/). Esto te permite establecer propiedades como tamaño de fuente, color y estilo.

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

## **Conclusión**
Aspose.Cells for C++ ofrece un conjunto completo de herramientas para gestionar las opciones de texto de formas en archivos de Excel. Usando la clase [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/), puedes personalizar fácilmente la alineación del texto, la orientación y el formato para cumplir con tus requisitos específicos.
{{< app/cells/assistant language="cpp" >}}
