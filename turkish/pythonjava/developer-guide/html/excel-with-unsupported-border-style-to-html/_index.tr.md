---
title: HTML olarak desteklenmeyen kenarlık stiliyle Excel
type: docs
weight: 80
url: /tr/python-java/excel-with-unsupported-border-style-to/
---

## **HTML'ye desteklenmeyen kenarlık stiline sahip Excel**
Microsoft Excel, Web Tarayıcılar tarafından desteklenmeyen bazı kesikli sınırları destekler. Aspose.Cells kullanılarak bu tür dosyalar HTML'e dönüştürüldüğünde, bu sınırlar kaldırılır. Ancak, Aspose.Cells for Python via Java, [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) özelliği ile benzer sınırların görüntülenmesini destekler. [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) özelliğinin değerini **True** olarak ayarlayarak desteklenmeyen sınırların dışarı aktarılmasını sağlayabilirsiniz.

Aşağıdaki örnek kod [örnek Excel dosyasını](sampleExportSimilarBorderStyle.xlsx) yükler ve görüntülenmeyen bazı sınırları içeren bir ekran görüntüsünde gösterildiği gibi. Ekran görüntüsü, [çıktı HTML](outputExportSimilarBorderStyle.zip) içinde [HtmlSaveOptions.ExportSimilarBorderStyle](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExportSimilarBorderStyle) özelliğinin etkisini daha ayrıntılı olarak gösterir.

![todo:image_alt_text](Export-Similar-Border-Style.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExportSimilarBorderStyle.py" >}}
