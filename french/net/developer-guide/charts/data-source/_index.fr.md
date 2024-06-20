---
title: Définir la source de données pour le graphique
description: Découvrez les différentes sources de données prises en charge par Aspose.Cells for .NET. Notre guide vous présentera les différents types de sources de données disponibles et vous montrera comment vous y connecter et récupérer des données à partir d elles pour peupler vos feuilles de calcul.
keywords: Aspose.Cells for .NET, création de graphiques, mise en forme des données, étiquettes, couleurs, polices de caractères, apparence, convivialité.
linktitle: Source de données
type: docs
weight: 10
url: /fr/net/data-formatting-in-charts/
---

Dans nos sujets précédents, nous avons déjà fourni de nombreux exemples pour démontrer comment vous pouvez définir une source de données pour votre graphique, mais dans ce sujet, nous allons fournir plus de détails sur les types de données qui peuvent être définis pour un graphique.

## **Définition des données du graphique**

Il existe deux types de données à manipuler lors de l'utilisation de graphiques avec Aspose.Cells, comme suit :

- Données du graphique.
- Données de catégorie.

### **Données du graphique**

Les données du graphique sont les données que nous utilisons comme source de données pour construire nos graphiques. Nous pouvons ajouter une plage de cellules (contenant des données de graphique) en appelant la méthode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add) de l'objet [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **Données de catégorie**

Les données de catégorie sont utilisées pour l'étiquetage des données du graphique et peuvent être ajoutées à [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) en utilisant sa propriété [**CategoryData**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata). Un exemple complet est donné ci-dessous pour démontrer l'utilisation des données du graphique et de catégorie. Après l'exécution du code d'exemple ci-dessus, un graphique à colonnes sera ajouté à la feuille de calcul comme indiqué ci-dessous.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **Sujets avancés**
- [Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage](/cells/fr/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Créer des graphiques dynamiques](/cells/fr/net/create-dynamic-charts/)
- [Méthode simple pour configurer un graphique en utilisant la méthode Chart.SetChartDataRange](/cells/fr/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Trouver le type de valeurs X et Y des points dans la série de graphiques](/cells/fr/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
