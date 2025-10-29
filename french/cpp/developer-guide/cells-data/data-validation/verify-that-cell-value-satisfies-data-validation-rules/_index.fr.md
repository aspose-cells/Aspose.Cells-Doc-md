---
title: Vérifiez que la valeur de la cellule satisfait les règles de validation des données avec C++
linktitle: Vérifiez que la valeur de la cellule satisfait aux règles de validation des données
type: docs
weight: 210
url: /fr/cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Apprenez comment vérifier si la valeur d une cellule satisfait les règles de validation des données via l API Aspose.Cells for C++.
keywords: Obtenir la valeur de validation de la cellule, obtenir la valeur de validation de la cellule, vérifier si une valeur satisfait aux règles de validation des données appliquées à la cellule
---

{{% alert color="primary" %}} 

Microsoft Excel permet aux utilisateurs d'ajouter des règles de validation des données aux cellules. Par exemple, une validation décimale précise que seuls des nombres compris entre 10 et 20 peuvent être saisis. Si un utilisateur entre un autre nombre, Excel affiche un message d'erreur et lui demande d'entrer un nombre dans la plage correcte. Si vous copiez et collez un nombre, disons 3, dans la cellule, Excel ne lance pas de vérification de validation ni n'affiche de message d'erreur.

Parfois, il est nécessaire de vérifier si une valeur satisfait les règles de validation des données appliquées à la cellule de manière programmée. Dans le cas ci-dessus, par exemple, l'entrée devrait échouer.

{{% /alert %}} 

## **Introduction**
Aspose.Cells fournit la méthode [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) pour valider les valeurs des cellules par programmation. Si la valeur d'une cellule ne satisfait pas la règle de validation des données appliquée à cette cellule, elle retourne **False**, sinon **True**.

Le code d'exemple suivant illustre comment fonctionne la méthode [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/). D'abord, il entre la valeur 3 dans C1. Parce que cela ne satisfait pas la règle de validation des données, la méthode [Cell.GetValidationValue()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/) retourne **False**. Ensuite, il entre la valeur 15 dans C1. Parce que cette valeur satisfait la règle de validation des données, la méthode retourne **True**. De même, pour la valeur 30, il retourne **False**.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate the workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access Cell C1
    // Cell C1 has the Decimal Validation applied on it.
    // It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Enter 3 inside this cell
    // Since it is not between 10 and 20, it should fail the validation
    cell.PutValue(3);

    // Check if number 3 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 3 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 15 inside this cell
    // Since it is between 10 and 20, it should succeed the validation
    cell.PutValue(15);

    // Check if number 15 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 15 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 30 inside this cell
    // Since it is not between 10 and 20, it should fail the validation again
    cell.PutValue(30);

    // Check if number 30 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 30 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Sortie**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
