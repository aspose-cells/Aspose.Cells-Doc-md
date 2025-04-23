---
title: Отключить CSS при сохранении в HTML
type: docs
weight: 320
url: /ru/java/disable-css-while-saving-to-html/
---

## **Возможные сценарии использования**

Когда вы сохраняете файл Excel в HTML формате с одной страницей, обычно элементы CSS встроены внутри файла HTML и находятся в разделе HEAD. Если этот файл прикрепить как содержимое / тело письма, элементы CSS обычно будут удалены большинством почтовых клиентов, что приведёт к неправильному отображению. В версии Aspose.Cells 24.12 введена опция, которая позволяет по желанию отключить CSS, чтобы стили применялись прямо внутри самих элементов HTML. Чтобы задать html как содержимое / тело письма, используйте свойство [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions/properties/#DisableCss) и установите его в **true**.



## **Отключить CSS при сохранении в HTML**

Следующий пример кода показывает использование свойства [**HtmlSaveOptions.DisableCss**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions/properties/#DisableCss). 



## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-java-HTML-DisableCss-1.java" >}}
{{< app/cells/assistant language="java" >}}
