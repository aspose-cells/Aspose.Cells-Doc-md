---
title: Golang kullanarak C++ ile Excel i PDF ye dönüştürün.
linktitle: Excel i PDF ye Dönüştür
type: docs
weight: 220
url: /tr/go-cpp/convert-excel-to-pdf/
description: Golang kullanarak C++ ile Aspose.Cells ile Excel çalışma kitaplarını PDF formatına dönüştürmeyi öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, Excel çalışma kitaplarını PDF'e dönüştürmeyi destekler. Bu örnekte, Excel çalışma kitabının PDF’ye tam dönüşümünü göreceğiz.

{{% /alert %}}

## **Excel Çalışma Kitabını PDF'e Dönüştürme**

PDF dosyaları, belge alışverişinde yaygın olarak kullanılmaktadır; hem organizasyonlar, hükümet sektörleri hem de bireyler arasında. Standart bir belge formatıdır ve yazılım geliştiricilerden, Microsoft Excel dosyalarını PDF belgelerine dönüştürmenin yollarını bulmaları istenir.

Aspose.Cells, Excel dosyalarını PDF'ye dönüştürmeyi destekler ve dönüşümde yüksek görsel sadakati korur.

{{% alert color="primary" %}}

Aspose.Cells for C++, çıktı belgelerinde API ve Sürüm Numarası hakkında bilgiyi doğrudan yazar. Örneğin, bir belgeyi PDF’ye dönüştürürken, Aspose.Cells for C++, **PDF Üreticisi** alanını, örneğin 'Aspose.Cells v23.2' değeriyle doldurur.

Lütfen, bu bilgiyi çıktı belgelerinde [**PdfSaveOptions.GetProducer()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getproducer/) özelliğini kullanarak değiştirebileceğinizi unutmayın.

{{% /alert %}}

### **Doğrudan Dönüşüm**

