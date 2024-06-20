---
title: Excel i PDF ye Dönüştür
type: docs
weight: 50
url: /tr/python-java/convert-excel-to-pdf/
description: Python ile Excel i PDF e nasıl dönüştürebileceğiniz hakkında bilgi edinin. Bu makale, Python ve kullanımı kolay Aspose.Cells for Python via Java API sını kullanarak Excel dosyalarını PDF e dönüştürmeyi göstermektedir.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---

## **Excel'i PDF'e dönüştür**

PDF belgeleri, kuruluşlar, hükümet sektörleri ve bireyler arasında belge değişimi için standart bir formatta yaygın olarak kullanılır. Yazılım geliştiricileri genellikle Microsoft Excel dosyalarını PDF belgelerine kolayca dönüştürmek için bir yöntem geliştirmeleri istenir. Aspose.Cells for Python via Java API, Excel dosyalarını PDF belgelerine (PDF/A dahil) dönüştürme olanağı sağlar. Aspose.Cell, elektronik tabloları yüksek doğruluk ve sadakat derecesiyle PDF'ye dönüştürür.

### **Doğrudan Dönüşüm**

Bir Excel dosyasını doğrudan PDF olarak kaydetmek için, [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) yöntemini kullanabilir ve ikinci parametre olarak [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)i geçebilirsiniz.

Aşağıdaki kod parçası, Excel'in PDF biçimine dönüştürülmesi için [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) ve [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) yöntemlerinin kullanımını göstermektedir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **Gelişmiş Dönüşüm**

PDF'ye dönüşüm üzerinde daha fazla kontrol sahibi olmak için API, [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) sınıfını sağlar. [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) sınıfı, dönüşüm için farklı özellikler belirlemek için kullanılabilir. [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) sınıfının farklı özelliklerinin belirlenmesi, sonuç PDF dosyası için Yazdırma, Yazı Tipi, Güvenlik ve Sıkıştırma ayarları üzerinde kontrol sağlar. En dikkat çekici özellik, Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlayan [**Compliance**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance) özelliğidir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, elektronik tabloyu PDF'ye dönüştürmeden hemen önce [**Workbook.calculateFormula**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#calculateFormula()) yöntemini çağırın. Bu, formüle bağımlı değerlerin yeniden hesaplanmasını ve doğru değerlerin PDF'e aktarılmasını sağlar.

{{% /alert %}}
