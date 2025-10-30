---
title: Büyük Veri Setlerine Sahip Büyük Dosyalarla Çalışırken Bellek Kullanımını Optimize Etme
type: docs
weight: 180
url: /tr/python-net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Büyük veri kümeleri ile çalışma kitabı oluştururken veya büyük bir Microsoft Excel dosyasını okurken, toplam RAM kullanımı her zaman önemli bir faktördür. Bu zorluğa karşı uyarlanabilecek önlemler vardır. Aspose.Cells for Python via .NET, bellek kullanımı azaltmak, düşürmek ve optimize etmek için bazı uygun seçenekler ve API çağrıları sağlar. Ayrıca, işlemin daha verimli çalışmasını ve daha hızlı çalışmasını sağlar.

Hücre verisi için bellek kullanımını optimize etmek ve genel bellek maliyetini azaltmak için [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) seçeneğini kullanın. Büyük veri setleri için hücreler oluştururken, varsayılan ayar ([**MemorySetting.NORMAL**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting)) kullanmaktan belirli bir miktarda bellek tasarrufu sağlayabilir.

{{% /alert %}}

## **Bellek Kullanımını Optimize Etme**

### **Büyük Excel Dosyaları Okuma**

Aşağıdaki örnek, optimize edilmiş modda büyük bir Microsoft Excel dosyasını nasıl okuyacağınızı göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.py" >}}

### **Büyük Excel Dosyaları Yazma**

Aşağıdaki örnek, optimize edilmiş bir modda bir çalışma sayfasına büyük bir veri seti yazmanın nasıl yapılacağını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OptimizingMemoryUsage-WritingLargeExcelFiles-1.py" >}}

## **Dikkat**

Varsayılan seçenek, [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) tüm sürümler için uygulanır. Ancak, bazı durumlarda, örneğin bir çalışma kitabı oluştururken hücreler için büyük bir veri kümesi oluşturmaları gereken durumlarda, [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) seçeneği hafıza kullanımını optimize edebilir ve uygulama için hafıza maliyetini azaltabilir. Bununla birlikte, bu seçenek bazı özel durumlarda performansı düşürebilir.

1. **Rastgele ve Tekrarlanan Şekilde Hücrelere Erişme**: Hücre koleksiyonuna erişmek için en verimli sıralama, önce bir satırda hücre hücre, ardından satır satır erişmektir. Özellikle, [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), [**RowCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/rowcollection) ve [**Row**](https://reference.aspose.com/cells/python-net/aspose.cells/row)'den elde edilen Numaralayıcı ile satırlara/hücrelere erişiyorsanız, performans [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) ile maksimize edilecektir.
1. **Hücreleri ve Satırları Ekleme ve Silme**: Hücreler/Satırlar için çok sayıda ekleme/silme işlemi varsa, *MemoryPreference* modu, *Normal* moduna göre performansın gözle görülür derecede düşmesine neden olacaktır.
1. **Farklı Hücre Türlerinde Çalışma**: Eğer hücrelerin çoğu dize değerleri veya formülleri içeriyorsa, hafıza maliyeti *Normal* mod ile aynı olacaktır, ancak boş hücreler veya hücre değerleri sayısal, mantıksal vb. ise, [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/python-net/aspose.cells/memorysetting) seçeneği daha iyi performans sunacaktır.

{{< app/cells/assistant language="python-net" >}}
