---
title: Визуализация дополнительных символов Unicode в выводе PDF по Aspose.Cells
type: docs
weight: 690
url: /ru/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---
{{% alert color="primary" %}} 

Обычные символы Unicode имеют длину 2 байта, а дополнительные символы Unicode имеют длину 4 байта. Aspose.Cells теперь поддерживает отрисовку этих 4-байтовых символов Unicode.

В стандарте символов Unicode дополнительные символы — это символы, которым присвоены кодовые точки от U+10000 до U+10FFFF. Другими словами, это символы Unicode больше, чем U+FFFF.

- В UTF-8 эти символы имеют длину 4 байта.
- В UTF-16 для этих символов требуется 2 суррогата (16-битные единицы).

{{% /alert %}} 
## **Визуализация дополнительных символов Unicode в выводе PDF по Aspose.Cells**
 На следующем снимке экрана показано, как Aspose.Cells визуализировал[исходный файл excel](5473390.xlsx) в[вывод PDF](5473391.pdf). Как вы можете видеть, все три дополнительных символа Unicode были отображены точно так же, как это было сделано Microsoft Excel.

![дело:изображение_альтернативный_текст](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

Вы можете использовать этот пример кода для преобразования[исходный файл excel](5473390.xlsx) в[вывод PDF](5473391.pdf).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
