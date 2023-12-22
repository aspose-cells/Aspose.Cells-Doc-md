---
title: Функция консолидации
type: docs
weight: 20
url: /ru/python-net/consolidation-function/
description: Как применить функцию консолидации к полям данных сводной таблицы с Aspose.Cells for Python via .NET.
keywords: ConsolidationFunction to Data Fields of Pivot Table.
---
##  **Функция консолидации**

 Aspose.Cells for Python via .NET можно использовать для применения ConsolidationFunction к полям данных (или полям значений) сводной таблицы. В Excel Microsoft вы можете щелкнуть правой кнопкой мыши поле значения и затем выбрать**Настройки поля значений...** и выберите вкладку *Суммировать значения по**. Оттуда вы можете выбрать любую функцию консолидации по вашему выбору, например, «Сумма», «Количество», «Среднее», «Макс», «Мин», «Продукт», «Отдельное количество» и т. д.

 Aspose.Cells for Python via .NET обеспечивает[**Функция консолидации**](https://reference.aspose.com/cells/python-net/aspose.cells/consolidationfunction/) перечисление для поддержки следующих функций консолидации.

- КонсолидацияФункция.СРЗНАЧ
- КонсолидацияФункция.COUNT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.DISTINCT_COUNT
- КонсолидацияФункция.МАКС
- КонсолидацияФункция.МИН
- КонсолидацияФункция.ПРОДУКТ
- КонсолидацияФункция.STD_DEV
- КонсолидацияФункция.STD_DEVP
- КонсолидацияФункция.СУММ
- КонсолидацияФункция.VAR
- КонсолидацияФункция.VARP

###  **Применение функции ConsolidationFunction к полям данных сводной таблицы**

 Применяется следующий код**AVERAGE** функцию консолидации к первому полю данных (или полю значения) и**DISTINCT_COUNT** функцию консолидации ко второму полю данных (или полю значения).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ConsolidationFunctions-1.py" >}}

{{% alert color="primary" %}}

Функция консолидации DISTINCT_COUNT поддерживается только Microsoft Excel 2013.

{{% /alert %}}
