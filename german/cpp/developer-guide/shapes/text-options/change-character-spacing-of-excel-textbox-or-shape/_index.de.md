---
title: Ändern Sie den Zeichenabstand des Excel Textfelds oder der Shape mit C++
linktitle: Zeichenabstand eines Excel TextBoxes oder einer Form ändern
type: docs
weight: 280
url: /de/cpp/change-character-spacing-of-excel-textbox-or-shape/
description: Lernen Sie, wie Sie den Zeichenabstand eines Excel Textboxs oder einer Shape mit Aspose.Cells und C++ ändern.
---

{{% alert color="primary" %}}

 Sie können den Zeichenabstand eines Excel-Textfelds oder einer Shape mit der [**TextOptions.GetSpacing()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getspacing/) Eigenschaft ändern.

{{% /alert %}}

Das folgende Beispiel ändert den Zeichenabstand des Textfelds in einer Excel-Datei auf Punkt 4 und speichert es dann auf der Festplatte.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your excel file inside a workbook object
    Workbook wb(srcDir + u"sampleChangeTextBoxOrShapeCharacterSpacing.xlsx");

    // Access your text box which is also a shape object from shapes collection
    Shape shape = wb.GetWorksheets().Get(0).GetShapes().Get(0);

    // Access the first font setting object via GetCharacters() method
    FontSetting fs = shape.GetRichFormattings()[0];

    // Set the character spacing to point 4
    fs.GetTextOptions().SetSpacing(4);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputChangeTextBoxOrShapeCharacterSpacing.xlsx", SaveFormat::Xlsx);

    std::cout << "Character spacing changed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
