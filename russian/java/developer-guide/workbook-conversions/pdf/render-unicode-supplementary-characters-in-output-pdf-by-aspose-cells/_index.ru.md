---
title: Отображайте дополнительные символы Юникода в выходном PDF с помощью Aspose.Cells
type: docs
weight: 690
url: /ru/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}} 

Обычные символы Юникода имеют длину 2 байта, а дополнительные символы Юникода - 4 байта. Aspose.Cells теперь поддерживает отображение этих дополнительных символов Юникода длиной 4 байта.

В стандарте символов Юникода дополнительные символы - это символы, которым назначены кодовые точки от U+10000 до U+10FFFF. Другими словами, это символы Юникода, большие чем U+FFFF.

- В UTF-8 каждый из этих символов имеет длину 4 байта.
- В UTF-16 для этих символов требуются 2 заместителя (16-битные единицы).

{{% /alert %}} 
## **Отобразите дополнительные символы Юникода в выходном PDF с помощью Aspose.Cells**
На следующем снимке экрана показано, как Aspose.Cells отобразил [исходный файл Excel](5473390.xlsx) в [выходной файл PDF](5473391.pdf). Как видите, все три дополнительных символа Юникода были отображены точно так же, как это сделал Microsoft Excel.

![todo:image_alt_text](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

Вы можете использовать этот образец кода для преобразования [исходного файла Excel](5473390.xlsx) в [выходной файл PDF](5473391.pdf).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
{{< app/cells/assistant language="java" >}}
