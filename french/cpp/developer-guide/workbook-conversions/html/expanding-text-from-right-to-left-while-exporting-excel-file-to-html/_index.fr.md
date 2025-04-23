---
title: Expansion du texte de droite à gauche lors de l exportation du fichier Excel en HTML avec C++
linktitle: Expansion du texte de droite à gauche lors de l exportation d un fichier Excel vers HTML
type: docs
weight: 60
url: /fr/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/
description: Apprenez à étendre le texte de droite à gauche lors de l exportation de fichiers Excel en HTML en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Aspose.Cells for C++ supporte désormais l'expansion du texte de droite à gauche lors de l'exportation des fichiers Excel en HTML. Cette fonctionnalité est implémentée depuis la version v8.9.0.0. Si votre fichier Excel source contient du texte qui s'étend de droite à gauche, Aspose.Cells l'exportera correctement en HTML.

{{% /alert %}} 

## **Expansion du texte de droite à gauche lors de l'exportation d'un fichier Excel vers HTML**

Le code d'exemple suivant convertit le [fichier Excel d'exemple](5115502.xlsx) en HTML. Cette capture d'écran montre l'apparence du fichier Excel dans Microsoft Excel 2013.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

Cette capture d'écran montre le [HTML de sortie généré avec la version précédente](5115509).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

Cette capture d'écran montre le [HTML de sortie généré avec la version plus récente](5115508).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Comme vous pouvez le voir dans les captures d'écran, la version plus récente étend le texte aligné à droite vers la gauche correctement, tout comme Microsoft Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source excel file inside the workbook object
    Workbook wb(srcDir + u"sample.xlsx");

    // Save workbook in html format
    U16String outputPath = srcDir + u"ExpandTextFromRightToLeft_out_" + CellsHelper::GetVersion() + u".html";
    wb.Save(outputPath, SaveFormat::Html);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
