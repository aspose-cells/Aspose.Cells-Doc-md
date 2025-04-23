---
title: Retourner une plage de valeurs en utilisant AbstractCalculationEngine avec C++
linktitle: Renvoyer une plage de valeurs en utilisant AbstractCalculationEngine
description: Cet article présente un moteur de calcul abstrait qui retourne une plage de valeurs dans Microsoft Excel en utilisant la bibliothèque Aspose.Cells avec C++. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour obtenir une plage de valeurs et retourner le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, un moteur de calcul abstrait qui renvoie une série de valeurs
type: docs
weight: 55
url: /fr/cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells fournit la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) qui est utilisée pour implémenter des fonctions définies par l'utilisateur ou personnalisées non prises en charge par Microsoft Excel en tant que fonctions intégrées.

Cet article expliquera comment renvoyer la plage de valeurs de [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/).

{{% /alert %}}

Le code suivant démontre l'utilisation de la classe [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) et retourne la plage de valeurs via sa méthode.

Créer une classe avec une fonction `CalculateCustomFunction`. Cette classe implémente [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomFunctionStaticValue : public AbstractCalculationEngine
{
public:
    void Calculate(CalculationData& data) override
    {
		Vector<Object> row1{Object(Date{2015, 6, 12, 10, 6, 30}) ,Object(2)};
        Vector<Object> row2{ Object(3.0) ,Object(U16String(u"Test")) };

        Vector<Vector<Object>> values{ row1 , row2 };

        // Create Object with the 2D Vector and set as calculated value
        Object calculatedValue(values);

        // Set the calculated value in the CalculationData object
        data.SetCalculatedValue(calculatedValue);
    }
};

```

Utilisez maintenant la fonction ci-dessus dans votre programme.

```c++
int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    Cell cell = cells.Get(0, 0);
    cell.SetArrayFormula(u"=MYFUNC()", 2, 2);

    Style style = cell.GetStyle();
    style.SetNumber(14);
    cell.SetStyle(style);

    CalculationOptions calculationOptions;

    // Create and set custom engine with proper memory management
    std::shared_ptr<CustomFunctionStaticValue> customEngine = 
        std::make_shared<CustomFunctionStaticValue>();
    calculationOptions.SetCustomEngine(customEngine.get());

    workbook.CalculateFormula(calculationOptions);

    workbook.GetSettings().GetFormulaSettings().SetCalculationMode(CalcModeType::Manual);
    workbook.Save(outDir + u"output_out.xlsx");
    workbook.Save(outDir + u"output_out.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
