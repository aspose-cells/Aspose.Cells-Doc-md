---
title: Возврат диапазона значений с помощью ICustomFunction
type: docs
weight: 270
url: /ru/java/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) устарел с момента выпуска Aspose.Cells for Java 20.8. Пожалуйста, используйте[**АннотацияРасчетДвигатель**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) учебный класс. Использование[**АннотацияРасчетДвигатель**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) класс описан в следующей статье.

[Возврат диапазона значений с помощью AbstractCalculationEngine](/cells/ru/java/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells предоставляет[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)интерфейс, который используется для реализации пользовательских или пользовательских функций, которые не поддерживаются Microsoft Excel как встроенные функции.

 В основном, когда вы реализуете[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) метод интерфейса, вам нужно вернуть одно значение ячейки. Но иногда вам нужно вернуть диапазон значений. В этой статье объясняется, как вернуть диапазон значений из[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}}

## **Возврат диапазона значений с помощью ICustomFunction**

 Следующий код реализует[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) и возвращает диапазон значений через свой метод. Пожалуйста, проверьте[выходной файл excel](5472922.xlsx) и[пдф](5472925.pdf) сгенерированный с кодом для вашей справки.

Создайте класс с функцией*ВычислитьПользовательскуюФункция*. Этот класс реализует[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Теперь используйте вышеуказанную функцию в своей программе.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
