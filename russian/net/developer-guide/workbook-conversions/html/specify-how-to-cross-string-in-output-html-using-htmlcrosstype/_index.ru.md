---
title: Укажите, как пересекать строку в выходном HTML с помощью HtmlCrossType.
type: docs
weight: 140
url: /ru/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **Возможные сценарии использования**

Когда ячейка содержит текст или строку, но она больше, чем ширина ячейки, тогда строка переполняется, если следующая ячейка в следующем столбце имеет значение null или пуста. Когда вы сохраняете файл Excel в формате HTML, вы можете управлять этим переполнением, указав перекрестный тип с помощью[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) перечисление. Он имеет следующие значения

- **HtmlCrossType.Default**: Отображение как в MS Excel, зависит от следующей ячейки. Если следующая ячейка пуста, строка будет пересекаться или будет усечена.

- **HtmlCrossType.MSExport**: Отобразить строку, как в MS Excel, экспортирующую HTML.

- **HtmlCrossType.Cross**: отображать перекрестную строку HTML, производительность при создании больших файлов HTML будет более чем в десять раз выше, чем при установке значения по умолчанию или FitToCell.

- **HtmlCrossType.FitToCell**: Отображает только строку в пределах ширины ячейки.

## **Укажите, как пересекать строку в выходном HTML с помощью HtmlCrossType.**

 Следующий пример кода загружает[образец файла Excel](51740732.xlsx) и сохраняет его в формате HTML, указав разные[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) . Пожалуйста, загрузите[вывод HTML](51740734.zip) генерируется с помощью этого кода. Образец файла Excel содержит изображение, выделенное красным цветом, как показано на этом снимке экрана, который показывает эффект[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) значения в выходном HTML.

![дело:изображение_альтернативный_текст](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
