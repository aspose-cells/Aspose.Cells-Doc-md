---
title: Укажите, как пересекать строку в выходном HTML с помощью HtmlCrossType.
type: docs
weight: 140
url: /ru/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **Возможные сценарии использования**

Если ячейка содержит текст или строку, но она больше, чем ширина ячейки, тогда строка переполняется, если следующая ячейка в следующем столбце имеет значение null или пуста. Когда вы сохраняете файл Excel в формате HTML, вы можете управлять этим переполнением, указав перекрестный тип с помощью[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)перечисление. Он имеет следующие значения

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): Отображается как MS Excel, который зависит от следующей ячейки. Если следующая ячейка пуста, строка будет пересекаться или будет усечена.

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS_EXPORT): Отобразить строку, как в MS Excel, экспортирующую HTML.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS) : отображать перекрестную строку HTML, производительность при создании больших файлов HTML будет более чем в десять раз выше, чем при установке значения[**ДЕФОЛТ**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) или же[**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT): отображать перекрестную строку HTML и скрывать правую строку, когда тексты перекрываются.

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT_TO_CELL): Отображает только строку в пределах ширины ячейки.

## **Укажите, как пересекать строку в выходном HTML с помощью HtmlCrossType.**

Следующий пример кода загружает[образец файла Excel](51740747.xlsx)и сохраняет его в формате HTML, указав разные[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)Пожалуйста, загрузите[вывод HTML](51740745.zip) файлы, созданные с помощью этого кода. Образец файла Excel содержит изображение, выделенное красным цветом, как показано на этом снимке экрана, который показывает эффект[**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType)значения в выходном HTML.

![дело:изображение_альтернативный_текст](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
