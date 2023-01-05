---
title: Formatage des données dans les graphiques
linktitle: La source de données
type: docs
weight: 50
url: /fr/java/data-formatting-in-charts/
---
{{% alert color="primary" %}}

Dans nos rubriques précédentes, nous avons déjà fourni de nombreux exemples pour démontrer comment définir une source de données pour votre graphique, mais dans cette rubrique, nous allons fournir plus de détails sur les types de données pouvant être définies pour un graphique.

{{% /alert %}}

## **Définition des données cartographiques**

Il existe deux types de données à traiter lorsque vous travaillez sur des graphiques en utilisant Aspose.Cells comme suit :

- [Données du graphique](/cells/fr/java/data-formatting-in-charts/#chart-data).
- [Données de catégorie](/cells/fr/java/data-formatting-in-charts/#category-data).

### **Données de graphique**

 Les données de graphique sont les données que nous utilisons comme source de données pour créer nos graphiques. Nous pouvons ajouter une plage de cellules (contenant des données de graphique) en appelant le[**SérieCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) objets[**Ajouter**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add(java.lang.Object)) méthode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **Données de catégorie**

 Les données de catégorie sont utilisées pour l'étiquetage des données de graphique et peuvent être ajoutées à[**SérieCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) en utilisant son[**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData)méthode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**Graphique à colonnes avec données de graphique et de catégorie** 

![tâche : image_autre_texte](data-formatting-in-charts_1.png)

## **Sujets avancés**
- [Créer des graphiques dynamiques](/cells/fr/java/create-dynamic-charts/)
- [Un moyen simple pour la configuration du graphique à l'aide de la méthode Chart.setChartDataRange](/cells/fr/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Trouver le type de valeurs X et Y des points dans la série de graphiques](/cells/fr/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [Définir le code de format des valeurs de la série de graphiques](/cells/fr/java/set-the-values-format-code-of-chart-series/)
