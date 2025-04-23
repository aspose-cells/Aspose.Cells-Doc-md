---
title: Modifier l espacement des caractères du TextBox ou de la forme Excel avec C++
linktitle: Modifier l espacement des caractères du TextBox ou de la forme Excel
type: docs
weight: 280
url: /fr/cpp/change-character-spacing-of-excel-textbox-or-shape/
description: Apprenez comment modifier l espacement des caractères du boîte de texte ou de la forme Excel en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Vous pouvez modifier l'espacement des caractères du TextBox ou de la forme Excel en utilisant la propriété [**TextOptions.GetSpacing()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getspacing/).

{{% /alert %}}

Le code exemple suivant modifie l'espacement des caractères de la zone de texte dans un fichier Excel à 4 points puis l'enregistre sur disque.

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
