---
title: Функция консолидации
type: docs
weight: 20
url: /ru/java/consolidation-function/
description: Примените ConsolidationFunction к полям данных сводной таблицы.
---
## **Функция консолидации**

 Aspose.Cells можно использовать для применения ConsolidationFunction к полям данных (или полям значений) сводной таблицы. В Microsoft Excel можно щелкнуть правой кнопкой мыши поле значения и выбрать**Настройки поля значения...** вариант, а затем выберите вкладку**Суммировать значения по**. Оттуда вы можете выбрать любую функцию консолидации по вашему выбору, такую как сумма, количество, среднее, максимальное, минимальное, продукт, отчетливое количество и т. д.

 Aspose.Cells предоставляет[**Функция консолидации**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) перечисление для поддержки следующих функций консолидации.

- Функция консолидации.SUM
- Функция консолидации.COUNT
- ConsolidationFunction.AVERAGE
- Функция консолидации.MAX
- Функция консолидации.МИН
- Функция консолидации.PRODUCT
- Функция консолидации.COUNT_NUMS
- Функция консолидации.STD_DEV
- Функция консолидации.STD_DEVP
- Функция консолидации.VAR
- Функция консолидации.VARP
- Функция консолидации.DISTINCT_COUNT

### **Применение ConsolidationFunction к полям данных сводной таблицы**

 Применяется следующий код**СРЕДНИЙ** функцию консолидации в первое поле данных (или поле значения) и**STD_DEV** функцию консолидации во второе поле данных (или поле значения).

Образец исходного файла и выходные файлы можно загрузить отсюда для тестирования примера кода:

[Исходный файл Excel](source.xlsx)

[Выходной файл Excel](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

Функция консолидации DistinctCount поддерживается только Microsoft Excel 2013.

{{% /alert %}}

