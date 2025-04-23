---
title: Gantt grafiği nasıl oluşturulur?
linktitle: Gantt grafiği nasıl oluşturulur?
type: docs
weight: 72
url: /tr/net/how-to-create-gantt-chart/
description: API ile Gantt Çizelgesi Oluşturma Hakkında Aspose.Cells for .NET numaralı API ile öğrenin.
keywords: C# ile Gantt çizelgesi oluşturma, Gantt çizelgesi ekleme, Gantt çizelgesi ekleme
---

## **Gantt grafiği nedir?**

Gantt grafiği, bir proje takvimini anlatan bir tür çubuk grafik türüdür. Bir projenin çeşitli unsurlarının başlangıç ve bitiş tarihlerini gösterir. Her görev veya etkinlik, süresine karşılık gelen bir çubukla temsil edilir. Gantt grafikleri ayrıca görevler arasındaki bağımlılıkları gösterir, böylece proje yöneticileri görevlerin tamamlanması gereken sıralamayı görselleştirebilir. Bunlar, proje yönetiminde projeleri etkin şekilde planlamak, zamanlamak ve izlemek için yaygın olarak kullanılır.

## **Excel'de Gantt Grafiği Nasıl Oluşturulur?**

Excel'de Gantt grafiği oluşturmak için aşağıdaki adımları izleyebilirsiniz:
1. Gantt grafiği için bazı veri ekleyin. 
<br>
<img src="00.png" width=50% />
1. Verileri seçin ve Giriş --> Çizelgeler --> Sütun veya Çubuk Grafiği Ekle --> Katlı Çubuk Çizelgesi seçeneğine gidin. Örneğin, B1:B7 hücrelerini seçin ve sonra **Katlı Çubuk** grafiği ekleyin.
<br>
<img src="1.png" width=50% />

1. Grafiği seçin,**Veri Ekle**->**Seri Adı** ve **Seri Değerleri** ayarlarını aşağıdaki gibi yapın.
<br>
<img src="2.png" width=50% />

1. Grafiği seçin, **Yatay (Kategori) Eksen Etiketleri** düzenleyin.
<br>
<img src="3.png" width=50% />

1. **Eksen Biçimlendir** seçeneğiyle Y Ekseni, **Kategorileri ters sırada** seçin.
1. **Mavi Serisi** seçin ve **Doldur->Doldurma Yok** olarak ayarlayın.
1. X Eksenini **Biçimlendir**, **Minimum ve Maksimum** ayarlarını yapın (1/5/2019:43470, 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. Grafikte **Veri Etiketleri Ekle**, artık bir gantt grafiği alacaksınız.
<br>
<img src="0.png" width=50% />


## **Aspose.Cells'te Gantt Çizelgesi Nasıl Eklenir**
Lütfen aşağıdaki örnek kodu inceleyin. Bu kod, bazı örnek veriler içeren [örnek Excel dosyasını](sample.xlsx) yükler. Ardından, başlangıç verilerine dayanarak yığılmış çubuk grafiği oluşturur ve ilgili özellikleri belirler. Son olarak, çalışma kitabını [çıkış XLSX formatında](result.xlsx) kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells tarafından oluşturulan Gantt çizelgesini gösterir.
<br>
<img src="5.png" width=60% />

### **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

{{< app/cells/assistant language="csharp" >}}