Aspose.Cells for C++, elektronik tablo dosyalarını PDF’ye dönüştürmeyi diğer yazılımlardan bağımsız olarak destekler. Basitçe, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfının [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) metodunu kullanarak bir Excel dosyasını PDF’ye kaydedin. [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) metodu, yerel Excel dosyalarını PDF formatına dönüştüren [**SaveFormat.Pdf**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enum üyesini sağlar.

Doğrudan Excel elektronik tablolarını PDF biçimine dönüştürmek için aşağıdaki adımları izleyin:

1. [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfının boş yapıcı metodunu çağırarak bir nesne oluşturun.
1. Varolan bir şablon dosyasını açabilir/yükleyebilir veya çalışma kitabını sıfırdan oluşturuyorsanız bu adımı atlayabilirsiniz.
1. Aspose.Cells'in API'lerini kullanarak elektronik tablo üzerinde herhangi bir çalışmayı (giriş verisi, biçimlendirme uygulama, formülleri ayarlama, resimler veya diğer çizim nesneleri ekleme ve benzeri) yapın.
Elektronik tablo kodu tamamlandığında, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfının [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) metodunu çağırarak elektronik tabloyu kaydedin.

Dosya formatı PDF olmalı, bu yüzden nihai PDF belgesini oluşturmak için [**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/) enum'undan *Pdf* (önceden tanımlanmış değer) seçin.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf.go" >}}
### **Gelişmiş Dönüşüm**

Ayrıca, dönüştürme için farklı özellikler ayarlamak amacıyla [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) sınıfını kullanmayı tercih edebilirsiniz. [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) sınıfının farklı özelliklerini ayarlamak, çıktı PDF'si için yazdırma, yazı tipi, güvenlik ve sıkıştırma ayarları üzerinde kontrol sağlar.

En önemli özellik [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/) olup, bu özellik PDF uyumluluk seviyesi ayarlamanıza olanak tanır. Şu anda PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab ve PDF/A-3u formatlarına kaydedebilirsiniz. Not: PDF/A formatı ile çıktı dosya boyutu normal PDF'den daha büyüktür.

#### **Çalışma Kitabını PDF/A Uyumlu Dosyalara Kaydetme**

Aşağıdaki kod parçası, [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) sınıfını kullanarak Excel dosyalarını PDF/A uyumlu PDF formatına kaydetmenin nasıl yapılacağını gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-1.go" >}}
{{% alert color="primary" %}}

Lütfen unutmayın, [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/) özelliği Aspose.Cells for C++ 5.3.0 sürümünün piyasaya sürülmesiyle eklenmiştir.

{{% /alert %}}

#### **PDF Oluşturma Saatini Ayarlayın**

[**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) sınıfı ile PDF oluşturma zamanını alabilir veya ayarlayabilirsiniz. Aşağıdaki kod, PDF dosyasının oluşturulma zamanını ayarlamak için [**PdfSaveOptions.GetCreatedTime()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcreatedtime/) özelliğinin kullanımını gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-2.go" >}}
#### **İçerik Erişilebilirlik Kopyalama seçeneğini Ayarlayın**

[**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) sınıfı ile, dönüştürülmüş PDF'de içerik erişimini kontrol etmek için [**GetAccessibilityExtractContent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/getaccessibilityextractcontent/) seçeneğini alıp ayarlayabilirsiniz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-3.go" >}}
#### **Özel özellikleri PDF'ye aktar**

[**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) sınıfı ile, kaynak çalışma kitabındaki özel özellikleri dışa aktarabilirsiniz. [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfcustompropertiesexport/) enumeratörü, özelliklerin dışa aktarım şeklini belirtmek için sağlanmıştır. Bu özellikler, Adobe Acrobat Reader'da Dosya seçeneğine tıklayarak ve ardından özellikler seçeneğine erişerek görüntülenebilir. Test amacıyla "sourceWithCustProps.xlsx" adlı şablon dosyası [buradan](sourceWithCustProps.xlsx) indirilebilir ve çıktı PDF dosyası "outSourceWithCustProps" [burada](outSourceWithCustProps.pdf) analiz edilmek üzere mevcuttur.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-4.go" >}}
### **Dönüşüm Özellikleri**

Her yeni sürümde dönüştürme özelliklerini geliştirmeye çalışıyoruz. Aspose.Cells'in Excel'den PDF'ye dönüştürme işlemi hâlâ bazı sınırlamalara sahiptir. MapChart, PDF formatına dönüştürme sırasında desteklenmemektedir. Ayrıca, bazı çizim nesneleri tam olarak desteklenmemektedir.

Aşağıdaki tablo, Aspose.Cells kullanılarak PDF'ye dışa aktarılırken tam veya kısmen desteklenen tüm özellikleri listelemektedir. Bu tablo son değildir ve tüm elektronik tablo niteliklerini kapsamaz, ancak PDF'ye dönüştürme sırasında desteklenmeyen veya kısmen desteklenen özellikleri tanımlar.

| **Belge Öğesi** | **Özellik** | **Destekleniyor** | **Notlar** |
| :- | :- | :- | :- |
| Hizalama |  | Evet |  |
| Arka plan ayarları |  | Evet |  |
| Kenarlık | Renk | Evet |  |
| Kenarlık | Çizgi stili | Evet |  |
| Kenarlık | Çizgi kalınlığı | Evet |  |
| Hücre Verisi |  | Evet |  |
| Yorumlar |  | Evet |  |
| Koşullu Biçimlendirme |  | Evet |  |
| Belge Özellikleri |  | Evet |  |
| Çizim Nesneleri |  | Kısmen | Çizim nesneleri için gölge ve 3-D efektleri tam desteklenmemekte; WordArt ve SmartArt kısmen desteklenmektedir. |
| Yazı Tipi | Boyut | Evet |  |
| Yazı Tipi | Renk | Evet |  |
| Yazı Tipi | Stil | Evet |  |
| Yazı Tipi | Altı çizili | Evet |  |
| Yazı Tipi | Efektleri | Evet |  |
| Resimler |  | Evet |  |
| Köprü Hükümeti |  | Evet |  |
| Grafikler |  | Kısmen | MapChart desteklenmiyor. |
| Birleşik Hücreler |  | Evet |  |
| Sayfa Sonu |  | Evet |  |
| Sayfa Düzeni | Üstbilgi/Altbilgi | Evet |  |
| Sayfa Düzeni | Kenar Boşlukları | Evet |  |
| Sayfa Düzeni | Sayfa Yönü | Evet |  |
| Sayfa Düzeni | Sayfa Boyutu | Evet |  |
| Sayfa Düzeni | Yazdırma Alanı | Evet |  |
| Sayfa Düzeni | Yazdırma Başlıkları | Evet |  |
| Sayfa Düzeni | Ölçekleme | Evet |  |
| Satır Yüksekliği/Sütun Genişliği |  | Evet |  |
| RTL (Sağdan Sola) Dili |  | Evet |  |

{{% alert color="primary" %}}

 Eğer çalışma sayfanız formüller içeriyorsa, çalışma sayfasını PDF formatına dönüştürmeden hemen önce [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) çağırmak en iyisidir. Bu, formüle bağlı değerlerin yeniden hesaplanmasını sağlar ve PDF'de doğru değerler gösterilir.

{{% /alert %}}

## **Gelişmiş Konular**
- [Adlandırılmış Yer İmleriyle PDF Yer İmi Ekleyin](/cells/tr/cpp/add-pdf-bookmarks-with-named-destinations/)
- [PDF'ye Kaydederken Yalnızca Belirli Unicode Karakterlerin Yazı Tipini Değiştirme](/cells/tr/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [XLSX Dosyasını PDF Biçimine Dönüştür](/cells/tr/cpp/convert-xlsx-file-to-pdf-format/)
- [PDFA-1a uyumlu PDF biçimine Excel dosyasını dönüştür](/cells/tr/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Resim veya Grafiklerle XLS Dosyasını PDF Biçimine Dönüştür](/cells/tr/cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Grafik Tablosu için PdfBookmarkEntry Oluştur](/cells/tr/cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır](/cells/tr/cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [DrawObjectEventHandler sınıfını kullanarak PDF'ye dönüştürürken DrawObject ve Sınırlı Alın](/cells/tr/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Excel Dosyasını PDF'e Dönüştürürken Yazı Tipi Yedeği İçin Uyarıları Al](/cells/tr/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Excel'den PDF'e Dönüştürme Sırasında Hataları Yoksay](/cells/tr/cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Oluşturulan Sayfa Sayısını Sınırla - Excel'den PDF'e Dönüştürme](/cells/tr/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [PDF'ye kaydederken yorumları yazdır](/cells/tr/cpp/print-comments-while-saving-to-pdf/)
- [Excel'i PDF'e dönüştürürken Office Eklentilerini renderla](/cells/tr/cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Excel'den PDF'ye Dönüşümde Her Excel Çalışsayarı İçin Bir PDF Sayfası Oluştur](/cells/tr/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Aspose.Cells ile çıktı PDF'inde Unicode Ek Karakterlerini renderla](/cells/tr/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Eklenti Görüntülerini Yeniden Örnekle](/cells/tr/cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Her Çalışsayarı Farklı Bir PDF Dosyasına Kaydet](/cells/tr/cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Excel'i Standart veya Minimum Boyutta PDF olarak kaydet](/cells/tr/cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Belirtilen Çalışsayfalarını PDF olarak kaydet](/cells/tr/cpp/save-specified-worksheets-to-pdf/)
- [Güvenli PDF Belgeleri](/cells/tr/cpp/secure-pdf-documents/)
- [Çıktı PDF ve görüntülerde metin geçişini belirle](/cells/tr/cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
