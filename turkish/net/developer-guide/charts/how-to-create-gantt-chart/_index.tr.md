---
title: Gantt grafiği nasıl oluşturulur
linktitle: Gantt grafiği nasıl oluşturulur
type: docs
weight: 72
url: /tr/net/how-to-create-gantt-chart/
description: Aspose.Cells ta Gantt grafiği nasıl oluşturulur.
keywords: Aspose ile Excel e Gantt Grafiği oluşturma/ekleme
---
## Gantt grafiği nedir

Gantt grafiği, projenizdeki görevleri zamanlamaya yardımcı olur ve ilerlemenizi izlemenize yardımcı olur.

## Excel'e Gantt grafiği ekleme

Basit bir proje zaman çizelgesi için bir Gantt grafiği ile durumu göstermek mi gerekiyor? Excel'de önceden tanımlanmış bir Gantt grafik türü olmasa da, görevlerin başlangıç ve bitiş tarihlerini göstermek için bir yığın çubuk grafiğini özelleştirebilirsiniz.

![todo:image_alt_text](00.png)

![todo:image_alt_text](0.png)

## Nasıl oluşturulur

- Grafik olarak görmek istediğiniz verileri seçin. Örneğimizde, bu B1:B7 ve sonra **Yığın Çubuk** grafiği ekleyin.

![todo:image_alt_text](1.png)

- Grafiği seçin, **Veri Seçimi**->**Ekle**'yi seçin, **Seri adı** ve **Seri değerleri**'ni aşağıdaki gibi ayarlayın

![todo:image_alt_text](2.png)

- Grafiği seçin, **Yatay(Kategori) Eksen Etiketleri**'ni Düzenleyin

![todo:image_alt_text](3.png)

- **Y Eksenini Biçimlendir**'in, **Kategorileri ters sırada seçin**
- **Mavi Seriyi** seçin ve **Doldur->Doldur Yok** olarak ayarlayın
- **X Eksenini Biçimlendir**'in, **Minimum ve Maksimum**'u ayarlayın (1/5/2019: 43470, 1/30/2019: 43494)

![todo:image_alt_text](4.png)

- Grafiğe **Veri Etiketleri Ekle**
Şimdi bir Gantt grafiğiniz var.

## Aspose.Cells'ta Gantt grafiği ekleme

Aşağıdaki örnek kod, [örnek dosyayı](örnek.xlsx) açarak bir Gantt grafiği oluşturur.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

Benzer bir dosya olan [sonuç dosyasını](sonuç.xlsx) alacaksınız. Dosyada aşağıdakileri göreceksiniz:

![todo:image_alt_text](5.png)

