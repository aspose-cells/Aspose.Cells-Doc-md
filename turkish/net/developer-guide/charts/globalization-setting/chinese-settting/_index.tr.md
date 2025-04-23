---
title: Çin Bölgesi için Grafikleri Görüntüye Dönüştür
description: Aspose.Cells for .NET ayarlarının Çin yapılandırmasını nasıl yapılacağını öğrenin. Rehberimiz, fontlar, boyutlar, metin yönleri ve daha fazlasını içeren Çince karakterleri ve formatları desteklemek için grafikleri nasıl yapılandıracağınızı gösterecektir.
keywords: Aspose.Cells for .NET, Grafikler, Çin Yapılandırması, Yazı Tipleri, Yazı Tipi Boyutu, Metin Yönü, Destek.
linktitle: Çin Bölgesi Ayarla
type: docs
weight: 9
url: /tr/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

Bu konuda, bir grafiğe Çin Bölgesi nasıl ayarlanacağını göstereceğiz.

{{% /alert %}}

## **Bir miras sınıfı tanımlar**

İlk adım olarak, [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) tarafından kalıtım alınan "ChartChineseSetttings" adlı bir sınıf tanımlamanız gerekir. 
Ardından ilgili işlevleri yeniden yazarak grafik öğelerinin metnini kendi dilinize göre belirleyebilirsiniz.
Kod örneği:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

## **Grafik İçin Çin Ayarı Yapın**

Bu adımda, önceki adımda tanımladığınız "ChartChineseSetttings" sınıfını kullanacaksınız.
Kod örneği:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Ardından çıktı görüntüsünde etkiyi görebilirsiniz, grafikteki unsurlar ayarlarınıza göre yeniden oluşturulur.

## **Sonuç**

Bu örnekte, bir grafiğe Çin Bölgesi ayarlamazsanız, aşağıdaki grafik öğelerinin varsayılan dilde, örneğin İngilizce olarak render edilebileceğini göreceksiniz.
Yukarıdaki işlemden sonra, Çin Bölgesi ayarlamazsak, bir çıktı grafik resmi elde edebiliriz.

|**Desteklenen unsurlar**|**Bu örnekteki değer**|**İngilizce ortamındaki varsayılan değer**|
| :- | :- | :- |
|Eksen Başlık Adı|坐标轴标题|Eksen Başlığı|
|Eksen Birimi Adı|百,千...|Yüz, Bin...|
|Grafik Başlık Adı|图表标题|Grafik Başlığı|
|Açıklama Artışı Adı|增加|Artış|
|Açıklama Azalışı Adı|减少|Azalma|
|Legend Total Name|汇总|Toplam|
|Other Name|其他|Diğer|
|Series Name|系列|Seri|
{{< app/cells/assistant language="csharp" >}}
