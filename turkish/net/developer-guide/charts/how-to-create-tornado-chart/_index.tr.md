---
title: Tornado grafiği nasıl oluşturulur.
type: docs
weight: 73
url: /tr/net/create-tornado-chart/
description: Aspose.Cells for .NET API ile bir tufan grafiği nasıl oluşturulur öğrenin.
keywords: C# ile bir tufan grafiği oluşturun, bir tufan grafiği ekleyin, bir tufan grafiği ekleyin.
---

## **Giriş**
Tufan grafiği, aynı zamanda tufan diyagramı veya tufan grafiği olarak da bilinen, Excel'de duyarlılık analizi için sıklıkla kullanılan bir veri görselleştirme türüdür. Belirli bir sonuç veya çıktı üzerinde değişkenlerin etkisini anlamanıza yardımcı olur.

## **Excel'de Bir Tufan Grafiği Nasıl Oluşturulur**
Excel'de bir tufan grafiği oluşturmak için şu adımları izleyebilirsiniz:
1. Verileri seçin ve Ekle --> Grafikler --> Sütun veya Çubuk Grafiği Ekle --> Yığılmış Çubuk Grafiği'ne tıklayın.
<br>
<img src="1.png" width=70% />
2. Y-eksenini değiştirin: Y-eksenine sağ tıklayın. Biçim eksenine tıklayın. Etiketlerde, etiket konumu açılır menüsüne tıklayın ve Düşük öğesini seçin.
<br>
<img src="2.png" width=70% />
3. Herhangi bir sütunu seçin ve biçimlendirmeye gidin. Uygun bir boşluk genişliği ayarlayın.
<br>
<img src="3.png" width=70% />
4. Tufan grafiğinden eksi işaretini (-) çıkaralım. X-eksenini seçin. Biçimlendirmeye gidin. Eksen seçeneklerinde, sayıya tıklayın. Kategoride, özel seçin. Biçim koduna ###0,###0 yazın. Ekle'ye tıklayın.
<br>
<img src="4.png" width=70% />
5. Y-eksenine tıklayın ve eksen seçeneklerine gidin. Eksen seçeneklerinde kategorileri ters sırada işaretleyin.
<br>
<img src="5.png" width=70% />

## **Aspose.Cells'te Bir Tufan Grafiği Nasıl Eklenir**
Lütfen aşağıdaki örnek kodu inceleyin. İçinde bazı örnek veriler içeren [örnek Excel dosyası](sample.xlsx) yükler. Ardından, başlangıç verilerine dayalı olarak yığılmış sütun grafiği oluşturur ve ilgili özellikleri ayarlar. Son olarak, çalışma kitabını [çıkış XLSX formatına](out.xlsx) kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells tarafından çıkış Excel dosyasında oluşturulan tufan grafiğini göstermektedir.
<br>
<img src="6.png" width=70% />

### **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-tornado-chart.cs" >}}
{{< app/cells/assistant language="csharp" >}}
