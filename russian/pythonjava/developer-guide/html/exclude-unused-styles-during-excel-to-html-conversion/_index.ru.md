---
title: Исключить неиспользуемые стили во время конвертации Excel в HTML
type: docs
weight: 30
url: /ru/python-java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Исключить неиспользуемые стили во время преобразования Excel в HTML**
Файлы Microsoft Excel могут содержать множество неиспользуемых стилей. При экспорте этих файлов в формат HTML также экспортируются неиспользуемые стили. Это приводит к увеличению размера выходного HTML. Aspose.Cells для Python via Java поддерживает исключение этих стилей во время конвертации файла Excel в HTML. Для этого API предоставляет свойство ExcludeUnusedStyles в HtmlSaveOptions. Установка значения свойства ExcludeUnusedStyles в True исключит все неиспользуемые стили из выходного HTML.

На следующем снимке экрана показаны неиспользуемые стили в HTML-файле, которые будут удалены путем установки значения свойства ExcludeUnusedStyles в True.

![todo:image_alt_text](HtmlSaveOptions-Exclude-Unused-Styles.png)

В следующем образце кода демонстрируется удаление неиспользуемых стилей во время конвертации Excel в HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
