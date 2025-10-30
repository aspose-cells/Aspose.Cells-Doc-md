---
title: Modifica lo Spaziamento tra i caratteri di una TextBox o Forma in Excel con C++
linktitle: Modifica lo spaziamento dei caratteri della casella di testo o della forma di Excel
type: docs
weight: 280
url: /it/cpp/change-character-spacing-of-excel-textbox-or-shape/
description: Impara come modificare lo spaziamento tra i caratteri di una casella di testo o forma in Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Puoi modificare lo spaziamento tra i caratteri di una casella di testo o forma in Excel usando la proprietà [**TextOptions.GetSpacing()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getspacing/).

{{% /alert %}}

Il seguente esempio di codice modifica l'interlinea del testo in una casella di testo di un file Excel a punto 4 e poi lo salva su disco.

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
