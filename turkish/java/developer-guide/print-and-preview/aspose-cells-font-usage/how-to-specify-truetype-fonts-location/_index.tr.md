---
title: TrueType Yazı Tiplerinin Konumunu Belirtme
type: docs
weight: 30
url: /tr/java/how-to-specify-truetype-fonts-location/
---

{{% alert color="primary" %}}

Bu makalede şunlar açıklanmaktadır:

1. [Aspose.Cells API'nın TrueType yazı tiplerini nerede aradığı](/cells/tr/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows)
1. [Aspose.Cells API için açıkça bir TrueType yazı tipi klasörü belirtme](/cells/tr/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder)
1. [Aspose.Cells API'nın yalnızca bir TrueType yazı tipi konumu kullanmasını nasıl kısıtlayacağınız](/cells/tr/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder)

{{% /alert %}}

## **Yazı Tipleriyle Çalışma**

### **Aspose.Cells'ın Windows'ta TrueType Yazı Tiplerini Nerede Aradığı**

Aspose.Cells, varsayılan olarak yazı tiplerini **Windows\Fonts** klasöründe arar. Bu varsayılan ayar çoğu zaman işe yarar, bu yüzden kendi yazı tiplerinizin klasörlerini yalnızca gerçekten ihtiyacınız olduğunda belirtin.

### **Aspose.Cells'te TrueType Yazı Tipleri Nerede Arar**

Varsayılan olarak, Aspose.Cells API, aşağıdaki tüm konumlarda yazı tiplerini arar, ancak farklı Linux dağıtımları yazı tiplerini farklı klasörlerde saklar.

1. /usr/share/fonts
1. /usr/local/share/fonts

{{% alert color="primary" %}}

Bu varsayılan davranış çoğu Linux dağıtımı için çalışacaktır, ancak her zaman çalışacağı garanti edilmez. TrueType yazı tiplerinin konumunu açıkça belirtmeniz gerekebilir. 

{{% /alert %}}

### **Bir Yazı Tipi Klasörünü Açıkça Belirtme**

Aspose.Cells API'leri, aşağıda açıklandığı gibi yazı tiplerini veya yazı tipi klasörlerini belirtmek için FontConfigs sınıfı için birçok fabrika yöntemi sunmuştur.

1. setFontFolder yöntemi, yazı tiplerinin bulunduğu klasörün konumunu içeren birinci parametrele String türünü ve ikinci parametrele Boolean türünü kabul eder ve Aspose.Cells API'lerinin klasörleri yazı tipi dosyaları için rekürsif olarak aramasını yönlendirir.
1. setFontFolders yöntemi, bu yaklaşımı kullanarak bir dizi String türünde alır, böylece birçok yazı tipi dizinini belirtebilirsiniz. Ayrıca, ikinci parametre olarak true belirterek Aspose.Cells API'lerini klasörleri rekürsif olarak aramasını da sağlayabilirsiniz.
1. setFontSources yöntemi, size bireysel yazı tiplerinin konumunu belirtmek için FontSourceBase türünde bir dizi kabul eder.

{{% alert color="primary" %}}

Yukarıda bahsedilen herhangi bir yöntemle yazı tipleri klasörünü belirtirken, yazı tipi konumunu uygulamanın başlangıcında ayarlamanızı öneririz; aksi takdirde kötü biçimlendirilmiş sonuçlar alabilirsiniz.

{{% /alert %}} {{% alert color="primary" %}}

Yukarıdaki yöntemlerden herhangi birini kullanarak yazı tipleri klasörünü belirtmek, Aspose.Cells API'nin sistem font klasörü gibi varsayılan konumlarda yazı tiplerini aramayacağının garantisini vermez.

{{% /alert %}}

### **Yalnızca Bir Yazı Tipi Klasörünü Kullanmak İçin Aspose.Cells'ın Nasıl Kısıtlanacağı**

Aspose.Cells for Java 8.1.0 sürümünden itibaren, **-DAspose.Cells.FontDirExc="YourFontDir** JVM argümanlarının ayarlanması, Aspose.Cells API'nin yalnızca belirtilen yazı tipleri konumunu kullanacağını sağlar.

Aşağıda gösterildiği gibi System.setProperty yöntemini kullanarak belirtilen argümanları ayarlayın.

{{< highlight java >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

Lütfen aşağıdakilere dikkat edin:

- Yukarıdaki ifade uygulamanın başlangıcında olmalıdır.
- Yukarıdaki yaklaşım, yukarıda tartışılan FontConfigs yöntemlerinden herhangi biriyle yazı klasörünü ayarlamayı gerektirmez.
- "FontDirSet" dizesi, gereken yazı tiplerini içeren klasörün tam yolunu olmalıdır.

{{% /alert %}}
