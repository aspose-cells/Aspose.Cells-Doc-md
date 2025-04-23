---
title: Formatage des données dans les graphiques
linktitle: Source de données
type: docs
weight: 50
url: /fr/java/data-formatting-in-charts/
---

{{% alert color="primary" %}}

Dans nos sujets précédents, nous avons déjà fourni de nombreux exemples pour démontrer comment vous pouvez définir une source de données pour votre graphique, mais dans ce sujet, nous allons fournir plus de détails sur les types de données qui peuvent être définis pour un graphique.

{{% /alert %}}

## **Définition des données du graphique**

Il existe deux types de données à manipuler lors de l'utilisation de graphiques avec Aspose.Cells, comme suit :

- [Données du graphique](/cells/fr/java/formatage-des-donnees-dans-les-graphiques/#donnees-du-graphique).
- [Données de catégorie](/cells/fr/java/formatage-des-donnees-dans-les-graphiques/#donnees-de-categorie).

### **Données du graphique**

Les données de graphique sont les données que nous utilisons comme source de données pour construire nos graphiques. Nous pouvons ajouter une plage de cellules (contenant des données de graphique) en appelant la méthode [**Add**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#add-java.lang.Object-) de l'objet [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsData-SettingChartsData.java" >}}

### **Données de catégorie**

Les données de catégorie sont utilisées pour l'étiquetage des données de graphique et peuvent être ajoutées à [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) en utilisant sa méthode [**setCategoryData**](https://reference.aspose.com/cells/java/com.aspose.cells/seriescollection#CategoryData).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingCategoryData-SettingCategoryData.java" >}}

**Diagramme en colonnes avec données de graphique & de catégorie** 

![todo:image_alt_text](data-formatting-in-charts_1.png)

## **Sujets avancés**
- [Créer des graphiques dynamiques](/cells/fr/java/create-dynamic-charts/)
- [Méthode Simple pour Configurer un Graphique en utilisant la méthode setChartDataRange de Chart](/cells/fr/java/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Trouver le type de valeurs X et Y des points dans la série de graphiques](/cells/fr/java/find-type-of-x-and-y-values-of-points-in-chart-series/)
- [Définir le code de format des valeurs de la série du graphique](/cells/fr/java/set-the-values-format-code-of-chart-series/)
{{< app/cells/assistant language="java" >}}
