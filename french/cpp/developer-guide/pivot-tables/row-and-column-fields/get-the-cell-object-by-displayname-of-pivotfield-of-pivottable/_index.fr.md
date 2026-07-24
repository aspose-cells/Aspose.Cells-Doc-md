---
title: Obtenez l objet de cellule par DisplayName de PivotField du tableau croisé dynamique en C++
linktitle: Obtenez l objet de cellule par DisplayName de PivotField du tableau croisé dynamique
type: docs
weight: 70
url: /fr/cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Apprenez comment récupérer l objet de cellule par le nom d affichage d un champ de pivot et appliquer une mise en forme en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 Aspose.Cells propose la méthode [**PivotTable::GetCellByDisplayName()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getcellbydisplayname/), que vous pouvez utiliser pour accéder à l'objet de cellule par le nom d'affichage d'un champ de pivot. Cette méthode est utile lorsque vous souhaitez mettre en évidence ou formater l'en-tête de votre champ de pivot. Cet article explique comment récupérer l'objet de cellule par le nom d'affichage d'un champ de données puis lui appliquer une mise en forme.

{{% /alert %}}

## **Obtenez l'objet de cellule par DisplayName de PivotField du tableau croisé dynamique**

 Le code suivant accède au premier tableau croisé dynamique de la feuille de calcul, puis récupère la cellule par le nom d'affichage du deuxième champ de données du tableau croisé dynamique. Il modifie ensuite la couleur de remplissage et la couleur de la police de la cellule en bleu clair et en noir, respectivement. Ci-dessous, des captures d'écran montrant l'apparence du tableau croisé dynamique avant et après l'exécution du code.

|**Tableau croisé dynamique - Avant**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"source.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    Cell cell = pivotTable.GetCellByDisplayName(pivotTable.GetDataFields().Get(0).GetDisplayName());

    Style style = cell.GetStyle();
    style.SetForegroundColor(Color::LightBlue());
    style.GetFont().SetColor(Color::Black());

    pivotTable.Format(cell.GetRow(), cell.GetColumn(), style);
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Pivot table formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

|**Tableau croisé dynamique - Après**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
{{< app/cells/assistant language="cpp" >}}
