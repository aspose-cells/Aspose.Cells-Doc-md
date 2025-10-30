---
title: Gestione delle opzioni del testo delle forme con C++
linktitle: Gestisci le opzioni di testo della forma
type: docs
weight: 200
url: /it/cpp/managing-shape-text-options/
description: Impara come gestire le opzioni del testo delle forme programmaticamente utilizzando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells offre funzionalità avanzate per gestire le opzioni del testo delle forme nei file Excel in modo programmatico. Questa guida spiega come manipolare le proprietà del testo delle forme come allineamento, orientamento e formattazione usando Aspose.Cells for C++.

{{% /alert %}}

## **Gestione delle opzioni del testo delle forme**

Aspose.Cells consente di personalizzare il testo all'interno delle forme nei file Excel. La classe [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) fornisce metodi e proprietà per gestire le opzioni del testo come allineamento, orientamento e formattazione.

### **Impostare l'allineamento del testo**
Puoi impostare l'allineamento orizzontale e verticale del testo all’interno di una forma utilizzando le proprietà [**GetTextHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettexthorizontalalignment/) e [**GetTextVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextverticalalignment/).

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

### **Impostare l'orientamento del testo**
Puoi anche impostare l'orientamento del testo all’interno di una forma utilizzando la proprietà [**TextOrientationType**](https://reference.aspose.com/cells/cpp/aspose.cells/textorientationtype/).

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

### **Formattare il testo**
Puoi formattare il testo all’interno di una forma usando la classe [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/). Questo ti permette di impostare proprietà come dimensione del carattere, colore e stile.

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

## **Conclusioni**
Aspose.Cells for C++ fornisce un set completo di strumenti per gestire le opzioni del testo delle forme nei file Excel. Utilizzando la classe [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/), puoi facilmente personalizzare l’allineamento del testo, l’orientamento e la formattazione per soddisfare le tue esigenze.
{{< app/cells/assistant language="cpp" >}}
