---
title: Çin Bölgesi için Grafiği Resme Dönüştür
linktitle: Çin Bölgesini Ayarla
type: docs
weight: 9
url: /tr/net/convert-chart-to-image-for-chinese-region/
alias: [/net/set-chinese-configuration-for-chart/]
---
{{% alert color="primary" %}}

Bu başlıkta, size bir grafik için Çin Bölgesini nasıl ayarlayacağınızı göstereceğiz.

{{% /alert %}}

##  **Bir kalıtım sınıfı tanımlar**

İlk adım, buradan miras alan bir "ChartChineseSettings" sınıfı tanımlamanız gerekir.[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Ardından, ilgili işlevleri yeniden yazarak, grafik öğelerinin metnini kendi dilinizde ayarlayabilirsiniz.
Kod örneği:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartChineseSetttings.cs" >}}

##  **Grafik İçin Çince Ayarı Yapılandır**

Bu adımda bir önceki adımda tanımladığınız "ChartChineseSettings" sınıfını kullanacaksınız.
Kod örneği:

```
	Workbook wb = new Workbook("Chinese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartChineseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Ardından çıktı görüntüsündeki efekti görebilirsiniz, grafikteki öğeler ayarlarınıza göre işlenecektir.

##  **Çözüm**

Bu örnekte, bir grafik için Çin Bölgesini ayarlamazsanız, aşağıdaki grafik öğeleri İngilizce gibi varsayılan dilde gösterilebilir.
Yukarıdaki işlemden sonra, Çin Bölgesi ile bir çıktı grafiği resmi elde edebiliriz.

|**desteklenen öğeler**|**Bu örnekteki değer**|**İngiliz ortamındaki varsayılan değer**|
| :- | :- | :- |
|Eksen Başlık Adı|坐标轴标题|Eksen Başlığı|
|Eksen Birimi Adı|百,千...|Yüzlerce, Binlerce...|
|Grafik Başlığı Adı|图表标题|Grafik başlığı|
|Efsane Artış Adı|增加|Arttırmak|
|Efsane Azaltma Adı|减少|Azaltmak|
|Açıklama Toplam Adı|汇总|Toplam|
|Diğer İsim|其他|Diğer|
|Seri Adı|系列|Seri|
