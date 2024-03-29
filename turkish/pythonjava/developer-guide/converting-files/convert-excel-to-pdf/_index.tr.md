﻿---
title: Excel'i PDF'e dönüştür
type: docs
weight: 50
url: /tr/python-java/convert-excel-to-pdf/
description: Python ile Excel'i PDF'e dönüştürme. Bu makale, Python ve kullanımı kolay Aspose.Cells for Python via Java API kullanarak Excel dosyalarını PDF'e dönüştürmeyi göstermektedir.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---
## **Excel'i PDF'e dönüştür**

PDF belgeleri, kuruluşlar, devlet sektörleri ve bireyler arasında belge alışverişinde standart bir format olarak yaygın şekilde kullanılmaktadır. Yazılım geliştiricilerden genellikle Microsoft Excel dosyalarını kolayca PDF belgelerine dönüştürmenin bir yolunu bulmaları istenir. Aspose.Cells for Python via Java API, Excel dosyalarını PDF belgesine (PDF/A dahil) dönüştürme olanağı sağlar. Aspose.Cell, elektronik tabloları yüksek derecede doğruluk ve doğrulukla PDF'e dönüştürür.

### **Doğrudan Dönüşüm**

Bir Excel dosyasını doğrudan PDF'e kaydetmek için,[**çalışma kitabı.kaydet**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) yöntem ve geçiş[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) ikinci parametre olarak

Aşağıdaki kod parçacığı, kullanımını gösterir[**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)ve[**çalışma kitabı.kaydet**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) Excel'i PDF biçimine dönüştürme yöntemi.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **Gelişmiş Dönüşüm**

PDF'e dönüştürme üzerinde daha fazla kontrole sahip olmak için API,[**PdfKaydetmeSeçenekleri**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)sınıf. bu[**PdfKaydetmeSeçenekleri**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)sınıf, dönüştürme için farklı öznitelikler ayarlamak için kullanılabilir. Farklı özelliklerin ayarlanması[**PdfKaydetmeSeçenekleri**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)class, ortaya çıkan PDF dosyası için Yazdırma, Yazı Tipi, Güvenlik ve Sıkıştırma ayarları üzerinde kontrol sahibi olmanızı sağlar. En dikkate değer özellik,[**uyma**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance)Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlar.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

 e-tablonuz formüller içeriyorsa,[**Workbook.calculateFormula**](https://reference.aspose.com/cells/python/asposecells.api/workbook#calculateFormula()) yöntemi, elektronik tabloyu PDF'e dönüştürmeden hemen önce. Bu, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}
