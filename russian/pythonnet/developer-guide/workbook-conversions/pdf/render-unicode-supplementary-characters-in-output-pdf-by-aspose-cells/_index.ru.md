---
title: Отображение дополнительных символов Юникода в выходном PDF с помощью Aspose.Cells для Python via .NET
type: docs
weight: 350
url: /ru/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Узнайте, как отображать дополнительные символы Юникода при преобразовании Excel в PDF с помощью Aspose.Cells для Python via .NET API.
keywords: Отображение дополнительных символов Юникода при сохранении файла в PDF с использованием Python, Отображение дополнительных символов Юникода при сохранении Excel в PDF с помощью Python, Показ дополнительных символов Юникода при преобразовании Excel в PDF с помощью Python, Вывод дополнительных символов Юникода для excel в pdf
---

{{% alert color="primary" %}}

Обычные символы Юникода занимают 2 байта, а дополнительные символы Юникода - 4 байта. Aspose.Cells для Python via .NET теперь поддерживает отображение этих дополнительных символов Юникода размером 4 байта.

В стандарте символов Юникода дополнительные символы - это символы, которым назначены кодовые точки от U+10000 до U+10FFFF. Другими словами, это символы Юникода, большие чем U+FFFF.

- В UTF-8 каждый из этих символов имеет длину 4 байта.
- В UTF-16 для этих символов требуются 2 заместителя (16-битные единицы).

{{% /alert %}}

## Отображение дополнительных символов Юникода в выходном PDF с помощью Aspose.Cells для Python via .NET

На следующем скриншоте показано, как Aspose.Cells для Python via .NET преобразовал [исходный файл Excel](5115563.xlsx) в [выходной PDF](5115564.pdf). Как видите, все три дополнительных символа Юникода были отображены точно так же, как это сделано в Microsoft Excel.

![todo:image_alt_text](output.png)

## Образец кода

Вы можете использовать этот образец кода для преобразования [исходного файла Excel](5115563.xlsx) в [выходной PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
