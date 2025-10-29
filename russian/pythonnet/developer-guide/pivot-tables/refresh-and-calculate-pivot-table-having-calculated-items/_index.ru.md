---
title: Обновление и вычисление сводной таблицы с вычисляемыми элементами
type: docs
weight: 40
url: /ru/python-net/refresh-and-calculate-pivot-table-having-calculated-items/
description: Эта статья показывает, как обновлять и рассчитывать сводную таблицу с расчетными элементами с помощью Aspose.Cells для Python via .NET.
keywords: Aspose.Cells для Python Excel, библиотека Excel Python, Обновление и рассчет сводной таблицы с расчетными элементами
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET теперь поддерживает обновление и расчет сводной таблицы с использованием расчетных элементов. Пожалуйста, используйте [**PivotTable.refresh_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/refresh_data/#) и [**PivotTable.calculate_data**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/calculate_data/#) как обычно, чтобы выполнить эту функцию.

{{% /alert %}}

## **Обновление и вычисление сводной таблицы с вычисляемыми элементами**

Приведенный ниже образец кода загружает [исходный файл Excel](5115238.xlsx), который содержит сводную таблицу с тремя расчетными элементами, такими как "add", "div", "div2". Сначала мы меняем значение ячейки D2 на 20, а затем обновляем и рассчитываем сводную таблицу с использованием API Aspose.Cells для Python via .NET и сохраняем книгу в формате PDF. Результаты в [выходном PDF](5115229.pdf) показывают, что Aspose.Cells для Python via .NET успешно обновил и рассчитал сводную таблицу с расчетными элементами. Вы можете проверить это с помощью Microsoft Excel, вручную устанавливая значение 20 в ячейке D2, а затем обновляя сводную таблицу с помощью сочетания клавиш Alt+F5 или нажатия кнопки Обновить в сводной таблице.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-RefreshAndCalculateItems-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
