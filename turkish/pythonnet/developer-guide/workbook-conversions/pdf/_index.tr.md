---
title: Pdf
type: docs
weight: 220
url: /tr/python-net/convert-excel-to-pdf/
description: Aspose.Cells Python via .NET API ile Excel in PDF e nasıl dönüştürüleceğini öğrenin
keywords: Python da Excel in PDF e dönüştürülmesi, Python kullanarak Excel i PDF e dönüştürme, Python ile Excel i PDF olarak kaydetme, Python da Excel den PDF e dönüştürme
---

{{% alert color="primary" %}}

Aspose.Cells Python via .NET, Excel Çalışma Kitabını PDF'e dönüştürmeyi destekler. Bu örnekte, bir Excel Çalışma Kitabının PDF'e tam dönüştürmesini göreceğiz.

{{% /alert %}}

## **Excel Çalışma Kitabını PDF'e Dönüştürme**

PDF dosyaları, kuruluşlar, devlet kurumları ve bireyler arasında belge değişiminde geniş ölçüde kullanılır. Standart bir belge biçimidir ve yazılım geliştiriciler genellikle Microsoft Excel dosyalarını PDF belgelerine dönüştürmek için bir yol bulmaları istenir.

Aspose.Cells for Python via .NET, Excel dosyalarını PDF'e dönüştürmeyi destekler ve dönüşümde yüksek görsel sadakati korur.

{{% alert color="primary" %}}

Aspose.Cells Python via .NET, çıktı belgelere API ve Sürüm Numarası hakkındaki bilgileri doğrudan yazar. Örneğin, Dokümanı PDF'e dönüştürürken Aspose.Cells Python via .NET, **PDF Üreticisi** alanını 'Aspose.Cells Python via .NET v23.2' gibi bir değerle doldurur.

Lütfen bu bilgileri çıktı Belgelerinde [**PdfSaveOptions.producer**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/producer/) özelliği ile değiştirebileceğinizi unutmayın.

{{% /alert %}}

### **Doğrudan Dönüşüm**

Aspose.Cells Python via .NET, diğer yazılımlardan bağımsız olarak elektronik tablolardan PDF'e dönüşümü destekler. Doğrudan bir Excel dosyasını PDF olarak kaydetmek için [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfının [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) metodu kullanılır. [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) metodu, yerel Excel dosyalarını PDF biçimine dönüştüren [**SaveFormat.PDF**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) numaralı üye sağlar.

Doğrudan Excel elektronik tablolarını PDF biçimine dönüştürmek için aşağıdaki adımları izleyin:

