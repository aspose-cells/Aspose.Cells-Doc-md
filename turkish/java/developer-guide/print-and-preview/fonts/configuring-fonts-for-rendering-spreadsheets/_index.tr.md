---
title: Yayınlanan İşlenmiş Elektronik Tablolar için Yazı Tiplerini Yapılandırma
type: docs
weight: 10
url: /tr/java/configuring-fonts-for-rendering-spreadsheets/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells API'ları, elektronik tabloları görüntü formatlarında işlemek ve onları PDF ve XPS formatlarına dönüştürmek için olanak sağlar. Dönüşüm sadakatini maksimuma çıkarmak için, elektronik tabloda kullanılan yazı tiplerinin işletim sisteminin varsayılan yazı tipi dizininde bulunmalıdır. Gerekli yazı tipleri mevcut değilse, Aspose.Cells API'ları gerekli yazı tiplerini bulmak için çaba harcayacaktır.

## **Yazı Tiplerinin Seçimi**

Aspose.Cells API'ları tarafından perde arkasında izlenen süreç aşağıda belirtilmiştir.

1. API, elektronik tabloda kullanılan tam olarak eşleşen yazı tipini dosya sistemi üzerinde bulmaya çalışır.
2. API, aynı ebeveyn düğümü altında kullanılan varsayılan yazı tipini belirleyebilecek olan [**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) özelliği altında belirtilen varsayılan yazı tipini kullanmaya çalışır.
3. API, yazı tipini belirleyemiyorsa, [**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) veya [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) özelliği altında belirtilen yazı tipini kullanmaya çalışır.
4. API, yazı tipini belirleyemiyorsa, [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) özelliği altında belirtilen yazı tipini kullanmaya çalışır.
1. API, [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) özelliği altında tanımlanan yazı tipi bulunamazsa, mevcut yazı tiplerinden en uygun olanını seçmeye çalışır.
1. Son olarak, API dosya sisteminde herhangi bir yazı tipi bulamazsa, çalışsayı Arial kullanarak elektronik tabloyu oluşturur.

{{% alert color="primary" %}}

Genellikle, Aspose.Cells API'leri Windows, Linux, MacOS üzerinde varsayılan işletim sistemi font dizinlerini tarar. [Aspose.Cells for Java 24.7](https://releases.aspose.com/cells/java/release-notes/2024/aspose-cells-for-java-24-7-release-notes/) sürümünden itibaren, API'ler ayrıca Office önbellekli bulut font dizinlerini de varsayılan olarak tarar.

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells API'leri, tek istisna ile her zaman işletim sisteminin varsayılan font dizinini tarar; bu, JVM argümanları **-DAspose.Cells.FontDirExc="YourFontDir"** ayarlandığında olur. Bu durumda, Aspose.Cells API'leri, işletim sisteminin varsayılan font dizinini taramayı atlar ve yalnızca yukarıda belirtilen JVM argümanlarında belirtilen yolu arar.

{{% /alert %}}

## **Özel Yazı Tipi Klasörlerini Ayarlayın**

Aspose.Cells API'leri, gerekli fontları işletim sisteminin varsayılan font dizininde arar. Gerekli fontlar sistem font dizininde mevcut değilse API'ler, özel (kullanıcı tanımlı) dizinler aracılığıyla arama yapar. [**FontConfigs**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs) sınıfı, özel font dizinlerini ayarlamak için aşağıda ayrıntıları verilen bir dizi yöntem sunmuştur.

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder-java.lang.String-boolean-): Bu yöntem, sadece bir klasör ayarlanacaksa kullanışlıdır.
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders-java.lang.String[]-boolean-): Bu yöntem, yazı tiplerinin birden fazla klasörde bulunduğu durumda ve kullanıcı tüm klasörleri tek tek birleştirmek yerine ayrı ayrı ayarlamak istediğinde kullanışlıdır.
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources-com.aspose.cells.FontSourceBase[]-): Bu mekanizma, kullanıcının birden fazla klasörden veya tek bir yazı tipi dosyasından veya bayt dizisinden yazı tiplerini yüklemek istemesi durumunda kullanışlıdır.

{{% alert color="primary" %}}

[**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder-java.lang.String-boolean-) ve [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders-java.lang.String[]-boolean-) yöntemleri, ikinci bir parametre olarak Boolean türünde bir değer kabul eder. İkinci parametre olarak **true** değerini iletmek, Aspose.Cells API'lerinin font dosyalarını alt klasörlere aramasını sağlar.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

Lütfen uygulamanın başında yukarıda belirtilen yöntemlerden herhangi birini kullanın; yani, Aspose.Cells API'lerinin diğer nesnelerini çağırmadan önce.

{{% /alert %}} {{% alert color="primary" %}}

Yukarıda belirtilen yöntemlerden birden fazlası font kaynaklarını ayarlamak için kullanıldığında, yalnızca son ayarlamalar etkili olacaktır.

{{% /alert %}}

## **Yazı Tipi Yedekleme Mekanizması**

Aspose.Cells API'leri ayrıca, render işlemleri için yedek font belirtme yeteneği sağlar. Bu mekanizma, dönüşümün gerçekleştirileceği makinede gerekli bir font bulunmadığında faydalıdır. Kullanıcılar, asıl gerekli fontun yerine geçmesi için bir dizi font adı sağlayabilir. Bunun için, Aspose.Cells API'leri FontConfigs.setFontSubstitutes yöntemini açığa çıkarmıştır ve bu yöntem 2 parametre kabul eder. İlk parametre **String** türünde olup, yerine geçecek fontun adı olmalıdır. İkinci parametre **String** türünde bir dizi olarak alınır. Kullanıcılar, orijinal fontun yerine geçecek bir dizi font adı sağlayabilirler (ilk parametrede belirtilen orijinal font için).

İşte basit bir kullanım senaryosu.

{{< highlight java >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

## **Bilgi Toplama**

Yukarıda bahsedilen yöntemlere ek olarak, Aspose.Cells API'leri, hangi kaynak ve yedeklemelerin ayarlandığı hakkında bilgi toplamak için de yöntemler sağlamıştır.

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--): Bu yöntem, belirtilen font kaynaklarının listesini içeren [**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource) türünde bir dizi döndürür. Eğer kaynaklar belirlenmemişse, [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--) yöntemi boş bir dizi döndürecektir.
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes-java.lang.String-): Bu yöntem, yerine geçme belirlenmiş font adını belirtmeye izin veren **String** türünde bir parametre alır. Belirtilen font adı için yerine geçme belirlenmemişse, [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes-java.lang.String-) yöntemi null döndürecektir.
{{< app/cells/assistant language="java" >}}
