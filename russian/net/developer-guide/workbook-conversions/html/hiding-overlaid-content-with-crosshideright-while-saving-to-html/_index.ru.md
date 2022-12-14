---
title: Скрытие наложенного содержимого с помощью CrossHideRight при сохранении в HTML
type: docs
weight: 100
url: /ru/net/hiding-overlaid-content-with-crosshideright-while-saving-to/
---
## **Возможные сценарии использования**

Когда вы сохраняете файл Excel в формате HTML, вы можете указать различные перекрестные типы для строк ячеек. По умолчанию Aspose.Cells генерирует HTML в соответствии с Microsoft Excel, но когда вы меняете перекрестный тип на[**КрестСкрытьПраво**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype), то он скрывает все строки с правой стороны ячейки, которые перекрываются или перекрываются со строкой ячейки.

## **Скрытие наложенного содержимого с помощью CrossHideRight при сохранении в HTML**

 Следующий пример кода загружает[образец файла Excel](64716894.xlsx) и сохраняет его в[вывод HTML](64716893.zip) после установки[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/htmlcrossstringtype)в качестве[**КрестСкрытьПраво**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype). Скриншот объясняет, как[**КрестСкрытьПраво**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype)влияет на вывод HTML из вывода по умолчанию.

![дело:изображение_альтернативный_текст](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.cs" >}}
