---
title: Noktayı toplam olarak ayarlama nasıl yapılır
description: Bazı Excel grafikleri, örneğin düşüş grafiği (WaterFall chart), noktayı toplam olarak ayarlamanız gerekebilir. Bu makale, Aspose.Cells kullanarak nasıl yapılacağını anlatmaktadır. 
keywords: WaterFall Grafiği, Nokta, toplam olarak ayarla.
type: docs
weight: 72
url: /tr/net/how-to-set-point-as-total/
---

## Excel Grafiklerinde "Noktayı toplam olarak ayarla" nedir?

 Bazı Excel grafiklerinde, örneğin WaterFall grafikte, bazı nokta verileri önceki noktaların toplamıdır, bu yüzden "noktayı toplam olarak ayarla" gerekebilir. Aşağıda örnek kod ve açıklamaları gösterilmektedir.

## WaterFall Grafiği için "Noktayı toplam olarak ayarla" gerekebilir 

![todo:image_alt_text](set-as-total1.png)

Bu resim, Excel'deki bir WaterFall grafiğini göstermektedir. Başlangıçta "Toplam" ile başlayan dört veri noktası görebiliyoruz ve bunlar önceki tüm verileri saymak için kullanılır.
Bu resimde, ayarlar tam anlamıyla doğru değil, bir nokta "Total 2024" seçildiğinde ve "Toplam olarak ayarla" seçeneğinin işaretli olmadığını görebiliyoruz.
Aşağıda düzenlenmesi gereken [örnek Excel dosyası](SampleSheet.xlsx) eklenmiştir ve bunu doğru şekilde ayarlamak için Aspose.Cells kullanılacaktır.

## Aspose.Cells kullanarak "Toplam olarak Nokta" ayarlama 

Dosyanın doğru şekilde ayarlanması için aşağıdaki kodu kullanıyoruz:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Set-point-as-total.cs" >}}

Aşağıdaki doğru [çıktı dosyasını](output.xlsx) edinebilirsiniz

Aşağıdaki şekilde gösterildiği gibi, dört "Toplam" veri noktası doğru şekilde ayarlandı ve önceki grafikten farkı görebilirsiniz.

![todo:image_alt_text](set-as-total2.png)
{{< app/cells/assistant language="csharp" >}}
