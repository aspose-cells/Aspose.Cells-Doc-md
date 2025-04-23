---
title: Utiliser la fonction FormulaText dans Aspose.Cells avec C++
linktitle: Utiliser la fonction FormulaText
description: Cet article présente comment utiliser la fonction FormulaText dans la bibliothèque Aspose.Cells pour traiter les formules dans Microsoft Excel. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser la méthode fournie par Aspose.Cells pour obtenir et définir le texte de la formule de la cellule et obtenir le résultat. Enfin, nous sauvegardons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, fonctions FormulaText
type: docs
weight: 60
url: /fr/cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText est une fonction d'Excel 2013 et ultérieure. Elle n'est pas prise en charge par les versions précédentes comme Excel 2010 ou 2007, etc. Comme son nom l'indique, elle imprime le texte de la formule qui est présente dans une cellule donnée. Cet article vous montrera comment faire usage de cette fonction en utilisant Aspose.Cells.

{{% /alert %}} 

Le code d'exemple suivant montre l'utilisation de FormulaText avec Aspose.Cells. Le code écrit d'abord une formule dans la cellule A1, puis imprime le texte de la formule en utilisant FormulaText dans la cellule A2.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some formula in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.SetFormula(u"=Sum(B1:B10)");

    // Get the text of the formula in cell A2 using FORMULATEXT function
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.SetFormula(u"=FormulaText(A1)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Print the results of A2, It will now print the text of the formula inside cell A1
    std::cout << cellA2.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sortie console**
Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
