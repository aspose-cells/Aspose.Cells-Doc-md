---
title: Работа с пользовательским движком вычислений
type: docs
weight: 70
url: /ru/net/aspose-cells-gridweb/custom-calculation-engine/
keywords: GridWeb, custom, calculation, CalculationEngine, GridAbstractCalculationEngine
description: Эта статья объясняет, как использовать GridAbstractCalculationEngine для настройки процесса вычислений в GridWeb.
---

## **Реализация пользовательского расчетного движка**

Aspose.Cells.Gridweb имеет мощный расчетный движок, который может вычислить почти все формулы Microsoft Excel. Несмотря на это, он также позволяет расширить расчетный движок по умолчанию, что предоставляет большую мощность и гибкость.

Следующие свойства и классы используются при реализации этой функции.


- [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine)
- [**GridCalculationData**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridcalculationdata)

Приведенный ниже код реализует пользовательский расчетный движок. Он реализует интерфейс [**GridAbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine), у которого есть метод [**Calculate(GridCalculationData data)**](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridabstractcalculationengine/methods/calculate). Этот метод вызывается для всех ваших формул. Внутри этого метода мы захватываем формулу **MYTESTFUNC** и умножаем ее на 2 для значения ее первого параметра.

### **Пример программирования**

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-CustomCalculation.cs" >}}

