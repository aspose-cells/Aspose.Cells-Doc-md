---
title: Создать фильтр для таблицы Excel
type: docs
weight: 15
url: /ru/java/create-slicer-to-excel-table/
---

## **Возможные сценарии использования**

Ползунок используется для быстрого фильтрации данных. Его можно использовать для фильтрации данных как в таблице, так и в сводной таблице. Microsoft Excel позволяет создать ползунок, выбрав таблицу или сводную таблицу, а затем щелкнув *Вставка > Ползунок*. Aspose.Cells также позволяет создавать ползунок с помощью метода *[**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/java/com.aspose.cells/slicercollection#add(com.aspose.cells.ListObject,%20com.aspose.cells.ListColumn,%20int,%20int))*.

## **Создать нарезчик для таблицы Excel**

Пожалуйста, посмотрите следующий образец кода. Он загружает [образец файла Excel](sampleCreateSlicerToExcelTable.xlsx), содержащий таблицу. Затем создает фильтр на основе первого столбца. Наконец, он сохраняет книгу в формате [output XLSX](outputCreateSlicerToExcelTable.xlsx).

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Slicers-CreateSlicerToExcelTable-1.java" >}}
