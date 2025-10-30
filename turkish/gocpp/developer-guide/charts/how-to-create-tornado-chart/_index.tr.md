---
title: Golang kullanarak C++ ile Tornado grafiği nasıl oluşturulur
linktitle: Tornado Grafiği Oluştur
type: docs
weight: 73
url: /tr/go-cpp/create-tornado-chart/
description: Aspose.Cells for C++ API kullanarak tornado grafiği nasıl oluşturulacağını öğrenin.
keywords: C++ ile tornado grafiği oluştur, tornado grafiği ekle, tornado grafiği yerleştir
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
5. Y-eksenine tıklayın ve eksen seçeneklerine gidin. Eksen seçeneklerinde, Kategorileri ters sırada işaretleyin.
<br>
<img src="5.png" width=70% />

## **Aspose.Cells'te Bir Tufan Grafiği Nasıl Eklenir**
Lütfen aşağıdaki örnek kodu inceleyin. İçinde bazı örnek veriler içeren [örnek Excel dosyası](sample.xlsx) yükler. Ardından, başlangıç verilerine dayalı olarak yığılmış sütun grafiği oluşturur ve ilgili özellikleri ayarlar. Son olarak, çalışma kitabını [çıkış XLSX formatına](out.xlsx) kaydeder. Aşağıdaki ekran görüntüsü, Aspose.Cells tarafından çıkış Excel dosyasında oluşturulan tufan grafiğini göstermektedir.
<br>
<img src="6.png" width=70% />

### **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToCreateTornadoChart.go" >}}
