---
title: Реализация собственного расчетного механизма для расширения стандартного расчетного механизма Aspose.Cells
type: docs
weight: 590
url: /ru/java/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells имеет мощный расчетный механизм, который может рассчитывать практически все формулы Microsoft Excel. Тем не менее, он также позволяет вам расширять стандартный расчетный механизм для обеспечения вам большей мощности и гибкости.

Следующие свойства и классы используются при реализации этой функции.

- [CalculationOptions.CustomEngine](https://reference.aspose.com/cells/java/com.aspose.cells/calculationoptions#CustomEngine)
- [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)
- [CalculationData](https://reference.aspose.com/cells/java/com.aspose.cells/CalculationData)

{{% /alert %}} 
## **Реализация пользовательского расчетного движка**
Следующий код реализует Пользовательский Расчетный Движок. Он реализует интерфейс [AbstractCalculationEngine](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine), который имеет только один метод [calculate(CalculationData data)](https://reference.aspose.com/cells/java/com.aspose.cells/abstractcalculationengine#calculate\(com.aspose.cells.CalculationData\)). Этот метод вызывается для всех ваших формул. Внутри этого метода мы захватываем функцию **TODAY** и добавляем один день к системной дате. Таким образом, если текущая дата - 27/07/2023, то пользовательский движок будет рассчитывать TODAY() как 28/07/2023.

### **Пример программирования**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.java" >}}

### **Результат**

Пожалуйста, проверьте вывод консоли приведенного выше образца кода, значение (дата/время) ячейки A1 с пользовательским движком должно быть на один день позже, чем результат без пользовательского движка.

### **Связанная статья**
{{% alert color="primary" %}} 

- [Прямой расчет пользовательской функции без записи ее на лист](/cells/ru/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
