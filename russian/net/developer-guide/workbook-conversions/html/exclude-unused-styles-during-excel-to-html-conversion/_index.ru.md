---
title: Исключить неиспользуемые стили во время преобразования Excel в HTML
type: docs
weight: 30
url: /ru/net/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Возможные сценарии использования**

Microsoft Файл Excel может содержать много неиспользуемых стилей. При экспорте файла Excel в формат HTML эти неиспользуемые стили также экспортируются. Это может увеличить размер HTML. Вы можете исключить неиспользуемые стили во время преобразования файла Excel в HTML с помощью[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) имущество. Когда вы установите его**истинный**все неиспользуемые стили исключаются из выходного HTML. На следующем снимке экрана показан пример неиспользуемого стиля внутри выходного HTML.

![дело:изображение_альтернативный_текст](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Исключить неиспользуемые стили во время преобразования Excel в HTML**

В следующем примере кода создается рабочая книга, а также создается неиспользуемый именованный стиль. Поскольку[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) установлен на**истинный** , этот неиспользуемый именованный стиль не будет экспортирован в[вывод HTML](61767778.zip) . Но если вы установите его на**ЛОЖЬ**, то этот неиспользуемый стиль будет присутствовать внутри выходного HTML-кода, который вы сможете увидеть в HTML-разметке, как показано на снимке экрана выше.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExcludeUnusedStylesInExcelToHTML.cs" >}}
