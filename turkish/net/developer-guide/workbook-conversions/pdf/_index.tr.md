---
title: Pdf
type: docs
weight: 220
url: /tr/net/convert-excel-to-pdf/
---

{{% alert color="primary" %}}

Aspose.Cells, Excel Çalışma Kitabını PDF'ye dönüştürmeyi destekler. Bu örnekte, bir Excel Çalışma Kitabının tam dönüşümünü göreceğiz.

{{% /alert %}}

## **Excel Çalışma Kitabını PDF'e Dönüştürme**

PDF dosyaları, kuruluşlar, devlet kurumları ve bireyler arasında belge değişiminde geniş ölçüde kullanılır. Standart bir belge biçimidir ve yazılım geliştiriciler genellikle Microsoft Excel dosyalarını PDF belgelerine dönüştürmek için bir yol bulmaları istenir.

Aspose.Cells, Excel dosyalarını PDF'ye dönüştürmeyi destekler ve dönüşümde yüksek görsel sadakati korur.

{{% alert color="primary" %}}

Aspose.Cells for .NET doğrudan API ve Sürüm Numarası hakkında bilgi yazmaktadır. Örneğin, Belgeyi PDF'ye dönüştürürken, Aspose.Cells for .NET **PDF Üreticisi** alanını 'Aspose.Cells v23.2' gib i bir değerle doldurur.

Lütfen bu bilgileri çıktı Belgelerinde [**PdfSaveOptions.Producer**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/producer/) özelliği ile değiştirebileceğinizi unutmayın.

{{% /alert %}}

### **Doğrudan Dönüşüm**

Diğer yazılımlardan bağımsız olarak Aspose.Cells for .NET, elektronik tablolardan PDF'ye dönüşümü destekler. Basitçe Excel dosyasını PDF olarak [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfı'nın [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) metodu kullanılarak kaydedin. [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) metodu, yerel Excel dosyalarını PDF formatına dönüştüren [**SaveFormat.Pdf**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) numaralı etkileşim üyesini sağlar.

Doğrudan Excel elektronik tablolarını PDF biçimine dönüştürmek için aşağıdaki adımları izleyin:

