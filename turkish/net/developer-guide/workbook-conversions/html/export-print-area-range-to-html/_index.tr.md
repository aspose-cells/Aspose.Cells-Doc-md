---
title: Yazdırma alanı aralığını HTML olarak dışa aktar
type: docs
weight: 60
url: /tr/net/export-print-area-range-to/
---
## **Olası Kullanım Senaryoları**

 Bu, yalnızca yazdırma alanını, yani tüm sayfa yerine seçilen hücre aralığını HTML'e aktarmamız gereken yaygın bir senaryodur. Bu özellik PDF oluşturma için zaten mevcuttur, ancak şimdi bu görevi HTML için de gerçekleştirebilirsiniz. Önce çalışma sayfasının sayfa yapısı nesnesinde yazdırma alanını ayarlayın. Daha sonra, kullan[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) yalnızca seçilen aralığı dışa aktarmak için işaretle.

## Basit kod

Aşağıdaki örnek kod bir çalışma kitabı yükler ve ardından yazdırma alanını HTML'e verir. Bu özelliği test etmek için örnek dosya aşağıdaki bağlantıdan indirilebilir:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
