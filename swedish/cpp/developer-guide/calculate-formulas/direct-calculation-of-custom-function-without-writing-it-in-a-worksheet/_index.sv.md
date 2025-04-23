---
title: Direktberäkning av anpassad funktion utan att skriva den i ett kalkylblad med C++
linktitle: Direktberäkning av anpassad funktion
description: Den här artikeln introducerar hur man använder Aspose.Cells biblioteket för att direkt beräkna anpassade funktioner i Microsoft Excel utan att skriva funktionen i en arbetsbok. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi använda de metoder som tillhandahålls av Aspose.Cells för att beräkna den anpassade funktionen och få resultatet. Slutligen sparar vi den modifierade Excel filen på disk.
keywords: Aspose.Cells, Excel, anpassade funktioner, direkt beräkning, ingen anledning att skriva, arbetsböcker
type: docs
weight: 90
url: /sv/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Direktberäkning av anpassad funktion utan att skriva den i ett kalkylblad**

Denna artikel förklarar hur du kan direkt beräkna dina anpassade funktioner utan att först skriva dem i ett kalkylblad. Använd metod [**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) för detta ändamål.

Vänligen se följande exempel kod som illustrerar användningen av denna metod. Vi har använt en anpassad funktion som heter MyCompany::CustomFunction() och vi beräknar dess värde som "Aspose.Cells." själva och sedan kombineras detta automatiskt med värdet av cell A1 som är "Välkommen till" av beräkningsmotorn och det slutgiltiga beräknade värdet returneras som "Välkommen till Aspose.Cells.". Som du kan se i koden har vi inte skrivit vår anpassade funktion någonstans i ett kalkylblad och den beräknas direkt av vår egen anpassade logik.

### **Programmeringsexempel**

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

### **Konsoloutput**

Nedan är konsol utmatningen av ovanstående provkod.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Relaterad artikel**

{{% alert color="primary" %}}

[Implementera anpassad beräkningsmotor för att utöka den standardmässiga beräkningsmotorn för Aspose.Cells](/cells/sv/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
