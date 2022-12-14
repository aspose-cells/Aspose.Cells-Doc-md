---
title: Excel'i PDF'ye Dönüştür
type: docs
weight: 50
url: /tr/python-java/convert-excel-to-pdf/
description: Python ile Excel'i PDF'ye dönüştürme. Bu makale, Java API aracılığıyla Python için Python ve kullanımı kolay Aspose.Cells kullanarak Excel dosyalarını PDF'ye dönüştürmeyi göstermektedir.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---
## **Excel'i PDF'ye Dönüştür**

PDF belgeleri, kuruluşlar, devlet sektörleri ve bireyler arasında belge alışverişinde standart bir format olarak yaygın şekilde kullanılmaktadır. Yazılım geliştiricilerinden genellikle Microsoft Excel dosyalarını kolayca PDF belgelerine dönüştürmenin bir yolunu bulmaları istenir. Java API aracılığıyla Python için Aspose.Cells, Excel dosyalarını PDF belgelerine (PDF/A dahil) dönüştürme yeteneği sağlar. Aspose.Cell, elektronik tabloları yüksek derecede doğruluk ve aslına uygun olarak PDF'ye dönüştürür.

### **Doğrudan Dönüşüm**

Bir Excel dosyasını doğrudan PDF'ye kaydetmek için,[**çalışma kitabı.kaydet**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)yöntem ve geçiş[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) ikinci parametre olarak

Aşağıdaki kod parçacığı, kullanımını gösterir[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)ve[**çalışma kitabı.kaydet**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) Excel'i PDF biçimine dönüştürme yöntemi.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **Gelişmiş Dönüşüm**

PDF'ye dönüştürme üzerinde daha fazla kontrole sahip olmak için API,[**PdfKaydetmeSeçenekleri**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)sınıf. bu[**PdfKaydetmeSeçenekleri**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)sınıf, dönüştürme için farklı öznitelikler ayarlamak için kullanılabilir. Farklı özelliklerin ayarlanması[**PdfKaydetmeSeçenekleri**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)class, ortaya çıkan PDF dosyası için Yazdırma, Yazı Tipi, Güvenlik ve Sıkıştırma ayarları üzerinde kontrol sahibi olmanızı sağlar. En dikkate değer özellik,[**uyma**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance)Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlar.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

 e-tablonuz formüller içeriyorsa,[**Workbook.calculateFormula**](https://reference.aspose.com/cells/python/asposecells.api/workbook#calculateFormula()) yöntemi, elektronik tabloyu PDF'ye dönüştürmeden hemen önce. Bu, formüle bağlı değerlerin yeniden hesaplanmasını ve doğru değerlerin PDF'de işlenmesini sağlar.

{{% /alert %}}
