---
title: Trois méthodes pour filtrer les données du graphique
description: Apprenez comment filtrer des graphiques dans Excel en utilisant Aspose.Cells pour Python via .NET. Notre guide complet montrera comment appliquer des filtres aux graphiques, personnaliser les éléments du graphique et utiliser des outils d analyse de données pour de meilleures perspectives et une prise de décision éclairée.
keywords: Aspose.Cells pour Python via .NET, Filtrage de graphiques dans Excel, Analyse de données, Prise de décision, Visualisation.
type: docs
weight: 2210
url: /fr/python-net/filtering-charts-in-excel/
---


## **1. Filtrer les séries pour afficher un graphique**

### **Étapes pour filtrer les séries d'un graphique dans Excel**
Dans Excel, nous pouvons filtrer des séries spécifiques d'un graphique, ce qui fait que ces séries filtrées ne sont pas affichées dans le graphique. Le graphique d'origine est montré dans **Figure 1**. Cependant, lorsque nous filtrons **Testseries2** et **Testseries4**, le graphique apparaîtra comme indiqué dans **Figure 2**.

Dans Aspose.Cells pour Python via .NET, nous pouvons effectuer une opération similaire. Pour un fichier [d'exemple](seriesFiltered.xlsx) comme celui-ci, si nous voulons filtrer **Testseries2** et **Testseries4**, nous pouvons exécuter le code suivant. De plus, nous conserverons deux listes : une ([n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/n_series/)) pour stocker toutes les séries sélectionnées et une autre ([filtered_n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/filtered_n_series/)) pour stocker les séries filtrées.

Veuillez **noter** que dans le code, lorsque nous définissons **chart.nSeries[0].is_filtered = TRUE;**, la première série dans [n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/n_series/) sera supprimée et placée à la position appropriée dans [filtered_n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/filtered_n_series/). Par la suite, le précédent **nSeries[1]** deviendra le nouvel élément en tête de liste, et toutes les autres séries seront décalées d'une position. Cela signifie que si nous exécutons ensuite **chart.nSeries[1].is_filtered = TRUE;**, nous supprimons effectivement la série originale en troisième position. Cela peut parfois prêter à confusion, nous recommandons donc de suivre l'opération dans le code, qui supprime les séries de la fin vers le début.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-seriesFiltered.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DataFilters.py" >}}

## **3. Filtrer les données en utilisant un tableau et laisser le changement du graphique**

Utiliser un tableau est similaire à la Méthode 2, en utilisant une plage, mais vous avez des avantages avec les tableaux par rapport aux plages. Lorsque vous modifiez votre plage en un tableau et ajoutez des données, le graphique se met à jour automatiquement. Avec une plage, vous devrez modifier la source de données.

### **Format en tableau dans Excel**

Cliquez à l'intérieur de vos données et utilisez **CTRL + T** ou utilisez l'onglet Accueil, **Format en Tableau**

![todo:image_alt_text](Figure4.png)

### **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](TableFilters.xlsx) montre la même fonctionnalité en utilisant Aspose.Cells.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TableFilters.py" >}}
{{< app/cells/assistant language="python-net" >}}
