---
title: Définir l espacement entre les lignes du paragraphe dans une forme ou une zone de texte avec C++
linktitle: Définir l espacement entre les lignes du paragraphe
type: docs
weight: 290
url: /fr/cpp/set-line-spacing-of-the-paragraph-in-a-shape-or-textbox/
description: Apprenez comment définir l espacement entre les lignes, l espace avant et l espace après dans un paragraphe au sein d une forme ou d une zone de texte en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Vous pouvez définir l'espacement des lignes du paragraphe, son espacement avant et après en utilisant les propriétés [**TextParagraph.GetLineSpace()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textparagraph/getlinespace/), [**TextParagraph.GetSpaceBefore()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textparagraph/getspacebefore/) et [**TextParagraph.GetSpaceAfter()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textparagraph/getspaceafter/) de la classe [**TextParagraph**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textparagraph/).

{{% /alert %}}

Le code d'échantillon suivant explique l'utilisation des propriétés mentionnées.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::Texts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add text box inside the sheet
    ws.GetShapes().AddTextBox(2, 0, 2, 0, 100, 200);

    // Access first shape which is a text box and set its text
    Shape shape = ws.GetShapes().Get(0);
    shape.SetText(u"Sign up for your free phone number.\nCall and text online for free.");

    // Access the first paragraph
    TextParagraph p = shape.GetTextBody().GetTextParagraphs().Get(1);

    // Set the line space
    p.SetLineSpaceSizeType(LineSpaceSizeType::Points);
    p.SetLineSpace(20);

    // Set the space after
    p.SetSpaceAfterSizeType(LineSpaceSizeType::Points);
    p.SetSpaceAfter(10);

    // Set the space before
    p.SetSpaceBeforeSizeType(LineSpaceSizeType::Points);
    p.SetSpaceBefore(10);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
