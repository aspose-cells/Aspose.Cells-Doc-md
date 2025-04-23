---
title: Excel Dosyasını PDFA 1a Uyumlu PDF Biçimine Dönüştürme
type: docs
weight: 80
url: /tr/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **Olası Kullanım Senaryoları**

PDF/A, belgelerin uzun süreli korunması için tasarlanmış benzersiz bir PDF türüdür. PDF/A, belgede kullanılan tüm fontları PDF dosyası içine gömmek için kullanılan bir ISO-standartlı Portable Document Format (PDF) sürümüdür. PDF/A, font bağlama (gömülme yerine) ve şifreleme gibi özellikleri yasaklayarak PDF'den farklılık gösterir. Aspose.Cells, Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlar (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab ve PDF/A-3u desteklenir). Bu konu, Excel çalışma kitabını PDF/A uyumlu (PDF/A-1a) PDF dosyasına kaydetmenin nasıl yapıldığını açıklar.

## **Excel dosyasını PDF/A-1a uyumlu PDF formatına dönüştür**

Geliştiriciler, dönüşüm için farklı özellikler belirlemek için [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) sınıfını kullanabilir. Çıktı PDF için baskı, font, güvenlik ve sıkıştırma ayarları üzerinde kontrol sağlayan [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) sınıfının farklı özelliklerini belirlemek, size kontrol imkanı verir. En önemli özellik [PdfSaveOptions.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance) olarak; bu, Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlar.

Aşağıdaki örnek kod, Excel dosyasını PDF/A-1a uyumlu PDF formatına dönüştürmenin nasıl yapıldığını açıklar. Lütfen [çıktı PDF](outputCompliancePdfA1a.pdf) ve bir referans için ekran görüntüsünü inceleyin.

## **Ekran Görüntüsü**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
{{< app/cells/assistant language="java" >}}
