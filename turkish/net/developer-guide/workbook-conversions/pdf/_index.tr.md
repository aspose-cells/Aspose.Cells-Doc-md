---
title: Pdf
type: docs
weight: 220
url: /tr/net/convert-excel-to-pdf/
---
{{% alert color="primary" %}}

Aspose.Cells, Excel Çalışma Kitabının PDF'e dönüştürülmesini destekler. Bu örnekte, bir Excel Çalışma Kitabının tamamen PDF'e dönüştürüldüğünü göreceğiz.

{{% /alert %}}

##  **Excel Çalışma Kitabını PDF'e dönüştürme**

PDF dosyaları kuruluşlar, devlet sektörleri ve bireyler arasında belge alışverişinde bulunmak için yaygın olarak kullanılır. Standart bir belge formatıdır ve yazılım geliştiricilerden sıklıkla Microsoft Excel dosyalarını PDF belgeye dönüştürmenin bir yolunu bulmaları istenir.

Aspose.Cells, Excel dosyalarının PDF'e dönüştürülmesini destekler ve dönüştürme sırasında yüksek görsel doğruluğu korur.

{{% alert color="primary" %}}

 Aspose.Cells for .NET, çıktı dokümanlarına doğrudan API ve Versiyon Numarası bilgilerini yazar. Örneğin, Belge PDF'e işlendiğinde Aspose.Cells for .NET doldurulur**PDF Üretici** değeri olan alan, örneğin 'Aspose.Cells v23.2'.

 Lütfen çıktı Belgelerindeki bu bilgiyi şu şekilde değiştirebileceğinizi unutmayın:**[PdfSaveOptions.Producer](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/producer/)** mülk.

{{% /alert %}}

###  **Doğrudan Dönüşüm**

 Aspose.Cells for .NET, diğer yazılımlardan bağımsız olarak elektronik tablolardan PDF'e dönüştürmeyi destekler. Bir Excel dosyasını PDF'e kaydetmeniz yeterlidir.**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)**sınıf'**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** yöntem.**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** yöntem şunları sağlar:**[SaveFormat.Pdf](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**yerel Excel dosyalarını PDF biçimine dönüştüren numaralandırma üyesi.

Excel elektronik tablolarını doğrudan PDF biçimine dönüştürmek için aşağıdaki adımları izleyin:

