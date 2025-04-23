---
title: Включить пользовательские CSS свойства при сохранении в HTML
type: docs
weight: 320
url: /ru/java/enable-css-custom-properties-while-saving-to-html/
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML, для сценария с несколькими вхождениями одной картинки в формате base64, с помощью пользовательского свойства данные изображения нужно сохранять только один раз, что повышает производительность итогового html. Пожалуйста, используйте свойство [**HtmlSaveOptions.EnableCssCustomProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions/properties/#EnableCssCustomProperties) и установите его на **true** при сохранении в HTML.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **Включить пользовательские свойства CSS при сохранении в HTML**

Следующий пример кода показывает использование свойства [**HtmlSaveOptions.EnableCssCustomProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions/properties/#EnableCssCustompPoperties). Скриншот показывает эффект этого свойства, когда оно не установлено в true. Пожалуйста, скачайте [пробный файл Excel](50528260.xlsx), используемый в этом коде, и [выводимый HTML](50528261.zip) для справки.



## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-Java-HTML-·java" >}}
{{< app/cells/assistant language="java" >}}
