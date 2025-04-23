---
title: Trois méthodes pour filtrer les données du graphique
description: Apprenez comment filtrer les graphiques dans Excel en utilisant Aspose.Cells for .NET. Notre guide complet démontrera comment appliquer des filtres aux graphiques, personnaliser les éléments du graphique, et utiliser les outils d analyse de données pour de meilleures insights et une prise de décision informée.
keywords: Aspose.Cells for .NET, Filtrer les graphiques dans Excel, Analyse de données, Prise de décision, Visualisation.
type: docs
weight: 2210
url: /fr/net/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. Filtrer les séries pour afficher un graphique**

### **Étapes pour filtrer les séries d'un graphique dans Excel**
Dans Excel, nous pouvons filtrer des séries spécifiques d'un graphique, ce qui fait que ces séries filtrées ne sont pas affichées dans le graphique. Le graphique d'origine est montré dans **Figure 1**. Cependant, lorsque nous filtrons **Testseries2** et **Testseries4**, le graphique apparaîtra comme indiqué dans **Figure 2**.

Dans Aspose.Cells, nous pouvons effectuer une opération similaire. Pour un fichier [exemple](seriesFiltered.xlsx) comme celui-ci, si nous voulons filtrer **Testseries2** et **Testseries4**, nous pouvons exécuter le code suivant. De plus, nous maintiendrons deux listes : une ([NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)) pour stocker toutes les séries sélectionnées et une autre ([FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filterednseries/)) pour stocker les séries filtrées.

Veuillez **noter** qu'dans le code, lorsque nous définissons **chart.NSeries[0].IsFiltered = true;**, la première série dans [NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/) sera supprimée et placée dans la position appropriée dans [FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filterednseries/). Ensuite, le précédent **NSeries[1]** deviendra le nouvel élément en première position dans la liste, et toutes les séries suivantes se décaleront d'une position. Cela signifie que si nous exécutons ensuite **chart.NSeries[1].IsFiltered = true;**, nous supprimons effectivement la série d'origine troisième. Cela peut parfois causer de la confusion, il est donc recommandé de suivre l'opération dans le code, qui supprime les séries de la fin vers le début.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

## **2. Filtrer les données et laisser le changement de graphique**

Filtrer vos données est un excellent moyen de gérer les filtres de graphique avec beaucoup de données. Lorsque vous filtrez les données, le graphique changera. Un problème que nous devrons aborder est de veiller à ce que le graphique reste à l'écran. Lorsque vous filtrez, vous obtenez des lignes cachées, et parfois, le graphique se trouvera dans ces lignes cachées.

![todo:image_alt_text](Figure3.png)

### **Étapes pour utiliser les filtres de données pour changer le graphique dans Excel**

1. Cliquez à l'intérieur de la plage de vos données.
2. Cliquez sur l'onglet **Données**, et activez les filtres en cliquant sur Filtres. Votre ligne d'en-tête aura des flèches déroulantes.
3. Créez un graphique en allant sur l'onglet **Insertion** et en sélectionnant un graphique à colonnes.
4. Filtrer maintenant vos données en utilisant les flèches déroulantes dans les données. N'utilisez pas les filtres de graphique.

### **Code d'exemple**
Le code d'exemple suivant montre la même fonctionnalité en utilisant Aspose.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

## **3. Filtrer les données en utilisant un tableau et laisser le changement du graphique**

Utiliser un tableau est similaire à la Méthode 2, en utilisant une plage, mais vous avez des avantages avec les tableaux par rapport aux plages. Lorsque vous modifiez votre plage en un tableau et ajoutez des données, le graphique se met à jour automatiquement. Avec une plage, vous devrez modifier la source de données.

### **Format en tableau dans Excel**

Cliquez à l'intérieur de vos données et utilisez **CTRL + T** ou utilisez l'onglet Accueil, **Format en Tableau**

![todo:image_alt_text](Figure4.png)

### **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](TableFilters.xlsx) montre la même fonctionnalité en utilisant Aspose.Cells.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}
{{< app/cells/assistant language="csharp" >}}
