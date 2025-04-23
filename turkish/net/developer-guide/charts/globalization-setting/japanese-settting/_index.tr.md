---
title: Japon Bölgesi İçin Grafikleri Görüntüye Dönüştür
description: Aspose.Cells for .NET ayarlarını kullanarak grafik için Japon yapılandırmasını nasıl belirleyeceğinizi öğrenin. Rehberimiz, Japon karakterleri ve biçimlendirmeyi desteklemek için yazı tipleri, boyut, metin yönü ve daha fazlasını nasıl yapılandıracağınızı gösterecektir.
keywords: Aspose.Cells for .NET, Grafikler, Japon yapılandırması, yazı tipi, yazı tipi boyutu, metin yönü, destek.
linktitle: Japon Bölgesi Belirle
type: docs
weight: 10
url: /tr/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---

{{% alert color="primary" %}}

Bu konuda, bir grafik için Japon Bölgesi nasıl belirleneceğini göstereceğiz.

{{% /alert %}}

## **Bir miras sınıfı tanımlar**

İlk adım olarak, [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) tarafından miras alınan "ChartJapaneseSetttings" adlı bir sınıf tanımlamanız gerekir. 
Ardından ilgili işlevleri yeniden yazarak grafik öğelerinin metnini kendi dilinize göre belirleyebilirsiniz.
Kod örneği:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

## **Grafik için Japon Yapılandırmasını Yapın**

Bu adımda, önceki adımda tanımladığınız "ChartJapaneseSetttings" sınıfını kullanacaksınız.
Kod örneği:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Ardından çıktı görüntüsünde etkiyi görebilirsiniz, grafikteki unsurlar ayarlarınıza göre yeniden oluşturulur.

## **Sonuç**

Bu örnekte, bir grafik için Japon Bölgesi belirlemezseniz, aşağıdaki grafik unsurları varsayılan dilde, yani İngilizce olarak oluşturulabilir.
Yukarıdaki işlemden sonra, Japon Bölgesi ile çıktı grafik resmi alabiliriz.

|**Desteklenen unsurlar**|**Bu örnekteki değer**|**İngilizce ortamındaki varsayılan değer**|
| :- | :- | :- |
|Eksen Başlığı Adı|軸タイトル|Eksen Başlığı|
|Eksen Birimi Adı|百,千...|Yüz, Bin...|
|Grafik Başlığı Adı|グラフ タイトル|Grafik Başlığı|
|Legend Artış Adı|ぞうか|Artış|
|Legend Azalma Adı|削減|Azalma|
|Legend Total Adı|すべての|Toplam|
|Diğer Adı|その他|Diğer|
|Seri Adı|シリーズ|Seri|
{{< app/cells/assistant language="csharp" >}}
