---
title: Функция консолидации
type: docs
weight: 20
url: /ru/java/consolidation-function/
description: Применить функцию консолидации к данным полей сводной таблицы.
---

## **Функция консолидации**

Aspose.Cells можно использовать для применения функции объединения к полям данных (или значениям) сводной таблицы. В Microsoft Excel вы можете щелкнуть правой кнопкой мыши на поле значения, затем выбрать опцию **Настройки поля значения...**, а затем выбрать вкладку **Сводные значения по**. Оттуда вы можете выбрать любую функцию объединения по своему выбору, такую как Сумма, Количество, Среднее, Максимум, Минимум, Произведение, Уникальное количество и т. д.

Aspose.Cells предоставляет перечисление [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) для поддержки следующих функций консолидации.

- ConsolidationFunction.SUM
- ConsolidationFunction.COUNT
- ConsolidationFunction.AVERAGE
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP
- ConsolidationFunction.DISTINCT_COUNT

### **Применение функции консолидации к данным полей сводной таблицы**

Следующий код применяет функцию консолидации **AVERAGE** к первому полю данных (или значению) и функцию консолидации **STD_DEV** ко второму полю данных (или значению).

Образец исходного файла и выходных файлов можно загрузить отсюда для тестирования образца кода:

[Исходный файл Excel](source.xlsx)

[Файл Excel вывода](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

Функция консолидации Уникальное количество поддерживается только Microsoft Excel 2013.

{{% /alert %}}

