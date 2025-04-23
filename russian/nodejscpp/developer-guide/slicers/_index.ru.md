---
title: Вставить фильтр
linktitle: Фильтры
type: docs
weight: 170
url: /ru/nodejs-cpp/create-slicer/
description: Управление слайсерами файлов Excel с помощью Aspose.Cells for Node.js via C++.
---

## **Возможные сценарии использования**

Слайсер используется для быстрого фильтрации данных. Он может использоваться для фильтрации данных как в таблице, так и в сводной таблице. Microsoft Excel позволяет создавать слайсер, выбирая таблицу или сводную таблицу и затем нажимая *Вставка > Слайсер*. Aspose.Cells for Node.js via C++ также позволяет создавать слайсер с помощью метода [**Worksheet.getSlicers().add()**](https://reference.aspose.com/cells/nodejs-cpp/slicercollection/#add-pivottable-string-string-).

## **Создать нарезчик для сводной таблицы**

Посмотрите следующий образец кода. Он загружает [пример файла Excel](67338470.xlsx), содержащего сводную таблицу. Затем создает слайсер на основе первого базового поля сводной таблицы. В конце сохраняет книгу в форматах [выходной XLSX](67338471.xlsx) и [выходной XLSB](67338472.xlsb). Скриншот ниже показывает созданный Aspose.Cells for Node.js via C++ слайсер в выходном файле Excel.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **Образец кода**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToPivotTable.js" >}}

## **Создать нарезчик для таблицы Excel**

Пожалуйста, посмотрите следующий образец кода. Он загружает [образец файла Excel](sampleCreateSlicerToExcelTable.xlsx), содержащий таблицу. Затем создает фильтр на основе первого столбца. Наконец, он сохраняет книгу в формате [output XLSX](outputCreateSlicerToExcelTable.xlsx).

### **Образец кода**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Slicers-CreateSlicerToExcelTable-1.js" >}}
