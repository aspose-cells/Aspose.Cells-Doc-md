---
title: Возвращение Диапазона Значений с Использованием AbstractCalculationEngine
type: docs
weight: 275
url: /ru/java/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет класс [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine), который используется для реализации определяемых пользователем или пользовательских функций, которые не поддерживаются Microsoft Excel в качестве встроенных функций.

В данной статье будет объяснено, как вернуть диапазон значений из [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{% /alert %}}

Приведенный ниже код демонстрирует использование [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) и возвращает диапазон значений через его метод.

Создайте класс с функцией *CalculateCustomFunction*. Этот класс расширяет [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Теперь используйте указанную выше функцию в своей программе.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ReturningRangeOfValues-1.java" >}}
{{< app/cells/assistant language="java" >}}
