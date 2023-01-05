---
title: Реализовать пользовательский механизм расчета, чтобы расширить механизм расчета по умолчанию Aspose.Cells.
type: docs
weight: 590
url: /ru/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells имеет мощный вычислительный механизм, который может вычислять почти все формулы Microsoft Excel. Несмотря на это, он также позволяет расширить механизм расчета по умолчанию, что обеспечивает большую мощность и гибкость.

При реализации этой функции используются следующие свойства и классы.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [АннотацияРасчетДвигатель](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [РасчетДанные](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **Реализовать пользовательский механизм расчета**
Следующий код реализует пользовательский механизм вычислений. Он реализует интерфейс[АннотацияРасчетДвигатель](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) который имеет только один метод[вычислить (данные вычисления)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Этот метод вызывается для всех ваших формул. Внутри этого метода мы фиксируем**СУММА** формуле и увеличивает ее значение на 30. Таким образом, если вычисленное значение Aspose.Cells равно 20, то наш пользовательский движок сделает его равным 50, добавив 30.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}
## **Консольный вывод**
Вот вывод консоли приведенного выше примера кода.

{{< highlight "java" >}}

 Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}
## **Связанная статья**
{{% alert color="primary" %}} 

- [Прямой расчет пользовательской функции без записи ее на листе](/cells/ru/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
