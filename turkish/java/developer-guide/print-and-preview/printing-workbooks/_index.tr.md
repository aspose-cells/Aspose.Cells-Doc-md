---
title: Çalışma Kitaplarını Yazdırma
type: docs
weight: 20
url: /tr/java/printing-workbooks/
description: Java kullanarak çalışma sayfalarını ve çalışma kitabını yazdırma. Bu makale, Aspose.Cells for Java API kullanarak çalışma sayfalarını ve çalışma kitabını yazdırmak için Java kodunu sağlar.
keywords: printing workbooks, printing worksheets, printing workbook sheets, printing a workbook, printing workbook java, printing worksheets java, printing excel workbook java, print excel worksheet java, print workbook, print worksheet
---
{{% alert color="primary" %}}

Bu belge, geliştiricilere elektronik tabloların nasıl yazdırılacağını (kısa bir şekilde) anlamalarını sağlamak için tasarlanmıştır.

{{% /alert %}}

## Kullanım Senaryosu

Elektronik tablonuzu oluşturmayı bitirdikten sonra, ihtiyaçlarınız için büyük olasılıkla sayfanın basılı bir kopyasını yazdırmak isteyeceksiniz. Yazdırırken, seçiminizi belirtmediğiniz sürece, MS Excel tüm çalışma sayfası alanını yazdırmak istediğinizi varsayar. Aşağıdaki ekran görüntüsü, çalışma kitabını Excel ile yazdırmak için iletişim kutusunu gösterir.

![yapılacaklar:resim_alternatif_Metin](printing-workbooks_1.png)

**Figür:** Yazdır İletişim Kutusu

## Aspose.Cells kullanarak Çalışma Kitaplarını Yazdırma

 Aspose.Cells for Java sağlar[**yazıcıya**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String) ) yöntemi[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) sınıf. kullanarak[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)) yönteminde, yazdırma işi adının yanı sıra yazıcı adını da sağlayabilirsiniz.

## Basit kod

### Seçilen Çalışma Sayfasını Yazdır

 Aşağıdaki kod parçacığı,[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)) yöntemi, seçtiğiniz çalışma sayfasını yazdırmak için.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### Tüm Çalışma Kitabını Yazdır

 Şunu da kullanabilirsiniz:[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String) ) tüm çalışma kitabını yazdırma yöntemi. Aşağıdaki kod parçacığı,[**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String)) tüm çalışma kitabını yazdırma yöntemi.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## İlgili Makaleler

- [Aspose.Cells ile yazdırırken İş veya Belge Adını belirtin](/cells/tr/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
