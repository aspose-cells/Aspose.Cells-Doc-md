---
title: Возврат диапазона значений с помощью AbstractCalculationEngine
type: docs
weight: 55
url: /ru/net/returning-a-range-of-values-using-abstractcalculationengine/
---
{{% alert color="primary" %}}

 Aspose.Cells предоставляет[**АннотацияРасчетДвигатель**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) класс, который используется для реализации пользовательских или пользовательских функций, которые не поддерживаются Microsoft Excel как встроенные функции.

 В этой статье объясняется, как вернуть диапазон значений из[**АннотацияРасчетДвигатель**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{% /alert %}}

 Следующий код демонстрирует использование[**АннотацияРасчетДвигатель**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) class и возвращает диапазон значений через свой метод.

Создайте класс с функцией*ВычислитьПользовательскуюФункция*. Этот класс реализует[**АннотацияРасчетДвигатель**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-CustomFunctionStaticValue.cs" >}}

Теперь используйте вышеуказанную функцию в своей программе.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingAbstractCalculationEngine-1.cs" >}}
