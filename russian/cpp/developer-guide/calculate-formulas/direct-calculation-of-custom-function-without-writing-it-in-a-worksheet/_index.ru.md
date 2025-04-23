---
title: Прямое вычисление пользовательской функции без её записи в лист с помощью C++
linktitle: Прямое вычисление пользовательской функции
description: Эта статья представляет, как использовать библиотеку Aspose.Cells для прямого расчета пользовательских функций в Microsoft Excel без записи функции в рабочем листе. Загружая существующий файл Excel или создавая новый файл Excel, мы можем использовать методы, предоставленные Aspose.Cells, для расчета пользовательской функции и получения результата. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, пользовательские функции, прямые расчеты, нет необходимости в написании, рабочие листы
type: docs
weight: 90
url: /ru/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Прямое вычисление пользовательской функции без её записи в лист**

Эта тема объясняет, как напрямую вычислить ваши пользовательские функции, не записывая их предварительно в лист. Пожалуйста, используйте метод [**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) для этой цели.

Посмотрите следующий пример кода, иллюстрирующий использование этого метода. Мы использовали пользовательскую функцию с именем MyCompany::CustomFunction() и самостоятельно вычисляем её значение как "Aspose.Cells." Тогда это значение автоматически конкатенируется с значением ячейки A1, которое равно "Welcome to " с помощью движка расчетов, и итоговое вычисленное значение возвращается как "Welcome to Aspose.Cells.". Как видно из кода, мы не записывали нашу пользовательскую функцию нигде в листе, и она вычисляется напрямую нашим собственным логикой.

### **Пример программирования**

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

### **Вывод в консоль**

Ниже приведен вывод консоли приведенного выше образца кода.

{{< highlight java >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Связанная статья**

{{% alert color="primary" %}}

[Реализация пользовательского движка расчетов для расширения стандартного движка Aspose.Cells](/cells/ru/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
