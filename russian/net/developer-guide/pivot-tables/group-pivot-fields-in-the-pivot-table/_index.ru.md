---
title: Группировать сводные поля в сводной таблице
type: docs
weight: 80
url: /ru/net/group-pivot-fields-in-the-pivot-table/
---
## **Возможные сценарии использования**

Microsoft Excel позволяет группировать сводные поля сводной таблицы. Когда имеется большой объем данных, связанных со сводным полем, часто бывает полезно сгруппировать их по разделам. Aspose.Cells также предоставляет эту функцию с помощью[**Сводная таблица.SetManualGroupField()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index)метод.

## **Группировать сводные поля в сводной таблице**

 Следующий пример кода загружает[образец файла Excel](64716818.xlsx) и выполняет группировку по первому сводному полю, используя[**Сводная таблица.SetManualGroupField()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/setmanualgroupfield/index)метод. Затем он обновляет и вычисляет данные сводной таблицы и сохраняет книгу как[выходной файл Excel](64716817.xlsx). На снимке экрана показано влияние примера кода на образец файла Excel. Как видно на скриншоте, первое сводное поле теперь сгруппировано по месяцам и кварталам.

![дело:изображение_альтернативный_текст](group-pivot-fields-in-the-pivot-table_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-GroupPivotFieldsInPivotTable.cs" >}}
