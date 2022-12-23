---
title: Укажите, как пересекать строку в выводе PDF и изображении
type: docs
weight: 110
url: /ru/java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Возможные сценарии использования**

Когда ячейка содержит текст или строку, но она больше, чем ширина ячейки, строка переполняется, если следующая ячейка в следующем столбце пуста или пуста. Когда вы сохраняете файл Excel в PDF/Image, вы можете управлять этим переполнением, указав перекрестный тип с помощью[**ТекстКроссТип**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)перечисление. Он имеет следующие значения

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): Отображение как в MS Excel, зависит от следующей ячейки. Если следующая ячейка пуста, строка будет пересекаться или будет усечена.

- [**ТекстКроссТип. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_KEEP): Отобразить строку, например экспорт MS Excel PDF/Image.

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_OVERRIDE): отображать весь текст, пересекая другие ячейки, и переопределять текст пересеченных ячеек.

- [**ТекстКроссТип.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT_IN_CELL): Отображает только строку в пределах ширины ячейки.

## **Укажите, как пересекать строку в выходных данных PDF/Image, используя TextCrossType.**

Следующий пример кода загружает образец файла Excel и сохраняет его в формате PDF/Image, указав разные[**ТекстКроссТип**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). Образец файла Excel и выходные файлы можно загрузить по следующим ссылкам:

[образецCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[выводCrossType.png](outputCrossType.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
