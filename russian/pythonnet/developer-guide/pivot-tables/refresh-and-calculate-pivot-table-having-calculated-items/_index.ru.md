---
title: Обновить и вычислить сводную таблицу с вычисляемыми элементами
type: docs
weight: 40
url: /ru/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: В этой статье показано, как обновить и вычислить сводную таблицу с вычисляемыми элементами с помощью Aspose.Cells for Python via .NET.
keywords: Refresh and Calculate Pivot Table with Calculated Items
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET теперь поддерживает обновление и расчет сводной таблицы с вычисляемыми элементами. Пожалуйста, используйте[**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) и[**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) как обычно для выполнения этой функции.

{{% /alert %}}

##  **Обновить и вычислить сводную таблицу с вычисляемыми элементами**

 Следующий пример кода загружает[исходный файл Excel](5115238.xlsx)которая содержит сводную таблицу с тремя вычисляемыми элементами, такими как «add», «div», «div2». Сначала мы изменяем значение ячейки D2 на 20, а затем обновляем и вычисляем сводную таблицу, используя API-интерфейсы Aspose.Cells, for Python, via .NET, и сохраняем книгу в формате PDF. Результаты в[вывод PDF](5115229.pdf) показывает, что Aspose.Cells for Python via .NET обновил и рассчитал сводную таблицу, успешно вычислив элементы. Вы можете проверить это с помощью Microsoft Excel, вручную поместив значение 20 в ячейку D2, а затем обновив сводную таблицу с помощью сочетания клавиш Alt + F5 или нажав кнопку «Обновить сводную таблицу».

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
