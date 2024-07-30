---
title: Gantt çizelgesi nasıl oluşturulur
linktitle: Gantt çizelgesi nasıl oluşturulur
type: docs
weight: 72
url: /tr/net/how-to-create-gantt-chart/
description: Aspose.Cells for .NET API ile bir Gantt çizelgesi nasıl oluşturulur öğrenin.
keywords: C# ile bir Gantt çizelgesi oluştur, bir Gantt çizelgesi ekle, bir Gantt çizelgesi ekle
---

## **Gantt çizelgesi nedir**

Gantt çizelgesi, bir proje takvimini gösteren bir çubuk çizelgesi türüdür. Bir projenin çeşitli unsurlarının başlangıç ve bitiş tarihlerini gösterir. Her görev veya etkinlik bir çubukla temsil edilir ve uzunluğu süresine karşılık gelir. Gantt çizelgeleri ayrıca görevler arasındaki bağımlılıkları da gösterir, bu sayede proje yöneticileri görevlerin tamamlanması gereken sıralamayı görselleştirebilir. Proje yönetiminde etkili bir şekilde planlama, programlama ve takip etmek için yaygın bir şekilde kullanılır.

## **Excel'de bir Gantt çizelgesi nasıl oluşturulur**

Excel'de bir Gantt çizelgesi oluşturabilirsiniz, şu adımları izleyerek:
1. Gantt şeması için bazı veriler ekleyin. 
<br>
<img src="00.png" width=50% />
1. Verileri seçin ve Ekle'ye gidin -> Grafikler -> Sütun veya Çubuk Grafiği Ekle -> Yığılmış Çubuk Grafiği. Örneğimizde, bu B1:B7 ve ardından Yığın Çubuk grafiği ekleme.
<br>
<img src="1.png" width=50% />

1. Şeması seçin, **Veri Seçimi**->**Ekle**, **Seri adı** ve **Seri değerlerini** aşağıdaki gibi ayarlayın.
<br>
<img src="2.png" width=50% />

1. Şemayı seçin, **Yatay(Kategori) Eksen Etiketleri**'ni düzenleyin.
<br>
<img src="3.png" width=50% />

1. Y Eksenini **Biçim** yapın, **Kategorileri ters sırada seç**.
1. **Mavi Seriyi** seçin ve **Dolgu->Dolgu Yok** ayarlayın.
1. X Eksenini **Biçim** yapın, **Minimum ve Maksimum** ayarlayın (1/5/2019:43470,1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. Şema için **Veri etiketleri ekle**, şimdi bir gantt şeması elde edersiniz.
<br>
<img src="0.png" width=50% />


## **Aspose.Cells'te Gantt Şeması Nasıl Eklenir**
Lütfen aşağıdaki örnek kodu inceleyin. Bazı örnek veriler içeren [örnek Excel dosyasını](sample.xlsx) yükler. Ardından, başlangıç verilerine dayalı olarak yığın çubuk grafiği oluşturur ve ilgili özellikleri ayarlar. Son olarak, çalışma kitabını [çıktı XLSX formatına](result.xlsx) kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells tarafından çıktı Excel dosyasında oluşturulan Gantt grafiğini gösterir.
<br>
<img src="5.png" width=60% />

### **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

