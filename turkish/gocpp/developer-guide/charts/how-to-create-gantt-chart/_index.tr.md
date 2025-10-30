---
title: Golang kullanarak C++ ile Gantt grafiği nasıl oluşturulur
linktitle: Gantt grafiği nasıl oluşturulur?
type: docs
weight: 72
url: /tr/go-cpp/how-to-create-gantt-chart/
description: Aspose.Cells for C++ API kullanarak Gantt grafiği nasıl oluşturulur öğrenin.
keywords: C++ ile Gantt grafiği oluşturma, Gantt grafiği ekleme, Gantt grafiği ekleme
---

## **Gantt grafiği nedir?**

Gantt grafiği, bir proje takvimini anlatan bir tür çubuk grafik türüdür. Bir projenin çeşitli unsurlarının başlangıç ve bitiş tarihlerini gösterir. Her görev veya etkinlik, süresine karşılık gelen bir çubukla temsil edilir. Gantt grafikleri ayrıca görevler arasındaki bağımlılıkları gösterir, böylece proje yöneticileri görevlerin tamamlanması gereken sıralamayı görselleştirebilir. Bunlar, proje yönetiminde projeleri etkin şekilde planlamak, zamanlamak ve izlemek için yaygın olarak kullanılır.

## **Excel'de Gantt Grafiği Nasıl Oluşturulur?**

Excel'de Gantt grafiği oluşturmak için aşağıdaki adımları izleyebilirsiniz:
1. Gantt grafiği için bazı veri ekleyin. 
<br>
<img src="00.png" width=50% />
1. Veriyi seçin ve Ekle --> Grafikler --> Sütun veya Çubuk Grafik Ekle --> Katlı Çubuk Grafik seçeneklerini kullanın. Örneğimizde, B1:B7, ve ardından **Katlı Çubuk** grafiği ekleyin.
<br>
<img src="1.png" width=50% />

1. Grafiği seçin, **Veri Seç**->**Ekle**, **Seri adı** ve **Seri değerleri** aşağıdaki gibi ayarlayın.
<br>
<img src="2.png" width=50% />

1. Grafiği seçin, **Yatay (Kategori) Eksen Etiketleri** düzenleyin.
<br>
<img src="3.png" width=50% />

1. **Eksen Biçimlendir** seçeneğiyle Y Ekseni, **Kategorileri ters sırada** seçin.
1. **Mavi Seri**yi seçin ve **Dolgu->HIÇ BİLGİ DOLGU** olarak ayarlayın.
1. **Eksen Biçimlendir** seçeneğiyle X Ekseni, **Minimum ve Maksimum**(1/5/2019:43470, 1/30/2019:43494) ayarını yapın.
<br>
<img src="4.png" width=50% />

1. Grafik için **Veri Etiketleri Ekle**, şimdi bir Gantt grafiği elde edeceksiniz.
<br>
<img src="0.png" width=50% />


## **Aspose.Cells'te Gantt Çizelgesi Nasıl Eklenir**
Lütfen aşağıdaki örnek kodu inceleyin. Bu kod, bazı örnek veriler içeren [örnek Excel dosyasını](sample.xlsx) yükler. Ardından, başlangıç verilerine dayanarak yığılmış çubuk grafiği oluşturur ve ilgili özellikleri belirler. Son olarak, çalışma kitabını [çıkış XLSX formatında](result.xlsx) kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells tarafından oluşturulan Gantt çizelgesini gösterir.
<br>
<img src="5.png" width=60% />

### **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToCreateGanttChart.go" >}}
