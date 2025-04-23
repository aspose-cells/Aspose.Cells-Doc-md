---
title: Создать фильтр для сводной таблицы
type: docs
weight: 10
url: /ru/java/create-slicer-to-a-pivot-table/
---

## **Возможные сценарии использования**
Срез используется для быстрого фильтрации данных. Его можно использовать для фильтрации данных в таблице или в сводной таблице. Microsoft Excel позволяет создавать срез, выбирая таблицу или сводную таблицу и нажав на *Вставка > Срез*. Aspose.Cells также позволяет создавать срез, вызывая метод [Worksheet.getSlicers().add()](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add-com.aspose.cells.PivotTable-int-int-com.aspose.cells.PivotField-).
## **Создать нарезчик для сводной таблицы**
Пожалуйста, посмотрите следующий образец кода. Он загружает [образец файла Excel](67338498.xlsx), содержащий сводную таблицу. Затем создает фильтр на основе первого базового поля сводной таблицы. Наконец, он сохраняет книгу в формате [output XLSX](67338497.xlsx) и [output XLSB](67338496.xlsb). На следующем скриншоте показан фильтр, созданный Aspose.Cells в выходном файле Excel.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-CreateSlicerToPivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
