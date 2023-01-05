---
title: Elektronik Tabloları Oluşturmak için Yazı Tiplerini Yapılandırma
type: docs
weight: 10
url: /tr/java/configuring-fonts-for-rendering-spreadsheets/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells API'leri, elektronik tabloları resim formatlarında oluşturmanın yanı sıra PDF ve XPS formatlarına dönüştürme olanağı sağlar. Dönüştürme doğruluğunu en üst düzeye çıkarmak için elektronik tabloda kullanılan yazı tiplerinin işletim sisteminin varsayılan yazı tipi dizininde bulunması gerekir. Gerekli yazı tiplerinin mevcut olmaması durumunda, Aspose.Cells API'leri gerekli yazı tiplerini mevcut olanlarla değiştirmeye çalışacaktır.

## **Yazı Tiplerinin Seçimi**

Aspose.Cells API'lerinin perde arkasında takip ettiği süreç aşağıdadır.

1. API, elektronik tabloda kullanılan yazı tipi adıyla tam olarak eşleşen dosya sistemindeki yazı tiplerini bulmaya çalışır.
1.  API aynı ada sahip yazı tiplerini bulamazsa, Çalışma Kitabı'nın altında belirtilen varsayılan yazı tipini kullanmayı dener.[**Varsayılan Stil. Yazı Tipi**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) Emlak.
1.  API, çalışma kitabının altında tanımlanan yazı tipini bulamazsa[**Varsayılan Stil. Yazı Tipi**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) özelliği altında belirtilen yazı tipini kullanmaya çalışır.[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) veya[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) Emlak.
1.  API altında tanımlanan yazı tipini bulamazsa[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) veya[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) özelliği altında belirtilen yazı tipini kullanmaya çalışır.[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) Emlak.
1.  API altında tanımlanan yazı tipini bulamazsa[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) özelliği, mevcut tüm yazı tiplerinden en uygun yazı tiplerini seçmeye çalışır.
1. Son olarak, API dosya sisteminde herhangi bir yazı tipi bulamazsa, elektronik tabloyu Arial kullanarak işler.

{{% alert color="primary" %}}

 Aspose.Cells API'leri her zaman işletim sisteminin varsayılan yazı tipi dizinini tek bir istisna dışında tarar; ne zaman JVM bağımsız değişkenleri**-DAspose.Cells.FontDirExc="FontDiziniz"**ayarlanır. Bu durumda, Aspose.Cells API'leri, işletim sisteminin varsayılan yazı tipi dizinini taramayı atlayacak ve yalnızca yukarıda belirtilen JVM bağımsız değişkenlerinde belirtilen yolu arayacaktır.

{{% /alert %}}

## **Özel Yazı Klasörlerini Ayarla**

 Aspose.Cells API'ler, gerekli yazı tipleri için işletim sisteminin varsayılan yazı tipi dizinini arar. Gerekli yazı tiplerinin sistemin yazı tipi dizininde bulunmaması durumunda, API'ler özel (kullanıcı tanımlı) dizinlerde arama yapar. bu[**Yazı Tipi Yapılandırmaları**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs)class, aşağıda ayrıntılı olarak açıklandığı gibi, özel yazı tipi dizinlerini ayarlamanın çeşitli yollarını ortaya çıkardı.

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)): Ayarlanacak yalnızca bir klasör varsa bu yöntem kullanışlıdır.
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)): Bu yöntem, yazı tipleri birden çok klasörde bulunduğunda ve kullanıcı tüm yazı tiplerini tek bir klasörde birleştirmek yerine tüm klasörleri ayrı ayrı ayarlamak istediğinde kullanışlıdır.
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources(com.aspose.cells.FontSourceBase[])): Bu mekanizma, kullanıcı birden çok klasörden yazı tiplerini veya tek bir yazı tipi dosyasını veya bir bayt dizisinden yazı tipi verilerini yüklemek istediğinde kullanışlıdır.

{{% alert color="primary" %}}

 Her ikisi de[**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)) & [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean) ) yöntemleri, bir Boole tipi ikinci parametreyi kabul eder. Geçen**doğru**ikinci parametre olarak Aspose.Cells API'lerini yazı tipi dosyaları için alt klasörleri aramaya yönlendirecektir.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

Lütfen başvuru başlangıcında yukarıda belirtilen yöntemlerden herhangi birini kullanınız, yani; Aspose.Cells API'lerinin diğer nesnelerini çağırmadan önce.

{{% /alert %}} {{% alert color="primary" %}}

Yazı tipi kaynaklarını ayarlamak için yukarıda belirtilen yöntemlerden birden fazlası kullanılırsa, yalnızca son ayarlar geçerli olacaktır.

{{% /alert %}}

## **Yazı Tipi Değiştirme Mekanizması**

Aspose.Cells API'ler, işleme amaçları için yedek yazı tipini belirtme olanağı da sağlar. Bu mekanizma, dönüştürmenin gerçekleşmesi gereken makinede gerekli bir yazı tipi bulunmadığında yardımcı olur. Kullanıcılar, başlangıçta gerekli olan yazı tipine alternatif olarak bir yazı tipi adları listesi sağlayabilir. Bunu başarmak için Aspose.Cells API'leri, 2 parametreyi kabul eden FontConfigs.setFontSubstitutes yöntemini kullanıma sunmuştur. İlk parametre türdedir**Sicim** , değiştirilmesi gereken yazı tipinin adı olmalıdır. İkinci parametre, bir tür dizisidir.**Sicim**. Kullanıcılar, orijinal yazı tipinin (ilk parametrede belirtilen) yerine geçen bir yazı tipi adları listesi sağlayabilir.

İşte basit bir kullanım senaryosu.

{{< highlight "java" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

## **Bilgi toplama**

Yukarıda belirtilen yöntemlere ek olarak, Aspose.Cells API'leri, hangi kaynakların ve ikamelerin ayarlandığı hakkında bilgi toplamak için araçlar da sağlamıştır.

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources() ): Bu yöntem, bir tür dizisi döndürür[**Yazı Tipi Kaynak Tabanı**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource)belirtilen yazı tipi kaynaklarının listesini içerir. Hiçbir kaynağın ayarlanmamış olması durumunda,[**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources()) yöntemi boş bir dizi döndürür.
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String) ): Bu yöntem, türünde bir parametre kabul eder**Sicim** değiştirmenin ayarlandığı yazı tipi adını belirtmeye izin verir. Belirtilen yazı tipi adı için herhangi bir ikame ayarlanmamışsa,[**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)) yöntemi null döndürür.
