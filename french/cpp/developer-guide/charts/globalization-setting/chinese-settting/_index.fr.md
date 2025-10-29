---
title: Convertir un graphique en image pour la région chinoise avec C++
linktitle: Définir la région chinoise
description: Apprenez à utiliser Aspose.Cells for C++ pour configurer la localisation chinoise pour les graphiques. Notre guide montrera comment configurer les graphiques pour supporter les caractères et formats chinois, y compris polices, tailles, orientations du texte, et plus encore.
keywords: Aspose.Cells for C++, graphiques, configuration chinoise, polices, taille de police, orientation du texte, support.
type: docs
weight: 9
url: /fr/cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

Dans ce sujet, nous vous montrerons comment définir la région chinoise pour un graphique.

{{% /alert %}}

## **Définit une classe d'héritage**

Première étape, vous devez définir une classe "ChartChineseSetttings" qui hérite de [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/). 
Ensuite, en surchargeant les fonctions associées, vous pouvez définir le texte des éléments du graphique dans votre propre langue.

Exemple de code :
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

Ensuite, vous pouvez voir l'effet dans l'image de sortie, les éléments du graphique seront rendus selon vos paramètres.

## **Conclusion**

Dans cet exemple, si vous ne définissez pas la région chinoise pour un graphique, les éléments du graphique suivants peuvent être rendus dans la langue par défaut, telle que l'anglais.
Après l'opération ci-dessus, nous pouvons obtenir une image de graphique de sortie avec une région chinoise.

|**Éléments pris en charge**|**Valeur dans cet exemple**|**valeur par défaut dans l'environnement anglais**|
| :- | :- | :- |
|Nom du titre de l'axe|坐标轴标题|Titre de l'axe|
|Nom de l'unité de l'axe|百,千...|Centaines, Milliers...|
|Nom du titre du graphique|图表标题|Titre du graphique|
|Nom de Légende Augmentation|增加|Augmentation|
|Nom de Légende Diminution|减少|Diminution|
|Nom de Légende Total|汇总|Total|
|Autre Nom|其他|Autre|
|Nom de Série|系列|Série|
{{< app/cells/assistant language="cpp" >}}
