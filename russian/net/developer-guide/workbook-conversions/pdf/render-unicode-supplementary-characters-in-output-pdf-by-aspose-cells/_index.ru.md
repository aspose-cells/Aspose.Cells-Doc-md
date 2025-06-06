---
title: Отображайте дополнительные символы Юникода в выходном PDF с помощью Aspose.Cells
type: docs
weight: 350
url: /ru/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}}

Обычные символы Юникода имеют длину 2 байта, а дополнительные символы Юникода - 4 байта. Aspose.Cells теперь поддерживает отображение этих дополнительных символов Юникода длиной 4 байта.

В стандарте символов Юникода дополнительные символы - это символы, которым назначены кодовые точки от U+10000 до U+10FFFF. Другими словами, это символы Юникода, большие чем U+FFFF.

- В UTF-8 каждый из этих символов имеет длину 4 байта.
- В UTF-16 для этих символов требуются 2 заместителя (16-битные единицы).

{{% /alert %}}

## Отображение дополнительных символов Юникода в выходном PDF при использовании Aspose.Cells

На следующем скриншоте показано, как Aspose.Cells преобразовал [исходный файл Excel](5115563.xlsx) в [выходной PDF](5115564.pdf). Как видно, все три дополнительных символа Юникода отображены точно так же, как это делает Microsoft Excel.

![todo:image_alt_text](output.png)

## Образец кода

Вы можете использовать этот образец кода для преобразования [исходного файла Excel](5115563.xlsx) в [выходной PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderUnicodeInOutput-RenderUnicodeInOutput.cs" >}}
{{< app/cells/assistant language="csharp" >}}
