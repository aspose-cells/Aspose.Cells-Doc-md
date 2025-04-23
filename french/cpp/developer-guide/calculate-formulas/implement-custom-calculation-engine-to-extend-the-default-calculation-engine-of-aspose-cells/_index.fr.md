---
title: Mettre en œuvre un moteur de calcul personnalisé pour étendre le moteur de calcul par défaut d Aspose.Cells avec C++
linktitle: Mettre en œuvre un moteur de calcul personnalisé
description: Cet article décrit comment étendre le moteur de calcul par défaut en implémentant un moteur de calcul personnalisé en utilisant la bibliothèque Aspose.Cells avec C++. En chargeant un fichier Excel existant ou en créant un nouveau, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour implémenter un moteur de calcul personnalisé et obtenir les résultats. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, moteur de calcul personnalisé, étend le moteur de calcul par défaut, C++
type: docs
weight: 80
url: /fr/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implémenter un moteur de calcul personnalisé**

Aspose.Cells dispose d'un puissant moteur de calcul qui peut calculer presque toutes les formules Microsoft Excel. Malgré cela, il vous permet également d'étendre le moteur de calcul par défaut, ce qui vous offre plus de puissance et de flexibilité.

La propriété et les classes suivantes sont utilisées pour implémenter cette fonctionnalité.

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationdata/)

Le code suivant implémente le moteur de calcul personnalisé. Il implémente l'interface [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) qui possède une méthode [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/). Cette méthode est appelée pour toutes vos formules. À l'intérieur de cette méthode, nous capturons la fonction **TODAY** et ajoutons un jour à la date système. Ainsi, si la date actuelle est le 27/07/2023, le moteur personnalisé calculera AUJOURDHUI() comme le 28/07/2023.

### **Exemple de programmation**

```c++
#include <iostream>
#include <cwctype>
#include "Aspose.Cells.h"
#include <chrono>

using namespace Aspose::Cells;

class CustomEngine : public AbstractCalculationEngine
{
public:
    void Calculate(CalculationData& data) override
    {
        U16String funcName = data.GetFunctionName();
        std::u16string upperName;
        for (int i = 0; i < funcName.GetLength(); ++i)
        {
            upperName.push_back(std::towupper(funcName[i]));
        }
		if (upperName == u"TODAY")
		{
			auto now = std::chrono::system_clock::now();
			std::time_t now_time = std::chrono::system_clock::to_time_t(now);
			std::tm local_tm;

#ifdef _WIN32
			localtime_s(&local_tm, &now_time);
#else
			localtime_r(&now_time, &local_tm);
#endif

            Date today{ local_tm.tm_year + 1900, local_tm.tm_mon + 1, local_tm.tm_mday };
			data.SetCalculatedValue(Date{ today.year, today.month, today.day + 1 });
		}
    }

    bool GetProcessBuiltInFunctions() override { return true; }
};

class ImplementCustomCalculationEngine
{
public:
    static void Run()
    {
        Workbook workbook;
        Worksheet sheet = workbook.GetWorksheets().Get(0);
        Cell a1 = sheet.GetCells().Get(u"A1");
        Style style = a1.GetStyle();
        style.SetNumber(14);
        a1.SetStyle(style);
        a1.SetFormula(u"=TODAY()");
        workbook.CalculateFormula();
        std::cout << "The value of A1 with default calculation engine: " << a1.GetStringValue().ToUtf8() << std::endl;
        CustomEngine engine;
        CalculationOptions opts;
        opts.SetCustomEngine(&engine);
        workbook.CalculateFormula(opts);
        std::cout << "The value of A1 with custom calculation engine: " << a1.GetStringValue().ToUtf8() << std::endl;
        std::cout << "Press any key to continue..." << std::endl;
        std::cin.get();
    }
};

int main()
{
    Aspose::Cells::Startup();
    ImplementCustomCalculationEngine::Run();
    Aspose::Cells::Cleanup();
    return 0;
}

```

### **Résultat**

Veuillez vérifier la sortie de la console du code d'échantillon ci-dessus, la valeur (date/heure) de A1 avec le moteur personnalisé devrait être un jour plus tard que le résultat sans le moteur personnalisé.

### **Article connexe**

{{% alert color="primary" %}}

[Calcul direct d'une fonction personnalisée sans l'écrire dans une feuille de calcul](/cells/fr/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
