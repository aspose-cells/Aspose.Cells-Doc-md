---
title: Définir la source de données pour le graphique
description: Découvrez les différentes sources de données prises en charge par Aspose.Cells pour Python via .NET. Notre guide vous expliquera les différents types de sources de données disponibles et vous montrera comment vous connecter et extraire des données pour remplir vos feuilles de calcul.
keywords: Aspose.Cells pour Python via .NET, création de graphiques, formatage de données, étiquettes, couleurs, polices, apparence, convivialité.
linktitle: Source de données
type: docs
weight: 10
url: /fr/python-net/data-formatting-in-charts/
---

Dans nos sujets précédents, nous avons déjà fourni de nombreux exemples pour démontrer comment vous pouvez définir une source de données pour votre graphique, mais dans ce sujet, nous allons fournir plus de détails sur les types de données qui peuvent être définis pour un graphique.

## **Définition des données du graphique**

Il existe deux types de données avec lesquels il faut travailler lors de la création de graphiques en utilisant Aspose.Cells pour Python via .NET :

- Données du graphique.
- Données de catégorie.

### **Données du graphique**

Les données du graphique sont les données que nous utilisons comme source de données pour construire nos graphiques. Nous pouvons ajouter une plage de cellules (contenant des données de graphique) en appelant la méthode [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/add) de l'objet [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingChartsData-1.py" >}}

### **Données de catégorie**

Les données de catégorie sont utilisées pour l'étiquetage des données du graphique et peuvent être ajoutées à [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) en utilisant sa propriété [**category_data**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection/category_data). Un exemple complet est donné ci-dessous pour démontrer l'utilisation des données du graphique et de catégorie. Après l'exécution du code d'exemple ci-dessus, un graphique à colonnes sera ajouté à la feuille de calcul comme indiqué ci-dessous.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SettingCategoryData-1.py" >}}

## **Sujets avancés**
- [Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage](/cells/fr/python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Créer des graphiques dynamiques](/cells/fr/python-net/create-dynamic-charts/)
- [Méthode simple pour configurer un graphique en utilisant la méthode Chart.SetChartDataRange](/cells/fr/python-net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Trouver le type de valeurs X et Y des points dans la série de graphiques](/cells/fr/python-net/find-type-of-x-and-y-values-of-points-in-chart-series/)
