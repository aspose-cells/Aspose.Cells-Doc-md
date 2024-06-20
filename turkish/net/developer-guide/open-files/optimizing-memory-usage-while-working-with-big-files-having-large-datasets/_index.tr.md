---
title: Büyük Veri Setlerine Sahip Büyük Dosyalarla Çalışırken Bellek Kullanımını Optimize Etme
type: docs
weight: 180
url: /tr/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Büyük veri setleri ile elektronik tablo oluştururken veya büyük bir Microsoft Excel dosyasını okurken, işlemin alacağı toplam RAM miktarı her zaman bir endişe kaynağıdır. Bu zorlukla başa çıkmak için adapte edilebilecek önlemler bulunmaktadır. Aspose.Cells, bellek kullanımını düşürmek, azaltmak ve optimize etmek için ilgili seçenekler ve API çağrıları sağlar. Ayrıca, işlemi daha verimli hale getirerek daha hızlı çalışmasına yardımcı olabilir.

Hücre verisi için bellek kullanımını optimize etmek ve genel bellek maliyetini azaltmak için [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) seçeneğini kullanın. Büyük veri setleri için hücreler oluştururken, varsayılan ayar ([**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)) kullanmaktan belirli bir miktarda bellek tasarrufu sağlayabilir.

{{% /alert %}}

## **Bellek Kullanımını Optimize Etme**

### **Büyük Excel Dosyaları Okuma**

Aşağıdaki örnek, optimize edilmiş modda büyük bir Microsoft Excel dosyasını nasıl okuyacağınızı göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **Büyük Excel Dosyaları Yazma**

Aşağıdaki örnek, optimize edilmiş bir modda bir çalışma sayfasına büyük bir veri seti yazmanın nasıl yapılacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **Dikkat**

Varsayılan seçenek, [**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) tüm sürümler için uygulanır. Ancak, bazı durumlarda, örneğin bir çalışma kitabı oluştururken hücreler için büyük bir veri kümesi oluşturmaları gereken durumlarda, [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) seçeneği hafıza kullanımını optimize edebilir ve uygulama için hafıza maliyetini azaltabilir. Bununla birlikte, bu seçenek bazı özel durumlarda performansı düşürebilir.

1. **Rastgele ve Tekrarlanan Şekilde Hücrelere Erişme**: Hücre koleksiyonuna erişmek için en verimli sıralama, önce bir satırda hücre hücre, ardından satır satır erişmektir. Özellikle, [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection) ve [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row)'den elde edilen Numaralayıcı ile satırlara/hücrelere erişiyorsanız, performans [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) ile maksimize edilecektir.
1. **Hücreleri ve Satırları Ekleme ve Silme**: Hücreler/Satırlar için çok sayıda ekleme/silme işlemi varsa, *MemoryPreference* modu, *Normal* moduna göre performansın gözle görülür derecede düşmesine neden olacaktır.
1. **Farklı Hücre Türlerinde Çalışma**: Eğer hücrelerin çoğu dize değerleri veya formülleri içeriyorsa, hafıza maliyeti *Normal* mod ile aynı olacaktır, ancak boş hücreler veya hücre değerleri sayısal, mantıksal vb. ise, [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) seçeneği daha iyi performans sunacaktır.
