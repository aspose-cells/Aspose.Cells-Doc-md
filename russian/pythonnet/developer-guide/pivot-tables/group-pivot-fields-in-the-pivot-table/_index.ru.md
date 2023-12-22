---
title: Группировка сводных полей в сводной таблице
type: docs
weight: 80
url: /ru/python-net/group-pivot-fields-in-the-pivot-table/
description: Как сгруппировать сводные поля в сводной таблице с помощью Aspose.Cells for Python via .NET.
keywords: Group Pivot Fields in the Pivot Table.
---
##  **Возможные сценарии использования**

Microsoft Excel позволяет группировать сводные поля сводной таблицы. Если к сводному полю относится большой объем данных, часто бывает полезно сгруппировать их по разделам. Aspose.Cells for Python via .NET также предоставляет эту функцию с помощью[**PivotTable.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float)метод.

##  **Группировка сводных полей в сводной таблице**

 Следующий пример кода загружает[образец файла Excel](64716818.xlsx) и выполняет группировку по первому сводному полю, используя[**PivotTable.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float) метод. Затем он обновляет и вычисляет данные сводной таблицы и сохраняет книгу как[выходной файл Excel](64716817.xlsx)На снимке экрана показано влияние примера кода на образец файла Excel. Как вы можете видеть на скриншоте, первое поле сводной таблицы теперь сгруппировано по месяцам и кварталам.

![задача: image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

##  **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.py" >}}
