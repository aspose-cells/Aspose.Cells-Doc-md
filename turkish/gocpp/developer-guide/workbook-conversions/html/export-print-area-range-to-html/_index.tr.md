---
title: Golang kullanarak C++ ile Yazdırma Alanı Aralığını HTML ye dışa aktar
linktitle: Yazdırma Alanı Aralığını HTML ye Dışa Aktar
type: docs
weight: 60
url: /tr/go-cpp/export-print-area-range-to/
description: Aspose.Cells for C++ kullanarak yazdırma alanı aralığını HTML ye nasıl dışa aktarmayı öğrenin.
---

## **Olası Kullanım Senaryoları**

Bu, genellikle tüm sayfa yerine yalnızca yazdırma alanını, yani seçili hücre aralığını HTML'ye dışa aktarmamız gerektiğinde karşılaşılan yaygın bir senaryodur. Bu özellik halihazırda PDF renderlama için kullanılabilir durumda; ancak artık bu işlemi HTML için de gerçekleştirebilirsiniz. İlk olarak, çalışma sayfasının sayfa düzeni nesnesinde yazdırma alanını ayarlayın. Daha sonra, yalnızca seçilen aralığı dışa aktarmak için [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportprintareaonly/) bayrağını kullanın.

## **Örnek Kod**

Aşağıdaki örnek kod, bir çalışma kitabını yükler ve ardından yazdırma alanını HTML'ye dışa aktarır. Bu özelliği test etmek için kullanılacak örnek dosya aşağıdaki bağlantıdan indirilebilir:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportPrintAreaRangeToHtml.go" >}}
