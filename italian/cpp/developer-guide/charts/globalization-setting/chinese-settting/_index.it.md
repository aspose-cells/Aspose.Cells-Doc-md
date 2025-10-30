---
title: Convertire il grafico in immagine per regione cinese con C++
linktitle: Imposta la regione cinese
description: Impara come usare Aspose.Cells for C++ per impostare la configurazione cinese per i grafici. La nostra guida dimostrerà come configurare i grafici per supportare i caratteri e i formati cinesi, inclusi font, dimensioni, direzioni del testo e altro.
keywords: Aspose.Cells for C++, Grafici, Configurazione cinese, Font, Dimensione font, Direzione del testo, Supporto.
type: docs
weight: 9
url: /it/cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

In questo argomento, ti mostreremo come impostare la regione cinese per un grafico.

{{% /alert %}}

## **Definisce una classe di ereditarietà**

 Primo passo, devi definire una classe "ChartChineseSetttings" che eredita da [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/). 
Quindi, sovrascrivendo le funzioni correlate, puoi impostare il testo degli elementi del grafico nella tua lingua.

Esempio di codice:
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

Poi puoi vedere l'effetto nell'immagine di output, gli elementi nel grafico saranno resi in base alle tue impostazioni.

## **Conclusioni**

In questo esempio, se non imposti la regione cinese per un grafico, determinati elementi del grafico potrebbero essere renderizzati nella lingua predefinita, come l'inglese.
Dopo l'operazione precedente, possiamo ottenere un'immagine del grafico in uscita con la regione cinese.

|**Elementi supportati**|**Valore in questo esempio**|**valore predefinito nell'ambiente inglese**|
| :- | :- | :- |
|Nome titolo asse|坐标轴标题|Titolo asse|
|Nome dell'unità dell'asse|百,千...|Centinaia, Migliaia...|
|Nome titolo grafico|图表标题|Titolo grafico|
|Nome leggenda aumento|增加|Aumento|
|Nome della Riduzione Leggenda|减少|Ridurre|
|Nome della Somma Totale Leggenda|汇总|Totale|
|Altro Nome|其他|Altro|
|Nome della Serie Leggenda|系列|Serie|
{{< app/cells/assistant language="cpp" >}}
