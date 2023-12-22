---
title: Her Çalışma Sayfasını Farklı Bir PDF Dosyasına Kaydetme
type: docs
weight: 130
url: /tr/python-net/save-each-worksheet-to-a-different-pdf-file/
description: Her Çalışma Sayfasını Aspose.Cells for Python via .NET API ile Farklı bir PDF Dosyasına nasıl kaydedeceğinizi öğrenin.
keywords: Python Save Each Worksheet to a Different PDF File
---
{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET, XLS dosyasının (resimler, grafikler vb. içeren) PDF belgeye dönüştürülmesini destekler. Aspose.Cells for Python via .NET, bir e-tabloyu PDF'e dönüştürmek için bağımsız olarak çalışabilir ve dönüşüm için Aspose.PDF for .NET'i kullanmanıza gerek yoktur. Tüm süreç bellekte yapılabildiğinden dönüştürme, yazılımın herhangi bir geçici dosya oluşturmasını veya kullanmasını gerektirmez.

{{% /alert %}} 
##  **Her Çalışma Sayfasını Farklı Bir PDF Dosyasına Kaydetme**
 Farklı PDF dosyaları oluşturmak için her çalışma sayfasını şablon Excel dosyanıza kaydetmeniz gerekiyorsa, bunu kolayca başarabilirsiniz. Bir sayfa dizini ayarlamayı deneyebilirsiniz**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** tek seferde PDF'e işleme seçeneği.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

 E-tablonuz formüller içeriyorsa, aramak en iyisidir.[**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) e-tabloyu PDF biçimine dönüştürmeden hemen önce. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlayacaktır.

{{% /alert %}}
