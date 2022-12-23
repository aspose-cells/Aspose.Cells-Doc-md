---
title: Elektronik Tabloları Oluşturmak için Yazı Tiplerini Yapılandırma
type: docs
weight: 10
url: /tr/net/configuring-fonts-for-rendering-spreadsheets/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells API'leri, elektronik tabloları resim formatlarında oluşturmanın yanı sıra PDF ve XPS formatlarına dönüştürme olanağı sağlar. Dönüştürme doğruluğunu en üst düzeye çıkarmak için elektronik tabloda kullanılan yazı tiplerinin işletim sisteminin varsayılan yazı tipi dizininde bulunması gerekir. Gerekli yazı tiplerinin mevcut olmaması durumunda, Aspose.Cells API'leri gerekli yazı tiplerini mevcut olanlarla değiştirmeye çalışacaktır.

## **Yazı Tiplerinin Seçimi**

Aspose.Cells API'lerinin perde arkasında takip ettiği süreç aşağıdadır.

1. API, elektronik tabloda kullanılan yazı tipi adıyla tam olarak eşleşen dosya sistemindeki yazı tiplerini bulmaya çalışır.
1.  API aynı ada sahip yazı tiplerini bulamazsa, Çalışma Kitabı'nın altında belirtilen varsayılan yazı tipini kullanmayı dener.**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)** Emlak.
1.  API, çalışma kitabının altında tanımlanan yazı tipini bulamazsa**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)** özelliği altında belirtilen yazı tipini kullanmaya çalışır.**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** veya**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)** Emlak.
1.  API altında tanımlanan yazı tipini bulamazsa**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** veya**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)** özelliği altında belirtilen yazı tipini kullanmaya çalışır.**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)** Emlak.
1.  API altında tanımlanan yazı tipini bulamazsa**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)** özelliği, mevcut tüm yazı tiplerinden en uygun yazı tiplerini seçmeye çalışır.
1. Son olarak, API dosya sisteminde herhangi bir yazı tipi bulamazsa, elektronik tabloyu Arial kullanarak işler.

## **Özel Yazı Klasörlerini Ayarla**

 Aspose.Cells API'ler, gerekli yazı tipleri için işletim sisteminin varsayılan yazı tipi dizinini arar. Gerekli yazı tiplerinin sistemin yazı tipi dizininde bulunmaması durumunda, API'ler özel (kullanıcı tanımlı) dizinlerde arama yapar. bu**[FontYapılandırmaları](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs)**class, aşağıda ayrıntılı olarak açıklandığı gibi, özel yazı tipi dizinlerini ayarlamanın çeşitli yollarını ortaya çıkardı.

1. **[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)**: Ayarlanacak yalnızca bir klasör varsa bu yöntem kullanışlıdır.
1. **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)**: Bu yöntem, yazı tipleri birden çok klasörde bulunduğunda ve kullanıcı tüm yazı tiplerini tek bir klasörde birleştirmek yerine tüm klasörleri ayrı ayrı ayarlamak istediğinde kullanışlıdır.
1. **[FontConfigs.SetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources)**: Bu mekanizma, kullanıcı birden çok klasörden yazı tiplerini veya tek bir yazı tipi dosyasını veya bir bayt dizisinden yazı tipi verilerini yüklemek istediğinde kullanışlıdır.

{{% alert color="primary" %}}

 Her ikisi de**[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)** & **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)** yöntemler bir Boole tipi ikinci parametreyi kabul eder. Geçen**doğru** çünkü ikinci parametre Aspose.Cells API'lerini yazı tipi dosyaları için alt klasörleri aramaya yönlendirecektir.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

Lütfen başvuru başlangıcında yukarıda belirtilen yöntemlerden herhangi birini kullanınız, yani; Aspose.Cells API'lerinin diğer nesnelerini çağırmadan önce.

{{% /alert %}} {{% alert color="primary" %}}

Yazı tipi kaynaklarını ayarlamak için yukarıda belirtilen yöntemlerin tümü kullanılırsa, yalnızca son ayarlar geçerli olacaktır.

{{% /alert %}}

## **Yazı Tipi Değiştirme Mekanizması**

 Aspose.Cells API'ler, işleme amaçları için yedek yazı tipini belirtme olanağı da sağlar. Bu mekanizma, dönüştürmenin gerçekleşmesi gereken makinede gerekli bir yazı tipi bulunmadığında yardımcı olur. Kullanıcılar, başlangıçta gerekli olan yazı tipine alternatif olarak bir yazı tipi adları listesi sağlayabilir. Bunu başarmak için Aspose.Cells API'leri,**[FontConfigs.SetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes)** 2 parametre kabul eden yöntem. İlk parametre türdedir**sicim** , değiştirilmesi gereken yazı tipinin adı olmalıdır. İkinci parametre, bir tür dizisidir.**sicim**Kullanıcılar, orijinal yazı tipi adının (ilk parametrede belirtilen) yerine geçen bir yazı tipi adları listesi sağlayabilir.

İşte basit bir kullanım senaryosu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **Bilgi toplama**

Yukarıda belirtilen yöntemlere ek olarak, Aspose.Cells API'leri, hangi kaynakların ve ikamelerin ayarlandığı hakkında bilgi toplamak için araçlar da sağlamıştır.

1. **[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)** yöntem bir tür dizisi döndürür**[FontSourceBase](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase)**belirtilen yazı tipi kaynaklarının listesini içerir. Hiçbir kaynağın ayarlanmamış olması durumunda,**[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)**yöntem boş bir dizi döndürür.
1. **[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)** yöntem, türde bir parametre kabul eder**sicim** değiştirmenin ayarlandığı yazı tipi adını belirtmeye izin verir. Belirtilen yazı tipi adı için herhangi bir ikame ayarlanmamışsa,**[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)**yöntem null döndürür.

## **ileri konular**
- [Elektronik tabloyu görüntülere dönüştürürken Varsayılan Yazı Tipini Ayarla](/cells/tr/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [PdfSaveOptions ve ImageOrPrintOptions'ın DefaultFont özelliğini önceliğe sahip olacak şekilde ayarlayın](/cells/tr/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Desteklenen Yazı Tipi Biçimleri](/cells/tr/net/supported-font-formats/)
- [Çalışma Sayfasından Görüntüye - Oluşturulan Görüntü için Piksel Biçimini Ayarla](/cells/tr/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
