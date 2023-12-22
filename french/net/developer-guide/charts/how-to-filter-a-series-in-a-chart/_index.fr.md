---
title: Trois méthodes de filtrage des données graphiques
description: Apprenez à filtrer les graphiques dans Excel en utilisant le Aspose.Cells for .NET. Notre guide complet vous montrera comment appliquer des filtres aux graphiques, personnaliser les éléments des graphiques et utiliser des outils d'analyse de données pour de meilleures informations et une prise de décision éclairée.
keywords: Aspose.Cells for .NET, Filtering Charts in Excel, Data Analysis, Decision Making, Visualization.
type: docs
weight: 2210
url: /fr/net/filtering-charts-in-excel/
---
{{% alert color="primary" %}}

##  **1. Filtrage des séries pour afficher un graphique**

###  **Étapes pour filtrer les séries à partir d'un graphique dans Excel**
 Dans Excel, nous pouvons filtrer des séries spécifiques d'un graphique, empêchant ainsi ces séries filtrées de s'afficher dans le graphique. Le graphique original est présenté dans**Figure 1**. Cependant, lorsque nous filtrons **Testseries2** et *Testseries4**, le graphique apparaîtra comme indiqué dans la *Figure 2**.

 En Aspose.Cells, on peut réaliser une opération similaire. Pour un[échantillon](seriesFiltered.xlsx) fichier comme celui-ci, si nous voulons filtrer**Série de tests2** et *Testseries4**, nous pouvons exécuter le code suivant. De plus, nous maintiendrons deux listes : une ([Série NS](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)) liste pour stocker toutes les séries sélectionnées et une autre ([Série NS filtrée](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/)) pour stocker la série filtrée.

S'il te plaît**note** que dans le code, quand on définit**chart.NSeries[0].IsFiltered = true;**, la première série de [NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/) sera supprimée et placé à la position appropriée dans [FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/). Par la suite, la précédente **NSeries[1]** deviendra le nouveau premier élément de la liste et toutes les séries suivantes seront décalées d’une position. Cela signifie que si nous exécutons ensuite *chart.NSeries[1].IsFiltered = true;**, nous supprimons effectivement la troisième série d'origine. Cela peut parfois prêter à confusion, nous recommandons donc de suivre l'opération dans le code, qui supprime les séries de la fin au début.

![tâche : image_alt_text](Figure1.png)

![tâche : image_alt_text](Figure2.png)

###  **Exemple de code**
 L'exemple de code suivant charge le[exemple de fichier Excel](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

##  **2. Filtrez les données et laissez le graphique changer**

Le filtrage de vos données est un excellent moyen de gérer les filtres de graphiques contenant beaucoup de données. Lorsque vous filtrez les données, le graphique change. Un problème que nous devrons résoudre est de nous assurer que le graphique reste à l'écran. Lorsque vous filtrez, vous obtenez des lignes masquées et, parfois, le graphique se trouve dans ces lignes masquées.

![tâche : image_alt_text](Figure3.png)

###  **Étapes pour utiliser les filtres de données pour modifier le graphique dans Excel**

1. Cliquez à l’intérieur de votre plage de données.
 2. Cliquez sur le**Données** et activez Filtres en cliquant sur Filtres. Votre ligne d'en-tête comportera des flèches déroulantes.
 3. Créez un graphique en accédant à**Insérer** et en sélectionnant un graphique à colonnes.
4. Filtrez maintenant vos données à l'aide des flèches déroulantes dans les données. N'utilisez pas les filtres de graphique.

###  **Exemple de code**
L'exemple de code suivant montre la même fonctionnalité en utilisant Aspsoe.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

##  **3. Filtrez les données à l'aide d'un tableau et laissez le graphique changer**

L'utilisation d'un tableau est similaire à la méthode 2, utilisant une plage, mais les tableaux présentent des avantages par rapport aux plages. Lorsque vous modifiez votre plage en tableau et ajoutez des données, le graphique est automatiquement mis à jour. Avec une plage, vous devrez changer la source de données.

###  **Formater sous forme de tableau dans Excel**

 Cliquez dans vos données et utilisez**CTRL + T** ou utilisez l'onglet Accueil,**Formater sous forme de tableau**

![tâche : image_alt_text](Figure4.png)

###  **Exemple de code**
 L'exemple de code suivant charge le[exemple de fichier Excel](TableFilters.xlsx) montre la même fonctionnalité en utilisant Aspsoe.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}