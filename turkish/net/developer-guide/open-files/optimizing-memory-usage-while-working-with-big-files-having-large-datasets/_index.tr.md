---
title: Büyük Veri Kümelerine Sahip Büyük Dosyalarla Çalışırken Bellek Kullanımını Optimize Etme
type: docs
weight: 180
url: /tr/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---
{{% alert color="primary" %}}

Büyük veri kümeleri içeren bir çalışma kitabı oluştururken veya büyük bir Microsoft Excel dosyasını okurken, işlemin alacağı toplam RAM miktarı her zaman endişe vericidir. Zorlukla başa çıkmak için uyarlanabilecek önlemler var. Aspose.Cells bazı ilgili seçenekler sunar ve API hafıza kullanımını azaltmak, azaltmak ve optimize etmek için çağrı yapar. Ayrıca, sürecin daha verimli çalışmasına ve daha hızlı çalışmasına yardımcı olabilir.

 Kullan[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)Hücre verileri için bellek kullanımını optimize etme ve genel bellek maliyetini düşürme seçeneği. Hücreler için büyük bir veri kümesi oluştururken, varsayılan ayarı kullanmaya kıyasla belirli bir miktarda bellek tasarrufu sağlayabilir ([**Bellek Ayarı.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)).

{{% /alert %}}

## **Belleği Optimize Etme**

### **Büyük Excel Dosyalarını Okuma**

Aşağıdaki örnek, büyük bir Microsoft Excel dosyasının optimize edilmiş modda nasıl okunacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **Büyük Excel Dosyaları Yazma**

Aşağıdaki örnek, optimize edilmiş modda bir çalışma sayfasına büyük bir veri kümesinin nasıl yazılacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **Dikkat**

 Varsayılan seçenek,[**Bellek Ayarı.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)tüm sürümler için geçerlidir. Hücreler için büyük bir veri kümesi içeren bir çalışma kitabı oluşturmak gibi bazı durumlarda,[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)seçeneği bellek kullanımını optimize edebilir ve uygulama için bellek maliyetini azaltabilir. Ancak bu seçenek aşağıdaki gibi bazı özel durumlarda performansı düşürebilir.

1. **Cells'e Rastgele ve Tekrarlayarak Erişim** : Hücre koleksiyonuna erişmek için en verimli sıralama, bir satırda hücre hücre ve ardından satır satırdır. Özellikle, Numaralandırıcı tarafından alınan satırlara/hücrelere erişirseniz[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), [**Satır Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection) ve[**Sıra**](https://reference.aspose.com/cells/net/aspose.cells/row) , performans ile maksimize edilecektir[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting).
1. **Cells & Satır Ekleme ve Silme** : Lütfen Cells/Satırlar için çok sayıda ekleme/silme işlemi varsa, performans düşüşünün dikkate değer olacağını unutmayın.*Bellek Tercihi* modu ile karşılaştırıldığında*Normal*mod.
1. **Farklı Cell Tiplerinde Çalışma** : Hücrelerin çoğu dize değerleri veya formüller içeriyorsa, bellek maliyeti aynı olacaktır.*Normal* ancak çok sayıda boş hücre varsa veya hücre değerleri sayısal, bool vb. ise,[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)seçeneği daha iyi performans verecektir.
