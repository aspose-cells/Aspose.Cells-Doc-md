---
title: Créer et personnaliser des graphiques
type: docs
weight: 10
url: /fr/cpp/creating-and-customizing-charts/
---
## **Scénarios d'utilisation possibles**

Un graphique est un affichage visuel d'informations. Aspose.Cells permet aux développeurs de visualiser des informations dans des graphiques comme le fait Microsoft Excel. Présenter des informations dans des graphiques est toujours utile aux décideurs pour prendre des décisions rapides et opportunes. Il est plus facile de voir rapidement des comparaisons, des modèles et des tendances dans les données avec des graphiques plutôt qu'avec des chiffres bruts. La création de graphiques au moment de l'exécution, basée sur les données d'une feuille de calcul, est l'une des fonctionnalités utiles de Aspose.Cells. Aspose.Cells prend en charge la création de graphiques standard et personnalisés. Ci-dessous, nous montrerons quelques exemples avec des exemples de fichiers sur la façon de créer des types de graphiques MS-Excel courants à l'aide de Aspose.Cells API.

## **Graphique pyramidal**

 Lorsque l'exemple de code est exécuté, un graphique pyramidal est ajouté à la feuille de calcul. Veuillez consulter le[fichier Excel de sortie](66519068.xlsx) de l'exemple de code suivant.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart.cpp" >}}

## **Graphique en ligne**

Dans l'exemple ci-dessus, il suffit de changer le[**Type de graphique**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70)à[**Type de graphique_Ligne**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70ad12ff1561ab1424a0c3095b6dc07ac25)crée un graphique en courbes. La source complète est fournie ci-dessous. lorsque le code est exécuté, un graphique linéaire est ajouté à la feuille de calcul. Veuillez consulter le[fichier Excel de sortie](66519069.xlsx) de l'exemple de code suivant.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart.cpp" >}}

## **Graphique à bulles**

Pour créer un graphique à bulles, le[**Type de graphique**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70) doit être réglé sur[**Type de graphique_bulle**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70a5efa533b454f9415e4497dbb2ab28b3d) et quelques propriétés supplémentaires telles que[**SetBubbleSizes**](https://reference.aspose.com/cells/cpp/class/aspose.cells.charts.i_series#a00cf890ba7ab419d31a522ab52b02e9d) & [**SetXValues**](https://reference.aspose.com/cells/cpp/class/aspose.cells.charts.i_series#a788ff4aa51dbf9bed5327298af93a6db) doivent être réglés en conséquence. Lors de l'exécution du code suivant, un graphique à bulles est ajouté à la feuille de calcul. Veuillez consulter le[fichier Excel de sortie](66519070.xlsx) de l'exemple de code suivant.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart.cpp" >}}

## **Création de graphiques personnalisés**

Jusqu'à présent, lorsque nous avons discuté des graphiques, nous avons examiné les graphiques standard qui ont leurs propres paramètres de mise en forme standard. Nous définissons uniquement la source de données, définissons quelques propriétés et le graphique est créé avec ses paramètres de format par défaut. Mais les API Aspose.Cells prennent également en charge la création de graphiques personnalisés qui permettent aux développeurs de créer des graphiques avec leurs propres paramètres de format. Les développeurs peuvent créer des graphiques personnalisés au moment de l'exécution à l'aide de Aspose.Cells.

Un graphique est composé d'une série de données. Lors de la création d'un graphique personnalisé, les développeurs ont la liberté d'utiliser différents types de graphiques pour différentes séries de données.

 L'exemple de code ci-dessous montre comment créer des graphiques personnalisés. Dans cet exemple, nous allons utiliser un histogramme pour la première série de données et un graphique linéaire pour la deuxième série. Le résultat est que nous ajoutons un graphique à colonnes, combiné à un graphique linéaire, à la feuille de calcul. Veuillez consulter le[fichier Excel de sortie](66519071.xlsx) de l'exemple de code suivant.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart.cpp" >}}
