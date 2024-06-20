---
title: Возврат диапазона значений с помощью ICustomFunction
type: docs
weight: 270
url: /ru/java/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) устарел с выходом Aspose.Cells for Java 20.8. Используйте класс [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine). Использование класса [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) описано в следующей статье.

[Возвращение Диапазона Значений с использованием AbstractCalculationEngine](/cells/ru/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells предоставляет интерфейс [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction), который используется для реализации пользовательских или пользовательских функций, которые не поддерживаются Microsoft Excel в качестве встроенных функций.

В основном, когда вы реализуете метод интерфейса [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction), вам необходимо возвращать значение одной ячейки. Но иногда вам нужно вернуть диапазон значений. В этой статье будет объяснено, как вернуть диапазон значений из [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}}

## **Возврат диапазона значений с использованием ICustomFunction**

Приведенный ниже код реализует [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) и возвращает диапазон значений через его метод. Пожалуйста, проверьте [файл Excel вывода](5472922.xlsx) и [pdf](5472925.pdf), сгенерированный с помощью кода в качестве справки.

Создайте класс с функцией *CalculateCustomFunction*. Этот класс реализует [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Теперь используйте указанную выше функцию в своей программе.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
