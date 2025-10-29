---
title: Actualiser les valeurs des formes liées avec C++
linktitle: Actualiser les valeurs des formes liées
type: docs
weight: 3200
url: /fr/cpp/refresh-values-of-linked-shapes/
description: Apprenez comment actualiser les valeurs des formes liées dans les fichiers Excel en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Parfois, vous avez une forme liée dans votre fichier Excel qui est liée à une cellule. Dans Microsoft Excel, le changement de la valeur de la cellule liée change également la valeur de la forme liée. Cela fonctionne également bien avec Aspose.Cells si vous souhaitez enregistrer votre classeur au format XLS ou XLSX. Cependant, si vous voulez enregistrer votre classeur au format PDF ou HTML, alors vous devrez appeler la méthode [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/updateselectedvalue/) pour rafraîchir la valeur de la forme liée.

{{% /alert %}}

## Exemple

La capture d'écran suivante montre le fichier Excel source utilisé dans l'exemple ci-dessous. Il dispose d'une image liée liée aux cellules A1 à E4. Nous allons changer la valeur de la cellule B4 avec Aspose.Cells puis appeler la méthode [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/updateselectedvalue/) pour actualiser la valeur de l'image et l'enregistrer au format PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Vous pouvez télécharger le [fichier Excel source](95584291.xlsx) et le [PDF de sortie](95584292.pdf) à partir des liens donnés.

### Code C++ pour actualiser les valeurs des formes liées

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleRefreshValueOfLinkedShapes.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell B4
    Cell cell = worksheet.GetCells().Get(u"B4");
    cell.PutValue(100);

    // Update the value of the Linked Picture which is linked to cell B4
    worksheet.GetShapes().UpdateSelectedValue();

    // Save the workbook in PDF format
    workbook.Save(outDir + u"outputRefreshValueOfLinkedShapes.pdf", SaveFormat::Pdf);

    std::cout << "Linked shapes value refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
