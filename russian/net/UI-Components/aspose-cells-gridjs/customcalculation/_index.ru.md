---
title: Работа с пользовательским вычислительным движком для GridJs
type: docs
weight: 250
url: /ru/net/aspose-cells-gridjs/customcalculation/
keywords: GridJs,custom,calculation,customcalculation
description: В этой статье описывается, как использовать пользовательский вычислительный движок для библиотеки Aspose.Cells.GridJs.
---

## **Реализация пользовательского расчетного движка**

Aspose.Cells.GridJs имеет мощный вычислительный движок, который может вычислять практически все формулы Microsoft Excel. Несмотря на это, он также позволяет расширить основной вычислительный движок, что обеспечивает большую мощность и гибкость.

Следующие свойства и классы используются при реализации этой функции.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridcalculationdata)

Приведенный ниже код реализует пользовательский расчетный движок. Он реализует интерфейс [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine), у которого есть метод [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/gridabstractcalculationengine/methods/calculate). Этот метод вызывается для всех ваших формул. Внутри этого метода мы захватываем формулу **MYTESTFUNC** и умножаем ее на 2 для значения ее первого параметра.

### **Пример программирования**

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "CustomCalculation.cs" >}}

