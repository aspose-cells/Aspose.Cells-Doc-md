---
title: Отображение дополнительных символов Юникода в выводе PDF на Aspose.Cells for Python via .NET
type: docs
weight: 350
url: /ru/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Узнайте, как отображать дополнительные символы Юникода при преобразовании Excel в PDF с помощью Aspose.Cells for Python via .NET API.
keywords: Python Render Unicode Supplementary characters while saving file to PDF, Print Unicode Supplementary characters while saving Excel to PDF using Python, Python Show Unicode Supplementary characters when converting Excel to PDF, Output Unicode Supplementary characters for excel to pdf
---
{{% alert color="primary" %}}

Обычные символы Юникода имеют длину 2 байта, а дополнительные символы Юникода — 4 байта. Aspose.Cells for Python via .NET теперь поддерживает рендеринг этих 4-байтовых символов Юникода.

В стандарте символов Юникода дополнительные символы — это символы, которым присвоены кодовые точки от U+10000 до U+10FFFF. Другими словами, это символы Юникода, большие, чем U+FFFF.

- В UTF-8 длина каждого из этих символов составляет 4 байта.
- В UTF-16 для этих символов требуются два заместителя (16-битные единицы).

{{% /alert %}}

##  Отображение дополнительных символов Юникода в выводе PDF на Aspose.Cells for Python via .NET

 На следующем снимке экрана показано, как Aspose.Cells for Python via .NET отображает[исходный файл Excel](5115563.xlsx) в[вывод PDF](5115564.pdf). Как вы можете видеть, все три дополнительных символа Юникода были отображены точно так же, как это было сделано в Excel Microsoft.

![задача: image_alt_text](output.png)

##  Образец кода

Вы можете использовать этот пример кода для преобразования[исходный файл Excel](5115563.xlsx) в[вывод PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
