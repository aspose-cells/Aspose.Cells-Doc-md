---  
title: Accéder à la table à partir de la cellule et ajouter des valeurs à l intérieur en utilisant des décalages de ligne et de colonne avec C++  
linktitle: Accéder à un tableau depuis une cellule et ajouter des valeurs à l intérieur en utilisant des décalages de ligne et de colonne  
type: docs  
weight: 230  
url: /fr/cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
description: Accéder à une table depuis une cellule et ajouter des valeurs en utilisant Aspose.Cells avec C++.  
---  

{{% alert color="primary" %}}  

Normalement, vous ajoutez des valeurs à l'intérieur de l'objet Table ou Liste en utilisant la méthode [**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/). Mais parfois, vous pourriez avoir besoin d'ajouter des valeurs à l'intérieur de l'objet Table ou Liste en utilisant les décalages de ligne et de colonne.  

Pour accéder à une table ou à un objet liste à partir d'une cellule, utilisez la méthode [**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/). Pour ajouter des valeurs à l'intérieur en utilisant les décalages de ligne et de colonne, utilisez la méthode [**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/).  

{{% /alert %}}  

La capture d'écran suivante montre le fichier Excel source utilisé dans le code. Il contient la table vide et met en évidence la cellule D5 qui se trouve dans la table. Nous accéderons à cette table à partir de la cellule D5 en utilisant la méthode [**Cell.GetTable()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettable/), puis ajouterons des valeurs à l'intérieur en utilisant les méthodes [**Cell.PutValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) et [**ListObject.PutCellValue**](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listobject/putcellvalue/).  

## Exemple  

### Captures d'écran comparant les fichiers source et de sortie  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

La capture d'écran suivante montre le fichier Excel de sortie généré par le code. Comme vous pouvez le voir, la cellule D5 a une valeur et la cellule F6, qui est située à l'emplacement 2,2 du tableau, a une valeur.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### Code C++ pour accéder à la table à partir de la cellule et ajouter des valeurs à l'intérieur en utilisant des décalages de ligne et de colonne  

Le code d'exemple suivant charge le fichier Excel source tel que montré dans la capture d'écran ci-dessus et ajoute des valeurs à l'intérieur du tableau, puis génère le fichier Excel de sortie tel qu'indiqué ci-dessus.  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from source Excel file
    Workbook workbook(srcDir + u"source.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell D5 which lies inside the table
    Cell cell = worksheet.GetCells().Get(u"D5");

    // Put value inside the cell D5
    cell.PutValue(u"D5 Data");

    // Access the Table from this cell
    ListObject table = cell.GetTable();

    // Add some value using Row and Column Offset
    table.PutCellValue(2, 2, u"Offset [2,2]");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```  
