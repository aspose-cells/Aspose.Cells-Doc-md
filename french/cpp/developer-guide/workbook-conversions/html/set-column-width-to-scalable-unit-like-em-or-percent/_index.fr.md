---
title: Définir la largeur de colonne en unité évolutive comme em ou pourcentage avec C++
linktitle: Définir la largeur de la colonne à une unité scalable telle que em ou pourcentage
type: docs
weight: 130
url: /fr/cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: Apprenez comment définir la largeur de colonne en unités évolutives comme em ou pourcentage en utilisant Aspose.Cells for C++.
---

Générer un fichier HTML à partir d'une feuille de calcul est très courant. La taille des colonnes est définie en "pt" ce qui fonctionne dans de nombreux cas. Cependant, il peut arriver qu'une taille fixe ne soit pas requise. Par exemple, si la largeur du panneau conteneur est de 600px où cette page HTML est affichée. Dans ce cas, des barres de défilement horizontales peuvent apparaître si la largeur de la table générée est plus grande. Il était nécessaire que cette taille fixe soit changée en une unité scalable telle que em ou pourcentage pour obtenir une meilleure présentation. Le code d'exemple suivant peut être utilisé où [**HtmlSaveOptions.GetWidthScalable()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getwidthscalable/) est défini sur **true** pour créer une largeur scalable.

Le fichier source d'exemple et les fichiers de sortie peuvent être téléchargés à partir des liens suivants:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

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

    // Load sample source file
    Workbook wb(srcDir + u"sampleForScalableColumns.xlsx");

    // Specify Html Save Options
    HtmlSaveOptions options;

    // Set the property for scalable width
    options.SetWidthScalable(true);

    // Specify image save format
    options.SetExportImagesAsBase64(true);

    // Save the workbook in Html format with specified Html Save Options
    wb.Save(outDir + u"outsampleForScalableColumns.html", options);

    std::cout << "Workbook saved successfully with scalable columns!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
