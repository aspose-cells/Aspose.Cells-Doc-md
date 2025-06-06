---
title: Büyük Veri Setlerine Sahip Büyük Dosyalarla Çalışırken Bellek Kullanımını Optimize Etme
type: docs
weight: 110
url: /tr/nodejs-java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

Büyük veri setleriyle çalışırken veya büyük bir Microsoft Excel dosyasını okurken, işlemin alacağı toplam RAM miktarı her zaman endişe kaynağıdır. Mücadele etmek için adapte edilebilecek önlemler bulunmaktadır. Aspose.Cells, bellek kullanımını azaltmak, düşürmek ve optimize etmek için bazı ilgili seçenekler ve API çağrıları sağlar. Ayrıca, işlemin daha verimli çalışmasına ve daha hızlı çalışmasına yardımcı olabilir.

Hücre verileri için kullanılan belleği azaltmak için [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) seçeneğini kullanın. Büyük veri kümesi oluştururken, varsayılan ayar kullanmaktan daha fazla bellek tasarrufu sağlayabilir.

{{% /alert %}}

## **Bellek Kullanımını Optimize Etme**

Aşağıdaki örnek, Aspose.Cells for Node.js via Java ile büyük verilerle çalışırken bellek kullanımını nasıl optimize edeceğinizi göstermektedir.

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "optimize-memory-usage-while-working-with-large-data.js" >}}

## **Dikkat**

Varsayılan seçenek, [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) tüm sürümler için uygulanır. Bir çalışma kitabı büyük bir veri kümesi için hücreler için bir çalışma kitabı oluşturma gibi bazı durumlarda, [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) seçeneği bellek kullanımını optimize edebilir ve uygulama için bellek maliyetini azaltabilir. Ancak bu seçenek özellikle iz sürmedeki bazı özel durumlarda performansı düşürebilir.

1. **Rastgele ve Tekrarlanan Şekilde Hücrelere Erişme**: Hücre koleksiyonuna erişmek için en verimli sıralama, önce bir satırda hücre hücre, ardından satır satır erişmektir. Özellikle, [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) ve [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row)'den elde edilen Numaralayıcı ile satırlara/hücrelere erişiyorsanız, performans [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) ile maksimize edilecektir.
1. **Hücreleri ve Satırları Ekleme & Silme**: Eğer Hücreler/Satırlar için birçok ekleme/silme işlemi varsa, [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) modu için performans düşüşü, [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) modu ile karşılaştırıldığında belirgin olacaktır.
1. **Farklı Hücre Türlerinde İşlemler**: Eğer hücrelerin çoğu dize değerleri veya formüller içeriyorsa, bellek maliyeti [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) modu ile aynı olacaktır ancak boş hücrelerin çok olduğu veya hücre değerlerinin sayısal, bool vb. olduğu durumlarda, [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) seçeneği daha iyi performans verecektir.

