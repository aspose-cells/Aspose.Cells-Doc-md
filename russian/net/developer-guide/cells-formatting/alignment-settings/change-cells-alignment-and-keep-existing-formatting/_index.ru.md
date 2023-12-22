---
title: Измените выравнивание Cells и сохраните существующее форматирование.
description: Используйте библиотеку Aspose.Cells, чтобы изменить выравнивание ячеек и сохранить существующее форматирование.
keywords: Aspose.Cells, C#, Cell alignment, preserve existing formatting
type: docs
weight: 340
url: /ru/net/change-cells-alignment-and-keep-existing-formatting/
---
##  **Возможные сценарии использования**

Иногда вам нужно изменить выравнивание нескольких ячеек, но при этом сохранить существующее форматирование. Aspose.Cells позволяет сделать это с помощью[**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments) свойство. Если вы установите его *true**, изменения в выравнивании произойдут, в противном случае — нет. Пожалуйста, обрати внимание,[**СтильФлаг**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) объект передается в качестве параметра[**Диапазон.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle)метод, который фактически применяет форматирование к диапазону ячеек.

##  **Измените выравнивание Cells и сохраните существующее форматирование.**

 Следующий пример кода загружает[образец файла Excel](67338585.xlsx) , создает диапазон и центр, выравнивает его по горизонтали и вертикали и сохраняет существующее форматирование без изменений. На следующем снимке экрана сравнивается образец файла Excel и[выходной файл Excel](67338586.xlsx) и показывает, что все существующее форматирование ячеек такое же, за исключением того, что ячейки теперь выравниваются по центру по горизонтали и вертикали.

![задача: image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

##  **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
