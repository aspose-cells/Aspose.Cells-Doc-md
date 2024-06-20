---
title: Функция консолидации
type: docs
weight: 20
url: /ru/python-net/consolidation-function/
description: Как применить функцию консолидации к полю данных сводной таблицы с помощью Aspose.Cells для Python via .NET.
keywords: Aspose.Cells для Python Excel, библиотека Excel Python, Функция консолидации для полей данных сводной таблицы с использованием библиотеки Aspose.Cells для Python Excel.
---

## **Функция консолидации**

Aspose.Cells для Python via .NET можно использовать для применения функции консолидации к полю данных (или значению) сводной таблицы. В Microsoft Excel вы можете щелкнуть правой кнопкой мыши по полю значений, а затем выбрать опцию **Настройки поля значений...**, а затем выберите вкладку **Суммировать значения по**. Оттуда вы можете выбрать любую функцию консолидации по вашему выбору, такую как Сумма, Количество, Среднее, Максимальное, Минимальное, Произведение, Уникальное количество и т. д.

Aspose.Cells для Python via .NET предоставляет перечисление [**ConsolidationFunction**](https://reference.aspose.com/cells/python-net/aspose.cells/consolidationfunction/) для поддержки следующих функций консолидации.

- ConsolidationFunction.AVERAGE
- ConsolidationFunction.COUNT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.DISTINCT_COUNT
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.SUM
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP

## **Как применить функцию консолидации к полям данных сводной таблицы с использованием библиотеки Aspose.Cells для Python Excel**

В следующем коде применяется **СРЕДНЕЕ** функция консолидации к первому полю данных (или значению) и **УНИКАЛЬНОЕ_КОЛИЧЕСТВО** функция консолидации ко второму полю данных (или значению).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ConsolidationFunctions-1.py" >}}

{{% alert color="primary" %}}

Функция консолидации УНИКАЛЬНОЕ_КОЛИЧЕСТВО поддерживается только в Microsoft Excel 2013.

{{% /alert %}}
