---
title: Экспорт комментариев при сохранении файла Excel в HTML
type: docs
weight: 40
url: /ru/java/export-comments-while-saving-excel-file-to-html/
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML комментарии не экспортируются. Однако Aspose.Cells предоставляет эту функцию с использованием свойства [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#IsExportComments). Если вы установите его **true**, то HTML также будет отображать комментарии, присутствующие в вашем файле Excel.

## **Экспорт комментариев при сохранении файла Excel в Html**

Следующий образец кода объясняет использование свойства [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#IsExportComments). На снимке экрана показан эффект кода на HTML, когда свойство установлено в **true**. Пожалуйста, загрузите [образец файла Excel](50528270.xlsx) и [сгенерированный HTML](50528269) для справки.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ExportCommentsWhileSavingExcelFileToHtml.java" >}}
{{< app/cells/assistant language="java" >}}
