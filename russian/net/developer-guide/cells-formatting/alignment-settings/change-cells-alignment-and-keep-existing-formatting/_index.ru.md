---
title: Изменение выравнивания ячеек и сохранение существующего форматирования
description: Используйте библиотеку Aspose.Cells для изменения выравнивания ячеек и сохранения существующего форматирования
keywords: Aspose.Cells, C#, Выравнивание ячейки, сохранение существующего форматирования
type: docs
weight: 340
url: /ru/net/change-cells-alignment-and-keep-existing-formatting/
---

## **Возможные сценарии использования**

Иногда вам может понадобиться изменить выравнивание нескольких ячеек, но при этом также сохранить существующее форматирование. Aspose.Cells позволяет сделать это, используя свойство [**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments). Если вы установите его **True**, изменения в выравнивании произойдут, в противном случае — нет. Обратите внимание, что объект [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) передается в качестве параметра в метод [**Range.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle), который фактически применяет форматирование к диапазону ячеек.

## **Изменение выравнивания ячеек и сохранение существующего форматирования**

Приведенный ниже образец кода загружает [образец файла Excel](67338585.xlsx), создает диапазон и центрирует его по горизонтали и вертикали, сохраняя все существующее форматирование нетронутым. Ниже приведено сравнение образца файла Excel и [выходного файла Excel](67338586.xlsx) и показано, что все существующее форматирование ячеек такое же, за исключением того, что ячейки теперь центрированы по горизонтали и вертикали.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
