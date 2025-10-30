---  
title: Node.js ile Çince Bölge için Grafik Dönüştürme ve Resim Formatına Çevirme C++ kullanarak  
description: Aspose.Cells for Node.js via C++ kullanarak grafikte Japonca yapılandırmayı nasıl ayarlayacağınızı öğrenin. Kılavuzumuz, grafiklerin Japonca karakterler ve formatlamayı destekleyecek şekilde nasıl yapılandırılacağını gösterecektir, bunlar fontlar, boyut, metin yönü ve daha fazlasını içerir.  
keywords: Aspose.Cells for Node.js via C++, Grafikler, Japonca yapılandırma, font, font boyutu, metin yönü, destek.  
linktitle: Japon Bölgesi Belirle  
type: docs  
weight: 10  
url: /tr/nodejs-cpp/convert-chart-to-image-for-japanese-region/  
alias: [/nodejs-cpp/set-japanese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
Bu konuda, bir grafik için Japon Bölgesi nasıl belirleneceğini göstereceğiz.  
{{% /alert %}}  

## **Bir miras sınıfı tanımlar**  

İlk adım olarak, [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/) sınıfından türeyen "ChartJapaneseSettings" adında bir sınıf tanımlamanız gerekir.  
Ardından ilgili işlevleri yeniden yazarak grafik öğelerinin metnini kendi dilinize göre belirleyebilirsiniz.  
Kod örneği:  
```javascript
const AsposeCells = require("aspose.cells.node");

class ChartJapaneseSettings extends AsposeCells.ChartGlobalizationSettings {
getAxisTitleName() {
return "軸タイトル";
}

getAxisUnitName(type) {
switch (type) {
case AsposeCells.DisplayUnitType.None:
return '';
case AsposeCells.DisplayUnitType.Hundreds:
return "百";
case AsposeCells.DisplayUnitType.Thousands:
return "千";
case AsposeCells.DisplayUnitType.TenThousands:
return "万";
case AsposeCells.DisplayUnitType.HundredThousands:
return "10万";
case AsposeCells.DisplayUnitType.Millions:
return "百万";
case AsposeCells.DisplayUnitType.TenMillions:
return "千万";
case AsposeCells.DisplayUnitType.HundredMillions:
return "億";
case AsposeCells.DisplayUnitType.Billions:
return "10億";
case AsposeCells.DisplayUnitType.Trillions:
return "兆";
default:
return '';
}
}

getChartTitleName() {
return "グラフ タイトル";
}

getLegendDecreaseName() {
return "削減";
}

getLegendIncreaseName() {
return "ぞうか";
}

getLegendTotalName() {
return "すべての";
}

getOtherName() {
return "その他";
}

getSeriesName() {
return "シリーズ";
}
}
```  

## **Grafik için Japon Yapılandırmasını Yapın**  

Bu adımda, önceki adımda tanımladığınız "ChartJapaneseSettings" sınıfını kullanacaksınız.  
Kod örneği:  

```javascript  
const { Workbook } = require('aspose.cells');

let wb = new Workbook("Japanese.xls");
wb.settings.globalizationSettings.chartSettings = new ChartJapaneseSettings();
let chart0 = wb.worksheets[0].charts[0];
chart0.toImage("Output.png");
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

{{< app/cells/assistant language="nodejs-cpp" >}}
