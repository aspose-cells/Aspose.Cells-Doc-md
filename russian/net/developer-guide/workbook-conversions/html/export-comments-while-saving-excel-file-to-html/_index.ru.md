---
title: Экспорт комментариев при сохранении файла Excel в HTML
type: docs
weight: 40
url: /ru/net/export-comments-while-saving-excel-file-to/
---

## **Возможные сценарии использования**

Когда вы сохраняете свой Excel файл в HTML, комментарии не экспортируются. Однако Aspose.Cells предоставляет эту функцию с помощью свойства [**HtmlSaveOptions.IsExportComments**](https://docs.aspose.com/cells/net/export-comments-while-saving-excel-file-to/). Если вы установите его **true**, то HTML также будет отображать комментарии, присутствующие в вашем Excel файле.

## **Экспортировать комментарии при сохранении файла Excel в HTML**

Следующий образец кода объясняет использование свойства [**HtmlSaveOptions.IsExportComments**](https://docs.aspose.com/cells/net/export-comments-while-saving-excel-file-to/). На скриншоте показан эффект этого кода на HTML, когда он установлен в **true**. Для справки загрузите [образец Excel файла](50528260.xlsx) и [сгенерированный HTML](5052826.txt).

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ExportCommentsWhileSavingExcelFileToHtml.cs" >}}
