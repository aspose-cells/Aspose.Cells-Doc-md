---
title: Скрытие перекрывающегося контента с помощью CrossHideRight при сохранении в HTML
type: docs
weight: 100
url: /ru/python-net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML вы можете указать разные типы пересечения для строк ячеек. По умолчанию Aspose.Cells для Python via .NET генерирует HTML по стандартам Microsoft Excel, но при изменении типа пересечения на [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/) он скрывает все строки справа от ячейки, которые налегают или перекрываются с содержимым ячейки.

## **Скрытие перекрывающегося содержимого с CrossHideRight при сохранении в Html**

Следующий образец кода загружает [образец файла Excel](64716894.xlsx) и сохраняет его в [выходной HTML](64716893.zip) после установки [**HtmlSaveOptions.html_cross_string_type**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/html_cross_string_type) в [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/). На скриншоте показано, как [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlcrosstype/) влияет на выходной HTML по умолчанию.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.py" >}}
{{< app/cells/assistant language="python-net" >}}
