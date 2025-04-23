---
title: Implementa il motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells con C++
linktitle: Implementa motore di calcolo personalizzato
description: Questo articolo descrive come estendere il motore di calcolo predefinito implementando un motore di calcolo personalizzato utilizzando la libreria Aspose.Cells con C++. Caricando un file Excel esistente o creando uno nuovo, possiamo usare i metodi forniti da Aspose.Cells per implementare un motore di calcolo personalizzato e ottenere i risultati. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, Motore di Calcolo Personalizzato, estende il motore di calcolo predefinito, C++
type: docs
weight: 80
url: /it/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implementare un Motore di Calcolo Personalizzato**

Aspose.Cells ha un potente motore di calcolo che può calcolare quasi tutte le formule di Microsoft Excel. Nonostante ciò, ti permette anche di estendere il motore di calcolo predefinito che ti offre maggiore potenza e flessibilità.

Le seguenti proprietà e classi vengono utilizzate nell'implementazione di questa funzionalità.

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationdata/)

Il seguente codice implementa il Motore di Calcolo Personalizzato. Implementa l'interfaccia [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) che ha un metodo [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/). Questo metodo viene chiamato per tutte le formule. All'interno di questo metodo, catturiamo la funzione **TODAY** e aggiungiamo un giorno alla data di sistema. Quindi, se la data corrente è il 27/07/2023, il motore personalizzato calcolerà TODAY() come 28/07/2023.

### **Esempio di programmazione**

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

### **Risultato**

Si prega di controllare l'output della console del codice di esempio sopra, il valore (data ora) di A1 con il motore personalizzato dovrebbe essere un giorno dopo rispetto al risultato senza il motore personalizzato.

### **Articolo correlato**

{{% alert color="primary" %}}

[Calcolo diretto di funzione personalizzata senza scriverla in un foglio di lavoro](/cells/it/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
