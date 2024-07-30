---
title: Работа с пользовательским вычислительным движком для GridJs
type: docs
weight: 250
url: /ru/java/aspose-cells-gridjs/how-to-use-custom-calculation-engine/
keywords: GridJs,custom,calculation,customcalculation
description: В этой статье описывается, как использовать пользовательский вычислительный движок для библиотеки Aspose.Cells.GridJs.
aliases:
  - /java/aspose-cells-gridjs/customcalculation/
  - /java/aspose-cells-gridjs/work-with-custom-calculation-engine/
---

## **Реализация пользовательского расчетного движка**

Aspose.Cells.GridJs имеет мощный вычислительный движок, который может вычислять практически все формулы Microsoft Excel. Несмотря на это, он также позволяет расширить основной вычислительный движок, что обеспечивает большую мощность и гибкость.

Следующие свойства и классы используются при реализации этой функции.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridcalculationdata)

Приведенный ниже код реализует пользовательский расчетный движок. Он реализует интерфейс [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine), у которого есть метод [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate). Этот метод вызывается для всех ваших формул. Внутри этого метода мы захватываем формулу **MYTESTFUNC** и умножаем ее на 2 для значения ее первого параметра.

### **Пример программирования**

```JAVA
class MyCalculation : GridAbstractCalculationEngine
        {
           public override void calculate(GridCalculationData data)
            {
                if (!"MYTESTFUNC".Equals(data.FunctionName.ToUpper()))
                {
                    return;
                }
                data.CalculatedValue = (decimal)(2.0 * (double)data.GetParamValue(0));
            }
        }
// in the startup.cs when you do initialization ,set the CalculateEngine		
  MyCalculation ce = new MyCalculation();
  GridJsWorkbook.CalculateEngine = ce;

```
