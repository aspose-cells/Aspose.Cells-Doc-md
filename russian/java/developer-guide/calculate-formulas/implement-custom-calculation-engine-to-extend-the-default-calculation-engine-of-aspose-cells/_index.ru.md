---
title: Внедрите пользовательский механизм вычислений, чтобы расширить механизм вычислений по умолчанию Aspose.Cells.
type: docs
weight: 590
url: /ru/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells имеет мощный вычислительный механизм, позволяющий рассчитывать почти все формулы Microsoft Excel. Несмотря на это, он также позволяет вам расширить механизм вычислений по умолчанию, что обеспечивает большую мощность и гибкость.

При реализации этой функции используются следующие свойства и классы.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [АннотацияРасчетДвигатель](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [Расчетные данные](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
##  **Внедрение пользовательского механизма вычислений**
Следующий код реализует пользовательский механизм вычислений. Он реализует интерфейс[АннотацияРасчетДвигатель](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) который имеет только один метод[calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Этот метод вызывается для всех ваших формул. Внутри этого метода мы фиксируем**TODAY** функцию и добавьте один день к системной дате. Таким образом, если текущая дата — 27.07.2023, то пользовательский механизм рассчитает TODAY() как 28.07.2023.

###  **Пример программирования**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

###  **Результат**

Пожалуйста, проверьте вывод консоли приведенного выше примера кода: значение (дата и время) A1 с пользовательским механизмом должно быть на один день позже, чем результат без специального механизма.

###  **Связанная статья**
{{% alert color="primary" %}} 

- [Прямой расчет пользовательской функции без записи ее на листе](/cells/ru/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
