---
title:  Utilisation de la classe ChartGlobalizationSettings pour définir une langue différente pour le composant graphique
description: Découvrez comment utiliser la classe ChartGlobalizationSettings dans Aspose.Cells for .NET pour définir différentes langues pour les composants graphiques. Notre guide vous aidera à comprendre comment localiser les éléments graphiques, les étiquettes et les légendes dans différentes langues, vous permettant ainsi de présenter vos données d'une manière culturellement appropriée.
keywords: Aspose.Cells for .NET, charting, chart globalization, languages, localization, ChartGlobalizationSettings, elements, labels, legends.
type: docs
weight: 2200
url: /fr/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---
##  **Scénarios d'utilisation possibles**

 Aspose.Cells Les API ont exposé le[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) classe afin de gérer les scénarios dans lesquels l'utilisateur souhaite définir le composant graphique dans une langue différente. étiquettes personnalisées pour les sous-totaux dans une feuille de calcul.

##  **Introduction à la classe ChartGlobalizationSettings**

 Le[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)La classe propose actuellement les 8 méthodes suivantes qui peuvent être remplacées dans une classe personnalisée pour traduire, telles que le nom AxisTitle, le nom AxisUnit, le nom ChartTitle, etc. dans une langue différente.
1. [**ObtenirAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Obtient le nom du titre pour Axis.
1. [**ObtenirAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Obtient le nom de l'unité de l'axe.
1. [**ObtenirChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): obtient le nom du titre du graphique.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Obtient le nom de Diminution pour Légende.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Obtient le nom de l'augmentation pour Legend.
1. [**ObtenirLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Obtient le nom de Total pour Legend.
1. [**ObtenirAutreNom**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/) : Obtient le nom des étiquettes "Autres" pour le graphique.
1. [**ObtenirNomSérie**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Obtient le nom de la série dans le graphique.

###  **Traduction de langue personnalisée**
Ici, nous allons créer un graphique en cascade basé sur les données suivantes. Les noms des composants du graphique seront affichés en anglais dans le graphique. Nous utiliserons un exemple en langue turque pour montrer comment afficher le titre du graphique, les noms d'augmentation/diminution de la légende, le nom du total et le titre de l'axe en turc.

![tâche : image_alt_text](sample.png)

##  **Exemple de code**
 L'exemple de code suivant charge le[exemple de fichier Excel](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

##  Sortie générée par l'exemple de code

Il s'agit de la sortie console de l'exemple de code ci-dessus.

{{< highlight "java" >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
