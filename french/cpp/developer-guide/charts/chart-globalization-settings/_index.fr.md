---
title: Utilisation de la classe ChartGlobalizationSettings pour définir différentes langues pour le composant graphique avec C++
linktitle: Utilisation de la classe ChartGlobalizationSettings
description: Apprenez à utiliser la classe ChartGlobalizationSettings dans Aspose.Cells for C++ pour définir différentes langues pour les composants du graphique. Notre guide vous aidera à comprendre comment localiser les éléments, étiquettes et légendes des graphiques dans différentes langues, vous permettant de présenter vos données de manière culturellement appropriée.
keywords: Aspose.Cells for C++, création de graphiques, mondialisation, langues, localisation, ChartGlobalizationSettings, éléments, étiquettes, légendes.
type: docs
weight: 2200
url: /fr/cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Scénarios d'utilisation possibles**

Les API d'Aspose.Cells ont exposé la classe [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) afin de traiter les scénarios où l'utilisateur souhaite définir un composant de graphique dans une langue différente, notamment des étiquettes personnalisées pour les sous-totaux dans une feuille de calcul. 

## **Introduction à la classe ChartGlobalizationSettings**

La classe [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) offre actuellement les 8 méthodes suivantes pouvant être surchargées dans une classe personnalisée pour traduire comme le nom de AxisTitle, le nom de AxisUnit, le nom de ChartTitle, etc., dans différentes langues.

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/) : Obtient le nom du titre de l'axe.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/) : Obtient le nom de l'unité d'axe.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/) : Obtient le nom du titre du graphique.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/) : Obtient le nom de la diminution pour la légende.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/) : Obtient le nom de l'augmentation pour la légende.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/) : Obtient le nom du total pour la légende.
1. [**GetOtherName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getothername/) : Obtient le nom des étiquettes "Autre" pour le graphique.
1. [**GetSeriesName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getseriesname/) : Obtient le nom des séries dans le graphique.

### **Traduction personnalisée**
Voici, nous allons créer un graphique en cascade basé sur les données suivantes. Les noms des composants du graphique seront affichés en anglais dans le graphique. Nous utiliserons un exemple de langue turque pour montrer comment afficher le titre du graphique, les noms d'augmentation/diminution de la légende, le nom total et le titre de l'axe en turc. 

![todo:image_alt_text](sample.png)

## **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](waterfall.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

class TurkeyChartGlobalizationSettings : public ChartGlobalizationSettings
{
public:
    TurkeyChartGlobalizationSettings() : ChartGlobalizationSettings() {}

    U16String GetChartTitleName() override
    {
        return u"Grafik Başlığı"; // Chart Title
    }

    U16String GetLegendIncreaseName() override
    {
        return u"Artış"; // Increase
    }

    U16String GetLegendDecreaseName() override
    {
        return u"Düşüş"; // Decrease
    }

    U16String GetLegendTotalName() override
    {
        return u"Toplam"; // Total
    }

    U16String GetAxisTitleName() override
    {
        return u"Eksen Başlığı"; // Axis Title
    }
};

void ChartGlobalizationSettingsTest()
{
    // Create an instance of existing Workbook
    U16String pathName = u"input.xlsx";
    Workbook workbook(pathName);

    // Set custom chartGlobalizationSettings, here is TurkeyChartGlobalizationSettings
    TurkeyChartGlobalizationSettings* globalizationSettings = new TurkeyChartGlobalizationSettings();
    workbook.GetSettings().GetGlobalizationSettings()->SetChartSettings(globalizationSettings);

    // Get the worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Load the chart from source worksheet
    ChartCollection chartCollection = worksheet.GetCharts();
    Chart chart = chartCollection.Get(0);

    // Chart Calculate
    chart.Calculate();

    // Get the chart title
    Title title = chart.GetTitle();

    // Output the name of the Chart title
    std::cout << "\nWorkbook chart title: " << title.GetText().ToUtf8() << std::endl;

    // Get the legend labels
    Vector<U16String> legendEntriesLabels = chart.GetLegend().GetLegendLabels();

    // Output the name of the Legend
    for (int i = 0; i < legendEntriesLabels.GetLength(); i++)
    {
        std::cout << "\nWorkbook chart legend: " << legendEntriesLabels[i].ToUtf8() << std::endl;
    }

    // Output the name of the Axis title
    Title categoryAxisTitle = chart.GetCategoryAxis().GetTitle();
    std::cout << "\nWorkbook category axis title: " << categoryAxisTitle.GetText().ToUtf8() << std::endl;

    delete globalizationSettings;
}

int main()
{
    Aspose::Cells::Startup();
    ChartGlobalizationSettingsTest();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Sortie générée par le code d'exemple

Il s'agit de la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
