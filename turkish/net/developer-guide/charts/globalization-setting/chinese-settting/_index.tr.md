---
title: Çin Bölgesi için Grafiği Resme Dönüştür
description: Grafikler için Aspose.Cells for .NET set Çince yapılandırmasını nasıl kullanacağınızı öğrenin. Kılavuzumuz, yazı tipleri, boyutlar, metin yönleri ve daha fazlası dahil olmak üzere Çince karakterleri ve formatları destekleyecek şekilde grafiklerin nasıl yapılandırılacağını gösterecektir.
keywords: Aspose.Cells for .NET, Charts, Chinese Configuration, Fonts, Font Size, Text Direction, Support.
linktitle: Çin Bölgesini Ayarla
type: docs
weight: 9
url: /tr/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---
{{% alert color="primary" %}}

Bu başlıkta size bir grafik için Çin Bölgesini nasıl ayarlayacağınızı göstereceğiz.

{{% /alert %}}

##  **Bir miras sınıfını tanımlar**

 İlk adım, miras alan bir "ChartChineseSettings" sınıfını tanımlamanız gerekir.[**GrafikKüreselleşmeAyarlar**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Daha sonra ilgili fonksiyonları yeniden yazarak grafik elemanlarının metnini kendi dilinizde ayarlayabilirsiniz.
Kod örneği:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

##  **Grafik İçin Çince Ayarını Yapılandırma**

Bu adımda bir önceki adımda tanımladığınız "ChartChineseSettings" sınıfını kullanacaksınız.
Kod örneği:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Daha sonra çıktı görüntüsündeki efekti görebilirsiniz; grafikteki öğeler ayarlarınıza göre oluşturulacaktır.

##  **Çözüm**

Bu örnekte, bir grafik için Çin Bölgesini ayarlamazsanız aşağıdaki grafik öğeleri İngilizce gibi varsayılan dilde görüntülenebilir.
Yukarıdaki işlemden sonra Çin Bölgesi ile çıktı grafiği resmi elde edebiliriz.

|**Desteklenen öğeler**|**Bu örnekteki değer**|**İngilizce ortamında varsayılan değer**|
| :- | :- | :- |
|Eksen Başlığı Adı|坐标轴标题|Eksen Başlığı|
|Eksen Birimi Adı|百,千...|Yüzlerce, binlerce...|
|Grafik Başlığı Adı|图表标题|Grafik başlığı|
|Efsane Artış Adı|增加|Arttırmak|
|Açıklama Adı Azaltma|减少|Azaltmak|
|Efsane Toplam Adı|汇总|Toplam|
|Diğer Ad|其他|Diğer|
|Seri Adı|系列|Seri|
