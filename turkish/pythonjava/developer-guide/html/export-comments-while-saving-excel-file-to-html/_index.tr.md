---
title: Excel Dosyasını HTML ye Kaydederken Yorumları Dışa Aktar
type: docs
weight: 60
url: /tr/python-java/export-comments-while-saving-excel-file-to/
---

## **Excel Dosyasını HTML'ye Kaydederken Yorumları Dışa Aktar**
Excel HTML'e dönüştürüldüğünde, yorumlar dışarı aktarılmaz. Aspose.Cells for Python via Java, Excel'den HTML'e dönüşüm sırasında yorumları dışarı aktarma özelliği sağlar. Bunun için API, [HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments) özelliğini sağlar. [HtmlSaveOptions.IsExportComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#IsExportComments) özelliğinin değerini **True** olarak ayarlamak, çıktı HTML'de yorumları dışarı aktarır.

Aşağıdaki ekran görüntüsü, örnek kod parçası tarafından oluşturulan çıktı HTML dosyasını gösterir.

![todo:image_alt_text](Export-Comments-while-Saving-Excel-file-to-Html.png)

Aşağıdaki örnek kod, Excel'den HTML'e dönüşüm sırasında yorumları dışarı aktarmayı gösterir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
