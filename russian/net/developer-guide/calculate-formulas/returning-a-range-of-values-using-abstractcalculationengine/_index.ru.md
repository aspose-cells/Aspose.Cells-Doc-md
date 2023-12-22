---
title: Возврат диапазона значений с помощью AbstractCalculationEngine
description: В этой статье представлена абстрактная вычислительная машина, которая возвращает диапазон значений в Excel Microsoft с использованием библиотеки Aspose.Cells. Загрузив существующий файл Excel или создав новый файл Excel, мы можем использовать методы, предоставленные Aspose.Cells, чтобы получить диапазон значений и вернуть результат. Наконец, мы сохраняем измененный файл Excel на диск.
keywords: Aspose.Cells, Excel, an abstract calculation engine that returns a series of values
type: docs
weight: 55
url: /ru/net/returning-a-range-of-values-using-abstractcalculationengine/
---
{{% alert color="primary" %}}

 Aspose.Cells обеспечивает[**АннотацияРасчетДвигатель**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) класс, который используется для реализации пользовательских или пользовательских функций, которые не поддерживаются Excel Microsoft как встроенные функции.

 В этой статье объясняется, как вернуть диапазон значений из[**АннотацияРасчетДвигатель**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{% /alert %}}

 Следующий код демонстрирует использование[**АннотацияРасчетДвигатель**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) class и возвращает диапазон значений через его метод.

Создайте класс с функцией *CalculateCustomFunction*. Этот класс реализует[**АннотацияРасчетДвигатель**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

Теперь используйте вышеуказанную функцию в своей программе.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
