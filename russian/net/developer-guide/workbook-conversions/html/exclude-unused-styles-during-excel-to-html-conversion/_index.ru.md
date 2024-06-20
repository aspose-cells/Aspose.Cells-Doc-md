---
title: Исключить неиспользуемые стили во время конвертации Excel в HTML
type: docs
weight: 30
url: /ru/net/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Возможные сценарии использования**

Файл Microsoft Excel может содержать множество неиспользуемых стилей. При экспорте файла Excel в формат HTML эти неиспользуемые стили также экспортируются. Это может увеличить размер HTML. Вы можете исключить неиспользуемые стили во время конвертации файла Excel в HTML, используя свойство [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles). Когда вы устанавливаете его **true**, все неиспользуемые стили исключаются из выходного HTML. На следующем скриншоте отображается образец неиспользуемого стиля в выходном HTML.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Исключить неиспользуемые стили во время преобразования Excel в HTML**

Следующий пример кода создает книгу и также создает неиспользуемый именованный стиль. Поскольку [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles) установлен в **true**, этот неиспользуемый именованный стиль не будет экспортирован в [выходное HTML](61767778.zip). Но если вы установите его в **false**, то этот неиспользуемый стиль будет присутствовать в выходном HTML, который вы сможете увидеть в разметке HTML, как показано на скриншоте выше.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExcludeUnusedStylesInExcelToHTML.cs" >}}
