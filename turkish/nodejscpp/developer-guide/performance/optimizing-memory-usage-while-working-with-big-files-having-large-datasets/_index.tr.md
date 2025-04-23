---
title: Büyük Veri Setlerine Sahip Büyük Dosyalarla Çalışırken Bellek Kullanımını Optimize Etme
type: docs
weight: 110
url: /tr/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Büyük veri setleriyle çalışırken veya büyük bir Microsoft Excel dosyasını okurken, işlemin alacağı toplam RAM miktarı her zaman endişe kaynağıdır. Mücadele etmek için adapte edilebilecek önlemler bulunmaktadır. Aspose.Cells, bellek kullanımını azaltmak, düşürmek ve optimize etmek için bazı ilgili seçenekler ve API çağrıları sağlar. Ayrıca, işlemin daha verimli çalışmasına ve daha hızlı çalışmasına yardımcı olabilir.

Hücre verileri için kullanılan belleği azaltmak için [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) seçeneğini kullanın. Büyük veri kümesi oluştururken, varsayılan ayar kullanmaktan daha fazla bellek tasarrufu sağlayabilir.

{{% /alert %}}

## **Bellek Kullanımını Optimize Etme**

Aşağıdaki örnek, büyük verilerle çalışırken bellek kullanımını optimize etmenin yollarını gösterir Aspose.Cells for Node.js via C++.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "OptimizingMemory.js" >}}

## **Dikkat**

Varsayılan seçenek, [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) tüm sürümler için uygulanır. Bir çalışma kitabı büyük bir veri kümesi için hücreler için bir çalışma kitabı oluşturma gibi bazı durumlarda, [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) seçeneği bellek kullanımını optimize edebilir ve uygulama için bellek maliyetini azaltabilir. Ancak bu seçenek özellikle iz sürmedeki bazı özel durumlarda performansı düşürebilir.

1. **Rastgele ve Tekrarlanan Şekilde Hücrelere Erişme**: Hücre koleksiyonuna erişmek için en verimli sıralama, önce bir satırda hücre hücre, ardından satır satır erişmektir. Özellikle, [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection) ve [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row)'den elde edilen Numaralayıcı ile satırlara/hücrelere erişiyorsanız, performans [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) ile maksimize edilecektir.
1. **Hücreleri ve Satırları Ekleme & Silme**: Eğer Hücreler/Satırlar için birçok ekleme/silme işlemi varsa, [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) modu için performans düşüşü, [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) modu ile karşılaştırıldığında belirgin olacaktır.
1. **Farklı Hücre Türlerinde İşlemler**: Eğer hücrelerin çoğu dize değerleri veya formüller içeriyorsa, bellek maliyeti [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) modu ile aynı olacaktır ancak boş hücrelerin çok olduğu veya hücre değerlerinin sayısal, bool vb. olduğu durumlarda, [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) seçeneği daha iyi performans verecektir.

