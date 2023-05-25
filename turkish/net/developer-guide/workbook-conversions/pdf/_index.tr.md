---
title: Pdf
type: docs
weight: 220
url: /tr/net/convert-excel-to-pdf/
---
{{% alert color="primary" %}}

Aspose.Cells, Excel Çalışma Kitabının PDF'e dönüştürülmesini destekler. Bu örnekte, bir Excel Çalışma Kitabının PDF'e tamamen dönüştürüldüğünü göreceğiz.

{{% /alert %}}

##  **Excel Çalışma Kitabını PDF'e Dönüştürme**

PDF dosyaları, kuruluşlar, devlet sektörleri ve bireyler arasında belge alışverişinde bulunmak için yaygın olarak kullanılır. Standart bir belge biçimidir ve yazılım geliştiricilerden genellikle Microsoft Excel dosyalarını PDF belgelerine dönüştürmenin bir yolunu bulmaları istenir.

Aspose.Cells, Excel dosyalarının PDF'e dönüştürülmesini destekler ve dönüştürmede yüksek görsel doğruluk sağlar.

{{% alert color="primary" %}}

 Aspose.Cells for .NET, API ve Sürüm Numarası ile ilgili bilgileri doğrudan çıktı belgelerine yazar. Örneğin, Belge PDF'e işlendiğinde, Aspose.Cells for .NET doldurulur**PDF Yapımcı** değeri olan alan, örneğin 'Aspose.Cells v23.2'.

 Lütfen çıktı Belgelerindeki bu bilgileri şu şekilde değiştirebileceğinizi unutmayın:**[PdfSaveOptions.Producer](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/producer/)** mülk.

{{% /alert %}}

###  **Doğrudan Dönüşüm**

Aspose.Cells for .NET, diğer yazılımlardan bağımsız olarak elektronik tablolardan PDF'e dönüştürmeyi destekler. kullanarak bir Excel dosyasını PDF'e kaydetmeniz yeterlidir.**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)** sınıf'**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** yöntem. bu**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** yöntemi sağlar**[SaveFormat.Pdf](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**yerel Excel dosyalarını PDF biçimine dönüştüren numaralandırma üyesi.

Excel elektronik tablolarını doğrudan PDF biçimine dönüştürmek için aşağıdaki adımları izleyin:

1.  nesnesinin örneğini oluşturun**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)**boş kurucusunu çağırarak sınıf.
1. Mevcut bir şablon dosyasını açabilir/yükleyebilir veya çalışma kitabını sıfırdan oluşturuyorsanız bu adımı atlayabilirsiniz.
1. Aspose.Cells' API'lerini kullanarak elektronik tablo üzerinde herhangi bir iş yapın (verileri girin, biçimlendirmeyi uygulayın, formülleri ayarlayın, resimler veya başka çizim nesneleri ekleyin, vb.).
1.  Elektronik tablo kodu tamamlandığında,**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)** sınıf'**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**elektronik tabloyu kaydetme yöntemi.

 Dosya formatı PDF olmalıdır, bu yüzden seçin*Pdf* (önceden tanımlanmış bir değer)**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**son PDF belgesini oluşturmak için numaralandırma.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

