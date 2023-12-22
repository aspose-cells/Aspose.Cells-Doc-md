---
title: Вставить срез
linktitle: Слайсеры
type: docs
weight: 170
url: /ru/python-net/create-slicer/
description: Управляйте срезами файлов Excel с помощью номера Aspose.Cells.
---
##  **Возможные сценарии использования**

Срез используется для быстрой фильтрации данных. Его можно использовать для фильтрации данных как в таблице, так и в сводной таблице. Microsoft Excel позволяет создать срез, выбрав таблицу или сводную таблицу, а затем нажав *Вставить > Срез*. Aspose.Cells for Python via .NET также позволяет создавать слайсер с помощью[**Рабочий лист.slicers.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicercollection/add/#aspose.cells.pivot.PivotTable-int-int-aspose.cells.pivot.PivotField)метод.

##  **Создайте срез в сводной таблице**

 См. следующий пример кода. Он загружает[образец файла Excel](67338470.xlsx) который содержит сводную таблицу. Затем он создает срез на основе первого базового сводного поля. Наконец, он сохраняет книгу в[вывод XLSX](67338471.xlsx) и[вывод XLSB](67338472.xlsb) формат. На следующем снимке экрана показан срез, созданный пользователем Aspose.Cells в выходном файле Excel.

![задача: image_alt_text](create-slicer-to-a-pivot-table_1.png)

###  **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Slicers-CreateSlicerToPivotTable.py" >}}

##  **Создать срез в таблицу Excel**

 См. следующий пример кода. Он загружает[образец файла Excel](sampleCreateSlicerToExcelTable.xlsx) который содержит таблицу. Затем он создает срез на основе первого столбца. Наконец, он сохраняет книгу в[вывод XLSX](outputCreateSlicerToExcelTable.xlsx) формат.

###  **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Examples-CSharp-Slicers-CreateSlicerToExcelTable-1.py" >}}

##  **Предварительные темы**
- [Изменить свойства среза](/cells/ru/python-net/change-slicer-properties/)
- [Нарисуйте срез при рендеринге Excel до PDF.](/cells/ru/python-net/draw-slicer-while-rendering-excel-to-pdf/)
- [Форматирование среза](/cells/ru/python-net/formatting-slicer/)
- [Удаление слайсера](/cells/ru/python-net/removing-slicer/)
- [Рендеринг слайсера](/cells/ru/python-net/rendering-slicer/)
- [Обновление слайсера](/cells/ru/python-net/updating-slicer/)
