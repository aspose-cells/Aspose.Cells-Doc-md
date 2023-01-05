---
title: Реализовать пользовательский механизм расчета, чтобы расширить механизм расчета по умолчанию Aspose.Cells.
type: docs
weight: 80
url: /ru/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---
## **Реализовать пользовательский механизм расчета**

Aspose.Cells имеет мощный вычислительный механизм, который может вычислять почти все формулы Microsoft Excel. Несмотря на это, он также позволяет расширить механизм расчета по умолчанию, что обеспечивает большую мощность и гибкость.

При реализации этой функции используются следующие свойства и классы.

- **[CalculationOptions.CustomEngine](https://reference.aspose.com/cells/net/aspose.cells/calculationoptions/properties/customengine)**
- **[AbstractCalculationEngine] (https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)**
- **[Данные расчета] (https://reference.aspose.com/cells/net/aspose.cells/calculationdata)**

Следующий код реализует пользовательский механизм вычислений. Он реализует интерфейс**[AbstractCalculationEngine] (https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine)** который имеет**[Рассчитать (данные CalculationData)] (https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/methods/calculate)** метод. Этот метод вызывается для всех ваших формул. Внутри этого метода мы фиксируем**Сумма** формуле и увеличивает ее значение на 30. Таким образом, если вычисленное значение Aspose.Cells равно 20, то наш пользовательский движок сделает его равным 50, добавив 30.

### **Образец программирования**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ImplementCustomCalculationEngine-ImplementCustomCalculationEngine.cs" >}}

### **Консольный вывод**

Вот вывод консоли приведенного выше примера кода.

{{< highlight "java" >}}

Without Custom Engine Value of A1: 20

With Custom Engine Value of A1: 50

{{< /highlight >}}

### **Связанная статья**

{{% alert color="primary" %}}

[Прямой расчет пользовательской функции без записи ее на листе](/cells/ru/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
