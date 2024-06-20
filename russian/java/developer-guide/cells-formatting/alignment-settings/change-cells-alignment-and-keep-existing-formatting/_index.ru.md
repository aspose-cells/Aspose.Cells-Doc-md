---
title: Изменение выравнивания ячеек и сохранение существующего форматирования
type: docs
weight: 260
url: /ru/java/change-cells-alignment-and-keep-existing-formatting/
---

## **Возможные сценарии использования**

Иногда вы хотите изменить выравнивание нескольких ячеек, сохраняя существующее форматирование. Aspose.Cells позволяет сделать это, используя свойство [**StyleFlag.Alignments**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#Alignments). Если вы установите его **true**, изменения в выравнивании произойдут, в противном случае - нет. Обратите внимание, что объект [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) передается в качестве параметра в метод [**Range.applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)), который фактически применяет форматирование к диапазону ячеек.

## **Изменение выравнивания ячеек и сохранение существующего форматирования**

Следующий образец кода загружает [образец файла Excel](67338592.xlsx), создает диапазон и центрирует его по горизонтали и вертикали, сохраняя при этом существующее форматирование. На следующем скриншоте сравниваются образец файла Excel и [выходной файл Excel](67338591.xlsx), и показано, что все существующее форматирование ячеек остается таким же, за исключением того, что ячейки теперь центрированы по горизонтали и вертикали.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.java" >}}
