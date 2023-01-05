---
title: Экспорт комментариев при сохранении файла Excel на номер HTML
type: docs
weight: 60
url: /ru/python-java/export-comments-while-saving-excel-file-to/
---
## **Экспорт комментариев при сохранении файла Excel на номер HTML**
Когда Excel преобразуется в HTML, комментарии не экспортируются. Aspose.Cells for Python via Java позволяет экспортировать комментарии во время преобразования Excel в HTML. Для этого API предоставляет[HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments)имущество. Установка значения[HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments) собственность на**Истинный** экспортирует комментарии в вывод HTML.

На следующем снимке экрана показан выходной файл HTML, сгенерированный фрагментом кода примера.

![дело:изображение_альтернативный_текст](Export-Comments-while-Saving-Excel-file-to-Html.png)

В следующем примере кода демонстрируется экспорт комментариев во время преобразования Excel в HTML.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
