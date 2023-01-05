---
title: Работа с пользовательским механизмом расчета для GridJs
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/customcalculation/
description: В этой статье описывается, как использовать пользовательский механизм вычислений для библиотеки Aspose.Cells.GridJs.
---
## **Реализовать пользовательский механизм расчета**

Aspose.Cells.GridJs имеет мощный вычислительный механизм, который может вычислять почти все формулы Microsoft Excel. Несмотря на это, он также позволяет расширить механизм расчета по умолчанию, что обеспечивает большую мощность и гибкость.

При реализации этой функции используются следующие свойства и классы.

 
- **[GridAbstractCalculationEngine] (https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)**
- **[GridCalculationData] (https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)**

Следующий код реализует пользовательский механизм вычислений. Он реализует интерфейс**[GridAbstractCalculationEngine] (https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)** который имеет**[Рассчитать (данные GridCalculationData)] (https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate)** метод. Этот метод вызывается для всех ваших формул. Внутри этого метода мы фиксируем**МАЙТЕСТФУНК** формулу и умножить на 2 значение первого параметра.

### **Образец программирования**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}
 
