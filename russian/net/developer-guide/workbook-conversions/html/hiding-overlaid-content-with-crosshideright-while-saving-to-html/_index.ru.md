---
title: Скрытие перекрывающегося контента с помощью CrossHideRight при сохранении в HTML
type: docs
weight: 100
url: /ru/net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Возможные сценарии использования**

Когда вы сохраняете свой Excel файл в HTML, вы можете указать различные типы крестиков для строк ячейки. По умолчанию Aspose.Cells генерирует HTML в соответствии с Microsoft Excel, но когда вы изменяете тип крестика на [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype), то скрываются все строки справа от строки ячейки, которые перекрываются или перекрывают строку ячейки.

## **Скрытие перекрывающегося содержимого с CrossHideRight при сохранении в Html**

Следующий образец кода загружает [образец файла Excel](64716894.xlsx) и сохраняет его в [выходной HTML](64716893.zip) после установки [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype) в [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). На скриншоте показано, как [**CrossHideRight**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) влияет на выходной HTML по умолчанию.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
{{< app/cells/assistant language="csharp" >}}
