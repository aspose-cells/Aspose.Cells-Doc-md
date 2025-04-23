---
title: Fonction de consolidation avec C++
linktitle: Fonction de consolidation
type: docs
weight: 20
url: /fr/cpp/consolidation-function/
description: Apprenez comment appliquer ConsolidationFunction aux champs de données d un tableau croisé dynamique à l aide d Aspose.Cells avec C++.
---

## **Fonction de consolidation**

Aspose.Cells peut être utilisé pour appliquer la fonction de consolidation aux champs de données (ou aux champs de valeur) du tableau croisé dynamique. Dans Microsoft Excel, vous pouvez cliquer avec le bouton droit sur le champ de valeur, puis sélectionner l'option **Paramètres du champ de valeur...** et ensuite sélectionner l'onglet **Recapituler les valeurs par**. À partir de là, vous pouvez sélectionner n'importe quelle fonction de consolidation de votre choix comme Somme, Nombre, Moyenne, Max, Min, Produit, Nombre distinct, etc.

Aspose.Cells fournit une énumération [**ConsolidationFunction**](https://reference.aspose.com/cells/cpp/aspose.cells/consolidationfunction/) pour prendre en charge les fonctions de consolidation suivantes.

- ConsolidationFunction::Moyenne
- ConsolidationFunction::Compte
- ConsolidationFunction::CountNums
- ConsolidationFunction::CompteDistincts
- ConsolidationFunction::Max
- ConsolidationFunction::Min
- ConsolidationFunction::Produit
- ConsolidationFunction::StdDev
- ConsolidationFunction::StdDevp
- ConsolidationFunction::Somme
- ConsolidationFunction::Var
- ConsolidationFunction::Varp

### **Application de la fonction de consolidation aux champs de données d'un tableau croisé dynamique**

Le code suivant applique la fonction de consolidation **Moyenne** au premier champ de données (ou champ de valeur) et la fonction de consolidation **Nombre distinct** au deuxième champ de données (ou champ de valeur).

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook from source excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table of the worksheet
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Apply Average consolidation function to first data field
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Average);

    // Apply DistinctCount consolidation function to second data field
    pivotTable.GetDataFields().Get(1).SetFunction(ConsolidationFunction::DistinctCount);

    // Calculate the data to make changes affect
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

La fonction de consolidation ComptageDistinct est prise en charge uniquement par Microsoft Excel 2013.

{{% /alert %}}
