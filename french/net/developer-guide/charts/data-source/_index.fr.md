---
title: Définir la source de données pour le graphique
linktitle: La source de données
type: docs
weight: 10
url: /fr/net/data-formatting-in-charts/
---
Dans nos rubriques précédentes, nous avons déjà fourni de nombreux exemples pour démontrer comment définir une source de données pour votre graphique, mais dans cette rubrique, nous allons fournir plus de détails sur les types de données pouvant être définies pour un graphique.

## **Définition des données cartographiques**

Il existe deux types de données à traiter lorsque vous travaillez sur des graphiques en utilisant Aspose.Cells comme suit :

- Données du graphique.
- Données de catégorie.

### **Données de graphique**

Les données de graphique sont les données que nous utilisons comme source de données pour créer nos graphiques. Nous pouvons ajouter une plage de cellules (contenant des données de graphique) en appelant le[**SérieCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) objets[**Ajouter**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add)méthode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingChartsData-1.cs" >}}

### **Données de catégorie**

 Les données de catégorie sont utilisées pour l'étiquetage des données de graphique et peuvent être ajoutées à[**SérieCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) en utilisant son[**Données de catégorie**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata)la propriété. Un exemple complet est donné ci-dessous pour illustrer l'utilisation des données de graphique et de catégorie. Après avoir exécuté l'exemple de code ci-dessus, un histogramme sera ajouté à la feuille de calcul, comme indiqué ci-dessous.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SettingCategoryData-1.cs" >}}

## **Sujets avancés**
- [Changer la source de données du graphique en feuille de calcul de destination lors de la copie de lignes ou d'une plage](/cells/fr/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Créer des graphiques dynamiques](/cells/fr/net/create-dynamic-charts/)
- [Méthode simple pour la configuration du graphique à l'aide de la méthode Chart.SetChartDataRange](/cells/fr/net/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Trouver le type de valeurs X et Y des points dans la série de graphiques](/cells/fr/net/find-type-of-x-and-y-values-of-points-in-chart-series/)
