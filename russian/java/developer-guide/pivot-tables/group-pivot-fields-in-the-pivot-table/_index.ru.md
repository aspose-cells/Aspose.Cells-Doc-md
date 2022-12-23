---
title: Группировать сводные поля в сводной таблице
type: docs
weight: 90
url: /ru/java/group-pivot-fields-in-the-pivot-table/
---
## **Возможные сценарии использования**

Microsoft Excel позволяет группировать сводные поля сводной таблицы. Когда к сводному полю относится большой объем данных, часто бывает полезно сгруппировать их по разделам. Aspose.Cells также предоставляет эту функцию с помощью[**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) метод.

## **Группировать сводные поля в сводной таблице**

Следующий пример кода загружает[образец файла Excel](64716838.xlsx)и выполняет группировку по первому сводному полю, используя[**PivotTable.setManualGroupField()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#setManualGroupField(com.aspose.cells.PivotField,%20com.aspose.cells.DateTime,%20com.aspose.cells.DateTime,%20java.util.ArrayList,%20int)) метод. Затем он обновляет и вычисляет данные сводной таблицы и сохраняет книгу как[выходной файл Excel](64716837.xlsx). На снимке экрана показано влияние примера кода на пример файла Excel. Как видно на скриншоте, первое сводное поле теперь сгруппировано по месяцам и кварталам.

![дело:изображение_альтернативный_текст](group-pivot-fields-in-the-pivot-table_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-GroupPivotFieldsInPivotTable.java" >}}
