---
title: Rechercher des données en utilisant des valeurs d origine avec C++
linktitle: Rechercher des données en utilisant les valeurs d origine
type: docs
weight: 380
url: /fr/cpp/search-data-using-original-values/
description: Apprenez comment rechercher des données en utilisant des valeurs d origine via l API Aspose.Cells for C++.
keywords: Rechercher des données en utilisant les valeurs d origine, Trouver des données en utilisant les valeurs d origine, Rechercher des données par les valeurs d origine, Trouver des données par les valeurs d origine
---

{{% alert color="primary" %}}

Parfois, la valeur des données est masquée car elle est formatée d'une certaine manière. Par exemple, supposons que la cellule D4 ait la formule =Somme(A1:A2) et que sa valeur soit 20 mais qu'elle soit formatée comme ---, alors la valeur 20 est masquée et ne peut pas être trouvée en utilisant les options de recherche de Microsoft Excel. Cependant, vous pouvez la trouver en utilisant Aspose.Cells avec [**LookInType.OriginalValues**](https://reference.aspose.com/cells/cpp/aspose.cells/lookintype/)

{{% /alert %}}

Le code d'exemple suivant illustre le point ci-dessus. Il trouve la cellule D4 qui ne peut pas être trouvée en utilisant les options de recherche de Microsoft Excel mais Aspose.Cells peut la trouver en utilisant [**LookInType.OriginalValues**](https://reference.aspose.com/cells/cpp/aspose.cells/lookintype/). Veuillez lire les commentaires à l'intérieur du code pour plus d'informations.

## Code C++ pour rechercher des données en utilisant des valeurs originales

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

    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add 10 in cell A1 and A2
    worksheet.GetCells().Get(u"A1").PutValue(10);
    worksheet.GetCells().Get(u"A2").PutValue(10);

    // Add Sum formula in cell D4 but customize it as ---
    Cell cell = worksheet.GetCells().Get(u"D4");

    Style style = cell.GetStyle();
    style.SetCustom(u"---", true);
    cell.SetStyle(style);

    // The result of formula will be 20 but 20 will not be visible because the cell is formatted as ---
    cell.SetFormula(u"=Sum(A1:A2)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Create find options, we will search 20 using original values otherwise 20 will never be found because it is formatted as ---
    FindOptions options;
    options.SetLookInType(LookInType::OriginalValues);
    options.SetLookAtType(LookAtType::EntireContent);

    Cell foundCell;
    int32_t obj = 20;

    // Find 20 which is Sum(A1:A2) and formatted as ---
    foundCell = worksheet.GetCells().Find(obj, foundCell, options);

    // Print the found cell
    std::cout << foundCell.ToString().ToUtf8() << std::endl;

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## Sortie console générée par le code d'exemple

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
