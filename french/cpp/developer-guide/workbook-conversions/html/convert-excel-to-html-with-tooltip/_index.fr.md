---
title: Convertir Excel en HTML avec infobulle en utilisant C++
linktitle: Convertir Excel en HTML avec info bulle
type: docs
weight: 200
url: /fr/cpp/convert-excel-to-html-with-tooltip/
description: Convertissez Excel en HTML tout en ajoutant des infobulles avec Aspose.Cells en utilisant C++.
---

## **Convertir Excel en HTML avec info-bulle**

Il peut arriver que le texte soit coupé dans le HTML généré et vous souhaitez afficher le texte complet en tant que tooltip lors du survol. Aspose.Cells le supporte en utilisant la propriété [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/). En définissant la propriété [**HtmlSaveOptions.GetAddTooltipText()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getaddtooltiptext/) à **true**, le texte complet sera ajouté en tant que tooltip dans le HTML généré.

L'image suivante montre l'info-bulle dans le fichier HTML généré.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Le code d'exemple suivant charge le [fichier Excel source](98107416.xlsx) et génère le [fichier HTML de sortie](98107417.zip) avec l'infobulle.

Code d'exemple

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the template file
    Workbook workbook(sourceDir + u"AddTooltipToHtmlSample.xlsx");

    // Setup HTML save options
    HtmlSaveOptions options;
    options.SetAddTooltipText(true);  // Enable tooltip text in output

    // Save as HTML
    workbook.Save(outputDir + u"AddTooltipToHtmlSample_out.html", options);

    std::cout << "Workbook saved with tooltip text added!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
