---
title: Группировка полей сводной таблицы
type: docs
weight: 90
url: /ru/java/group-pivot-fields-in-the-pivot-table/
---

## **Возможные сценарии использования**

Microsoft Excel позволяет группировать сводные поля сводной таблицы. Когда существует большое количество данных, относящихся к сводному полю, часто полезно группировать их по разделам. Aspose.Cells также предоставляет эту функцию с помощью метода [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)).

## **Группировка полей сводной таблицы**

Приведенный ниже образец кода загружает [образец файла Excel](64716838.xlsx) и выполняет группировку по первому сводному полю с использованием метода [**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)). Затем он обновляет и вычисляет данные сводной таблицы и сохраняет книгу как [выходной файл Excel](64716837.xlsx). На скриншоте показан эффект образца кода на образцовом файле Excel. Как видно на скриншоте, первое сводное поле теперь сгруппировано по месяцам и кварталам.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