1. Boş kurucuyu çağırarak [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfının nesnesini örnekleyin.
1. Varolan bir şablon dosyasını açabilir/yükleyebilir veya çalışma kitabını sıfırdan oluşturuyorsanız bu adımı atlayabilirsiniz.
1. Aspose.Cells for Python via .NET' API'leri kullanarak elektronik tabloda herhangi bir işlem yapın (giriş verileri, biçimlendirme uygulama, formüller belirleme, resimler veya diğer çizim nesneleri ekleme vb.).
1. Elektronik tablo kodu tamamlandığında, elektronik tabloyu kaydetmek için [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfının [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) yöntemini çağırın.

Dosya biçimi PDF olmalı, bu nedenle nihai PDF belgesini oluşturmak için [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) numaralamasından *PDF* (önceden tanımlanmış bir değer) seçin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

### **Gelişmiş Dönüşüm**

Ayrıca dönüştürme için farklı özellikler belirlemek için [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) sınıfını kullanmayı seçebilirsiniz. [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) sınıfın farklı özelliklerini belirlemek, çıktı PDF için yazdırma, yazı tipi, güvenlik ve sıkıştırma ayarlarını denetlemenizi sağlar. En önemli özellik [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/) sınıfıdır, bu da Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlar.

#### **Çalışma Kitabını PDF/A Uyumlu Dosyalara Kaydetme**

Aşağıdaki kod parçacığı, Excel dosyalarını PDF/A uyumlu PDF biçimine kaydetmek için [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) sınıfının nasıl kullanılacağını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

Lütfen dikkat, [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/) özelliği Aspose.Cells for Python via .NET sürümü için .NET 5.3.0 ile birlikte eklendi.

{{% /alert %}}

#### **PDF Oluşturma Saatini Ayarlayın**

[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) sınıfı ile PDF oluşturma saatinizi alabilir veya ayarlayabilirsiniz. Aşağıdaki kod, PDF dosyasının oluşturma zamanını belirlemek için [**PdfSaveOptions.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/) özelliğin kullanımını göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

#### **İçerik Erişilebilirlik Kopyalama seçeneğini Ayarlayın**

[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) sınıfı ile dönüştürülen PDF'de içerik erişimini kontrol etmek için PDF [**PdfSecurityOptions.accessibility_extract_content**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/) seçeneğini alabilir veya ayarlayabilirsiniz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

#### **Özel özellikleri PDF'ye aktar**

[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) sınıfı ile kaynak elektronik tablodaki özel özellikleri PDF'ye aktarabilirsiniz. Özellikleri nasıl aktarılacağını belirtmek için [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/) numaralama sağlanmaktadır. Bu özellikler, aşağıdaki resimde gösterildiği gibi Adobe Acrobat Reader'da Dosya'ya tıklayarak ardından özellikler seçeneğini tıklayarak görüntülenebilir. Şablon dosyası "sourceWithCustProps.xlsx" test etmek için [buradan](sourceWithCustProps.xlsx) indirilebilir ve çıktı PDF dosyası "outSourceWithCustProps" analiz için [buradan](outSourceWithCustProps.pdf) temin edilebilir.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

### **Dönüşüm Özellikleri**

Her yeni sürümle dönüşüm özelliklerini geliştirmeye çalışıyoruz. Aspose.Cell'in Excel'den PDF'ye dönüştürme hala birkaç kısıtlamaya sahiptir. HaritaÇizelgesi, PDF biçimine dönüştürülürken desteklenmez. Ayrıca, bazı çizim nesneleri iyi desteklenmez.

Aşağıdaki tablo, Aspose.Cells for Python via .NET'ı kullanarak PDF'ye dışa aktarırken tamamen veya kısmen desteklenen tüm özellikleri listeler. Bu tablo kesin değildir ve tüm elektronik tablo özelliklerini kapsamaz, ancak dönüşüm için desteklenmeyen veya kısmen desteklenen özellikleri belirler.

|**Belge Öğesi**|**Özellik**|**Desteklenen**|**Notlar**|
| :- | :- | :- | :- |
|Hizalama| |Evet| |
|Arka plan Ayarları| |Evet| |
|Kenarlık|Renk|Evet| |
|Kenarlık|Çizgi stili|Evet| |
|Kenarlık|Çizgi genişliği|Evet| |
|Hücre Verisi| |Evet| |
|Yorumlar| |Evet| |
|Koşullu Biçimlendirme| |Evet| |
|Döküman Özellikleri| |Evet| |
|Çizim Nesneleri| |Kısmen|Çizim nesneleri için gölge ve 3-B efektleri iyi desteklenmez; WordArt ve SmartArt kısmen desteklenir.|
|Yazı Tipi|Boyut|Evet| |
|Yazı Tipi|Rengi|Evet| |
|Yazı Tipi|Stili|Evet| |
|Yazı Tipi|Altı çizili|Evet| |
|Yazı Tipi|Efektleri|Evet||
|Resimler| |Evet| |
|Hyperlink| |Evet| |
|Grafikler| |Kısmen|Harita Grafikleri desteklenmiyor.|
|Birleştirilmiş Hücreler| |Evet| |
|Sayfa Sonu| |Evet| |
|Sayfa Ayarı|Üstbilgi/Altbilgi|Evet| |
|Sayfa Ayarı|Kenar Boşlukları|Evet| |
|Sayfa Ayarı|Sayfa Yönü|Evet| |
|Sayfa Ayarı|Sayfa Boyutu|Evet| |
|Sayfa Ayarı|Yazdırma Alanı|Evet| |
|Sayfa Ayarı|Yazdırma Başlıkları|Evet| |
|Sayfa Ayarı|Ölçekleme|Evet| |
|Satır Yüksekliği/Sütun Genişliği| |Evet| |
|RTL (Sağdan Sola) Dil| |Evet| |

{{% alert color="primary" %}}

Eğer elektronik tablonuz formüller içeriyorsa, elektronik tabloyu PDF formatına dönüştürmeden önce [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) yöntemini çağırmanız en iyisidir. Böyle yapmak, formül bağımlı değerlerin yeniden hesaplanmasını sağlayacak ve doğru değerler PDF olarak oluşturulacaktır.

{{% /alert %}}

## **Gelişmiş Konular**
- [PDF Yer İmlerini Ekle](/cells/tr/python-net/add-pdf-bookmarks/)
- [Adlandırılmış Yer İmleriyle PDF Yer İmi Ekleyin](/cells/tr/python-net/add-pdf-bookmarks-with-named-destinations/)
- [Çıktı PDF'inde Boş Sayfa Oluşmasını Engelle](/cells/tr/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [XLSX Dosyasını PDF Biçimine Dönüştür](/cells/tr/python-net/convert-xlsx-file-to-pdf-format/)
- [PDFA-1a uyumlu PDF biçimine Excel dosyasını dönüştür](/cells/tr/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Resim veya Grafiklerle XLS Dosyasını PDF Biçimine Dönüştür](/cells/tr/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Grafik Tablosu için PdfBookmarkEntry Oluştur](/cells/tr/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır](/cells/tr/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Excel'den PDF'e Dönüştürme Sırasında Hataları Yoksay](/cells/tr/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [Oluşturulan Sayfa Sayısını Sınırla - Excel'den PDF'e Dönüştürme](/cells/tr/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [PDF'ye kaydederken yorumları yazdır](/cells/tr/python-net/print-comments-while-saving-to-pdf/)
- [Excel'i PDF'e dönüştürürken Office Eklentilerini renderla](/cells/tr/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Excel'den PDF'ye Dönüşümde Her Excel Çalışsayarı İçin Bir PDF Sayfası Oluştur](/cells/tr/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Aspose.Cells ile çıktı PDF'inde Unicode Ek Karakterlerini renderla](/cells/tr/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Eklenti Görüntülerini Yeniden Örnekle](/cells/tr/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [Her Çalışsayarı Farklı Bir PDF Dosyasına Kaydet](/cells/tr/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [Excel'i Standart veya Minimum Boyutta PDF olarak kaydet](/cells/tr/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Belirtilen Çalışsayfalarını PDF olarak kaydet](/cells/tr/python-net/save-specified-worksheets-to-pdf/)
- [Güvenli PDF Belgeleri](/cells/tr/python-net/secure-pdf-documents/)
- [Çıktı PDF ve görüntülerde metin geçişini belirle](/cells/tr/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)
