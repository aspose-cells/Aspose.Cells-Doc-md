---
title: Исключить неиспользуемые стили во время преобразования Excel в HTML
type: docs
weight: 30
url: /ru/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---
## **Исключить неиспользуемые стили во время преобразования Excel в HTML**
Microsoft Файлы Excel могут содержать множество неиспользуемых стилей. Когда эти файлы экспортируются в формат HTML, неиспользуемые стили также экспортируются. Это приводит к увеличению размера выходного HTML. Aspose.Cells для Python через Java поддерживает исключение этих стилей во время преобразования файла Excel в HTML. Для этого API предоставляет[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles)имущество. Установка значения[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) собственность на**Истинный** исключит все неиспользуемые стили из выходного HTML.

На следующем снимке экрана показаны неиспользуемые стили в файле HTML, которые будут удалены путем установки значения[HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) собственность на**Истинный**.

![дело:изображение_альтернативный_текст](HtmlSaveOptions-Exclude-Unused-Styles.png)

В следующем примере кода показано удаление неиспользуемых стилей во время преобразования Excel в HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
