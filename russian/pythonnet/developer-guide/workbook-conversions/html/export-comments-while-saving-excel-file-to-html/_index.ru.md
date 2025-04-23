---
title: Экспорт комментариев при сохранении файла Excel в HTML
type: docs
weight: 40
url: /ru/python-net/export-comments-while-saving-excel-file-to/
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML комментарии не экспортируются. Однако Aspose.Cells для Python via .NET предоставляет эту функцию с помощью свойства [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments). Если установить его значение в **true**, то HTML также будет отображать комментарии, присутствующие в файле Excel.

## **Экспортировать комментарии при сохранении файла Excel в HTML**

Следующий образец кода объясняет использование свойства [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments). На скриншоте показан эффект этого кода на HTML, когда он установлен в **true**. Для справки загрузите [образец Excel файла](50528260.xlsx) и [сгенерированный HTML](5052826.txt).

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
