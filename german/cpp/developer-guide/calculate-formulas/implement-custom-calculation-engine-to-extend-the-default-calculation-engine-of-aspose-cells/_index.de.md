---
title: Implementieren Sie eine benutzerdefinierte Berechnungs Engine, um die Standard Berechnungs Engine von Aspose.Cells mit C++ zu erweitern
linktitle: Implementieren Sie eine benutzerdefinierte Berechnungs Engine
description: Dieser Artikel beschreibt, wie die Standard Berechnungs Engine durch die Implementierung einer benutzerdefinierten Berechnungs Engine mit der Aspose.Cells Bibliothek in C++ erweitert werden kann. Durch das Laden einer existierenden Excel Datei oder das Erstellen einer neuen Datei können wir die von Aspose.Cells bereitgestellten Methoden verwenden, um eine benutzerdefinierte Berechnungs Engine zu implementieren und die Ergebnisse zu erhalten. Schließlich speichern wir die modifizierte Excel Datei auf der Festplatte.
keywords: Aspose.Cells, Excel, benutzerdefinierte Berechnungs Engine, erweitert die Standard Berechnungs Engine, C++
type: docs
weight: 80
url: /de/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Benutzerdefinierten Berechnungsmotor implementieren**

Aspose.Cells verfügt über einen leistungsstarken Berechnungsmotor, der fast alle Microsoft Excel-Formeln berechnen kann. Trotzdem ermöglicht es Ihnen auch, den standardmäßigen Berechnungsmotor zu erweitern, was Ihnen mehr Leistung und Flexibilität bietet.

Die folgenden Eigenschaften und Klassen werden zur Umsetzung dieses Merkmals verwendet.

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationdata/)

Der folgende Code implementiert den benutzerdefinierten Berechnungsmotor. Er implementiert die Schnittstelle [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/), die eine Methode [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/) hat. Diese Methode wird für alle Formeln aufgerufen. Innerhalb dieser Methode erfassen wir die Funktion **TODAY** und fügen ein Tag zum Systemdatum hinzu. Wenn das aktuelle Datum beispielsweise der 27/07/2023 ist, berechnet der benutzerdefinierte Motor TODAY() als 28/07/2023.

### **Programmierbeispiel**

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

### **Ergebnis**

Bitte überprüfen Sie die Konsolenausgabe des obigen Beispielcodes, der Wert (Datum/Uhrzeit) von A1 mit benutzerdefiniertem Motor sollte einen Tag später sein als das Ergebnis ohne benutzerdefinierten Motor.

### **Verwandter Artikel**

{{% alert color="primary" %}}

[Direkte Berechnung einer benutzerdefinierten Funktion, ohne sie in einem Arbeitsblatt zu schreiben](/cells/de/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
