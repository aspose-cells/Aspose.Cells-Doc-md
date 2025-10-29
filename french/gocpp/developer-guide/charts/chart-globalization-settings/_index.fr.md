---
title: Utilisation de la classe ChartGlobalizationSettings pour définir différentes langues pour le composant graphique avec Golang via C++
linktitle: Utilisation de la classe ChartGlobalizationSettings
description: Apprenez à utiliser la classe ChartGlobalizationSettings dans Aspose.Cells for C++ pour définir différentes langues pour les composants du graphique. Notre guide vous aidera à comprendre comment localiser les éléments, étiquettes et légendes des graphiques dans différentes langues, vous permettant de présenter vos données de manière culturellement appropriée.
keywords: Aspose.Cells for C++, création de graphiques, mondialisation, langues, localisation, ChartGlobalizationSettings, éléments, étiquettes, légendes.
type: docs
weight: 2200
url: /fr/go-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Scénarios d'utilisation possibles**

Les API d'Aspose.Cells ont exposé la classe [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/) afin de traiter les scénarios où l'utilisateur souhaite définir un composant de graphique dans une langue différente, notamment des étiquettes personnalisées pour les sous-totaux dans une feuille de calcul. 

## **Introduction à la classe ChartGlobalizationSettings**

La classe [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/) offre actuellement les 8 méthodes suivantes pouvant être surchargées dans une classe personnalisée pour traduire comme le nom de AxisTitle, le nom de AxisUnit, le nom de ChartTitle, etc., dans différentes langues.

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxistitlename/) : Obtient le nom du titre de l'axe.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxisunitname/) : Obtient le nom de l'unité d'axe.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getcharttitlename/) : Obtient le nom du titre du graphique.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegenddecreasename/) : Obtient le nom de la diminution pour la légende.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendincreasename/) : Obtient le nom de l'augmentation pour la légende.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendtotalname/) : Obtient le nom du total pour la légende.
1. [**GetOtherName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getothername/) : Obtient le nom des étiquettes "Autre" pour le graphique.
1. [**GetSeriesName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getseriesname/) : Obtient le nom des séries dans le graphique.

### **Traduction personnalisée**
Voici, nous allons créer un graphique en cascade basé sur les données suivantes. Les noms des composants du graphique seront affichés en anglais dans le graphique. Nous utiliserons un exemple de langue turque pour montrer comment afficher le titre du graphique, les noms d'augmentation/diminution de la légende, le nom total et le titre de l'axe en turc. 

![todo:image_alt_text](sample.png)

## **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](waterfall.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartGlobalizationSettings.go" >}}
## Sortie générée par le code d'exemple

Il s'agit de la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
