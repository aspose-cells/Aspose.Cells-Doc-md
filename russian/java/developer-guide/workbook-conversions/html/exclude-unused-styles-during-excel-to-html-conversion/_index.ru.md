---
title: Исключить неиспользуемые стили во время преобразования Excel в HTML
type: docs
weight: 30
url: /ru/java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Возможные сценарии использования**

Microsoft Файл Excel может содержать много неиспользуемых стилей. При экспорте файла Excel в формат HTML эти неиспользуемые стили также экспортируются. Это может увеличить размер HTML. Вы можете исключить неиспользуемые стили во время преобразования файла Excel в HTML с помощью[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)имущество. Когда вы установите его**истинный**, все неиспользуемые стили исключаются из выходных данных HTML. На следующем снимке экрана показан образец неиспользуемого стиля в выходных данных HTML.

![дело:изображение_альтернативный_текст](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Исключить неиспользуемые стили во время преобразования Excel в HTML**

В следующем примере кода создается рабочая книга, а также создается неиспользуемый именованный стиль. Поскольку[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)установлен на**истинный**, поэтому этот неиспользуемый именованный стиль не будет экспортирован в[вывод HTML](61767781.zip). Но если вы установите его**ЛОЖЬ**, то этот неиспользуемый стиль будет присутствовать внутри вывода HTML, который вы можете увидеть в разметке HTML, как показано на снимке экрана выше.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
