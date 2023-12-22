---
title: Définir la source de données pour le graphique
description: Découvrez les différentes sources de données prises en charge par Aspose.Cells for .NET. Notre guide vous guidera à travers les différents types de sources de données disponibles et vous montrera comment les connecter et en récupérer des données pour remplir vos feuilles de calcul.
keywords: Aspose.Cells for .NET, charting, data formatting, labels, colors, fonts, appearance, usability.
linktitle: La source de données
type: docs
weight: 10
url: /fr/net/data-formatting-in-charts/
---
Dans nos rubriques précédentes, nous avons déjà fourni de nombreux exemples pour démontrer comment définir une source de données pour votre graphique, mais dans cette rubrique, nous allons fournir plus de détails sur les types de données qui peuvent être définies pour un graphique.

##  **Définition des données du graphique**

Il existe deux types de données à traiter lorsque vous travaillez sur des graphiques en utilisant Aspose.Cells, comme suit :

- Données graphiques.
- Données de catégorie.

###  **Données du graphique**

 Les données graphiques sont les données que nous utilisons comme source de données pour créer nos graphiques. Nous pouvons ajouter une plage de cellules (contenant des données de graphique) en appelant le[**SérieCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) objets[**Ajouter**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)méthode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

###  **Données de catégorie**

 Les données de catégorie sont utilisées pour l'étiquetage des données graphiques et peuvent être ajoutées à[**SérieCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) en utilisant son[**CatégorieDonnées**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)propriété. Un exemple complet est donné ci-dessous pour démontrer l’utilisation des données de graphique et de catégorie. Après avoir exécuté l'exemple de code ci-dessus, un histogramme sera ajouté à la feuille de calcul comme indiqué ci-dessous.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

##  **Sujets avancés**
- [Changer la source de données du graphique en feuille de calcul de destination lors de la copie de lignes ou d'une plage](/cells/fr/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Créer des graphiques dynamiques](/cells/fr/net/create-dynamic-charts/)
- [Un moyen simple de configurer un graphique à l'aide de la méthode Chart.SetChartDataRange](/cells/fr/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Rechercher le type de valeurs X et Y des points dans une série de graphiques](/cells/fr/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