1. Boş kurucuyu çağırarak [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının nesnesini örnekleyin.
1. Varolan bir şablon dosyasını açabilir/yükleyebilir veya çalışma kitabını sıfırdan oluşturuyorsanız bu adımı atlayabilirsiniz.
3. Aspose.Cells'in API'lerini kullanarak elektronik tabloda herhangi bir işlem yapın (giriş verileri, biçimlendirme uygulama, formüller belirleme, resimler veya diğer çizim nesneleri ekleme vb.).
1. Elektronik tablo kodu tamamlandığında, elektronik tabloyu kaydetmek için [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıfının [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) yöntemini çağırın.

Dosya biçimi PDF olmalı, bu nedenle nihai PDF belgesini oluşturmak için *Pdf* (önceden tanımlanmış bir değer) olarak [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) sınıfının numaralandırmasından seçim yapın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **Gelişmiş Dönüşüm**

Dönüşüm için farklı özellikleri ayarlamak için [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) sınıfını kullanabilirsiniz. [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) sınıfının farklı özelliklerini ayarlamak, çıktı PDF'nin yazdırma, font, güvenlik ve sıkıştırma ayarları üzerinde kontrol sahibi olmanızı sağlar. 

En önemli özellik [**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance), PDF standartları uyumluluk seviyesini ayarlamanıza olanak tanır. Şu anda PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab ve PDF/A-3u formatlarına kaydedebilirsiniz. PDF/A formatı ile, çıktı dosyasının boyutu düzenli PDF dosyasının boyutundan daha büyüktür.

#### **Çalışma Kitabını PDF/A Uyumlu Dosyalara Kaydetme**

Aşağıdaki kod parçacığı, Excel dosyalarını PDF/A uyumlu PDF biçimine kaydetmek için [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) sınıfının nasıl kullanılacağını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

Lütfen, [**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) özelliğinin Aspose.Cells for .NET 5.3.0 sürümü ile birlikte eklendiğine dikkat edin.

{{% /alert %}}

#### **PDF Oluşturma Saatini Ayarlayın**

[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) sınıfı ile PDF oluşturma saatinizi alabilir veya ayarlayabilirsiniz. Aşağıdaki kod, PDF dosyasının oluşturma zamanını belirlemek için [**PdfSaveOptions.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime) özelliğin kullanımını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **İçerik Erişilebilirlik Kopyalama seçeneğini Ayarlayın**

[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) sınıfı ile dönüştürülen PDF'de içerik erişimini kontrol etmek için PDF [**AccessibilityExtractContent**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent) seçeneğini alabilir veya ayarlayabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **Özel özellikleri PDF'ye aktar**

[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) sınıfı ile kaynak elektronik tablodaki özel özellikleri PDF'ye aktarabilirsiniz. Özellikleri nasıl aktarılacağını belirtmek için [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport) numaralama sağlanmaktadır. Bu özellikler, aşağıdaki resimde gösterildiği gibi Adobe Acrobat Reader'da Dosya'ya tıklayarak ardından özellikler seçeneğini tıklayarak görüntülenebilir. Şablon dosyası "sourceWithCustProps.xlsx" test etmek için [buradan](sourceWithCustProps.xlsx) indirilebilir ve çıktı PDF dosyası "outSourceWithCustProps" analiz için [buradan](outSourceWithCustProps.pdf) temin edilebilir.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

### **Dönüşüm Özellikleri**

Her yeni sürümle dönüşüm özelliklerini geliştirmeye çalışıyoruz. Aspose.Cell'in Excel'den PDF'ye dönüştürme hala birkaç kısıtlamaya sahiptir. HaritaÇizelgesi, PDF biçimine dönüştürülürken desteklenmez. Ayrıca, bazı çizim nesneleri iyi desteklenmez.

Aşağıdaki tablo, Aspose.Cells kullanarak PDF'ye dışa aktarırken tamamen veya kısmen desteklenen tüm özellikleri listeleyen bir tablodur. Bu tablo son değildir ve tüm elektronik tablo özniteliklerini kapsamaz, ancak dışa aktarmak için tamamen veya kısmen desteklenmeyen özellikleri tanımlar.

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

Eğer elektronik tablonuz formüller içeriyorsa, elektronik tabloyu PDF biçimine dönüştirmeden önce [**Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) yöntemini çağırmanız en iyisidir. Böylece formül bağımlı değerler yeniden hesaplanacak ve doğru değerler PDF biçiminde yapılandırılacaktır.

{{% /alert %}}

## **Gelişmiş Konular**
- [PDF Yer İmlerini Ekle](/cells/tr/net/add-pdf-bookmarks/)
- [Adlandırılmış Yer İmleriyle PDF Yer İmi Ekleyin](/cells/tr/net/add-pdf-bookmarks-with-named-destinations/)
- [Çıktı PDF'inde Boş Sayfa Oluşmasını Engelle](/cells/tr/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [PDF'ye Kaydederken Yalnızca Belirli Unicode Karakterlerin Yazı Tipini Değiştirme](/cells/tr/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [MS Excel Çalışma Kitabında Harici Kaynakların Yüklenmesine Kontrol Etmek](/cells/tr/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [XLSX Dosyasını PDF Biçimine Dönüştür](/cells/tr/net/convert-xlsx-file-to-pdf-format/)
- [PDFA-1a uyumlu PDF biçimine Excel dosyasını dönüştür](/cells/tr/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Resim veya Grafiklerle XLS Dosyasını PDF Biçimine Dönüştür](/cells/tr/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Grafik Tablosu için PdfBookmarkEntry Oluştur](/cells/tr/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Tüm Çalışsayfa Sütunlarını Tek PDF Sayfasına Sığdır](/cells/tr/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [DrawObjectEventHandler sınıfını kullanarak PDF'ye dönüştürürken DrawObject ve Sınırlı Alın](/cells/tr/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Excel Dosyasını PDF'e Dönüştürürken Yazı Tipi Yedeği İçin Uyarıları Al](/cells/tr/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Excel'den PDF'e Dönüştürme Sırasında Hataları Yoksay](/cells/tr/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Oluşturulan Sayfa Sayısını Sınırla - Excel'den PDF'e Dönüştürme](/cells/tr/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [PDF'ye kaydederken yorumları yazdır](/cells/tr/net/print-comments-while-saving-to-pdf/)
- [Excel'i PDF'e dönüştürürken Office Eklentilerini renderla](/cells/tr/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Excel'den PDF'ye Dönüşümde Her Excel Çalışsayarı İçin Bir PDF Sayfası Oluştur](/cells/tr/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Aspose.Cells ile çıktı PDF'inde Unicode Ek Karakterlerini renderla](/cells/tr/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Eklenti Görüntülerini Yeniden Örnekle](/cells/tr/net/resampling-added-images-excel-to-pdf-conversion/)
- [Her Çalışsayarı Farklı Bir PDF Dosyasına Kaydet](/cells/tr/net/save-each-worksheet-to-a-different-pdf-file/)
- [Excel'i Standart veya Minimum Boyutta PDF olarak kaydet](/cells/tr/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Belirtilen Çalışsayfalarını PDF olarak kaydet](/cells/tr/net/save-specified-worksheets-to-pdf/)
- [Güvenli PDF Belgeleri](/cells/tr/net/secure-pdf-documents/)
- [Çıktı PDF ve görüntülerde metin geçişini belirle](/cells/tr/net/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="csharp" >}}
