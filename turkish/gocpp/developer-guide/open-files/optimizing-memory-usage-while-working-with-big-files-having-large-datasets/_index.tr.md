---
title: Büyük Veri Setlerine Sahip Büyük Dosyalarla Çalışırken Bellek Kullanımını Optimize Etme (Golang ve C++ ile)
linktitle: Bellek Kullanımını Optimize Etmek
type: docs
weight: 180
url: /tr/go-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
description: Büyük Excel dosyalarıyla çalışırken bellek kullanımını optimize etmeyi Aspose.Cells ile Golang ve C++ kullanarak öğrenin.
---

{{% alert color="primary" %}}

Büyük veri setleri ile elektronik tablo oluştururken veya büyük bir Microsoft Excel dosyasını okurken, işlemin alacağı toplam RAM miktarı her zaman bir endişe kaynağıdır. Bu zorlukla başa çıkmak için adapte edilebilecek önlemler bulunmaktadır. Aspose.Cells, bellek kullanımını düşürmek, azaltmak ve optimize etmek için ilgili seçenekler ve API çağrıları sağlar. Ayrıca, işlemi daha verimli hale getirerek daha hızlı çalışmasına yardımcı olabilir.

Hücre verisi için bellek kullanımını optimize etmek ve genel bellek maliyetini azaltmak için [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/) seçeneğini kullanın. Büyük veri setleri için hücreler oluştururken, varsayılan ayar ([**MemorySetting.Normal**](https://reference.aspose.com/cells/go-cpp/memorysetting/)) kullanmaktan belirli bir miktarda bellek tasarrufu sağlayabilir.

{{% /alert %}}

## **Bellek Kullanımını Optimize Etme**

### **Büyük Excel Dosyaları Okuma**

Aşağıdaki örnek, optimize edilmiş modda büyük bir Microsoft Excel dosyasını nasıl okuyacağınızı göstermektedir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OptimizingMemoryUsageWhileWorkingWithBigFilesHavingLargeDatasets.go" >}}
### **Büyük Excel Dosyaları Yazma**

Aşağıdaki örnek, optimize edilmiş bir modda bir çalışma sayfasına büyük bir veri seti yazmanın nasıl yapılacağını gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OptimizingMemoryUsageWhileWorkingWithBigFilesHavingLargeDatasets-1.go" >}}
## **Dikkat**

Varsayılan seçenek, [**MemorySetting.Normal**](https://reference.aspose.com/cells/go-cpp/memorysetting/) tüm sürümler için uygulanır. Ancak, bazı durumlarda, örneğin bir çalışma kitabı oluştururken hücreler için büyük bir veri kümesi oluşturmaları gereken durumlarda, [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/) seçeneği hafıza kullanımını optimize edebilir ve uygulama için hafıza maliyetini azaltabilir. Bununla birlikte, bu seçenek bazı özel durumlarda performansı düşürebilir.

1. **Rastgele ve Tekrarlanan Şekilde Hücrelere Erişme**: Hücre koleksiyonuna erişmek için en verimli sıralama, önce bir satırda hücre hücre, ardından satır satır erişmektir. Özellikle, [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) ve [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/)'den elde edilen Numaralayıcı ile satırlara/hücrelere erişiyorsanız, performans [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) ile maksimize edilecektir.
1. **Hücreleri ve Satırları Ekleme ve Silme**: Hücreler/Satırlar için çok sayıda ekleme/silme işlemi varsa, *MemoryPreference* modu, *Normal* moduna göre performansın gözle görülür derecede düşmesine neden olacaktır.
1. **Farklı Hücre Türlerinde Çalışma**: Eğer hücrelerin çoğu dize değerleri veya formülleri içeriyorsa, hafıza maliyeti *Normal* mod ile aynı olacaktır, ancak boş hücreler veya hücre değerleri sayısal, mantıksal vb. ise, [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/go-cpp/memorysetting/) seçeneği daha iyi performans sunacaktır.
