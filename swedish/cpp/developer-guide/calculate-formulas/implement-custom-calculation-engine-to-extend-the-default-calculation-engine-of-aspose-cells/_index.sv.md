---
title: Implementera anpassad beräkningsmotor för att utöka den standardmässiga beräkningsmotorn för Aspose.Cells med C++
linktitle: Implementera anpassad beräkningsmotor
description: Denna artikel beskriver hur du kan utöka den standardmässiga beräkningsmotorn genom att implementera en anpassad beräkningsmotor med Aspose.Cells biblioteket med C++. Genom att ladda en befintlig Excel fil eller skapa en ny kan vi använda metoderna som tillhandahålls av Aspose.Cells för att implementera en anpassad beräkningsmotor och få resultaten. Slutligen sparar vi den modifierade Excel filen till disk.
keywords: Aspose.Cells, Excel, Anpassad beräkningsmotor, utökar den standardmässiga beräkningsmotorn, C++
type: docs
weight: 80
url: /sv/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implementera anpassad beräkningsmotor**

Aspose.Cells har en kraftfull beräkningsmotor som kan beräkna nästan alla Microsoft Excel formler. Trots detta tillåter det dig också att utöka standardberäkningsmotorn vilket ger dig större kraft och flexibilitet.

Följande egenskap och klasser används vid implementering av denna funktion.

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationdata/)

Följande kod implementerar den anpassade beräkningsmotorn. Den implementerar gränssnittet [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) som har en [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/)-metod. Denna metod anropas mot alla dina formler. Inne i denna metod fångar vi **TODAY**-funktionen och lägger till en dag till systemdatumet. Så om dagens datum är 27/07/2023, kommer den anpassade motorn att beräkna TODAY() som 28/07/2023.

### **Programmeringsexempel**

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

### **Resultat**

Vänligen kolla konsolens utmatning av den ovanstående provkoden, värdet (datumtid) av A1 med anpassad motor bör vara en dag senare än resultatet utan anpassad motor.

### **Relaterad artikel**

{{% alert color="primary" %}}

[Direktberäkning av anpassad funktion utan att skriva den i ett kalkylblad](/cells/sv/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
