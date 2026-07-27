---
title: Группировка полей сводной таблицы
type: docs
weight: 80
url: /ru/net/group-pivot-fields-in-the-pivot-table/
---

## **Возможные сценарии использования**

В Microsoft Excel можно группировать поля сводной таблицы. Когда имеется большое количество данных, связанных с полем сводной таблицы, часто полезно сгруппировать их по разделам. Aspose.Cells также предоставляет эту функцию с помощью метода [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/groupby/).

## **Группировка полей сводной таблицы**

Приведенный ниже образец кода загружает [образец файла Excel](64716818.xlsx) и выполняет группировку по первому полю сводной таблицы с помощью метода [**PivotTable.GroupBy()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield/groupby/). Затем он обновляет и вычисляет данные сводной таблицы и сохраняет книгу Excel как [выходной файл Excel](64716817.xlsx). На скриншоте показан эффект образца кода на образцовый файл Excel. Как видно на скриншоте, первое поле сводной таблицы теперь сгруппировано по месяцам и кварталам.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.cs" >}}
{{< app/cells/assistant language="csharp" >}}
