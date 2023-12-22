---
title: Kasırga grafiği nasıl oluşturulur
type: docs
weight: 73
url: /tr/net/create-tornado-chart/
description: Aspose.Cells for .NET API'i kullanarak kasırga grafiğinin nasıl oluşturulacağını öğrenin.
keywords: C# create a tornado chart, add a tornado chart, insert a tornado chart
---
##  **giriiş**
Kasırga diyagramı veya kasırga grafiği olarak da bilinen kasırga grafiği, Excel'de duyarlılık analizi için sıklıkla kullanılan bir veri görselleştirme türüdür. Değişen değişkenlerin belirli bir sonuç veya sonuç üzerindeki etkisini anlamanıza yardımcı olur.

##  **Excel'de Kasırga Grafiği Nasıl Oluşturulur**
Aşağıdaki adımları izleyerek Excel'de bir kasırga grafiği oluşturabilirsiniz:
1. Verileri seçin ve Ekle --> Grafikler --> Sütun veya Çubuk Grafik Ekle --> Yığılmış Çubuk Grafik'e gidin. Üstüne tıkla.
<br>
<img src="1.png" width=70% />
2. Y eksenini değiştirin: Y eksenine sağ tıklayın. Biçim eksenine tıklayın. Etiketlerde etiket konumu açılır menüsüne tıklayın ve Düşük öğeyi seçin.
<br>
<img src="2.png" width=70% />
3. Herhangi bir çubuğu seçin ve biçimlendirmeye gidin. Uygun bir boşluk genişliği ayarlayın.
<br>
<img src="3.png" width=70% />
4. Kasırga haritasından eksi işaretini (-) kaldıralım. X eksenini seçin. Biçimlendirmeye gidin. Eksen seçeneklerinde sayıya tıklayın. Kategoride özel'i seçin. Format koduna ###0,###0 yazın. Ekle'ye tıklayın.
<br>
<img src="4.png" width=70% />
5. y eksenine tıklayın ve eksen seçeneklerine gidin. Eksen seçeneklerinde Kategorileri ters sırayla işaretleyin.
<br>
<img src="5.png" width=70% />

##  **Aspose.Cells'de Kasırga Grafiği Nasıl Eklenir?**
 Lütfen aşağıdaki örnek koda bakın. Şunu yükler:[örnek Excel dosyası](sample.xlsx) bazı örnek veriler içerir. Daha sonra ilk verilere dayalı olarak yığılmış çubuk grafiği oluşturur ve ilgili özellikleri ayarlar. Son olarak çalışma kitabını şuraya kaydeder:[çıktı XLSX biçimi](out.xlsx). Aşağıdaki ekran görüntüsü, çıktı Excel dosyasında Aspose.Cells tarafından oluşturulan kasırga grafiğini göstermektedir.
<br>
<img src="6.png" width=70% />

###  **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-tornado-chart.cs" >}}