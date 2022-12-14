---
title: Возврат диапазона значений с помощью AbstractCalculationEngine
type: docs
weight: 275
url: /ru/java/returning-a-range-of-values-using-abstractcalculationengine/
---
{{% alert color="primary" %}}

 Aspose.Cells предоставляет[**АннотацияРасчетДвигатель**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) класс, который используется для реализации пользовательских или пользовательских функций, которые не поддерживаются Microsoft Excel как встроенные функции.

 В этой статье объясняется, как вернуть диапазон значений из[**АннотацияРасчетДвигатель**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{% /alert %}}

 Следующий код демонстрирует использование[**АннотацияРасчетДвигатель**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)и возвращает диапазон значений через свой метод.

Создайте класс с функцией*ВычислитьПользовательскуюФункция* . Этот класс расширяет[**АннотацияРасчетДвигатель**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Теперь используйте вышеуказанную функцию в своей программе.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ReturningRangeOfValues-1.java" >}}
