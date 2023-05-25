---
title: Japon Bölgesi için Grafiği Resme Dönüştür
linktitle: Japon Bölgesini Ayarla
type: docs
weight: 10
url: /tr/net/convert-chart-to-image-for-japanese-region/
alias: [/net/set-japanese-configuration-for-chart/]
---
{{% alert color="primary" %}}

Bu konuda size bir grafik için Japon Bölgesini nasıl ayarlayacağınızı göstereceğiz.

{{% /alert %}}

##  **Bir kalıtım sınıfı tanımlar**

 İlk adım, buradan miras alan bir "ChartJapaneseSettings" sınıfı tanımlamanız gerekir.[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/). 
Ardından, ilgili işlevleri yeniden yazarak, grafik öğelerinin metnini kendi dilinizde ayarlayabilirsiniz.
Kod örneği:
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "ChartJapaneseSetttings.cs" >}}

##  **Grafik İçin Japonca Ayarı Yapılandır**

Bu adımda, bir önceki adımda tanımladığınız "ChartJapaneseSettings" sınıfını kullanacaksınız.
Kod örneği:

```
	Workbook wb = new Workbook("Japanese.xls");
	wb.Settings.GlobalizationSettings.ChartSettings = new ChartJapaneseSetttings();
	Chart chart0 = wb.Worksheets[0].Charts[0];
	chart0.ToImage("Output.png");
```

Ardından çıktı görüntüsündeki efekti görebilirsiniz, grafikteki öğeler ayarlarınıza göre işlenecektir.

##  **Çözüm**

Bu örnekte, bir grafik için Japon Bölgesini ayarlamazsanız, aşağıdaki grafik öğeleri İngilizce gibi varsayılan dilde gösterilebilir.
Yukarıdaki işlemden sonra Japon Bölgesi ile bir çıktı grafiği resmi elde edebiliriz.

|**desteklenen öğeler**|**Bu örnekteki değer**|**İngiliz ortamındaki varsayılan değer**|
| :- | :- | :- |
|Eksen Başlık Adı|軸タイトル|Eksen Başlığı|
|Eksen Birimi Adı|百,千...|Yüzlerce, Binlerce...|
|Grafik Başlığı Adı|グラフ タイトル|Grafik başlığı|
|Efsane Artış Adı|ぞうか|Arttırmak|
|Efsane Azaltma Adı|削減|Azaltmak|
|Açıklama Toplam Adı|すべての|Toplam|
|Diğer İsim|その他|Diğer|
|Seri Adı|シリーズ|Seri|
