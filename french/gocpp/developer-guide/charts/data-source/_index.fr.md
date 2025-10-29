---
title: Définir la source de données pour le graphique avec Golang via C++
linktitle: Source de données
type: docs
weight: 10
url: /fr/go-cpp/data-formatting-in-charts/
description: Découvrez les différentes sources de données supportées par Aspose.Cells for C++. Notre guide vous expliquera les différents types de sources de données disponibles et comment les connecter et en extraire des données pour remplir vos feuilles de calcul.
keywords: Aspose.Cells for C++, graphiques, formatage des données, étiquettes, couleurs, polices, apparence, convivialité.
---

Dans nos sujets précédents, nous avons déjà fourni de nombreux exemples pour démontrer comment vous pouvez définir une source de données pour votre graphique. Dans ce sujet, nous allons fournir plus de détails sur les types de données pouvant être configurés pour un graphique.

## **Définition des données du graphique**

Il existe deux types de données à manipuler lors de l'utilisation de graphiques avec Aspose.Cells, comme suit :

- Données du graphique.
- Données de catégorie.

### **Données du graphique**

Les données du graphique sont les données que nous utilisons comme source de données pour construire nos graphiques. Nous pouvons ajouter une plage de cellules (contenant des données de graphique) en appelant la méthode [**Add**](https://reference.aspose.com/cells/go-cpp/seriescollection/add/) de l'objet [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource.go" >}}
### **Données de catégorie**

Les données de catégorie sont utilisées pour l'étiquetage des données du graphique et peuvent être ajoutées à [**SeriesCollection**](https://reference.aspose.com/cells/go-cpp/seriescollection/) en utilisant sa propriété [**GetCategoryData()**](https://reference.aspose.com/cells/go-cpp/seriescollection/getcategorydata/). Un exemple complet est donné ci-dessous pour démontrer l'utilisation des données du graphique et de catégorie. Après l'exécution du code d'exemple ci-dessus, un graphique à colonnes sera ajouté à la feuille de calcul comme indiqué ci-dessous.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataSource-1.go" >}}
## **Sujets avancés**
- [Changer la source de données du graphique vers la feuille de calcul de destination lors de la copie des lignes ou de la plage](/cells/fr/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Créer des graphiques dynamiques](/cells/fr/cpp/create-dynamic-charts/)
- [Méthode simple pour configurer un graphique en utilisant la méthode Chart.SetChartDataRange](/cells/fr/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Trouver le type de valeurs X et Y des points dans la série de graphiques](/cells/fr/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
