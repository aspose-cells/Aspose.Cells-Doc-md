---
title: Укажите, как пересекать строку в выводе PDF и изображении
type: docs
weight: 20
url: /ru/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Укажите, как пересекать строку в выводе PDF и изображении**
 Если ячейка содержит текст или строку, превышающую ширину ячейки, строка переполняется, если следующая ячейка в следующем столбце имеет значение null или пуста. Когда вы сохраняете файл Excel в PDF/Image, вы можете управлять этим переполнением, указав перекрестный тип с помощью[ТекстКроссТип](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType) перечисление. Он имеет следующие значения

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): Отображение как в MS Excel, зависит от следующей ячейки. Если следующая ячейка пуста, строка будет пересекаться или будет усечена.
- [ТекстКроссТип. CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP): Отобразить строку, аналогичную экспорту MS Excel PDF/Image.
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE)отображать весь текст, пересекая другие ячейки, и переопределять текст пересеченных ячеек.
- [TextCrossType.STRICT_В_КЛЕТКА](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL): Отображает только строку в пределах ширины ячейки.

Следующий пример кода загружает образец файла Excel и сохраняет его в формате PDF/Image, указав другой TextCrossType. Образец файла Excel и выходные файлы можно загрузить по следующим ссылкам:

[образецCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[выводCrossType.png](outputCrossType.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
