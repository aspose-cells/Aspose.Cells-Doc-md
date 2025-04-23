---
title: Activer les propriétés CSS personnalisées lors de l’enregistrement en HTML avec C++
linktitle: Activer les propriétés CSS personnalisées lors de l enregistrement en HTML
type: docs
weight: 320
url: /fr/cpp/enable-css-custom-properties-while-saving-to-html/
description: Découvrez comment activer les propriétés CSS personnalisées lors de l enregistrement des fichiers Excel en HTML en utilisant Aspose.Cells for C++. Améliorez la performance en réduisant les données d image redondantes.
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, dans le scénario où il y a plusieurs occurrences d'une même image en base64, avec la propriété personnalisée, les données de l'image n'ont besoin d'être sauvegardées qu'une seule fois, ce qui peut améliorer la performance de l'HTML résultant. Veuillez utiliser la propriété [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/) et la définir à **true** lors de l'enregistrement en HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Activer les propriétés personnalisées CSS lors de l'enregistrement en HTML**

Le code d'exemple ci-dessous montre l'utilisation de la propriété [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getenablecsscustomproperties/). La capture d'écran montre l'effet de cette propriété lorsqu'elle n'est pas définie à **true**. Veuillez télécharger le [fichier Excel d'exemple](50528260.xlsx) utilisé dans ce code et le [HTML généré](50528261.zip) pour référence.

## **Code d'exemple**

```cpp
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

    // Load sample workbook
    Workbook wb(srcDir + u"sampleEnableCssCustomProperties.xlsx");

    // Create HtmlSaveOptions object
    HtmlSaveOptions opts;

    // Set ExportImagesAsBase64 to true
    opts.SetExportImagesAsBase64(true);

    // Enable EnableCssCustomProperties
    opts.SetEnableCssCustomProperties(true);

    // Save the workbook in HTML format
    wb.Save(outDir + u"outputEnableCssCustomProperties.html", opts);

    std::cout << "Workbook saved successfully with CSS custom properties enabled!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
