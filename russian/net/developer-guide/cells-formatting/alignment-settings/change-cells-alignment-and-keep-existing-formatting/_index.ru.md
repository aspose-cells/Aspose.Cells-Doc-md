---
title: Изменить выравнивание Cells и сохранить существующее форматирование
type: docs
weight: 340
url: /ru/net/change-cells-alignment-and-keep-existing-formatting/
---
## **Возможные сценарии использования**

Иногда вам нужно изменить выравнивание нескольких ячеек, но при этом сохранить существующее форматирование. Aspose.Cells позволяет сделать это с помощью[**StyleFlag.Alignments**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/alignments) имущество. Если вы установите его**истинный** , в противном случае изменения в выравнивании не произойдут. Пожалуйста, обрати внимание,[**СтильФлаг**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) объект передается в качестве параметра[**Диапазон.ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/applystyle)метод, который фактически применяет форматирование к диапазону ячеек.

## **Изменить выравнивание Cells и сохранить существующее форматирование**

 Следующий пример кода загружает[образец файла Excel](67338585.xlsx) , создает диапазон, а центр выравнивает его по горизонтали и вертикали и сохраняет существующее форматирование без изменений. На следующем снимке экрана сравнивается образец файла Excel и[выходной файл Excel](67338586.xlsx)и показывает, что все существующее форматирование ячеек такое же, за исключением того, что ячейки теперь выровнены по центру по горизонтали и вертикали.

![дело:изображение_альтернативный_текст](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-ChangeCellsAlignmentAndKeepExistingFormatting.cs" >}}
