---
title: Создать фильтр для сводной таблицы
type: docs
weight: 10
url: /ru/java/create-slicer-to-a-pivot-table/
---

## **Возможные сценарии использования**
Фильтр используется для быстрого фильтрования данных. Его можно использовать для фильтрации данных как в обычной таблице, так и в сводной таблице. Microsoft Excel позволяет создавать фильтр, выбрав таблицу или сводную таблицу, а затем нажав *Вставка > Фильтр*. Aspose.Cells также позволяет создавать фильтр с помощью метода [Worksheet.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add\(com.aspose.cells.PivotTable,%20int,%20int,%20com.aspose.cells.PivotField\)).
## **Создать нарезчик для сводной таблицы**
Пожалуйста, посмотрите следующий образец кода. Он загружает [образец файла Excel](67338498.xlsx), содержащий сводную таблицу. Затем создает фильтр на основе первого базового поля сводной таблицы. Наконец, он сохраняет книгу в формате [output XLSX](67338497.xlsx) и [output XLSB](67338496.xlsb). На следующем скриншоте показан фильтр, созданный Aspose.Cells в выходном файле Excel.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
