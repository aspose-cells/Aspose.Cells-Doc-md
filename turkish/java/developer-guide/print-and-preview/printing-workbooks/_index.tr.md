---
title: Elektronik Tabloları Yazdırma
type: docs
weight: 20
url: /tr/java/printing-workbooks/
description: Java kullanarak elektronik tabloları ve çalışma kitaplarını nasıl yazdıracağınızı anlatan bir makale. Bu makale Aspose.Cells for Java API sını kullanarak Java kodunu elektronik tabloları ve çalışma kitaplarını yazdırmak için sağlar.
keywords: çalışma kitapları yazdırma, çalışma sayfalarını yazdırma, çalışma kitabı sayfalarını yazdırma, bir çalışma kitabı yazdırma, çalışma kitabı java yazdırmak, çalışma sayfalarını java yazdırmak, excel çalışma kitabı java yazdırmak, excel çalışma sayfası java yazdırmak, çalışma kitabı yazdırma, çalışma sayfası yazdırma
---

{{% alert color="primary" %}}

Bu belge, geliştiricilere elektronik tabloların nasıl yazdırılacağının (kapsamlı bir şekilde) anlayışını sağlamak için tasarlanmıştır.

{{% /alert %}}

## Kullanım Senaryosu

Elektronik tablonuzu oluşturmayı tamamladıktan sonra muhtemelen ihtiyacınıza göre sayfanın kağıda basılı bir kopyasını almak isteyeceksinizdir. Yazdırdığınızda, MS Excel, seçim yapmadıkça bütün çalışma sayfasını yazdırmak istediğinizi varsayar. Aşağıdaki ekran görüntüsü, Excel ile çalışma kitabını yazdırmak için iletişim kutusunu göstermektedir.

![todo:image_alt_text](printing-workbooks_1.png)

**Şekil:** Yazdırma İletişim Kutusu

## Aspose.Cells Kullanarak Çalışma Kitaplarını Yazdırma

Aspose.Cells for Java, [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) sınıfının [**toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-) metodunu sağlar. [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-) metodunu kullanarak yazıcı adını ve yazdırma işi adını sağlayabilirsiniz.

## Örnek Kod

### Seçili Çalışma Sayfasını Yazdır

Aşağıdaki kod örneği, [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-) metodunun seçili çalışma sayfasını yazdırmak için nasıl kullanılacağını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### Bütün Çalışma Kitabını Yazdır

Bütün çalışma kitabını yazdırmak için [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-) metodunu kullanabilirsiniz. Aşağıdaki kod örneği, [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-) metodunun bütün çalışma kitabını yazdırmak için nasıl kullanılacağını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## İlgili Makaleler

- [Aspose.Cells ile yazdırırken İş veya Belge Adı belirtin](/cells/tr/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
{{< app/cells/assistant language="java" >}}
