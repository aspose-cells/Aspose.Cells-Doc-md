---  
title: Node.js ile Çince Bölge için Grafik Dönüştürme ve Resim Formatına Çevirme C++ kullanarak  
description: Aspose.Cells for Node.js via C++ kullanarak Çince karakterler ve formatlar için grafiklerin yapılandırılmasını, fontlar, boyutlar, metin yönleri ve daha fazlasını öğrenin.  
keywords: Aspose.Cells for Node.js, Grafikler, Çince Yapılandırma, Fontlar, Yazı Tipi Boyutu, Metin Yönü, Destek.  
linktitle: Çin Bölgesi Ayarla  
type: docs  
weight: 9  
url: /tr/nodejs-cpp/convert-chart-to-image-for-chinese-region/  
alias: [/nodejs-cpp/set-chinese-configuration-for-chart/]  
---  

{{% alert color="primary" %}}  
Bu konuda, bir grafiğe Çin Bölgesi nasıl ayarlanacağını göstereceğiz.  
{{% /alert %}}  

## **Bir miras sınıfı tanımlar**  

İlk adım, `[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/chartglobalizationsettings/)` sınıfından miras alan "ChartChineseSetttings" adlı bir sınıf tanımlamaktır.  
Ardından ilgili işlevleri yeniden yazarak grafik öğelerinin metnini kendi dilinize göre belirleyebilirsiniz.  
Kod örneği:  
```javascript
const AsposeCells = require("aspose.cells.node");

class ChartChineseSettings extends AsposeCells.ChartGlobalizationSettings {
getAxisTitleName() {
return "坐标轴标题";
}

getAxisUnitName(type) {
switch (type) {
case AsposeCells.DisplayUnitType.None:
return '';
case AsposeCells.DisplayUnitType.Hundreds:
return '百';
case AsposeCells.DisplayUnitType.Thousands:
return '千';
case AsposeCells.DisplayUnitType.TenThousands:
return '万';
case AsposeCells.DisplayUnitType.HundredThousands:
return '十万';
case AsposeCells.DisplayUnitType.Millions:
return '百万';
case AsposeCells.DisplayUnitType.TenMillions:
return '千万';
case AsposeCells.DisplayUnitType.HundredMillions:
return '亿';
case AsposeCells.DisplayUnitType.Billions:
return '十亿';
case AsposeCells.DisplayUnitType.Trillions:
return '兆';
default:
return '';
}
}

getChartTitleName() {
return "图表标题";
}

getLegendDecreaseName() {
return "减少";
}

getLegendIncreaseName() {
return "增加";
}

getLegendTotalName() {
return "汇总";
}

getOtherName() {
return "其他";
}

getSeriesName() {
return "系列";
}
}
```  

## **Grafik İçin Çin Ayarı Yapın**  

Bu adımda, önceki adımda tanımladığınız "ChartChineseSetttings" sınıfını kullanacaksınız.  
Kod örneği:  

```javascript  
const Workbook = require('aspose.cells');  
const wb = new Workbook("Chinese.xls");  
wb.settings.globalizationSettings.chartSettings = new ChartChineseSetttings();  
const chart0 = wb.worksheets[0].charts[0];  
chart0.toImage("Output.png");  
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

