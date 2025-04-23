---
title: Ändra teckengapet i Excel TextBox eller Shape med C++
linktitle: Ändra karaktärsavståndet för Excel TextBox eller Shape
type: docs
weight: 280
url: /sv/cpp/change-character-spacing-of-excel-textbox-or-shape/
description: Lär dig hur man ändrar teckengapet för Excel textbox eller form med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Du kan ändra teckengapet för Excel-textbox eller form med egenskapen [**TextOptions.GetSpacing()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getspacing/).

{{% /alert %}}

Följande exempel ändrar teckengapet för textrutan i en Excel-fil till punkt 4 och sparar den sedan på disk.

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
