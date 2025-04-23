---
title: Exclure les styles inutilisés lors de la conversion d Excel en HTML avec C++
linktitle: Exclure les styles inutilisés
type: docs
weight: 30
url: /fr/cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Découvrez comment exclure les styles inutilisés lors de la conversion d Excel en HTML en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Les fichiers Microsoft Excel peuvent contenir de nombreux styles inutilisés. Lors de l'exportation du fichier Excel en format HTML, ces styles inutilisés sont également exportés, ce qui peut augmenter la taille du HTML. Vous pouvez exclure ces styles inutilisés lors de la conversion d'un fichier Excel en HTML en utilisant la propriété [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexcludeunusedstyles/). Lorsqu'elle est définie à **true**, tous les styles inutilisés sont exclus du HTML de sortie. La capture d'écran suivante montre un style inutilisé dans le HTML de sortie.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Exclure les styles inutilisés lors de la conversion d'Excel en HTML**

Le code d'exemple ci-dessous crée un classeur et crée également un style nommé inutilisé. Comme la propriété [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexcludeunusedstyles/) est définie à **true**, ce style inutilisé ne sera pas exporté dans le [HTML de sortie](61767778.zip). Cependant, si vous la définissez à **false**, ce style inutilisé sera présent dans le HTML de sortie, que vous pouvez voir dans la balise HTML comme montré dans la capture d'écran ci-dessus.

## **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook wb;

    // Create an unused named style
    Style unusedStyle = wb.CreateStyle();
    unusedStyle.SetName(u"UnusedStyle_XXXXXXXXXXXXXX");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put some value in cell C7
    ws.GetCells().Get(u"C7").PutValue(u"This is sample text.");

    // Specify html save options, we want to exclude unused styles
    HtmlSaveOptions opts;

    // Comment this line to include unused styles
    opts.SetExcludeUnusedStyles(true);

    // Save the workbook in html format
    wb.Save(u"outputExcludeUnusedStylesInExcelToHTML.html", opts);

    std::cout << "Workbook saved successfully with unused styles excluded!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
