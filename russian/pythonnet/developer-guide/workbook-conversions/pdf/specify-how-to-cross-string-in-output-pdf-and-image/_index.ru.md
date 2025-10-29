---
title: Указание того, как пересекать строку в выходном PDF и изображении
type: docs
weight: 120
url: /ru/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: Узнайте, как пересечь строку в выходном PDF и изображении с помощью Aspose.Cells для Python via .NET API.
keywords: Python Пересечение строки в выходном PDF и изображении
---

## **Возможные сценарии использования**

Когда ячейка содержит текст или строку, но она больше ширины ячейки, то строка переполняется, если следующая ячейка в следующем столбце пуста или пуста. Когда вы сохраняете свой файл Excel в PDF / изображение, вы можете контролировать это переполнение, указав тип пересечения с использованием перечисления [**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/). Оно имеет следующие значения

- **TextCrossType.DEFAULT**: Отображать текст как MS Excel, который зависит от следующей ячейки. Если следующая ячейка равна null, строка будет пересекаться или усекаться.

- **TextCrossType.CROSS_KEEP**: Отображать строку как MS Excel в формате PDF / изображении

- **TextCrossType.CROSS_OVERRIDE**: Отображать весь текст, пересекаясь с другими ячейками и перезаписывая текст пересекаемых ячеек

- **TextCrossType.STRICT_IN_CELL**: Отображать только строку в пределах ширины ячейки.

## **Указание того, как пересекать строку в выходном PDF/изображении с использованием TextCrossType**

В следующем примере кода загружается образец файла Excel и сохраняется в формат PDF/изображение, указав разные [**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/). Образец файла Excel и выходные файлы можно скачать по следующим ссылкам:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Образец кода

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
