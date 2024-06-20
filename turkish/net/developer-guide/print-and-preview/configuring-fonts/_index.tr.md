---
title: Yayınlanan İşlenmiş Elektronik Tablolar için Yazı Tiplerini Yapılandırma
type: docs
weight: 10
url: /tr/net/configuring-fonts-for-rendering-spreadsheets/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells API'ları, elektronik tabloları görüntü formatlarında işlemek ve onları PDF ve XPS formatlarına dönüştürmek için olanak sağlar. Dönüşüm sadakatini maksimuma çıkarmak için, elektronik tabloda kullanılan yazı tiplerinin işletim sisteminin varsayılan yazı tipi dizininde bulunmalıdır. Gerekli yazı tipleri mevcut değilse, Aspose.Cells API'ları gerekli yazı tiplerini bulmak için çaba harcayacaktır.

## **Yazı Tiplerinin Seçimi**

Aspose.Cells API'ları tarafından perde arkasında izlenen süreç aşağıda belirtilmiştir.

1. API, elektronik tabloda kullanılan tam olarak eşleşen yazı tipini dosya sistemi üzerinde bulmaya çalışır.
2. API, aynı ebeveyn düğümü altında kullanılan varsayılan yazı tipini belirleyebilecek olan [**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) özelliği altında belirtilen varsayılan yazı tipini kullanmaya çalışır.
3. API, yazı tipini belirleyemiyorsa, [**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) veya [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) özelliği altında belirtilen yazı tipini kullanmaya çalışır.
4. API, yazı tipini belirleyemiyorsa, [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) özelliği altında belirtilen yazı tipini kullanmaya çalışır.
1. API, [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname) özelliği altında tanımlanan yazı tipi bulunamazsa, mevcut yazı tiplerinden en uygun olanını seçmeye çalışır.
1. Son olarak, API dosya sisteminde herhangi bir yazı tipi bulamazsa, çalışsayı Arial kullanarak elektronik tabloyu oluşturur.

## **Özel Yazı Tipi Klasörlerini Ayarlayın**

Aspose.Cells API'leri, gerekli yazı tipleri için işletim sisteminin varsayılan yazı tipi dizininde arama yapar. Gerekli yazı tipleri sistemde bulunmuyorsa, API'ler özel (kullanıcı tanımlı) dizinleri arar. [**FontConfigs**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs) sınıfı, özel yazı tipi dizinlerini ayarlamak için aşağıda detaylı olarak açıklanan bir dizi yol sağlamıştır.

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder): Bu yöntem, sadece bir klasör ayarlanacaksa kullanışlıdır.
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders): Bu yöntem, yazı tiplerinin birden fazla klasörde bulunduğu durumda ve kullanıcı tüm klasörleri tek tek birleştirmek yerine ayrı ayrı ayarlamak istediğinde kullanışlıdır.
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources): Bu mekanizma, kullanıcının birden fazla klasörden veya tek bir yazı tipi dosyasından veya bayt dizisinden yazı tiplerini yüklemek istemesi durumunda kullanışlıdır.

{{% alert color="primary" %}}

[**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder) ve [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders) yöntemleri her ikisi de ikinci olarak gelen Boolean türünde bir parametre kabul eder. İkinci parametre olarak **true** geçmek, Aspose.Cells API'lerini yazı tipleri dosyalarını aramak için alt klasörlere yönlendirir.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

Lütfen uygulamanın başlangıcında yukarıda belirtilen yöntemlerden herhangi birini kullanın; diğer Aspose.Cells API nesnelerini çağırmadan önce.

{{% /alert %}} {{% alert color="primary" %}}

Yukarıda bahsedilen tüm yöntemler, yazı tiplerini ayarlamak için kullanıldığında, sadece son ayarlamalar etkili olacaktır.

{{% /alert %}}

## **Yazı Tipi Yedekleme Mekanizması**

Aspose.Cells API'leri, dönüşümün gerçekleşeceği makinede gerekli yazı tipinin bulunmaması durumunda yedek yazı tipini belirtme yeteneği de sağlar. Bu mekanizma, kullanıcının orijinalde gereken yazı tipinin bulunmaması durumunda alternatif bir yazı tipi listesi sağlamak istediğinde yardımcı olur. Bunun için Aspose.Cells API'leri [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes) yöntemini açığa çıkardı, bu yöntem 2 parametre kabul eder. Birinci parametre **string** türündedir ve yedeklemesi yapılacak yazı tipinin adı olmalıdır. İkinci parametre, **string** türünde bir dizi olmalıdır. Kullanıcılar, orijinal yazı tipi adına yedek olarak bir yazı tipi listesi sağlayabilir. (Birinci parametrede belirtilen orijinal yazı tipi adına yedek olarak.)

İşte basit bir kullanım senaryosu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **Bilgi Toplama**

Yukarıda bahsedilen yöntemlere ek olarak, Aspose.Cells API'leri, hangi kaynak ve yedeklemelerin ayarlandığı hakkında bilgi toplamak için de yöntemler sağlamıştır.

1. [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources) yöntemi, belirtilen yazı tipi kaynaklarının listesini içeren [**FontSourceBase**](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase) türünde bir dizi döndürür. Kaynaklar ayarlanmamışsa, [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources) yöntemi boş bir dizi döndürecektir.
1. [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes) yöntemi, belirtilen yazı tipi için ayarlama yapılmasını sağlamak için **string** türünde bir parametre kabul eder. Belirtilen yazı tipi için ayarlama yapılmamışsa, [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes) yöntemi null döndürecektir.

## **Gelişmiş Konular**
- [Yaygın Olarak Kullanılan Yazı tipini Resimlere Dönüştürürken Belirleme](/cells/tr/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [PdfSaveOptions ve ImageOrPrintOptions'ın DefaultFont özelliğini öncelikli şekilde ayarlayın](/cells/tr/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Desteklenen Yazı Tipi Biçimleri](/cells/tr/net/supported-font-formats/)
- [Elektronik Tabloyu Görüntüye - Görüntülenen Görüntü İçin Pixel Biçimini Ayarlama](/cells/tr/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
