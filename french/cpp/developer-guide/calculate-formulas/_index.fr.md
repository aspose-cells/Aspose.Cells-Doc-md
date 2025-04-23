---
title: Calcul des formules avec C++
linktitle: Calcul des formules
description: Cet article présente comment utiliser la bibliothèque Aspose.Cells pour calculer des formules dans Microsoft Excel avec C++. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour calculer la formule et obtenir le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, formules, calculs, Calcul direct de formule, Calcul des formules à plusieurs reprises, ajouter des formules.
type: docs
weight: 125
url: /fr/cpp/calculate-formulas/
---

## **Ajout de formules et calcul de résultats**

Aspose.Cells dispose d’un moteur de calcul de formules intégré. Il peut non seulement recalculer les formules importées à partir de modèles de conception, mais également supporter le calcul des résultats des formules ajoutées en temps réel.

Aspose.Cells supporte la plupart des formules ou fonctions qui font partie de Microsoft Excel (Consultez [la liste des fonctions supportées par le moteur de calcul](/cells/fr/cpp/supported-formula-functions/)). Ces fonctions peuvent être utilisées via les API ou dans les feuilles de conception. Aspose.Cells supporte un ensemble énorme de formules mathématiques, de chaînes, booléennes, de date/heure, statistiques, base de données, recherche, et de référence.

Utilisez la propriété [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/) ou les méthodes [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/) de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) pour ajouter une formule à une cellule. Lors de l’application d’une formule, commencez toujours la chaîne par un signe égal (=), comme lors de la création d’une formule dans Microsoft Excel, et utilisez une virgule (,) pour délimiter les paramètres des fonctions.

Pour calculer les résultats des formules, l’utilisateur peut appeler la méthode [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) de la classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), qui traite toutes les formules intégrées dans un fichier Excel. Ou, il peut appeler la méthode [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) de la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/), qui traite toutes les formules intégrées dans une feuille. Ou, l’utilisateur peut également appeler la méthode [**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/) de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/), qui traite la formule d’une seule cellule :

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add values to cells
    worksheet.GetCells().Get(u"A1").PutValue(1);
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(3);

    // Add a SUM formula to cell A4
    worksheet.GetCells().Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Calculate the results of formulas
    workbook.CalculateFormula();

    // Get the calculated value of cell A4
    U16String value = worksheet.GetCells().Get(u"A4").GetStringValue();

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Important à savoir pour les formules**

{{% alert color="primary" %}}

La propriété **GetFormula** et les méthodes **SetFormula(...)** de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) fonctionnent différemment des méthodes **Calculate** des classes [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/), et [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). La propriété **GetFormula** et les méthodes **SetFormula(...)** ajoutent simplement la formule à une cellule mais ne calculent pas le résultat à l’exécution. Pour obtenir le résultat des formules, veuillez appeler les méthodes **Calculate**.

{{% /alert %}}

## **Calcul direct de formule**

Aspose.Cells possède un moteur de calcul de formules intégré. En plus de calculer les formules importées à partir d'un fichier, Aspose.Cells peut calculer les résultats des formules directement.

Parfois, vous souhaitez calculer directement les résultats des formules sans les ajouter dans une feuille de calcul. Les valeurs des cellules utilisées dans la formule existent déjà dans une feuille, et tout ce que vous avez à faire est de trouver le résultat de ces valeurs en utilisant une formule Microsoft Excel sans ajouter la formule dans une feuille.

Vous pouvez utiliser les API du moteur de calcul de formules d'Aspose.Cells pour [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) à [**calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) pour obtenir les résultats de telles formules sans les ajouter dans la feuille :

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

    // Create a workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put 20 in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.PutValue(20);

    // Put 30 in cell A2
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.PutValue(30);

    // Calculate the Sum of A1 and A2
    Aspose::Cells::Object results = worksheet.CalculateFormula(u"=Sum(A1:A2)");

    // Print the output
    std::cout << "Value of A1: " << cellA1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Value of A2: " << cellA2.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Result of Sum(A1:A2): " << results.ToString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

Le code ci-dessus produit la sortie suivante :
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Comment calculer des formules de manière répétée**

Lorsqu'il y a beaucoup de formules dans le classeur et que l'utilisateur doit les calculer à plusieurs reprises en modifiant uniquement une petite partie d'entre elles, il peut être utile pour la performance d'activer la chaîne de calcul des formules : [**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/cpp/aspose.cells/formulasettings/getenablecalculationchain/).

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the template workbook
    Workbook workbook(srcDir + u"book1.xls");

    // Print the time before formula calculation
    auto start = std::chrono::system_clock::now();
    std::time_t start_time = std::chrono::system_clock::to_time_t(start);
    std::cout << "Start time: " << std::ctime(&start_time);

    // Set the CreateCalcChain as true
    workbook.GetSettings().GetFormulaSettings().SetEnableCalculationChain(true);

    // Calculate the workbook formulas
    workbook.CalculateFormula();

    // Print the time after formula calculation
    auto end = std::chrono::system_clock::now();
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);
    std::cout << "End time: " << std::ctime(&end_time);

    // Change the value of one cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"newvalue");

    // Re-calculate those formulas which depend on cell A1
    workbook.CalculateFormula();

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Important à savoir**

{{% alert color="primary" %}}

Par défaut, la chaîne de calcul est désactivée. La création de la chaîne demande également du temps supplémentaire, et la première fois que vous calculez des formules ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)) peut consommer plus de temps processeur et de mémoire par rapport au calcul des formules sans chaîne. Si l'utilisateur n'a pas besoin de recalculer fréquemment, le comportement par défaut (calculer la formule directement sans créer de chaîne de calcul) est la meilleure option.

{{% /alert %}}

## **Sujets avancés**
- [Ajouter des cellules à la fenêtre de surveillance des formules Microsoft Excel](/cells/fr/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Calcul de la fonction SIERREUR en utilisant Aspose.Cells](/cells/fr/cpp/calculating-ifna-function-using-aspose-cells/)
- [Calcul de la formule de tableau de données](/cells/fr/cpp/calculation-of-array-formula-of-data-tables/)
- [Calcul des fonctions MINIFS et MAXIFS d'Excel 2016](/cells/fr/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Réduire le temps de calcul de la méthode Cell.Calculate](/cells/fr/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Calcul direct d'une fonction personnalisée sans l'écrire dans une feuille de calcul](/cells/fr/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implémenter un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut d'Aspose.Cells](/cells/fr/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Retourner une plage de valeurs en utilisant AbstractCalculationEngine](/cells/fr/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Définir le mode de calcul de formule du classeur](/cells/fr/cpp/setting-formula-calculation-mode-of-workbook/)
- [Utilisation de la fonction FormulaText dans Aspose.Cells](/cells/fr/cpp/using-formulatext-function-in-aspose-cells/)
