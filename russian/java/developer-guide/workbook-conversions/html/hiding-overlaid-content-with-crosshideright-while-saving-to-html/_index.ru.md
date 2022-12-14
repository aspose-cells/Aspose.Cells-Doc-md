---
title: Скрытие наложенного содержимого с помощью CrossHideRight при сохранении в HTML
type: docs
weight: 100
url: /ru/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---
## **Возможные сценарии использования**

Когда вы сохраняете файл Excel в формате HTML, вы можете указать различные перекрестные типы для строк ячеек. По умолчанию Aspose.Cells генерирует HTML в соответствии с Microsoft Excel, но при изменении[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)к[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)затем он скрывает все строки с правой стороны ячейки, которые перекрываются или перекрываются со строкой ячейки.

## **Скрытие наложенного содержимого с помощью CrossHideRight при сохранении в HTML**

Следующий пример кода загружает[образец файла Excel](64716916.xlsx)и сохраняет его в[вывод HTML](64716915.zip)после установки[**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType)в качестве[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT). Скриншот объясняет, как[**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT)влияет на вывод HTML из вывода по умолчанию.

![дело:изображение_альтернативный_текст](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
