---
title: Yazdırma alanı aralığını HTML'ye aktar
type: docs
weight: 60
url: /tr/java/export-print-area-range-to-html/
---
## Olası Kullanım Senaryoları

Bu, yalnızca yazdırma alanını, yani tüm sayfa yerine seçili hücre aralığını HTML'ye aktarmamız gereken çok yaygın bir senaryodur. Bu özellik PDF oluşturma için zaten mevcuttur, ancak artık bu görevi HTML için de gerçekleştirebilirsiniz. İlk olarak, çalışma sayfasının sayfa düzeni nesnesinde yazdırma alanını ayarlayın. Daha sonra kullanım[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly)yalnızca seçilen aralığı dışa aktarma özelliği.

## Yazdırma alanı aralığını HTML'ye dışa aktarmak için Java kodu

Aşağıdaki örnek kod bir çalışma kitabı yükler ve ardından yazdırma alanını HTML'ye verir. Bu özelliği test etmek için örnek dosya aşağıdaki bağlantıdan indirilebilir:

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

