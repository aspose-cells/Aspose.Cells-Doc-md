---
title: Manipuler la taille de la position et le graphique du concepteur
type: docs
weight: 45
url: /fr/net/manipulate-position-size-and-designer-chart/
---
## **Position et taille du graphique**
 Parfois, vous souhaitez modifier la position ou la taille du graphique nouveau ou existant dans la feuille de calcul. Aspose.Cells fournit le[Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) propriété pour y parvenir. Vous pouvez utiliser ses sous-propriétés pour redimensionner le graphique avec de nouvelles**la taille** et**largeur** ou repositionnez-le avec de nouveaux** X** et**Coordonnées Y**.
### **Contrôle de la position et de la taille du graphique**
Pour modifier la position (coordonnées X, Y) ou la taille (hauteur, largeur) du graphique, utilisez ces propriétés :

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Graphique.ObjetGraphique.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

L'exemple suivant explique l'utilisation des API ci-dessus, il charge le classeur existant qui contient un graphique dans sa première feuille de calcul. Ensuite, il redimensionne et repositionne le graphique en utilisant Aspose.Cells.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **Manipulation des graphiques de concepteur**
Il arrive parfois que vous ayez besoin de manipuler ou de modifier des graphiques dans des fichiers de modèle de concepteur. Aspose.Cells prend entièrement en charge la manipulation du contenu et des éléments des graphiques de concepteur. Les données, le contenu du graphique, l'image d'arrière-plan et les mises en forme peuvent être conservés avec précision.
### **Manipulation de graphiques Designer dans des fichiers modèles**
Pour manipuler les graphiques de concepteur dans les fichiers de modèle, utilisez le graphique associé API. Par exemple, vous pouvez utiliser la propriété Worksheet.Charts pour obtenir la collection de graphiques existante dans le fichier de modèle.
#### **Création d'un graphique**
L'exemple suivant montre comment créer un diagramme pyramidal. Nous manipulerons ce graphique plus tard.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **Manipulation du graphique**
L'exemple suivant montre comment manipuler le graphique existant. Dans cet exemple, nous modifions le graphique créé ci-dessus. Dans la sortie générée, notez que l'étiquette de date d'un point de données a été définie sur "Royaume-Uni, 30K".



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **Manipulation d'un graphique en courbes dans le modèle Designer**
Dans cet exemple, nous allons manipuler un graphique linéaire. Nous ajouterons des séries de données au graphique existant et modifierons les couleurs de leurs lignes.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

