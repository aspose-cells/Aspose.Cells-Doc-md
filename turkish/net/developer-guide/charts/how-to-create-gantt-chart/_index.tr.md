---
title: Gantt şeması nasıl oluşturulur
linktitle: Gantt şeması nasıl oluşturulur
type: docs
weight: 72
url: /tr/net/how-to-create-gantt-chart/
description: Aspose.Cells'de Gantt şeması nasıl oluşturulur?
keywords: create/insert Gantt Chart Excel Aspose
---
##  Gantt şeması nedir

Gantt şeması proje görevlerinizi planlamanıza ve ardından ilerlemenizi izlemenize yardımcı olur.

##  Excel'e Gantt grafiği ekleme

Gantt şemasıyla basit bir proje zamanlaması için durumu göstermeniz mi gerekiyor? Excel'de önceden tanımlanmış bir Gantt grafiği türü olmasa da, görevlerin başlangıç ve bitiş tarihlerini gösterecek şekilde yığılmış bir çubuk grafiği özelleştirerek bir benzetim yapabilirsiniz:

![yapılacak şey:image_alt_text](00.png)

![yapılacak şey:image_alt_text](0.png)

##  Nasıl oluşturulurum

-  Grafiği oluşturmak istediğiniz verileri seçin. Örneğimizde bu B1:B7 ve ardından Ekle**Yığılmış Çubuk** çizelge.

![yapılacak şey:image_alt_text](1.png)

- Grafiği seçin,**Veri Seç**->****Ekle**, **Seri adını ayarlayın** Ve**Seri değerleri** aşağıdaki gibi

![yapılacak şey:image_alt_text](2.png)

-  Grafiği seçin, Düzenleyin**Yatay(Kategori) Eksen Etiketleri**

![yapılacak şey:image_alt_text](3.png)

- **Ekseni Biçimlendir** Y Ekseni'ni seçin**Kategoriler ters sırada**
-  Şunu seçin:**Mavi Serisi** ve ayarlayın**Doldur->Doldurma YOK**
- **Ekseni Biçimlendir** X Ekseni, *Minimum ve Maksimum**'u ayarlayın(1/5/2019:43470,1/30/2019:43494)

![yapılacak şey:image_alt_text](4.png)

- **Veri dosyaları ekle** grafik için
Artık bir gantt grafiği elde ediyorsunuz.

## Aspose.Cells'e Gantt şemasını ekleyin

 Aşağıdaki örnek kod, bir Gantt grafiği açarak bir Gantt grafiği oluşturur.[örnek dosya](sample.xlsx)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

 Şuna benzer bir dosya alacaksınız[sonuç dosyası](result.xlsx).Dosyada aşağıdakileri göreceksiniz:

![yapılacak şey:image_alt_text](5.png)

