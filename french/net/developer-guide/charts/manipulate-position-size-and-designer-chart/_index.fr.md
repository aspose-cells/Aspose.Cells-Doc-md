---
title: Manipuler la taille de la position et le graphique du concepteur
description: Découvrez comment utiliser Aspose.Cells for .NET pour manipuler efficacement la position, la taille et le graphique du concepteur dans Microsoft Excel. Notre guide montrera comment ajuster ces propriétés pour une mise en page et une visualisation améliorées.
keywords: Aspose.Cells for .NET, Position, Size, Designer Chart, Microsoft Excel, Layout, Visualization.
type: docs
weight: 45
url: /fr/net/manipulate-position-size-and-designer-chart/
---
##  **Position et taille du graphique**
 Parfois, vous souhaitez modifier la position ou la taille du graphique nouveau ou existant dans la feuille de calcul. Aspose.Cells fournit le[Graphique.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) propriété pour y parvenir. Vous pouvez utiliser ses sous-propriétés pour redimensionner le graphique avec de nouveaux**hauteur** et**largeur** ou repositionnez-le avec un nouveau**X** et **Y** coordonnées.
###  **Contrôler la position et la taille du graphique**
Pour modifier la position (coordonnées X, Y) ou la taille (hauteur, largeur) du graphique, utilisez ces propriétés :

1. [Graphique.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Graphique.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Hauteur](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

L'exemple suivant explique l'utilisation des API ci-dessus, il charge le classeur existant qui contient un graphique dans sa première feuille de calcul. Ensuite, il redimensionne et repositionne le graphique en utilisant Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
##  **Manipulation des graphiques du concepteur**
Il arrive parfois que vous deviez manipuler ou modifier des graphiques dans les fichiers de modèles de concepteur. Aspose.Cells prend entièrement en charge la manipulation du contenu et des éléments des graphiques du concepteur. Les données, le contenu du graphique, l'image d'arrière-plan et les formats peuvent être conservés avec précision.
###  **Manipulation des graphiques du concepteur dans les fichiers modèles**
Pour manipuler les graphiques du concepteur dans les fichiers modèles, utilisez le graphique associé API. Par exemple, vous pouvez utiliser la propriété Worksheet.Charts pour obtenir la collection de graphiques existante dans le fichier modèle.
####  **Créer un graphique**
L'exemple suivant montre comment créer un graphique pyramidal. Nous manipulerons ce graphique plus tard.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
####  **Manipulation du graphique**
L'exemple suivant montre comment manipuler le graphique existant. Dans cet exemple, nous modifions le graphique créé ci-dessus. Dans la sortie générée, notez que l'étiquette de date d'un point de données a été définie sur « Royaume-Uni, 30 000 ».



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
####  **Manipulation d'un graphique linéaire dans le modèle du concepteur**
Dans cet exemple, nous allons manipuler un graphique linéaire. Nous ajouterons quelques séries de données au graphique existant et modifierons les couleurs de leurs lignes.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

