---
title: Вставить TimeLine
linktitle: Линии времени
type: docs
weight: 170
url: /ru/python-net/create-timeline/
description: Узнайте, как создать линию времени с помощью Aspose.Cells для Python via .NET.
keywords: Aspose.Cells для Python Excel, библиотека Python Excel, создание временной линии на Python, добавление временной линии через Aspose.Cells для Python, вставка временной линии с помощью Aspose.Cells для Python.
---

## **Возможные сценарии использования**

Вместо настройки фильтров для отображения дат можно использовать линию временных диаграмм — динамический фильтр, который позволяет легко фильтровать по дате/времени и увеличивать период, который вам нужен, с помощью элемента управления-ползунка. Microsoft Excel позволяет создавать линию времени, выбрав сводную таблицу, а затем щелкнув *Вставка > Линия времени*. Aspose.Cells для Python via .NET также позволяет создавать линию времени с использованием метода [**Worksheet.timelines.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.timelines/timelinecollection/#methods).

## **Как создать временную линию для сводной таблицы с использованием библиотеки Aspose.Cells для Python Excel**

Пожалуйста, ознакомьтесь с примером кода ниже. Он загружает [образец файла Excel](input.xlsx), содержащий сводную таблицу. Затем создает временную линию на основе первого базового поля сводной таблицы. Наконец, он сохраняет книгу в формате [XLSX вывода](output.xlsx). На следующем скриншоте показана линия времени, созданная Aspose.Cells для Python via .NET в выходном файле Excel.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-CreateTimelineToPivotTable.py" >}}

