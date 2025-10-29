---
title: Masquer le contenu superposé avec CrossHideRight lors de l’enregistrement en HTML avec C++
linktitle: Masquer le contenu superposé avec CrossHideRight lors de l enregistrement en HTML
type: docs
weight: 100
url: /fr/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: Utilisez CrossHideRight avec Aspose.Cells en C++ pour masquer le contenu superposé lors de l’enregistrement en HTML.
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, vous pouvez spécifier différents types de croisement pour les chaînes de cellules. Par défaut, Aspose.Cells génère du HTML selon Microsoft Excel, mais lorsque vous modifiez le type de croisement en [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype), il masque toutes les chaînes situées à droite de la cellule qui sont overlay ou qui se chevauchent avec la chaîne de la cellule.

## **Masquer le contenu superposé avec CrossHideRight lors de l'enregistrement en HTML**

Le code d’exemple suivant charge le [fichier Excel d'exemple](64716894.xlsx) et l’enregistre en [HTML de sortie](64716893.zip) après avoir réglé [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/gethtmlcrossstringtype/) comme [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype). La capture d’écran explique comment [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) influence le HTML de sortie par rapport à la sortie par défaut.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook wb(sourceDir + u"sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");

    // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::CrossHideRight);

    // Save to HTML with HtmlSaveOptions
    wb.Save(outputDir + u"outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html", opts);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
