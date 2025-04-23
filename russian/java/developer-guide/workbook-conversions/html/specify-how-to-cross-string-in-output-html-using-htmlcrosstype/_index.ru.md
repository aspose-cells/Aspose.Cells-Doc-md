---
title: Указать, как пересекать строку в выходном HTML с использованием HtmlCrossType
type: docs
weight: 140
url: /ru/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Возможные сценарии использования**

Когда ячейка содержит текст или строку, но она больше ширины ячейки, то строка переполняется, если следующая ячейка в следующем столбце пуста или пуста. При сохранении вашего файла Excel в формате HTML вы можете контролировать этот переполнение, указав тип пересечения с использованием перечисления [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType). Оно имеет следующие значения

- [**HtmlCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT): Отображать как в MS Excel, что зависит от следующей ячейки. Если следующая ячейка пуста, строка пересечется или будет усечена.

- [**HtmlCrossType.MS_EXPORT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#MS-EXPORT): Отображать строку как MS Excel при экспортировании в HTML.

- [**HtmlCrossType.CROSS**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS): Отображать пересечение строк HTML, производительность создания больших файлов HTML будет более чем в десять раз быстрее, чем установка значения в [**DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#DEFAULT) или [**FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT-TO-CELL).

- [**HtmlCrossType.CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS-HIDE-RIGHT): Отображать пересечение строк HTML и скрывать правую строку, когда тексты перекрываются.

- [**HtmlCrossType.FIT_TO_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#FIT-TO-CELL): Отображать только строку в пределах ширины ячейки.

## **Указать, как пересекать строку в выходном HTML с использованием HtmlCrossType**

В следующем образце кода загружается [образец Excel файла](51740747.xlsx) и сохраняется в HTML формате, указав разные [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType). Пожалуйста, скачайте [выходные файлы HTML](51740745.zip), сгенерированные этим кодом. Образец Excel файла содержит изображение, ограниченное красным цветом, как показано на этом снимке экрана, который показывает эффект значений [**HtmlCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlCrossType) в выходном HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.java" >}}
{{< app/cells/assistant language="java" >}}
