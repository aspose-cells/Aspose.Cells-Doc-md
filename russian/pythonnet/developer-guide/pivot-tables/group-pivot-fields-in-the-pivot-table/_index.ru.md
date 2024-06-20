---
title: Группировка полей сводной таблицы
type: docs
weight: 80
url: /ru/python-net/group-pivot-fields-in-the-pivot-table/
description: Как сгруппировать поля сводной таблицы в Aspose.Cells для Python via .NET.
keywords: Aspose.Cells для Python Excel, библиотека Excel Python, Как сгруппировать поля сводной таблицы с использованием библиотеки Aspose.Cells для Python Excel.
---

## **Возможные сценарии использования**

Microsoft Excel позволяет группировать поля сводной таблицы. Когда имеется большое количество данных, связанных с полем сводной таблицы, часто бывает полезно группировать их в разделы. Aspose.Cells для Python via .NET также предоставляет эту функцию с использованием метода [**PivotTable.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float).

## **Как сгруппировать поля сводной таблицы**

Приведенный ниже образец кода загружает [образец файла Excel](64716818.xlsx) и выполняет группировку по первому полю сводной таблицы с помощью метода [**PivotTable.set_manual_group_field()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/set_manual_group_field/#int-float-float-list-float). Затем он обновляет и вычисляет данные сводной таблицы и сохраняет книгу Excel как [выходной файл Excel](64716817.xlsx). На скриншоте показан эффект образца кода на образцовый файл Excel. Как видно на скриншоте, первое поле сводной таблицы теперь сгруппировано по месяцам и кварталам.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.py" >}}
