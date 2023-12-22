---
title: Japonya Bölgesi için Grafiği Resme Dönüştür
description: Grafiğin Japonca yapılandırmasını ayarlama Aspose.Cells for .NET'in nasıl kullanılacağını öğrenin. Kılavuzumuz, yazı tipleri, boyut, metin yönü ve daha fazlası dahil olmak üzere Japonca karakterleri ve biçimlendirmeyi destekleyecek şekilde grafiklerin nasıl yapılandırılacağını gösterecektir.
keywords: Aspose.Cells for .NET, Charts, Japanese configuration, font, font size, text direction, support.
linktitle: Japon Bölgesini Ayarla
type: docs
weight: 10
url: /tr/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---
{{% alert color="primary" %}}

Bu başlıkta size bir grafik için Japon Bölgesini nasıl ayarlayacağınızı göstereceğiz.

{{% /alert %}}

##  **Bir miras sınıfını tanımlar**

 İlk adım, miras alan bir "ChartJapaneseSettings" sınıfını tanımlamanız gerekir.[**GrafikKüreselleşmeAyarlar**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Daha sonra ilgili fonksiyonları yeniden yazarak grafik elemanlarının metnini kendi dilinizde ayarlayabilirsiniz.
Kod örneği:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

##  **Grafik İçin Japonca Ayarını Yapılandırma**

Bu adımda bir önceki adımda tanımladığınız "ChartJapaneseSettings" sınıfını kullanacaksınız.
Kod örneği:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Daha sonra çıktı görüntüsündeki efekti görebilirsiniz; grafikteki öğeler ayarlarınıza göre oluşturulacaktır.

##  **Çözüm**

Bu örnekte, bir grafik için Japonca Bölgesini ayarlamazsanız aşağıdaki grafik öğeleri İngilizce gibi varsayılan dilde görüntülenebilir.
Yukarıdaki işlemden sonra Japon Bölgesi ile çıktı grafiği resmi elde edebiliriz.

|**Desteklenen öğeler**|**Bu örnekteki değer**|**İngilizce ortamında varsayılan değer**|
| :- | :- | :- |
|Eksen Başlığı Adı|軸タイトル|Eksen Başlığı|
|Eksen Birimi Adı|百,千...|Yüzlerce, binlerce...|
|Grafik Başlığı Adı|グラフ タイトル|Grafik başlığı|
|Efsane Artış Adı|ぞうか|Arttırmak|
|Açıklama Adı Azaltma|削減|Azaltmak|
|Efsane Toplam Adı|すべての|Toplam|
|Diğer Ad|その他|Diğer|
|Seri Adı|シリーズ|Seri|
