---
title: Ajuster automatiquement la hauteur des lignes pour le rendu avec C++
linktitle: Ajuster automatiquement les lignes pour le rendu
type: docs
weight: 130
url: /fr/cpp/autofit-rows-for-rendering/
description: Apprenez comment ajuster automatiquement la hauteur des lignes pour le rendu dans les fichiers Excel en utilisant Aspose.Cells avec C++.
---

En général, lorsque vous souhaitez afficher tout le texte dans une cellule, vous pouvez ajuster automatiquement la ligne en mode Normal avec un zoom à 100% dans Microsoft Excel. Cela permet au texte d'être entièrement visible en mode Normal, et même lorsque vous imprimez ou enregistrez le fichier au format PDF, le texte sera affiché correctement.

Cependant, dans certains cas, l'ajustement automatique de la ligne fonctionne bien en mode Normal, mais lorsque vous passez en mode d'impression ou enregistrez le fichier au format PDF, le texte est tronqué. Veuillez vérifier le fichier source [Book1.xlsx](Book1.xlsx) et les captures d'écran.

![le texte est tronqué en mode d'impression](text_clipped_in_printview.png)

Si vous souhaitez empêcher la coupure de texte dans le fichier PDF sauvegardé, vous pouvez ajuster automatiquement la hauteur de la ligne avec l'option [AutoFitterOptions.GetForRendering()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getforrendering/).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize workbook instance
    Workbook workbook(u"Book1.xlsx");

    // Set autofit options for rendering
    AutoFitterOptions autoFitterOptions;
    autoFitterOptions.SetForRendering(true);

    // Autofit rows with options
    workbook.GetWorksheets().Get(0).AutoFitRows(autoFitterOptions);

    // Save to PDF
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    Aspose::Cells::Cleanup();
}
```

Maintenant, le texte n'est pas tronqué dans le fichier PDF de sortie.

![le texte n'est pas tronqué dans le PDF enregistré](text_not_clipped_in_saved_pdf.png)
{{< app/cells/assistant language="cpp" >}}