###  **Gelişmiş Dönüşüm**

 kullanmayı da tercih edebilirsiniz.**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** dönüşüm için farklı öznitelikler ayarlamak için sınıf. Farklı özelliklerin ayarlanması**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** class, PDF çıktısı için yazdırma, yazı tipi, güvenlik ve sıkıştırma ayarları üzerinde kontrol sağlar. En önemli özellik şudur:**[Uygunluk](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlar.

####  **Çalışma Kitabını PDF/A Uyumlu Dosyalara Kaydetme**

 Aşağıda sağlanan kod parçacığı, nasıl kullanılacağını gösterir.**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**Excel dosyalarını PDF/A uyumlu PDF biçiminde kaydetmek için sınıf.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

 Lütfen dikkat,**[Uygunluk](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**özellik Aspose.Cells for .NET 5.3.0 sürümüyle eklendi.

{{% /alert %}}

####  **PDF Oluşturma Zamanını Ayarlayın**

 İle**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**sınıf, PDF oluşturma saatini alabilir veya ayarlayabilirsiniz. Aşağıdaki kod, kullanımını gösterir**[PdfSaveOptions.CreatedTime](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)** PDF dosyasının oluşturulma zamanını ayarlamak için özellik.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

####  **ContentCopyForAccessibility seçeneğini ayarlayın**

İle**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** sınıfı, PDF'i alabilir veya ayarlayabilirsiniz**[AccessibilityExtractContent](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)**dönüştürülen PDF'de içerik erişimini kontrol etme seçeneği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

####  **Özel özellikleri PDF olarak dışa aktarın**

İle**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** sınıfı, kaynak çalışma kitabındaki özel özellikleri PDF'e verebilirsiniz.**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)** Numaralandırıcı, özelliklerin dışa aktarılma şeklini belirtmek için sağlanmıştır. Bu özellikler, Adobe Acrobat Reader'da aşağıdaki görüntüde olduğu gibi Dosya ve ardından özellikler seçeneği tıklanarak gözlemlenebilir. "sourceWithCustProps.xlsx" şablon dosyası indirilebilir[Burada](sourceWithCustProps.xlsx) test etmek ve çıktı almak için PDF dosyası "outSourceWithCustProps" mevcuttur[Burada](outSourceWithCustProps.pdf) analiz için.

![yapılacaklar:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

###  **Dönüşüm Nitelikleri**

Her yeni sürümde dönüştürme özelliklerini geliştirmek için çalışıyoruz. Aspose.Cell'in Excel'den PDF'e dönüştürme işleminde hala birkaç sınırlama vardır. PDF biçimine dönüştürülürken bazı elektronik tablo biçimlendirmeleri kaybolabilir. Ayrıca, bazı çizim nesneleri henüz desteklenmemektedir.

Aşağıdaki tablo, Aspose.Cells kullanılarak PDF'e dışa aktarılırken tamamen veya kısmen desteklenen tüm özellikleri listeler. Bu tablo nihai değildir ve tüm elektronik tablo özniteliklerini kapsamaz ancak PDF'e dönüştürme için desteklenmeyen veya kısmen desteklenen özellikleri tanımlar. .

|**Belge Öğesi**|**Bağlanmak**|**desteklenen**|**notlar**|
| :- | :- | :- | :- |
|Hizalama| |Evet| |
|Arka plan ayarları| |Evet| |
|Sınır|Renk|Evet| |
|Sınır|Çizgi stili|Evet| |
|Sınır|Hat genişliği|Evet| |
|Cell veri| |Evet| |
|Yorumlar| |Evet| |
|Koşullu biçimlendirme| |Evet| |
|Döküman özellikleri| |Evet| |
|Çizim Nesneleri| |Kısmen|Desteklenen Nesneler: TextBox, Line, Rectangle, Oval, GroupBox, Button, CheckBox, RadioButton, ListBox, ComboBox, Label|
|Yazı tipi|Boyut|Evet| |
|Yazı tipi|Renk|Evet| |
|Yazı tipi|stil|Evet| |
|Yazı tipi|Altını çizmek|Evet| |
|Yazı tipi|Etkileri|Kısmen|Yalnızca üzeri çizili efekt desteklenir|
|Görüntüler| |Evet| |
|köprü| |Evet| |
|Grafikler| |Kısmen||
|Birleştirilmiş Cells| |Evet| |
|Sayfa sonu| |Evet| |
|Sayfa ayarı|Üstbilgi Altbilgi|Evet| |
|Sayfa ayarı|kenar boşlukları|Evet| |
|Sayfa ayarı|Sayfa yönlendirmesi|Evet| |
|Sayfa ayarı|Sayfa boyutu|Evet| |
|Sayfa ayarı|Alanı yazdır|Evet| |
|Sayfa ayarı|Başlıkları Yazdır|Evet| |
|Sayfa ayarı|ölçekleme|Evet| |
|Satır Yüksekliği/Sütun Genişliği| |Evet| |
|RTL (Sağdan Sola) Dili| |Evet| |

{{% alert color="primary" %}}

 E-tablonuz formüller içeriyorsa, aramak en iyisidir**[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)** elektronik tabloyu PDF biçimine dönüştürmeden hemen önce. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}

##  **ileri konular**
- [PDF Yer İşaretlerini Ekle](/cells/tr/net/add-pdf-bookmarks/)
- [Adlandırılmış Hedeflerle PDF Yer İmleri Ekle](/cells/tr/net/add-pdf-bookmarks-with-named-destinations/)
- [Yazdırılacak Hiçbir Şey Olmadığında Çıktı PDF'de Boş Sayfadan Kaçının](/cells/tr/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [PDF'e kaydederken Yazı Tipini yalnızca belirli Unicode karakterlerinde değiştirin](/cells/tr/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [PDF'e işlenirken MS Excel Çalışma Kitabında Dış Kaynakların yüklenmesini kontrol edin](/cells/tr/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [XLSX Dosyasını PDF Formatına Dönüştür](/cells/tr/net/convert-xlsx-file-to-pdf-format/)
- [Excel dosyasını PDFA-1a ile uyumlu PDF biçimine dönüştürün](/cells/tr/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [XLS Dosyasını Resim veya Grafiklerle PDF'e Dönüştür](/cells/tr/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Grafik Sayfası için PdfBookmarkEntry Oluşturun](/cells/tr/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Tüm Çalışma Sayfası Sütunlarını Tek PDF Sayfaya Sığdır](/cells/tr/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [DrawObjectEventHandler sınıfını kullanarak PDF'e işlerken DrawObject ve Bound'u alın](/cells/tr/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Excel Dosyasını İşlerken Yazı Tipi Değiştirme Uyarıları Alın](/cells/tr/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Excel'i PDF Olarak İşlerken Hataları Yoksay](/cells/tr/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Oluşturulan Sayfa Sayısını Sınırla - Excel PDF Dönüşümü ile](/cells/tr/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [PDF'e kaydederken Yorumları Yazdır](/cells/tr/net/print-comments-while-saving-to-pdf/)
- [Excel'i PDF'e dönüştürürken Office Eklentilerini işleyin](/cells/tr/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Render Bir PDF Sayfa Başına Excel Çalışma Sayfası - Excel'den PDF'e Dönüştürme](/cells/tr/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Unicode Tamamlayıcı karakterleri PDF çıktısında Aspose.Cells ile işleyin](/cells/tr/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Eklenen Görüntüleri Yeniden Örnekleme - Excel'den PDF'e Dönüştürme](/cells/tr/net/resampling-added-images-excel-to-pdf-conversion/)
- [Her Çalışma Sayfasını Farklı Bir PDF Dosyasına Kaydet](/cells/tr/net/save-each-worksheet-to-a-different-pdf-file/)
- [Excel'i Standart veya Minimum Boyutla PDF'e kaydedin](/cells/tr/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Belirtilen Çalışma Sayfalarını PDF'e Kaydet](/cells/tr/net/save-specified-worksheets-to-pdf/)
- [Güvenli PDF Belgeler](/cells/tr/net/secure-pdf-documents/)
- [PDF çıktısında ve görüntüde dizenin nasıl çaprazlanacağını belirtin](/cells/tr/net/specify-how-to-cross-string-in-output-pdf-and-image/)
