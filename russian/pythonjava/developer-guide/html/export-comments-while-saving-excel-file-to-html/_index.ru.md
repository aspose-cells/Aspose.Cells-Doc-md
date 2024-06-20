---
title: Экспорт комментариев при сохранении файла Excel в HTML
type: docs
weight: 60
url: /ru/python-java/export-comments-while-saving-excel-file-to/
---

## **Экспортировать комментарии при сохранении файла Excel в HTML**
При конвертации Excel в HTML комментарии не экспортируются. Aspose.Cells для Python via Java предоставляет возможность экспортировать комментарии во время конвертации Excel в HTML. Для этого API предоставляет свойство IsExportComments в HtmlSaveOptions. Установка значения свойства IsExportComments в True экспортирует комментарии в выходное HTML.

На следующем снимке экрана показан выходной HTML-файл, сгенерированный образцом кода.

![todo:image_alt_text](Export-Comments-while-Saving-Excel-file-to-Html.png)

В следующем образце кода демонстрируется экспорт комментариев во время конвертации Excel в HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
