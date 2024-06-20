---
title: Указание того, как пересекать строку в выходном PDF и изображении
type: docs
weight: 20
url: /ru/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Указание способа пересечения строк в выходном PDF и изображении**
Если ячейка содержит текст или строку, которая больше ширины ячейки, строка перекрывается, если следующая ячейка в следующем столбце является пустой или пустой. При сохранении файла Excel в формат PDF/изображение вы можете контролировать это пересечение, указав тип пересечения с помощью перечисления [TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype). Оно имеет следующие значения

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): Отображение, подобное MS Excel, зависит от следующей ячейки. Если следующая ячейка пуста, строка пересечется или будет усечена.
- [TextCrossType. CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP) : Отображение строки аналогично экспорту PDF/изображения MS Excel
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE) : Отображение всего текста путем пересечения других ячеек и переопределения текста пересеченных ячеек
- [TextCrossType.STRICT_IN_CELL](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL) : Отображение строки только в пределах ширины ячейки.

Следующий образец кода загружает образец Excel-файла и сохраняет его в формате PDF/Image, указывая разные типы TextCrossType. Образец Excel-файла и файлы результатов можно загрузить по следующим ссылкам:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
