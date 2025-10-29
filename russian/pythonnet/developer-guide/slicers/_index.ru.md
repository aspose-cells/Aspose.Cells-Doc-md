---
title: Вставить фильтр
linktitle: Фильтры
type: docs
weight: 170
url: /ru/python-net/create-slicer/
description: Управляйте условиями Excel файлов с помощью Aspose.Cells.
keywords: Aspose.Cells для Python Excel, библиотека Excel Python, Python Создать Slicer без Excel, Добавить Slicer через Aspose.Cells для Python, Вставить Slicer с использованием Aspose.Cells для Python.
---

## **Возможные сценарии использования**

Срезка используется для быстрой фильтрации данных. Ее можно использовать для фильтрации данных как в таблице, так и в сводной таблице. Microsoft Excel позволяет создавать срезку, выбирая таблицу или сводную таблицу, а затем щелкая *Вставка > Срезка*. Aspose.Cells для Python via .NET также позволяет создавать срезку с помощью метода [**Worksheet.slicers.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercollection/add/#aspose.cells.pivot.PivotTable-int-int-aspose.cells.pivot.PivotField).

## **Как создать срезку для сводной таблицы с использованием библиотеки Aspose.Cells для Python Excel**

Пожалуйста, ознакомьтесь со следующим образцовым кодом. Он загружает [образец Excel-файла](67338470.xlsx), который содержит сводную таблицу. Затем создается срезка на основе первого базового сводного поля. Наконец, рабочая книга сохраняется в формате [XLSX](67338471.xlsx) и [XLSB](67338472.xlsb). Ниже показана срезка, созданная Aspose.Cells в выходном файле Excel.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-CreateSlicerToPivotTable.py" >}}

## **Как создать срезку для таблицы Excel с использованием библиотеки Aspose.Cells для Python Excel**

Пожалуйста, посмотрите следующий образец кода. Он загружает [образец файла Excel](sampleCreateSlicerToExcelTable.xlsx), содержащий таблицу. Затем создает фильтр на основе первого столбца. Наконец, он сохраняет книгу в формате [output XLSX](outputCreateSlicerToExcelTable.xlsx).

### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.py" >}}

## **Продвинутые темы**
- [Изменить свойства фильтра](/cells/ru/python-net/change-slicer-properties/)
- [Нарисуйте фильтр при рендеринге Excel в PDF](/cells/ru/python-net/draw-slicer-while-rendering-excel-to-pdf/)
- [Форматирование фильтра](/cells/ru/python-net/formatting-slicer/)
- [Удаление срезки](/cells/ru/python-net/removing-slicer/)
- [Рендеринг срезки](/cells/ru/python-net/rendering-slicer/)
- [Обновление среза](/cells/ru/python-net/updating-slicer/)
{{< app/cells/assistant language="python-net" >}}
