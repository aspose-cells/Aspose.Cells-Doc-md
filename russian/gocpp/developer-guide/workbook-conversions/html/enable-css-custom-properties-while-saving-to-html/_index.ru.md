---
title: Включите пользовательские свойства CSS при сохранении в HTML с помощью Golang через C++
linktitle: Включить пользовательские CSS свойства при сохранении в HTML
type: docs
weight: 320
url: /ru/go-cpp/enable-css-custom-properties-while-saving-to-html/
description: Узнайте, как включить пользовательские свойства CSS при сохранении файлов Excel в HTML с помощью Aspose.Cells for C++. Улучшите производительность за счет уменьшения повторяющихся данных изображений.
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML, при наличии нескольких случаев одного изображения в base64, с помощью пользовательского свойства данные изображения нужно сохранять только один раз, что повышает производительность полученного HTML. Используйте свойство [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getenablecsscustomproperties/) и установите его в **true** при сохранении в HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Включить пользовательские свойства CSS при сохранении в HTML**

Следующий пример показывает использование свойства [**HtmlSaveOptions.GetEnableCssCustomProperties()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getenablecsscustomproperties/). Скриншот отображает эффект этого свойства, когда оно не установлено в **true**. Скачайте [пример файла Excel](50528260.xlsx), используемый в этом коде, и [сгенерированный HTML](50528261.zip) для ознакомления.

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnableCssCustomPropertiesWhileSavingToHtml.go" >}}
