---
title: Calcul de la fonction IFNA en utilisant Aspose.Cells avec C++
linktitle: Calcul de la fonction IFNA
description: Comment calculer les fonctions IFNA en utilisant la bibliothèque Aspose.Cells avec C++. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour calculer la fonction IFNA et obtenir le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, fonctions IFNA, calculs, C++
type: docs
weight: 40
url: /fr/cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells prend en charge le calcul de la fonction Excel IFNA. La fonction IFNA renvoie la valeur que vous spécifiez si la formule renvoie la valeur d'erreur #N/A ; sinon, elle renvoie le résultat de la formule.

{{% /alert %}} 

## **Calcul de la fonction SIERREUR en utilisant Aspose.Cells**
Le code d'exemple suivant illustre le calcul de la fonction IFNA par Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create new workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add data for VLOOKUP
    worksheet.GetCells().Get(u"A1").PutValue(u"Apple");
    worksheet.GetCells().Get(u"A2").PutValue(u"Orange");
    worksheet.GetCells().Get(u"A3").PutValue(u"Banana");

    // Access cell A5 and A6
    Cell cellA5 = worksheet.GetCells().Get(u"A5");
    Cell cellA6 = worksheet.GetCells().Get(u"A6");

    // Assign IFNA formula to A5 and A6
    cellA5.SetFormula(u"=IFNA(VLOOKUP(\"Pear\",$A$1:$A$3,1,0),\"Not found\")");
    cellA6.SetFormula(u"=IFNA(VLOOKUP(\"Orange\",$A$1:$A$3,1,0),\"Not found\")");

    // Calculate the formula of workbook
    workbook.CalculateFormula();

    // Print the values of A5 and A6
    std::cout << cellA5.GetStringValue().ToUtf8() << std::endl;
    std::cout << cellA6.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sortie console**
Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

Not found

Orange

{{< /highlight >}}
