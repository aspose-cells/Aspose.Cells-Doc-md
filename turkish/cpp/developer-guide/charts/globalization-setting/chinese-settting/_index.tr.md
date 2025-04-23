---
title: Çin Bölgesi için Grafik Dönüşümünü Resme Çevir C++ ile
linktitle: Çin Bölgesi Ayarla
description: Aspose.Cells for C++ kullanarak tablolar için Çince yapılandırma ayarlamayı öğrenin. Rehberimiz, yazı tipleri, boyutlar, metin yönleri ve daha fazlası dahil olmak üzere Çince karakterleri ve biçimleri desteklemek üzere tabloları nasıl yapılandıracağınızı gösterecektir.
keywords: Aspose.Cells for C++, Tablolar, Çince Yapılandırma, Yazı Tipleri, Yazı Tipi Boyutu, Metin Yönü, Destek.
type: docs
weight: 9
url: /tr/cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

Bu konuda, bir grafiğe Çin Bölgesi nasıl ayarlanacağını göstereceğiz.

{{% /alert %}}

## **Bir miras sınıfı tanımlar**

İlk adım, `[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/)` sınıfından miras alan "ChartChineseSetttings" adlı bir sınıf tanımlamaktır. 
Daha sonra, ilgili fonksiyonları ezerek, grafik öğelerinin metnini kendi dilinizde ayarlayabilirsiniz.

Kod örneği:
```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

class ChartChineseSettings : public ChartGlobalizationSettings
{
public:
	ChartChineseSettings() {}
	virtual ~ChartChineseSettings() {}

	virtual U16String GetAxisTitleName()
	{
		return U16String(u"\u5750\u6807\u8F74\u6807\u9898");
	}

	virtual U16String GetAxisUnitName(DisplayUnitType type)
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
			return U16String(u"\u5341\u4E07");
		case DisplayUnitType::Millions:
			return U16String(u"\u767E\u4E07");
		case DisplayUnitType::TenMillions:
			return U16String(u"\u5343\u4E07");
		case DisplayUnitType::HundredMillions:
			return U16String(u"\u4EBF");
		case DisplayUnitType::Billions:
			return U16String(u"\u5341\u4EBF");
		case DisplayUnitType::Trillions:
			return U16String(u"\u5146");
		default:
			return U16String(u"");
		}
	}

	virtual U16String GetChartTitleName()
	{
		return U16String(u"\u56FE\u8868\u6807\u9898");
	}

	virtual U16String GetLegendDecreaseName()
	{
		return U16String(u"\u51CF\u5C11");
	}

	virtual U16String GetLegendIncreaseName()
	{
		return U16String(u"\u589E\u52A0");
	}

	virtual U16String GetLegendTotalName()
	{
		return U16String(u"\u6C47\u603B");
	}

	virtual U16String GetOtherName()
	{
		return U16String(u"\u5176\u4ED6");
	}

	virtual U16String GetSeriesName()
	{
		return U16String(u"\u7CFB\u5217");
	}
};

//Config Chinese Setting For Chart
//In this step, you will use the class "ChartChineseSetttings" you defined in the previous step.
int main()
{
	Workbook wb("Chinese.xls");
	ChartChineseSettings* chartChineseSettings = new ChartChineseSettings();
	wb.GetSettings().GetGlobalizationSettings()->SetChartSettings(chartChineseSettings);
	Chart chart0 = wb.GetWorksheets().Get(0).GetCharts().Get(0);
	chart0.ToImage("Output.png");
	delete chartChineseSettings;
	return 0;
}

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
