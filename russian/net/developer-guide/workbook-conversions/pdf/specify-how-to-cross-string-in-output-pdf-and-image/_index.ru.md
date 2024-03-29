﻿---
title: Укажите, как пересекать строку в выводе PDF и изображении
type: docs
weight: 120
url: /ru/net/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Возможные сценарии использования**

Если ячейка содержит текст или строку, но она больше, чем ширина ячейки, строка переполняется, если следующая ячейка в следующем столбце пуста или пуста. Когда вы сохраняете файл Excel в PDF/Image, вы можете управлять этим переполнением, указав перекрестный тип с помощью[**ТекстКроссТип**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)перечисление. Он имеет следующие значения

- **TextCrossType.Default**: Отображать текст, как в MS Excel, который зависит от следующей ячейки. Если следующая ячейка пуста, строка будет пересекаться или будет усечена.

- **TextCrossType.CrossKeep**: Отобразить строку, например экспорт MS Excel PDF/Image.

- **TextCrossType.CrossOverride**: отображать весь текст, пересекая другие ячейки, и переопределять текст пересеченных ячеек.

- **Тексткросстипе.StrictInCell**: отображать строку только в пределах ширины ячейки.

## **Укажите, как пересекать строку в выходных данных PDF/Image, используя TextCrossType.**

Следующий пример кода загружает образец файла Excel и сохраняет его в формате PDF/Image, указав разные[**ТекстКроссТип**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype). Образец файла Excel и выходные файлы можно загрузить по следующим ссылкам:

[образецCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[выводCrossType.png](81920904.png)

### Образец кода

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
