---
title: Büyük Veri Kümelerine Sahip Büyük Dosyalarla Çalışırken Bellek Kullanımını Optimize Etme
type: docs
weight: 110
url: /tr/nodejs-java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

Büyük veri kümeleri içeren bir çalışma kitabı oluştururken veya büyük bir Microsoft Excel dosyasını okurken, işlemin alacağı toplam RAM miktarı her zaman endişe vericidir. Zorlukla başa çıkmak için uyarlanabilecek önlemler var. Aspose.Cells bazı ilgili seçenekler sunar ve API hafıza kullanımını azaltmak, azaltmak ve optimize etmek için çağrı yapar. Ayrıca, sürecin daha verimli çalışmasına ve daha hızlı çalışmasına yardımcı olabilir.

 Kullanmak[**Bellek Ayarı.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) Genel bellek maliyetini azaltmak için hücreler verileri için kullanılan belleği optimize etme seçeneği. Hücreler için büyük veri seti oluştururken, varsayılan ayarı kullanmaya kıyasla belirli bir miktarda bellek tasarrufu sağlayabilir.[**Bellek Ayarı.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **Belleği Optimize Etme**

Aşağıdaki örnek, Aspose.Cells for Node.js via Java'de büyük verilerle çalışırken bellek kullanımının nasıl optimize edileceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-nodejs-optimize-memory-usage-while-working-with-large-data.java" >}}

## **Dikkat**

 Varsayılan seçenek,[**Bellek Ayarı.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)tüm sürümler için geçerlidir. Hücreler için büyük bir veri kümesi içeren bir çalışma kitabı oluşturmak gibi bazı durumlarda,[**Bellek Ayarı.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)seçeneği bellek kullanımını optimize edebilir ve uygulama için bellek maliyetini azaltabilir. Ancak bu seçenek aşağıdaki gibi bazı özel durumlarda performansı düşürebilir.

1. **Cells'e Rastgele ve Tekrarlayarak Erişim** : Hücre koleksiyonuna erişmek için en verimli sıralama, bir satırda hücre hücre ve ardından satır satırdır. Özellikle, Numaralandırıcı tarafından alınan satırlara/hücrelere erişirseniz[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**Satır Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) ve[**Sıra**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) , performans ile maksimize edilecektir[**Bellek Ayarı.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE).
1. **Cells & Satır Ekleme ve Silme** : Lütfen Cells/Satırlar için çok sayıda ekleme/silme işlemi varsa, performans düşüşünün dikkate değer olacağını unutmayın.[**Bellek Ayarı.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) modu ile karşılaştırıldığında[**Bellek Ayarı.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)mod.
1. **Farklı Cell Tiplerinde Çalışma** : Hücrelerin çoğu dize değerleri veya formüller içeriyorsa, bellek maliyeti aynı olacaktır.[**Bellek Ayarı.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL)ancak çok sayıda boş hücre varsa veya hücre değerleri sayısal, bool vb. ise,[**Bellek Ayarı.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE)seçeneği daha iyi performans verecektir.

