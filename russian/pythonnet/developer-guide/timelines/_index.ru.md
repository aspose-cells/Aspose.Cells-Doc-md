---
title: Вставить временную шкалу
linktitle: Сроки
type: docs
weight: 170
url: /ru/python-net/create-timeline/
description: Узнайте, как создать временную шкалу с помощью Aspose.Cells for Python via .NET.
---
##  **Возможные сценарии использования**

Вместо настройки фильтров для отображения дат вы можете использовать временную шкалу сводной таблицы — параметр динамического фильтра, который позволяет легко фильтровать по дате и времени и увеличивать масштаб нужного периода с помощью ползунка. Microsoft Excel позволяет создать временную шкалу, выбрав сводную таблицу и нажав *Вставка > Временная шкала*. Aspose.Cells for Python via .NET также позволяет создавать временную шкалу с помощью[**Рабочий лист.timelines.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.timelines/timelinecollection/#methods)метод.

##  **Создайте временную шкалу для сводной таблицы**

 См. следующий пример кода. Он загружает[образец файла Excel](input.xlsx)который содержит сводную таблицу. Затем он создает временную шкалу на основе первого базового сводного поля. Наконец, он сохраняет книгу в[вывод XLSX](output.xlsx) формат. На следующем снимке экрана показана временная шкала, созданная Aspose.Cells for Python via .NET в выходном файле Excel.

![задача: image_alt_text](create-timeline-to-a-pivot-table_1.png)

###  **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-CreateTimelineToPivotTable.py" >}}

