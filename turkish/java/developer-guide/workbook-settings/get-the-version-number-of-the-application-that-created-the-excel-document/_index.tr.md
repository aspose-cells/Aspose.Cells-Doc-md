---
title: Excel Belgesini Oluşturan Uygulamanın Sürüm Numarasını Almak
type: docs
weight: 150
url: /tr/java/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

Sıklıkla, bir Microsoft Excel belgesini oluşturan uygulamanın sürüm numarasını bilmeniz gerekir. Aspose.Cells bu amaca yönelik [**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version) özelliğini sağlar.

{{% /alert %}}

Aşağıdaki örnek kod, [**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version) özelliğinin nasıl kullanılacağını göstermektedir. Microsoft Excel 2003, 2007, 2010 ve 2013 ile oluşturulmuş Excel dosyalarını yükler ve bu Excel belgelerini oluşturan uygulamanın sürüm numarasını yazdırır.

Referansınız için, aşağıda örnek kodun oluşturduğu konsol çıktısı bulunmaktadır.

{{< highlight java >}}

Excel 2003 XLS Version: 726502

Excel 2007 XLS Version: 786432

Excel 2010 XLS Version: 917504

Excel 2013 XLS Version: 983040

Excel 2007 XLSX Version: 12.0000

Excel 2010 XLSX Version: 14.0300

Excel 2013 XLSX Version: 15.0300

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetVersionNumberofApplication-GetVersionNumberofApplication.java" >}}
