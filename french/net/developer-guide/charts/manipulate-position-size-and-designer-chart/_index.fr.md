---
title: Manipuler la position, la taille et la conception du graphique
description: Apprenez à utiliser Aspose.Cells for .NET pour manipuler efficacement la position, la taille et la conception du graphique dans Microsoft Excel. Notre guide vous montrera comment ajuster ces propriétés pour une présentation et une visualisation améliorées.
keywords: Aspose.Cells for .NET, Position, Taille, Conception du graphique, Microsoft Excel, Mise en page, Visualisation.
type: docs
weight: 45
url: /fr/net/manipulate-position-size-and-designer-chart/
---

## **Position et taille du graphique**
Parfois, vous voulez changer la position ou la taille du graphique, nouveau ou existant, à l'intérieur de la feuille de calcul. Aspose.Cells fournit la propriété [Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) pour y parvenir. Vous pouvez utiliser ses sous-propriétés pour redimensionner le graphique avec une nouvelle **hauteur** et **largeur** ou le repositionner avec de nouvelles coordonnées **X** et **Y**.
### **Contrôle de la position et la taille du graphique**
Pour changer la position (coordonnées X, Y) ou la taille (hauteur, largeur) du graphique, utilisez ces propriétés :

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

L'exemple suivant explique l'utilisation des API ci-dessus, il charge le classeur existant qui contient un graphique dans sa première feuille. Ensuite, il redimensionne et repositionne le graphique en utilisant Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **Manipulation des graphiques de concepteur**
Il y a des moments où vous avez besoin de manipuler ou de modifier des graphiques dans des fichiers de modèle de concepteur. Aspose.Cells prend en charge pleinement la manipulation des contenus et des éléments de graphique de concepteur. Les données, les contenus des graphiques, l'image de fond et les mises en forme peuvent être conservés avec précision.
### **Manipulation des graphiques de concepteur dans les fichiers de modèle**
Pour manipuler des graphiques de concepteur dans des fichiers de modèle, utilisez l'API liée au graphique. Par exemple, vous pouvez utiliser la propriété Worksheet.Charts pour obtenir la collection de graphiques existante dans le fichier de modèle.
#### **Création d'un graphique**
L'exemple suivant montre comment créer un graphique en forme de pyramide. Nous manipulerons ce graphique plus tard.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **Manipulation du graphique**
L'exemple suivant montre comment manipuler le graphique existant. Dans cet exemple, nous modifions le graphique créé précédemment. Dans la sortie générée, notez que l'étiquette de date d'un point de données a été définie sur 'Royaume-Uni, 30K'.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **Manipulation d'un graphique linéaire dans le modèle de concepteur**
Dans cet exemple, nous manipulerons un graphique linéaire. Nous ajouterons des séries de données au graphique existant et changerons leurs couleurs de ligne.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
