---
title: HTML ye Baskı Alanı Aralığını Dışa Aktar
type: docs
weight: 60
url: /tr/net/export-print-area-range-to/
---

## **Olası Kullanım Senaryoları**

Bu, tüm sayfaların değil, yalnızca seçilen hücre aralığının dışa aktarılması gereken yaygın bir senaryodur. Bu özellik zaten PDF dönüştürme için mevcut olup, şimdi bunu HTML için de yapabilirsiniz. İlk olarak, çalışma sayfasının sayfa düzeni nesnesinde baskı alanını ayarlayın. Daha sonra yalnızca seçili aralığı dışa aktarmak için [**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) bayrağını kullanın.

## Örnek Kod

Aşağıdaki örnek kod, bir çalışma kitabı yükler ve daha sonra baskı alanını HTML'e dışa aktarır. Bu özelliği test etmek için örnek dosyayı aşağıdaki bağlantıdan indirebilirsiniz:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
