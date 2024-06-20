---
title: Указать, как пересекать строку в выходном HTML с использованием HtmlCrossType
type: docs
weight: 140
url: /ru/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Возможные сценарии использования**

Когда ячейка содержит текст или строку, но она больше ширины ячейки, то строка переполняется, если следующая ячейка в следующем столбце пуста или пуста. При сохранении файла Excel в HTML вы можете контролировать этот переполнение, указав тип пересечения с помощью перечисления [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). Оно имеет следующие значения

- **HtmlCrossType.Default**: Отображается как в MS Excel, зависит от следующей ячейки. Если следующая ячейка пуста, строка пересечется или будет усечена.

- **HtmlCrossType.MSExport**: Отображение строки как при экспорте HTML из MS Excel.

- **HtmlCrossType.Cross**: Отображение строки пересечения HTML, производительность при создании больших HTML-файлов будет более чем в десять раз быстрее, чем при установке значения Default или FitToCell.

- **HtmlCrossType.FitToCell**: Отображение строки только в пределах ширины ячейки.

## **Указать, как пересекать строку в выходном HTML с использованием HtmlCrossType**

Следующий образец кода загружает [образец файла Excel](51740732.xlsx) и сохраняет его в формат HTML, указав разные [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). Пожалуйста, загрузите [сгенерированные выходные HTML-файлы](51740734.zip) с этим кодом. Образец файла Excel содержит изображение со светло-красной рамкой как показано на этом скриншоте, который показывает эффект значений [**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) на выходном HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
