---
title: Afficher les caractères supplémentaires Unicode dans le PDF de sortie avec C++ par Aspose.Cells
linktitle: Render Unicode Supplementary Characters
type: docs
weight: 350
url: /fr/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Apprenez comment rendre les caractères supplémentaires Unicode dans le PDF de sortie en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Les caractères Unicode normaux ont une longueur de 2 octets tandis que les caractères Unicode supplémentaires ont une longueur de 4 octets. Aspose.Cells prend maintenant en charge le rendu de ces caractères Unicode de 4 octets.

Dans la norme des caractères Unicode, les Caractères supplémentaires sont les caractères aux points de code de U+10000 à U+10FFFF. En d'autres termes, ce sont les caractères Unicode supérieurs à U+FFFF.

- En UTF-8, ces caractères ont une longueur de 4 octets.
- En UTF-16, ces caractères nécessitent 2 substituts (unités de 16 bits).

{{% /alert %}}

## Rendre les caractères Unicode supplémentaires dans le PDF de sortie par Aspose.Cells

La capture d'écran suivante montre comment Aspose.Cells a rendu le [fichier Excel source](5115563.xlsx) en [PDF de sortie](5115564.pdf). Comme vous pouvez le voir, les trois caractères Unicode supplémentaires ont été rendus exactement de la même manière que par Microsoft Excel.

![todo:image_alt_text](output.png)

## Code d'exemple

Vous pouvez utiliser ce code d'exemple pour convertir le [fichier Excel source](5115563.xlsx) en [PDF de sortie](5115564.pdf).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"unicode-supplementary-characters.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"RenderUnicodeInOutput_out.pdf";

    // Load the source excel file containing Unicode Supplementary characters
    Workbook wb(inputFilePath);

    // Save the workbook as PDF
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully with Unicode Supplementary characters!" << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```
