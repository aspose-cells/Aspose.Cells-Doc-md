---
title: Указать, как пересекать строку в выходном HTML с использованием HtmlCrossType
type: docs
weight: 140
url: /ru/python-net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---

## **Возможные сценарии использования**

Когда ячейка содержит текст или строку, но она больше ширины ячейки, то строка переполняется, если следующая ячейка в следующем столбце пуста или пуста. При сохранении файла Excel в HTML вы можете контролировать этот переполнение, указав тип пересечения с помощью перечисления [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype). Оно имеет следующие значения

- **HtmlCrossType.DEFAULT**: отображение как в MS Excel, зависит от следующей ячейки. Если следующая ячейка пуста, строка пересекается или будет усечена.

- **HtmlCrossType.MS_EXPORT**: отображение строки как при экспорте HTML в MS Excel.

- **HtmlCrossType.CROSS**: отображение пересекающихся строк в HTML, создание больших HTML-файлов будет в более чем в десять раз быстрее, чем при установке значения по умолчанию или FitToCell.

- **HtmlCrossType.CROSS_HIDE_RIGHT**: отображение пересекающихся строк в HTML и скрытие правой строки, когда тексты перекрываются.

- **HtmlCrossType.FIT_TO_CELL**: отображение только внутри ширины ячейки.

## **Указать, как пересекать строку в выходном HTML с использованием HtmlCrossType**

Следующий образец кода загружает [образец файла Excel](51740732.xlsx) и сохраняет его в формат HTML, указав разные [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype). Пожалуйста, загрузите [сгенерированные выходные HTML-файлы](51740734.zip) с этим кодом. Образец файла Excel содержит изображение со светло-красной рамкой как показано на этом скриншоте, который показывает эффект значений [**HtmlCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype) на выходном HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SpecifyHtmlCrossTypeInOutputHTML.py" >}}
