---
title: Использование функции ICustomFunction
type: docs
weight: 20
url: /ru/cpp/using-icustomfunction-feature/
---
## **Вступление**
В этой статье рассказывается, как использовать функцию ICustomFunction для реализации пользовательских функций с помощью API Aspose.Cells.

Интерфейс ICustomFunction позволяет добавлять пользовательские функции расчета формул для расширения основного механизма расчета Aspose.Cells для удовлетворения определенных требований. Эта функция полезна для определения пользовательских (определяемых пользователем) функций в файле шаблона или в коде, где пользовательская функция может быть реализована и оценена с использованием Aspose.Cells API, как и любая другая функция Excel по умолчанию Microsoft.
## **Использование функции ICustomFunction**
В следующем примере кода реализован интерфейс ICustomFunction, который оценивает и возвращает значения двух пользовательских функций, т. е. MySampleFunc() и YourSampleFunc(). Эти пользовательские функции находятся внутри ячеек A1 и A2 соответственно. Затем он вызывает метод IWorkbook.CalculateFormula(false, ICustomFunction), чтобы вызвать реализацию метода ICustomFunction.CalculateCustomFunction(). Затем он выводит на консоль значения A1 и A2, которые на самом деле являются значениями, возвращаемыми функцией ICustomFunction.CalculateCustomFunction(). Дополнительные сведения см. в выводе примера кода на консоль ниже.
## **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Formulas-UsingICustomFunctionFeature.cpp" >}}


## **Консольный вывод**
{{< highlight "java" >}}

 Value of A1: MY sample function was called successfully.

Value of A2: YOUR sample function was called successfully.

{{< /highlight >}}
