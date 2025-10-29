---
title: Insérer une image basée sur la référence de cellule avec C++
linktitle: Insérer une image basée sur la référence de la cellule
type: docs
weight: 150
url: /fr/cpp/insert-a-picture-based-on-cell-reference/
description: Apprenez comment insérer une image basée sur la référence de cellule en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Parfois, vous avez une image vide et vous devez afficher des données ou du contenu dans l'image en définissant une référence de cellule dans la barre de formule. Aspose.Cells prend en charge cette fonctionnalité (Microsoft Excel 2010).

{{% /alert %}}

## Insertion d'une image basée sur la référence de la cellule

Aspose.Cells prend en charge l'affichage du contenu d'une cellule de feuille de calcul dans une forme d'image. Vous pouvez lier l'image à la cellule qui contient les données que vous souhaitez afficher. Étant donné que la cellule ou la plage de cellules est liée à l'objet graphique, les modifications apportées aux données de cette cellule ou plage de cellules apparaissent automatiquement dans l'objet graphique. Ajoutez une image à la feuille de calcul en appelant la méthode [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) de la collection [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Spécifiez la plage de cellules en utilisant l'attribut [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) de l'objet [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

### Exemple de code

```cpp
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    cells.Get(U16String(u"A1")).PutValue(U16String(u"A1"));
    cells.Get(U16String(u"C10")).PutValue(U16String(u"C10"));

    Aspose::Cells::Vector<uint8_t> imagedata = ConditionalFormattingIcon::GetIconImageData(IconSetType::TrafficLights31, 0);

    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddPicture(0, 3, imagedata, 10, 10);
    pic.SetFormula(U16String(u"A1:C10"));

    workbook.GetWorksheets().Get(0).GetShapes().UpdateSelectedValue();
    workbook.Save(outDir + u"referencedpicture.out.xlsx");

    std::cout << "Referenced picture added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
