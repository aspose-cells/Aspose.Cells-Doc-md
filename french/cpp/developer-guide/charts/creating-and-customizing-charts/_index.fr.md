---
title: Création et personnalisation de graphiques
type: docs
weight: 10
url: /fr/cpp/creating-and-customizing-charts/
---
##  **Scénarios d'utilisation possibles**

Un graphique est un affichage visuel d’informations. Aspose.Cells permet aux développeurs de visualiser les informations dans des graphiques tout comme le fait Microsoft Excel. La présentation des informations sous forme de graphiques est toujours utile aux décideurs pour prendre des décisions rapides et opportunes. Il est plus facile de visualiser rapidement des comparaisons, des modèles et des tendances dans les données à l'aide de graphiques plutôt que de chiffres bruts. La création de graphiques au moment de l'exécution, basés sur les données d'une feuille de calcul, est l'une des fonctionnalités utiles de Aspose.Cells. Aspose.Cells prend en charge la création de graphiques standard et personnalisés. Ci-dessous, nous montrerons quelques exemples avec des exemples de fichiers sur la façon de créer certains types de graphiques MS-Excel courants à l'aide de Aspose.Cells API.

##  **Graphique pyramidal**

 Lorsque l'exemple de code est exécuté, un graphique pyramidal est ajouté à la feuille de calcul. Veuillez consulter le[sortie du fichier Excel](66519068.xlsx) de l’exemple de code suivant.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

##  **Graphique en ligne**

Dans l'exemple ci-dessus, il suffit de changer le[**Type de graphique**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)à**`ChartType :: Ligne`**crée un graphique linéaire. La source complète est fournie ci-dessous. lorsque le code est exécuté, un graphique linéaire est ajouté à la feuille de calcul. Veuillez consulter le[sortie du fichier Excel](66519069.xlsx) de l’exemple de code suivant.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

##  **Graphique à bulles**

Afin de créer un graphique à bulles, le[**Type de graphique**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) doit être réglé sur**`ChartType_Bulle`** et quelques propriétés supplémentaires telles que[**Définir les tailles de bulles**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/) & [**DéfinirXValeurs**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/) doivent être réglés en conséquence. Lors de l'exécution du code suivant, un graphique à bulles est ajouté à la feuille de calcul. Veuillez consulter le[sortie du fichier Excel](66519070.xlsx) de l’exemple de code suivant.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

##  **Création de graphiques personnalisés**

Jusqu'à présent, lorsque nous avons discuté des graphiques, nous avons examiné les graphiques standard dotés de leurs propres paramètres de formatage standard. Nous définissons uniquement la source de données, définissons quelques propriétés et le graphique est créé avec ses paramètres de format par défaut. Mais les API Aspose.Cells prennent également en charge la création de graphiques personnalisés qui permettent aux développeurs de créer des graphiques avec leurs propres paramètres de format. Les développeurs peuvent créer des graphiques personnalisés au moment de l'exécution à l'aide du Aspose.Cells.

Un graphique est composé d'une série de données. Lors de la création d'un graphique personnalisé, les développeurs ont la liberté d'utiliser différents types de graphiques pour différentes séries de données.

 L'exemple de code ci-dessous montre comment créer des graphiques personnalisés. Dans cet exemple, nous allons utiliser un histogramme pour la première série de données et un graphique linéaire pour la deuxième série. Le résultat est que nous ajoutons un histogramme, combiné à un graphique linéaire, à la feuille de calcul. Veuillez consulter le[sortie du fichier Excel](66519071.xlsx) de l’exemple de code suivant.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
