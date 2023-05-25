---
title:  Utilisation de la classe ChartGlobalizationSettings pour définir une langue différente pour le composant graphique
type: docs
weight: 2200
url: /fr/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---
##  **Scénarios d'utilisation possibles**

 Aspose.Cells Les API ont exposé le[**Paramètres de globalisation du graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) class afin de gérer les scénarios dans lesquels l'utilisateur souhaite définir le composant de graphique dans une langue différente. étiquettes personnalisées pour les sous-totaux dans une feuille de calcul.

##  **Introduction à la classe ChartGlobalizationSettings**

 Le[**Paramètres de globalisation du graphique**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)La classe propose actuellement les 8 méthodes suivantes qui peuvent être remplacées dans une classe personnalisée pour traduire, telles que le nom AxisTitle, le nom AxisUnit, le nom ChartTitle, etc. dans une langue différente.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Obtient le nom du titre pour l'axe.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Obtient le nom de l'unité de l'axe.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Obtient le nom du titre du graphique.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Obtient le nom de la diminution pour la légende.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Obtient le nom de l'augmentation pour Legend.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Obtient le nom de Total pour la légende.
1. [**ObtenirAutreNom**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): Obtient le nom des étiquettes "Autre" pour le graphique.
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): obtient le nom de la série dans le graphique.

###  **Traduction de langue personnalisée**
Ici, nous allons créer un graphique en cascade basé sur les données suivantes. Les noms des composants du graphique seront affichés en anglais dans le graphique. Nous utiliserons un exemple en turc pour montrer comment afficher le titre du graphique, les noms d'augmentation/diminution de la légende, le nom total et le titre de l'axe en turc.

![todo:image_alt_text](sample.png)

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
