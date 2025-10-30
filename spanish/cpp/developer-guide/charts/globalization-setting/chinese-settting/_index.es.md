---
title: Convertir gráfico a imagen para región china con C++
linktitle: Establecer región china
description: Aprenda cómo usar Aspose.Cells for C++ para configurar la configuración china para gráficos. Nuestra guía mostrará cómo configurar gráficos para soportar caracteres y formatos chinos, incluidos fuentes, tamaños, direcciones de texto y más.
keywords: Aspose.Cells for C++, gráficos, configuración china, fuentes, tamaño de fuente, dirección del texto, soporte.
type: docs
weight: 9
url: /es/cpp/convert-chart-to-image-for-chinese-region/
alias: [/cpp/set-chinese-configuration-for-chart/]
---

{{% alert color="primary" %}}

En este tema, te mostraremos cómo configurar la región china para un gráfico.

{{% /alert %}}

## **Define una clase de herencia**

El primer paso, necesita definir una clase "ChartChineseSetttings" que herede de [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/). 
Luego, al sobrescribir las funciones relacionadas, puede configurar el texto de los elementos del gráfico en su propio idioma.

Ejemplo de código:
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

Entonces puedes ver el efecto en la imagen de salida, los elementos en el gráfico se renderizarán de acuerdo a tu configuración.

## **Conclusión**

En este ejemplo, si no se establece la Región China para un gráfico, los siguientes elementos del gráfico pueden renderizarse en el idioma predeterminado, como el inglés.
Después de la operación anterior, podemos obtener una imagen de gráfico de salida con la Región China.

|**Elementos soportados**|**Valor en este ejemplo**|**valor predeterminado en el entorno inglés**|
| :- | :- | :- |
|Nombre del Título del Eje|坐标轴标题|Título del Eje|
|Nombre de la Unidad del Eje|百,千...|Cientos, Miles...|
|Nombre del Título del Gráfico|图表标题|Título del Gráfico|
|Nombre del Aumento de la Leyenda|增加|Aumento|
|Nombre de la Disminución de la Leyenda|减少|Disminución|
|Nombre Total de la Leyenda|汇总|Total|
|Otro Nombre|其他|Otro|
|Nombre de la Serie|系列|Serie|
{{< app/cells/assistant language="cpp" >}}
