---
title: Gérer les options de texte de forme avec C++
linktitle: Gérer les options de texte de forme
type: docs
weight: 200
url: /fr/cpp/managing-shape-text-options/
description: Apprenez comment gérer les options de texte de forme de manière programmatique en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells offre des fonctionnalités puissantes pour gérer les options de texte de forme dans les fichiers Excel de manière programmatique. Ce guide explique comment manipuler les propriétés de texte de forme telles que l'alignement, l'orientation et la mise en forme en utilisant Aspose.Cells for C++.

{{% /alert %}}

## **Gestion des options de texte de forme**

Aspose.Cells vous permet de personnaliser le texte à l'intérieur des formes dans les fichiers Excel. La classe [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) fournit des méthodes et propriétés pour gérer les options de texte telles que l'alignement, l'orientation et la mise en forme.

### **Réglage de l'alignement du texte**
Vous pouvez définir l'alignement horizontal et vertical du texte dans une forme à l'aide des propriétés [**GetTextHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettexthorizontalalignment/) et [**GetTextVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextverticalalignment/).

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

### **Réglage de l'orientation du texte**
Vous pouvez également définir l'orientation du texte dans une forme à l'aide de la propriété [**TextOrientationType**](https://reference.aspose.com/cells/cpp/aspose.cells/textorientationtype/).

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

### **Mise en forme du texte**
Vous pouvez formater le texte dans une forme en utilisant la classe [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/). Cela vous permet de définir des propriétés telles que la taille de la police, la couleur et le style.

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
Aspose.Cells for C++ fournit un ensemble complet d'outils pour gérer les options de texte dans les formes dans les fichiers Excel. En utilisant la classe [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/), vous pouvez facilement personnaliser l'alignement du texte, l'orientation et la mise en forme pour répondre à vos besoins spécifiques.
{{< app/cells/assistant language="cpp" >}}
