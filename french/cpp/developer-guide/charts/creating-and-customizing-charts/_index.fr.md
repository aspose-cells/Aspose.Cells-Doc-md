---
title: Création et personnalisation des graphiques
type: docs
weight: 10
url: /fr/cpp/creating-and-customizing-charts/
---

## **Scénarios d'utilisation possibles**

Un graphique est une présentation visuelle des informations. Aspose.Cells permet aux développeurs de visualiser des informations dans des graphiques tout comme le fait Microsoft Excel. Présenter des informations dans des graphiques est toujours utile pour les décideurs afin de prendre des décisions rapides et opportunes. Il est plus facile de voir rapidement des comparaisons, des motifs et des tendances dans les données avec des graphiques plutôt que des chiffres bruts. La création de graphiques à l'exécution, basée sur les données d'une feuille de calcul, est l'une des fonctionnalités utiles d'Aspose.Cells. Aspose.Cells prend en charge la création de graphiques standard et personnalisés. Ci-dessous, nous montrerons quelques exemples avec des fichiers d'exemple sur la manière de créer certains types de graphiques MS-Excel courants à l'aide de l'API Aspose.Cells.

## **Diagramme en pyramide**

Lorsque le code d'exemple est exécuté, un graphique en pyramide est ajouté à la feuille de calcul. Veuillez consulter le [fichier Excel de sortie](66519068.xlsx) du code d'exemple suivant.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

## **Diagramme linéaire**

Dans l'exemple ci-dessus, en modifiant simplement [**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) en **`ChartType::Line`** crée un graphique en courbes. Le code source complet est fourni ci-dessous. Lorsque le code est exécuté, un graphique en courbes est ajouté à la feuille de calcul. Veuillez consulter le [fichier Excel de sortie](66519069.xlsx) du code d'exemple suivant.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

## **Diagramme en bulles**

Afin de créer un graphique en bulles, [**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) doit être défini sur **`ChartType_Bubble`** et quelques propriétés supplémentaires telles que [**SetBubbleSizes**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/) & [**SetXValues**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/) doivent être définies en conséquence. Après l'exécution du code suivant, un graphique en bulles est ajouté à la feuille de calcul. Veuillez consulter le [fichier Excel de sortie](66519070.xlsx) du code d'exemple suivant.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

## **Création de graphiques personnalisés**

Jusqu'à présent, lorsque nous avons discuté des graphiques, nous avons examiné des graphiques standards qui ont leurs propres paramètres de formatage standard. Nous définissons simplement la source de données, définissons quelques propriétés et le graphique est créé avec ses paramètres de format par défaut. Mais les API Aspose.Cells prennent également en charge la création de graphiques personnalisés qui permet aux développeurs de créer des graphiques avec leurs propres paramètres de formatage. Les développeurs peuvent créer des graphiques personnalisés à l'exécution à l'aide d'Aspose.Cells.

Un graphique est composé d'une série de données. Lors de la création d'un graphique personnalisé, les développeurs ont la liberté d'utiliser différents types de graphiques pour différentes séries de données.

L'exemple de code ci-dessous démontre comment créer des graphiques personnalisés. Dans cet exemple, nous allons utiliser un graphique en colonnes pour la première série de données et un graphique en ligne pour la deuxième série. Le résultat est que nous ajoutons un graphique en colonnes, combiné avec un graphique en ligne, à la feuille de calcul. Veuillez consulter le [fichier Excel de sortie](66519071.xlsx) du code d'exemple suivant.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
