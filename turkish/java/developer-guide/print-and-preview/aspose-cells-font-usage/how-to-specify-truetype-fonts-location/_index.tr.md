---
title: TrueType Yazı Tiplerinin Konumu Nasıl Belirlenir?
type: docs
weight: 30
url: /tr/java/how-to-specify-truetype-fonts-location/
---
{{% alert color="primary" %}}

Bu makale şunları açıklamaktadır:

1. [Aspose.Cells API, TrueType yazı tiplerini nerede arar?](/cells/tr/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [Aspose.Cells API için TrueType yazı tipi klasörlerini açıkça belirtme](/cells/tr/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [Aspose.Cells API'i yalnızca bir TrueType yazı tipi konumu kullanacak şekilde kısıtlama](/cells/tr/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **Yazı Tipleriyle Çalışmak**

### **Aspose.Cells, Windows'de TrueType Yazı Tiplerini Aradığı Yer**

 Aspose.Cells, içinde yazı tiplerini arar.**Windows\Yazı Tipleri** Klasör. Bu varsayılan ayar çoğu zaman çalışır, bu nedenle yalnızca gerçekten ihtiyacınız varsa kendi yazı tipi klasörlerinizi belirtin.

### **Aspose.Cells, Linux'ta TrueType Yazı Tiplerini Nerede Arar?**

Varsayılan olarak, Aspose.Cells API, farklı Linux dağıtımları yazı tiplerini farklı klasörlerde saklasa da, aşağıdaki konumların tümünde yazı tiplerini arar.

1. /usr/paylaş/yazı tipleri
1. /usr/yerel/paylaş/yazı tipleri

{{% alert color="primary" %}}

 Bu varsayılan davranış, çoğu Linux dağıtımı için çalışacaktır, ancak her zaman çalışacağı garanti edilmez. TrueType yazı tiplerinin konumunu açıkça belirtmeniz gerekebilir.

{{% /alert %}}

### **Yazı Tipi Klasörünü Açıkça Belirtme**

Aspose.Cells API'ler, FontConfigs sınıfının aşağıda açıklandığı gibi yazı tiplerini veya yazı tipi klasörlerini belirtmesi için birçok fabrika yöntemini kullanıma sunmuştur.

1. setFontFolder yöntemi, String türündeki ilk parametreyi yazı tipi dizinine konumu ile kabul ederken, Boolean türündeki ikinci parametre, Aspose.Cells APis'i yazı tipi dosyaları için tekrar tekrar klasörleri aramaya yönlendirir.
1. setFontFolders yöntemi, String türünde bir dizi kabul eder, böylece bu yaklaşımı kullanarak birçok yazı tipi dizini belirtebilirsiniz. Aspose.Cells APis'i, ikinci parametre olarak true'yu belirterek tekrar tekrar klasörleri aramaya yönlendirebilirsiniz.
1. setFontSources yöntemi, tek tek yazı tiplerinin konumlarının bir listesini belirtmeniz için FontSourceBase türünde bir dizi kabul eder.

{{% alert color="primary" %}}

Yukarıda belirtilen yöntemlerden herhangi birini kullanarak yazı tipi klasörünü belirtirken, yazı tipi konumunu uygulamanın başında ayarlamanızı öneririz, aksi takdirde kötü biçimlendirilmiş sonuçlar alabilirsiniz.

{{% /alert %}} {{% alert color="primary" %}}

Yazı tipleri klasörünün yukarıdaki yöntemlerden herhangi biri kullanılarak ayarlanması, Aspose.Cells API'in yazı tiplerini sistemin yazı tipi klasörü gibi varsayılan konumlarda aramayacağını garanti etmez.

{{% /alert %}}

### **Aspose.Cells'i Yalnızca Bir Yazı Tipi Klasörü Kullanacak Şekilde Kısıtlama**

 Aspose.Cells for Java 8.1.0'dan başlayarak, JVM bağımsız değişkenlerini şu şekilde ayarlayın:**-DAspose.Cells.FontDirExc="YourFontDir**Aspose.Cells API'in yalnızca belirtilen yazı tipi konumunu kullanmasını sağlayacaktır.

Aşağıda gösterildiği gibi System.setProperty yöntemini kullanarak belirtilen bağımsız değişkenleri ayarlayın.

{{< highlight "java" >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

Lütfen aşağıdakilere dikkat edin:

- Yukarıdaki ifade başvurunuzun başında olmalıdır.
- Yukarıdaki yaklaşımı kullanmak, yukarıda tartışılan FontConfigs yöntemlerinden herhangi birini kullanarak yazı tipi dizininin ayarlanmasını gerektirmez.
- "FontDirSet" dizesi, gerekli yazı tiplerini içeren klasörün tam yolu olmalıdır.

{{% /alert %}}
