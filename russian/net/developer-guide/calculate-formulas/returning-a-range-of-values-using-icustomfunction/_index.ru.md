---
title: Возврат диапазона значений с помощью ICustomFunction
type: docs
weight: 50
url: /ru/net/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) устарел с момента выпуска Aspose.Cells for Java 20.8. Пожалуйста, используйте[**АннотацияРасчетДвигатель**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) учебный класс. Использование[**АннотацияРасчетДвигатель**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) класс описан в следующей статье.

[Возврат диапазона значений с помощью AbstractCalculationEngine](/cells/ru/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells предоставляет[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)интерфейс, который используется для реализации пользовательских или пользовательских функций, которые не поддерживаются Microsoft Excel как встроенные функции.

 В основном, когда вы реализуете[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) метод интерфейса, вам нужно вернуть одно значение ячейки. Но иногда вам нужно вернуть диапазон значений. В этой статье объясняется, как вернуть диапазон значений из[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

 Следующий код реализует[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)и возвращает диапазон значений через свой метод.

 Создайте класс с функцией*ВычислитьПользовательскуюФункция*. Этот класс реализует[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Теперь используйте вышеуказанную функцию в своей программе.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
