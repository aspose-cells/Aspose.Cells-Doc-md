---
title: Исключить неиспользуемые стили во время конвертации Excel в HTML
type: docs
weight: 30
url: /ru/java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Возможные сценарии использования**

Файл Microsoft Excel может содержать множество неиспользуемых стилей. При экспорте файла Excel в формат HTML эти неиспользуемые стили также экспортируются. Это может увеличить размер HTML. Вы можете исключить неиспользуемые стили во время конвертации файла Excel в HTML, используя свойство [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles). Когда оно установлено как **true**, все неиспользуемые стили исключаются из выходного HTML. В следующем скриншоте отображается пример неиспользуемого стиля в выходном HTML.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Исключить неиспользуемые стили во время преобразования Excel в HTML**

Следующий пример кода создает книгу и также создает неиспользуемый именованный стиль. Поскольку [**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles) установлен как **true**, этот неиспользуемый именованный стиль не будет экспортирован в [выходное HTML](61767781.zip). Но если установить как **false**, то этот неиспользуемый стиль будет присутствовать в выходном HTML, который затем можно увидеть в разметке HTML, как показано на скриншоте выше.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
