---
title: Работа с пользовательским расчетным движком
type: docs
weight: 70
url: /ru/net/working-with-custom-calculation-engine/
---
## **Реализовать пользовательский механизм расчета**

Aspose.Cells.Gridweb имеет мощный механизм вычислений, который может вычислять почти все формулы Microsoft Excel. Несмотря на это, он также позволяет расширить механизм расчета по умолчанию, что обеспечивает большую мощность и гибкость.

При реализации этой функции используются следующие свойства и классы.

 
- **[GridAbstractCalculationEngine] (https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)**
- **[GridCalculationData] (https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridcalculationdata)**

Следующий код реализует пользовательский механизм вычислений. Он реализует интерфейс**[GridAbstractCalculationEngine] (https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine)** который имеет**[Рассчитать (данные GridCalculationData)] (https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate)** метод. Этот метод вызывается для всех ваших формул. Внутри этого метода мы фиксируем**МАЙТЕСТФУНК** формулу и умножить на 2 значение первого параметра.

### **Образец программирования**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

