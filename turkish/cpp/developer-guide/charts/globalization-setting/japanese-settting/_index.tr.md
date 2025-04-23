---
title: Japon Bölgesi için Grafik Dönüşümünü Resme Çevir C++ ile
linktitle: Japon Bölgesi Belirle
type: docs
weight: 10
url: /tr/cpp/convert-chart-to-image-for-japanese-region/
alias: [/cpp/set-japanese-configuration-for-chart/]
description: Aspose.Cells for C++ kullanarak tablonun Japonca yapılandırmasını ayarlamayı öğrenin. Rehberimiz, Japonca karakterleri ve biçimlendirmeyi desteklemek için nasıl yapılandırılacağını gösterecek, yazı tipleri, boyut, metin yönü ve daha fazlasını içerecektir.
keywords: Aspose.Cells for C++, Tablolar, Japonca yapılandırma, yazı tipi, yazı tipi boyutu, metin yönü, destek.
---

{{% alert color="primary" %}}

Bu konuda, bir grafik için Japon Bölgesi nasıl belirleneceğini göstereceğiz.

{{% /alert %}}

## **Bir miras sınıfı tanımlar**

İlk adım, `[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/)` sınıfından miras alan `ChartJapaneseSettings` adlı bir sınıf tanımlamaktır. 
Daha sonra, ilgili fonksiyonları ezerek, grafik öğelerinin metnini kendi dilinizde ayarlayabilirsiniz.
Kod örneği:
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

class ChartJapaneseSetttings : public ChartGlobalizationSettings
{
public:
    ChartJapaneseSetttings() : ChartGlobalizationSettings() {}

    U16String GetAxisTitleName() override
    {
        return U16String(u"\u8EF8\u30BF\u30A4\u30C8\u30EB");
    }

    U16String GetAxisUnitName(DisplayUnitType type) override
    {
        switch (type)
        {
        case DisplayUnitType::None:
            return U16String(u"");
        case DisplayUnitType::Hundreds:
            return U16String(u"\u767E");
        case DisplayUnitType::Thousands:
            return U16String(u"\u5343");
        case DisplayUnitType::TenThousands:
            return U16String(u"\u4E07");
        case DisplayUnitType::HundredThousands:
            return U16String(u"\u0031\u0030\u4E07");
        case DisplayUnitType::Millions:
            return U16String(u"\u767E\u4E07");
        case DisplayUnitType::TenMillions:
            return U16String(u"\u5343\u4E07");
        case DisplayUnitType::HundredMillions:
            return U16String(u"\u5104");
        case DisplayUnitType::Billions:
            return U16String(u"\u0031\u0030\u5104");
        case DisplayUnitType::Trillions:
            return U16String(u"\u5146");
        default:
            return U16String(u"");
        }
    }

    U16String GetChartTitleName() override
    {
        return U16String(u"\u30B0\u30E9\u30D5\u0020\u30BF\u30A4\u30C8\u30EB");
    }

    U16String GetLegendDecreaseName() override
    {
        return U16String(u"\u524A\u6E1B");
    }

    U16String GetLegendIncreaseName() override
    {
        return U16String(u"\u305E\u3046\u304B");
    }

    U16String GetLegendTotalName() override
    {
        return U16String(u"\u3059\u3079\u3066\u306E");
    }

    U16String GetOtherName() override
    {
        return U16String(u"\u305D\u306E\u4ED6");
    }

    U16String GetSeriesName() override
    {
        return U16String(u"\u30B7\u30EA\u30FC\u30BA");
    }
};
```

## **Grafik için Japon Yapılandırmasını Yapın**

Bu adımda, önceki adımda tanımladığınız `ChartJapaneseSettings` sınıfını kullanacaksınız.
Kod örneği:

```cpp
    Workbook wb("Japanese.xls");
    wb.GetSettings().GetGlobalizationSettings().SetChartSettings(new ChartJapaneseSettings());
    Chart chart0 = wb.GetWorksheets().Get(0).GetCharts().Get(0);
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
