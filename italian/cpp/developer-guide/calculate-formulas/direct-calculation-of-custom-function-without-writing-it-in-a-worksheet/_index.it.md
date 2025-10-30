---
title: Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro con C++
linktitle: Calcolo diretto della funzione personalizzata
description: Questo articolo introduce come utilizzare la libreria Aspose.Cells per calcolare direttamente le funzioni personalizzate in Microsoft Excel senza scriverle nel foglio di lavoro. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare i metodi forniti da Aspose.Cells per calcolare la funzione personalizzata e ottenere il risultato. Alla fine, salviamo il file Excel modificato sul disco.
keywords: Aspose.Cells, Excel, funzioni personalizzate, calcoli diretti, non c è bisogno di scrivere, fogli di lavoro
type: docs
weight: 90
url: /it/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Calcolo diretto della funzione personalizzata senza scriverla in un foglio di lavoro**

Questo argomento spiega come calcolare direttamente le proprie funzioni personalizzate senza prima scriverle in un foglio di lavoro. Utilizzare il metodo [**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) a questo scopo.

Vedi il seguente esempio di codice che illustra l'uso di questo metodo. Abbiamo utilizzato una funzione personalizzata chiamata MyCompany::CustomFunction() e calcoliamo il suo valore come "Aspose.Cells." manually, e questo valore viene automaticamente concatenato con il valore della cella A1, che è "Benvenuto in ", tramite il motore di calcolo. Il valore finale calcolato viene restituito come "Benvenuto in Aspose.Cells.". Come puoi vedere nel codice, non abbiamo scritto la nostra funzione personalizzata da nessuna parte in un foglio di lavoro ed è calcolata direttamente dalla nostra logica personalizzata.

### **Esempio di programmazione**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class ICustomEngine : public AbstractCalculationEngine
{
public:
    void Calculate(CalculationData& data) override
    {
        // Check the formula name and calculate it yourself
        if (data.GetFunctionName() == u"MyCompany.CustomFunction")
        {
            // This is our calculated value
            data.SetCalculatedValue(Aspose::Cells::Object(u"Aspose.Cells."));
        }
    }
};

class ImplementDirectCalculationOfCustomFunction
{
public:
    static void Run()
    {
        Aspose::Cells::Startup();

        // Create a workbook
        Workbook wb;

        // Access first worksheet
        Worksheet ws = wb.GetWorksheets().Get(0);

        // Add some text in cell A1
        ws.GetCells().Get(u"A1").PutValue(u"Welcome to ");

        // Create a calculation options with custom engine
        CalculationOptions opts;
        opts.SetCustomEngine(new ICustomEngine());

        // This line shows how you can call your own custom function without
        // a need to write it in any worksheet cell
        // After the execution of this line, it will return
        // Welcome to Aspose.Cells.
        Aspose::Cells::Object ret = ws.CalculateFormula(u"=A1 & MyCompany.CustomFunction()", opts);

        // Print the calculated value on Console
        std::cout << "Calculated Value: " << ret.ToString().ToUtf8() << std::endl;

        Aspose::Cells::Cleanup();
    }
};

int main()
{
    ImplementDirectCalculationOfCustomFunction::Run();
    return 0;
}
```

### **Output della console**

Di seguito è riportato l'output della console del codice di esempio sopra.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Articolo correlato**

{{% alert color="primary" %}}

[Implementa motore di calcolo personalizzato per estendere il motore di calcolo predefinito di Aspose.Cells](/cells/it/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
