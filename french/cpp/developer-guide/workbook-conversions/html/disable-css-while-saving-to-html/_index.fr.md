---
title: Désactiver CSS lors de l enregistrement en HTML avec C++
linktitle: Désactiver le CSS lors de l enregistrement en HTML
type: docs
weight: 320
url: /fr/cpp/disable-css-while-saving-to-html/
description: Apprenez comment désactiver CSS lors de l enregistrement de fichiers Excel en HTML en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

 Lorsque vous enregistrez votre fichier Excel en HTML à page unique, généralement les éléments CSS seront intégrés dans le fichier HTML et situés dans la section HEAD. Si vous attachez ce fichier comme contenu/corps d’un email, les éléments CSS seront supprimés par la plupart des clients de messagerie, ce qui entraînera un rendu incorrect. La version 24.12 d'Aspose.Cells introduit une option permettant de désactiver de manière optionnelle CSS, permettant aux styles d’être appliqués directement dans les éléments HTML eux-mêmes. Si vous souhaitez définir le HTML comme contenu/corps de l’email, veuillez utiliser la propriété [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/) et la définir à **true**.

## **Désactiver le CSS lors de l'enregistrement en HTML**

 Le code d'exemple suivant montre l’utilisation de la propriété [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getdisablecss/).

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
    Workbook wb(srcDir + u"sampleDisableCss.xlsx");

    // Disable CSS
    HtmlSaveOptions opts;
    opts.SetDisableCss(true);

    // Save the workbook in HTML
    wb.Save(outDir + u"outputDisable.html", opts);

    std::cout << "Workbook saved with CSS disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
