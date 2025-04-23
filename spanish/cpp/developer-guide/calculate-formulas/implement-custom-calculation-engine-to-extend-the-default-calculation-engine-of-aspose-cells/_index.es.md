---
title: Implementar motor de cálculo personalizado para extender el motor de cálculo predeterminado de Aspose.Cells con C++
linktitle: Implementar motor de cálculo personalizado
description: Este artículo describe cómo extender el motor de cálculo predeterminado implementando un motor de cálculo personalizado usando la biblioteca Aspose.Cells con C++. Al cargar un archivo de Excel existente o crear uno nuevo, podemos usar los métodos proporcionados por Aspose.Cells para implementar un motor de cálculo personalizado y obtener los resultados. Finalmente, guardamos el archivo de Excel modificado en disco.
keywords: Aspose.Cells, Excel, motor de cálculo personalizado, extiende el motor de cálculo predeterminado, C++
type: docs
weight: 80
url: /es/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implementar Motor de Cálculo Personalizado**

Aspose.Cells tiene un potente motor de cálculo que puede calcular casi todas las fórmulas de Microsoft Excel. A pesar de esto, también te permite extender el motor de cálculo predeterminado, lo que te brinda mayor potencia y flexibilidad.

Se utilizan las siguientes propiedades y clases para implementar esta funcionalidad.

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationdata/)

El siguiente código implementa el Motor de Cálculo Personalizado. Implementa la interfaz [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) que tiene un método [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/). Este método se llama para todas tus fórmulas. Dentro de este método, capturamos la función **TODAY** y añadimos un día a la fecha del sistema. Así que si la fecha actual es 27/07/2023, entonces el motor personalizado calculará TODAY() como 28/07/2023.

### **Ejemplo de Programación**

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

### **Resultado**

Por favor revisa la salida de consola del código de muestra anterior, el valor (fecha y hora) de A1 con el motor personalizado debería ser un día después del resultado sin el motor personalizado.

### **Artículo Relacionado**

{{% alert color="primary" %}}

[Cálculo directo de función personalizada sin escribirla en una hoja de cálculo](/cells/es/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
