---
title: Convertir gráfico a imagen para región japonesa con C++
linktitle: Establecer Región Japonesa
type: docs
weight: 10
url: /es/cpp/convert-chart-to-image-for-japanese-region/
alias: [/cpp/set-japanese-configuration-for-chart/]
description: Aprenda cómo usar Aspose.Cells for C++ para configurar la configuración japonesa para el gráfico. Nuestra guía mostrará cómo configurar gráficos para soportar caracteres y formato japoneses, incluidos fuentes, tamaño, dirección del texto y más.
keywords: Aspose.Cells for C++, gráficos, configuración japonesa, fuente, tamaño de fuente, dirección del texto, soporte.
---

{{% alert color="primary" %}}

En este tema, te mostraremos cómo configurar la Región japonesa para un gráfico.

{{% /alert %}}

## **Define una clase de herencia**

El primer paso, necesita definir una clase `ChartJapaneseSettings` que herede de [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/). 
Luego, al sobrescribir las funciones relacionadas, puede configurar el texto de los elementos del gráfico en su propio idioma.
Ejemplo de código:
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

## **Configurar Ajustes Japoneses Para Gráfico**

En este paso, usará la clase `ChartJapaneseSettings` que definió en el paso anterior.
Ejemplo de código:

```cpp
    Workbook wb("Japanese.xls");
    wb.GetSettings().GetGlobalizationSettings().SetChartSettings(new ChartJapaneseSettings());
    Chart chart0 = wb.GetWorksheets().Get(0).GetCharts().Get(0);
    chart0.ToImage("Output.png");
```

Entonces puedes ver el efecto en la imagen de salida, los elementos en el gráfico se renderizarán de acuerdo a tu configuración.

## **Conclusión**

En este ejemplo, si no defines la Región japonesa para un gráfico, es posible que los siguientes elementos del gráfico se rendericen en el idioma predeterminado, como el inglés.
Después de la operación anterior, podemos obtener una imagen de gráfico de salida con la Región japonesa.

|**Elementos soportados**|**Valor en este ejemplo**|**valor predeterminado en el entorno inglés**|
| :- | :- | :- |
|Nombre del Título del Eje|軸タイトル|Título del Eje|
|Nombre de la Unidad del Eje|百,千...|Cientos, Miles...|
|Nombre del Título del Gráfico|グラフ タイトル|Título del Gráfico|
|Nombre de Aumento de Leyenda|ぞうか|Aumento|
|Nombre de Disminución de Leyenda|削減|Disminución|
|Nombre Total de Leyenda|すべての|Total|
|Otro Nombre|その他|Otro|
|Nombre de la Serie|シリーズ|Serie|
