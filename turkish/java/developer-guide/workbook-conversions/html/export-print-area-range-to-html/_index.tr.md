---
title: HTML ye Baskı Alanı Aralığını Dışa Aktar
type: docs
weight: 60
url: /tr/java/export-print-area-range-to-html/
---

## Olası Kullanım Senaryoları

Bu, sadece baskı alanını yani seçili hücre aralığını tüm sayfa yerine HTML'e dışa aktarmamız gereken çok yaygın bir senaryodur. Bu özellik zaten PDF dönüşümü için kullanılabilir, ancak artık bu görevi HTML için de gerçekleştirebilirsiniz. İlk olarak, çalışsayfa sayfa düzeni nesnesinde baskı alanını ayarlayın. Daha sonra yalnızca seçili aralığı dışa aktarmak için [**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly) özelliğini kullanın.

## Baskı alanı aralığını HTML'e dışa aktarmak için Java kodu

Aşağıdaki örnek kod, bir çalışma kitabı yükler ve ardından baskı alanını HTML'e dışa aktarır. Bu özelliği test etmek için örnek dosyayı aşağıdaki bağlantıdan indirebilirsiniz:

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

