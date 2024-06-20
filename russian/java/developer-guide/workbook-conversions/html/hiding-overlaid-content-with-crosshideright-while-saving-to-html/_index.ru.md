---
title: Скрытие перекрывающегося контента с помощью CrossHideRight при сохранении в HTML
type: docs
weight: 100
url: /ru/java/hiding-overlaid-content-with-crosshideright-while-saving-to-html/
---

## **Возможные сценарии использования**

Когда вы сохраняете свой файл Excel в HTML, вы можете указать разные типы скрещивания для строк ячеек. По умолчанию Aspose.Cells генерирует HTML в соответствии с Microsoft Excel, но когда вы меняете [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) на [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT), то перекрывающийся или перекрывающийся контент с правой стороны ячейки скрывается.

## **Скрытие наложенного содержимого с помощью CrossHideRight при сохранении в HTML**

Следующий образец кода загружает [образец файла Excel](64716916.xlsx) и сохраняет его в [выходном HTML](64716915.zip) после установки [**HtmlSaveOptions.HtmlCrossStringType**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#HtmlCrossStringType) как [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT). Снимок экрана объясняет, как [**CROSS_HIDE_RIGHT**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlcrosstype#CROSS_HIDE_RIGHT) влияет на выходной HTML из стандартного вывода.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-HidingOverlaidContentWithCrossHideRightWhileSavingToHtml.java" >}}
