---
title: Вставить фильтр
linktitle: Фильтры
type: docs
weight: 170
url: /ru/net/create-slicer/
description: Управляйте условиями Excel файлов с помощью Aspose.Cells.
---

## **Возможные сценарии использования**

Ползунок используется для быстрого фильтрации данных. Его можно использовать для фильтрации данных как в таблице, так и в сводной таблице. Microsoft Excel позволяет создать ползунок, выбрав таблицу или сводную таблицу, а затем щелкнув *Вставка > Ползунок*. Aspose.Cells также позволяет создавать ползунок с помощью метода *[**Worksheet.Slicers.Add()**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicercollection/methods/add/index)*.

## **Создать нарезчик для сводной таблицы**

Пожалуйста, ознакомьтесь со следующим образцовым кодом. Он загружает [образец Excel-файла](67338470.xlsx), который содержит сводную таблицу. Затем создается срезка на основе первого базового сводного поля. Наконец, рабочая книга сохраняется в формате [XLSX](67338471.xlsx) и [XLSB](67338472.xlsb). Ниже показана срезка, созданная Aspose.Cells в выходном файле Excel.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-CreateSlicerToPivotTable.cs" >}}

## **Создать нарезчик для таблицы Excel**

Пожалуйста, посмотрите следующий образец кода. Он загружает [образец файла Excel](sampleCreateSlicerToExcelTable.xlsx), содержащий таблицу. Затем создает фильтр на основе первого столбца. Наконец, он сохраняет книгу в формате [output XLSX](outputCreateSlicerToExcelTable.xlsx).

### **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.cs" >}}

## **Продвинутые темы**
- [Изменить свойства фильтра](/cells/ru/net/change-slicer-properties/)
- [Нарисуйте фильтр при рендеринге Excel в PDF](/cells/ru/net/draw-slicer-while-rendering-excel-to-pdf/)
- [Форматирование фильтра](/cells/ru/net/formatting-slicer/)
- [Удаление срезки](/cells/ru/net/removing-slicer/)
- [Рендеринг срезки](/cells/ru/net/rendering-slicer/)
- [Обновление среза](/cells/ru/net/updating-slicer/)
{{< app/cells/assistant language="csharp" >}}
