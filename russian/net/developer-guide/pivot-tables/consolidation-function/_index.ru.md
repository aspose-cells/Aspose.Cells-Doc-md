---
title: Функция консолидации
type: docs
weight: 20
url: /ru/net/consolidation-function/
---

## **Функция консолидации**

Aspose.Cells можно использовать для применения функции объединения к полям данных (или значениям) сводной таблицы. В Microsoft Excel вы можете щелкнуть правой кнопкой мыши на поле значения, затем выбрать опцию **Настройки поля значения...**, а затем выбрать вкладку **Сводные значения по**. Оттуда вы можете выбрать любую функцию объединения по своему выбору, такую как Сумма, Количество, Среднее, Максимум, Минимум, Произведение, Уникальное количество и т. д.

Aspose.Cells предоставляет перечисление [**ConsolidationFunction**](https://reference.aspose.com/cells/net/aspose.cells/consolidationfunction) для поддержки следующих функций консолидации.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

### **Применение функции консолидации к данным полей сводной таблицы**

Следующий код применяет функцию объединения **Среднее** к первому полю данных (или значению) и функцию объединения **Уникальное количество** ко второму полю данных (или значению).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ConsolidationFunctions-1.cs" >}}

{{% alert color="primary" %}}

Функция консолидации Уникальное количество поддерживается только Microsoft Excel 2013.

{{% /alert %}}
