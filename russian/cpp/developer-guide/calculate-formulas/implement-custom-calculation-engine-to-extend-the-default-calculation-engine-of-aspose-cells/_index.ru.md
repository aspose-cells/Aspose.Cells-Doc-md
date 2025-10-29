---
title: Реализуйте пользовательский движок расчетов для расширения стандартного движка Aspose.Cells с помощью C++
linktitle: Реализуйте пользовательский движок расчетов
description: Эта статья описывает, как расширить стандартный движок расчетов, реализовав пользовательский движок расчета с помощью Aspose.Cells и C++. Загружая существующий файл Excel или создавая новый, мы можем использовать предоставленные Aspose.Cells методы для реализации пользовательского движка расчетов и получения результатов. В конце мы сохраняем изменённый файл Excel на диск.
keywords: Aspose.Cells, Excel, пользовательский движок расчетов, расширяет стандартный движок, C++
type: docs
weight: 80
url: /ru/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Реализация пользовательского расчетного движка**

Aspose.Cells имеет мощный расчетный механизм, который может рассчитывать практически все формулы Microsoft Excel. Тем не менее, он также позволяет вам расширять стандартный расчетный механизм для обеспечения вам большей мощности и гибкости.

Следующие свойства и классы используются при реализации этой функции.

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationdata/)

Приведенный ниже код реализует пользовательский расчетный движок. Он реализует интерфейс [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/), который имеет метод [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/). Этот метод вызывается для всех ваших формул. Внутри этого метода мы захватываем функцию **TODAY** и добавляем один день к системной дате. Таким образом, если текущая дата - 27/07/2023, то пользовательский движок будет рассчитывать TODAY() как 28/07/2023.

### **Пример программирования**

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

### **Результат**

Пожалуйста, проверьте вывод консоли приведенного выше образца кода, значение (дата/время) ячейки A1 с пользовательским движком должно быть на один день позже, чем результат без пользовательского движка.

### **Связанная статья**

{{% alert color="primary" %}}

[Прямое вычисление пользовательской функции без её записи в лист](/cells/ru/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
