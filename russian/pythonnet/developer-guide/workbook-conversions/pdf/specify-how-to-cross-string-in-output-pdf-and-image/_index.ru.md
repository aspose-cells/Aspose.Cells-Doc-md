---
title: Укажите, как пересекать строку в выводе PDF и изображении.
type: docs
weight: 120
url: /ru/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: Узнайте, как пересечь строку в выводе PDF и изображение с помощью Aspose.Cells for Python via .NET API.
keywords: Python Cross String in output PDF and image
---
##  **Возможные сценарии использования**

Если ячейка содержит текст или строку, но ее размер превышает ширину ячейки, строка переполняется, если следующая ячейка в следующем столбце имеет значение NULL или пуста. Когда вы сохраняете файл Excel в PDF/Image, вы можете контролировать это переполнение, указав перекрестный тип с помощью[**ТекстКроссТип**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)перечисление. Он имеет следующие значения

- *TextCrossType.DEFAULT**: отображать текст, подобный MS Excel, который зависит от следующей ячейки. Если следующая ячейка равна нулю, строка пересечется или будет усечена.

- *TextCrossType.CROSS_KEEP**: отображать строку, например, при экспорте MS Excel PDF/Image.

- *TextCrossType.CROSS_OVERRIDE**: отображать весь текст путем пересечения других ячеек и переопределять текст пересекаемых ячеек.

- *TextCrossType.STRICT_IN_CELL**: отображать строку только в пределах ширины ячейки.

##  **Укажите, как пересекать строку в выводе PDF/Image с помощью TextCrossType.**

Следующий пример кода загружает образец файла Excel и сохраняет его в формате PDF/Image, указав разные[**ТекстКроссТип**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)Образец файла Excel и выходные файлы можно загрузить по следующим ссылкам:

[образецCrossType.xlsx](81920905.xlsx)

[выходнойCrossType.pdf](81920903.pdf)

[выходнойCrossType.png](81920904.png)

###  Образец кода

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
