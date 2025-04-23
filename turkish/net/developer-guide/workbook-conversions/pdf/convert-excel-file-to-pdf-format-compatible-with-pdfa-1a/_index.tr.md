---
title: Excel Dosyasını PDFA 1a Uyumlu PDF Biçimine Dönüştürme
type: docs
weight: 130
url: /tr/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **Olası Kullanım Senaryoları**

PDF/A, belgelerin uzun süreli korunması için tasarlanmış benzersiz bir PDF türüdür. PDF/A, belgede kullanılan tüm fontları PDF dosyası içine gömmek için kullanılan bir ISO-standartlı Portable Document Format (PDF) sürümüdür. PDF/A, font bağlama (gömülme yerine) ve şifreleme gibi özellikleri yasaklayarak PDF'den farklılık gösterir. Aspose.Cells, Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlar (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab ve PDF/A-3u desteklenir). Bu konu, Excel çalışma kitabını PDF/A uyumlu (PDF/A-1a) PDF dosyasına kaydetmenin nasıl yapıldığını açıklar.

## **Excel dosyasını PDF/A-1a uyumlu PDF formatına dönüştürme**

Geliştiriciler, dönüşüm için [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) sınıfını kullanarak farklı özellikler belirleyebilir. Çeşitli [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) sınıfı özelliklerini ayarlamak, çıktı PDF için yazdırma, yazı tipi, güvenlik ve sıkıştırma ayarları üzerinde kontrol sağlar. En önemli özellik, Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenize olanak tanıyan [**PdfSaveOptions.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) özelliğidir.

Aşağıdaki örnek kod, Excel dosyasını PDF/A-1a uyumlu PDF formatına dönüştürmenin nasıl yapıldığını açıklar. Lütfen [çıktı PDF](outputCompliancePdfA1a.pdf) ve referans için ekran görüntüsünü inceleyin.

## **Ekran Görüntüsü**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.cs" >}}
{{< app/cells/assistant language="csharp" >}}
