---
title: Вставить TimeLine
linktitle: Линии времени
type: docs
weight: 170
url: /ru/nodejs-cpp/create-timeline/
description: Узнайте, как создать временную шкалу с помощью Aspose.Cells for Node.js via C++.
---

## **Возможные сценарии использования**

Вместо настройки фильтров для отображения дат, вы можете использовать динамический фильтр — временную шкалу PivotTable, которая позволяет легко фильтровать по дате/времени и увеличивать интересующий вас период с помощью ползунка. Microsoft Excel позволяет создавать временную шкалу, выбрав сводную таблицу и нажав **Вставка > Временная шкала**. Aspose.Cells for Node.js via C++ также позволяет создавать временную шкалу с использованием метода [**Worksheet.getTimelines().add()**](https://reference.aspose.com/cells/nodejs-cpp/timelinecollection/#add-pivottable-number-number-string-).

## **Создать временную линию для сводной таблицы**

Смотрите следующий пример кода. Он загружает [пример файла Excel](input.xlsx), содержащий сводную таблицу. Затем создает временную шкалу на основе первого базового поля сводной таблицы. В конце сохраняет книгу в формате [output XLSX](output.xlsx). Следующий скриншот показывает созданную временную шкалу с помощью Aspose.Cells for Node.js via C++ в выходном файле Excel.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Образец кода**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-CreateTimelineToPivotTable.js" >}}

