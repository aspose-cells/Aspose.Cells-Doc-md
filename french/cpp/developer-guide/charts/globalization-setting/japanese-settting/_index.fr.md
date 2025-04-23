---
title: Convertir un graphique en image pour la région japonaise avec C++
linktitle: Définir la région japonaise
type: docs
weight: 10
url: /fr/cpp/convert-chart-to-image-for-japanese-region/
alias: [/cpp/set-japanese-configuration-for-chart/]
description: Apprenez comment utiliser Aspose.Cells for C++ pour configurer la localisation japonaise pour le graphique. Notre guide expliquera comment configurer les graphiques pour supporter les caractères japonais et la mise en forme, y compris polices, tailles, orientation du texte, et plus encore.
keywords: Aspose.Cells for C++, graphiques, configuration japonaise, police, taille de police, orientation du texte, support.
---

{{% alert color="primary" %}}

Dans ce sujet, nous allons vous montrer comment définir la région japonaise pour un graphique.

{{% /alert %}}

## **Définit une classe d'héritage**

Première étape, vous devez définir une classe `ChartJapaneseSettings` qui hérite de [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/). 
Ensuite, en surchargeant les fonctions associées, vous pouvez définir le texte des éléments du graphique dans votre propre langue.
Exemple de code :
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

## **Configurer le paramètre japonais pour le graphique**

Dans cette étape, vous utiliserez la classe `ChartJapaneseSettings` que vous avez définie à l’étape précédente.
Exemple de code :

```cpp
    Workbook wb("Japanese.xls");
    wb.GetSettings().GetGlobalizationSettings().SetChartSettings(new ChartJapaneseSettings());
    Chart chart0 = wb.GetWorksheets().Get(0).GetCharts().Get(0);
    chart0.ToImage("Output.png");
```

Ensuite, vous pouvez voir l'effet dans l'image de sortie, les éléments du graphique seront rendus selon vos paramètres.

## **Conclusion**

Dans cet exemple, si vous ne définissez pas la région japonaise pour un graphique, les éléments de graphique suivants peuvent être rendus dans la langue par défaut, telle que l'anglais.
Après l'opération ci-dessus, nous pouvons obtenir une image de graphique de sortie avec la région japonaise.

|**Éléments pris en charge**|**Valeur dans cet exemple**|**valeur par défaut dans l'environnement anglais**|
| :- | :- | :- |
|Nom du titre de l'axe|軸タイトル|Titre de l'axe|
|Nom de l'unité de l'axe|百,千...|Centaines, Milliers...|
|Nom du titre du graphique|グラフ タイトル|Titre du graphique|
|Nom de l'augmentation de la légende|ぞうか|Augmentation|
|Nom de la diminution de la légende|削減|Diminution|
|Nom total de la légende|すべての|Total|
|Autre nom|その他|Autre|
|Nom de la série|シリーズ|Série|
