---
title: Использование функции AbstractCalculationEngine
type: docs
weight: 20
url: /ru/cpp/using-abstractcalculationengine-feature/
---

## Функции все еще находятся в процессе разработки, поэтому оставайтесь на связи.


## **Введение**
Эта статья предоставляет понимание того, как использовать функцию [AbstractCalculationEngine](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) для реализации пользовательских функций с помощью API Aspose.Cells.

<!--

Интерфейс AbstractCalculationEngine позволяет добавлять пользовательские функции вычисления формул для расширения базового вычислительного движка Aspose.Cells, чтобы удовлетворить определенные требования. Эта функция полезна для определения пользовательских функций в файле шаблона или в коде, где пользовательская функция может быть реализована и оценена с использованием API Aspose.Cells, как любая другая функция для Microsoft Excel по умолчанию.
## **Использование функции AbstractCalculationEngine**
Следующий образец кода реализует интерфейс AbstractCalculationEngine, который вычисляет и возвращает значения двух пользовательских функций: MySampleFunc() и YourSampleFunc(). Эти пользовательские функции находятся в ячейках A1 и A2 соответственно. Затем он вызывает метод Workbook.CalculateFormula(const CalculationOptions& options) для вызова реализации функции AbstractCalculationEngine.Calculate(CalculationData& data). Затем он выводит значения A1 и A2 в консоль. Пожалуйста, обратитесь к выводу консоли образца кода ниже для получения более подробной справки.
## **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature-new.cpp" >}}


## **Вывод в консоль**
{{< highlight java >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
-->