1.  Bir nesneyi somutlaştırın**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)**boş yapıcısını çağırarak sınıfı.
1. Mevcut bir şablon dosyasını açabilir/yükleyebilir veya çalışma kitabını sıfırdan oluşturuyorsanız bu adımı atlayabilirsiniz.
1. Aspose.Cells' API'lerini kullanarak elektronik tablo üzerinde herhangi bir çalışma yapın (veri girişi, biçimlendirme uygulama, formül ayarlama, resim veya diğer çizim nesneleri ekleme vb.).
1.  Elektronik tablo kodu tamamlandığında,**[Çalışma Kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook)**sınıf'**[Kaydet](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**Elektronik tabloyu kaydetme yöntemi.

 Dosya formatı PDF olmalıdır, bu yüzden seçin*Pdf* (önceden tanımlanmış bir değer)**[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**son PDF belgesini oluşturmak için numaralandırma.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

###  **Gelişmiş Dönüşüm**

 Ayrıca şunları kullanmayı da tercih edebilirsiniz:**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** Dönüşüm için farklı öznitelikler ayarlamak için sınıf. Farklı özelliklerin ayarlanması**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** sınıfı, PDF çıktısının yazdırma, yazı tipi, güvenlik ve sıkıştırma ayarları üzerinde kontrol sahibi olmanızı sağlar. En önemli özellik,**[Uyumluluk](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlar.

####  **Çalışma Kitabını PDF/A Uyumlu Dosyalara Kaydetme**

 Aşağıda verilen kod parçacığı, bu özelliğin nasıl kullanılacağını gösterir.**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**Excel dosyalarını PDF/A uyumlu PDF biçiminde kaydetmek için sınıf.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

Lütfen dikkat:**[Uyumluluk](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**özelliği Aspose.Cells for .NET 5.3.0 sürümüyle eklendi.

{{% /alert %}}

####  **PDF Oluşturma Zamanını Ayarlayın**

 İle**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**sınıf, PDF oluşturma zamanını alabilir veya ayarlayabilirsiniz. Aşağıdaki kod kullanımını göstermektedir**[PdfSaveOptions.CreatedTime](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)** PDF dosyasının oluşturulma zamanını ayarlama özelliği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

####  **ContentCopyForAccessibility seçeneğini ayarlayın**

İle**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** sınıf, PDF'i alabilir veya ayarlayabilirsiniz.**[AccessibilityExtractContent](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)** Dönüştürülen PDF'deki içerik erişimini kontrol etme seçeneği.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

####  **Özel özellikleri PDF'e aktarın**

İle**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** sınıfında kaynak çalışma kitabındaki özel özellikleri PDF'e aktarabilirsiniz.**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)**özelliklerin dışa aktarılma şeklini belirtmek için numaralandırıcı sağlanmıştır. Bu özellikleri Adobe Acrobat Reader'da aşağıdaki görüntüdeki gibi Dosya ve ardından özellikler seçeneğine tıklayarak gözlemleyebilirsiniz. "sourceWithCustProps.xlsx" şablon dosyası indirilebilir[Burada](sourceWithCustProps.xlsx) test etmek ve çıktı almak için PDF dosyası "outSourceWithCustProps" mevcuttur[Burada](outSourceWithCustProps.pdf) analiz için.

![yapılacak şey:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

###  **Dönüşüm Özellikleri**

Her yeni sürümde dönüştürme özelliklerini geliştirmek için çalışıyoruz. Aspose.Cell'in Excel'den PDF'e dönüşümü hâlâ birkaç sınırlamaya sahiptir. PDF biçimine dönüştürme sırasında MapChart desteklenmez. Ayrıca bazı çizim nesneleri yeterince desteklenmiyor.

Aşağıdaki tablo, Aspose.Cells kullanılarak PDF'e dışa aktarıldığında tamamen veya kısmen desteklenen tüm özellikleri listeler. Bu tablo nihai değildir ve tüm e-tablo niteliklerini kapsamaz ancak desteklenmeyen veya PDF'e dönüştürülmesi kısmen desteklenen özellikleri tanımlar. .

|**Belge Öğesi**|**Bağlanmak**|**Destekleniyor**|**Notlar**|
| :- | :- | :- | :- |
|Hizalama| |Evet| |
|Arka plan ayarları| |Evet| |
|Sınır|Renk|Evet| |
|Sınır|Çizgi stili|Evet| |
|Sınır|Hat genişliği|Evet| |
|Cell Veri| |Evet| |
|Yorumlar| |Evet| |
|Koşullu biçimlendirme| |Evet| |
|Döküman özellikleri| |Evet| |
|Çizim Nesneleri| |Kısmen|Nesneleri çizmeye yönelik gölge ve 3 boyutlu efektler iyi desteklenmemektedir; WordArt ve SmartArt kısmen desteklenmektedir.|
|Yazı tipi|Boyut|Evet| |
|Yazı tipi|Renk|Evet| |
|Yazı tipi|Stil|Evet| |
|Yazı tipi|Altını çizmek|Evet| |
|Yazı tipi|Etkileri|Evet||
|Görüntüler| |Evet| |
|Köprü| |Evet| |
|Grafikler| |Kısmen|MapChart desteklenmiyor.|
|Birleştirildi Cells| |Evet| |
|Sayfa sonu| |Evet| |
|Sayfa ayarı|Üstbilgi Altbilgi|Evet| |
|Sayfa ayarı|Marjlar|Evet| |
|Sayfa ayarı|Sayfa yönlendirmesi|Evet| |
|Sayfa ayarı|Sayfa boyutu|Evet| |
|Sayfa ayarı|Alanı yazdır|Evet| |
|Sayfa ayarı|Başlıkları Yazdır|Evet| |
|Sayfa ayarı|Ölçeklendirme|Evet| |
|Satır Yüksekliği/Sütun Genişliği| |Evet| |
|RTL (Sağdan Sola) Dil| |Evet| |

{{% alert color="primary" %}}

 E-tablonuz formüller içeriyorsa, aramak en iyisidir.**[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)** e-tabloyu PDF biçimine dönüştürmeden hemen önce. Bunu yapmak, formüle bağlı değerlerin yeniden hesaplanmasını ve PDF'de doğru değerlerin oluşturulmasını sağlayacaktır.

{{% /alert %}}

##  **İleri konular**
- [PDF Yer İmlerini Ekle](/cells/tr/net/add-pdf-bookmarks/)
- [Adlandırılmış Hedeflere Sahip PDF Yer İşaretlerini Ekle](/cells/tr/net/add-pdf-bookmarks-with-named-destinations/)
- [Yazdırılacak Bir Şey Olmadığında PDF Çıkışında Boş Sayfadan Kaçının](/cells/tr/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [PDF'e kaydederken Yazı Tipini yalnızca belirli Unicode karakterlerde değiştirin](/cells/tr/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [PDF'e işlenirken MS Excel Çalışma Kitabında Dış Kaynakların yüklenmesini kontrol edin](/cells/tr/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [XLSX Dosyasını PDF Formatına Dönüştür](/cells/tr/net/convert-xlsx-file-to-pdf-format/)
- [Excel dosyasını PDFA-1a ile uyumlu PDF formatına dönüştürün](/cells/tr/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Görüntüler veya Grafikler içeren XLS Dosyasını PDF'e dönüştürün](/cells/tr/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Grafik Sayfası için PdfBookmarkEntry Oluşturun](/cells/tr/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Tüm Çalışma Sayfası Sütunlarını Tek PDF Sayfaya Sığdır](/cells/tr/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [DrawObjectEventHandler sınıfını kullanarak PDF'e işleme sırasında DrawObject ve Bound'u alın](/cells/tr/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Excel Dosyasını Oluştururken Yazı Tipi Değişikliği Uyarıları Alma](/cells/tr/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Excel'i PDF'e Oluştururken Hataları Yoksay](/cells/tr/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Oluşturulan Sayfa Sayısını Sınırlayın - Excel'i PDF Dönüşümüyle Sınırlayın](/cells/tr/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [PDF'e kaydederken Yorumları Yazdır](/cells/tr/net/print-comments-while-saving-to-pdf/)
- [Excel'i PDF'e dönüştürürken Office Eklentilerini işleyin](/cells/tr/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Excel Çalışma Sayfası Başına Bir PDF Sayfa Oluşturma - Excel'den PDF'e Dönüştürme](/cells/tr/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [PDF ve Aspose.Cells çıktılarındaki Unicode Tamamlayıcı karakterleri işle](/cells/tr/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Eklenen Görselleri Yeniden Örnekleme - Excel'den PDF'e Dönüştürme](/cells/tr/net/resampling-added-images-excel-to-pdf-conversion/)
- [Her Çalışma Sayfasını Farklı Bir PDF Dosyasına Kaydetme](/cells/tr/net/save-each-worksheet-to-a-different-pdf-file/)
- [Excel'i Standart veya Minimum Boyutla PDF'e kaydedin](/cells/tr/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Belirtilen Çalışma Sayfalarını PDF'e Kaydet](/cells/tr/net/save-specified-worksheets-to-pdf/)
- [Güvenli PDF Belgeler](/cells/tr/net/secure-pdf-documents/)
- [PDF çıktısında ve görüntüde dizenin nasıl çaprazlanacağını belirtin](/cells/tr/net/specify-how-to-cross-string-in-output-pdf-and-image/)
