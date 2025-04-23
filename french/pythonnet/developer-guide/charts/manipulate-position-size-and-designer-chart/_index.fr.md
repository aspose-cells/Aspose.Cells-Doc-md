---
title: Manipuler la position, la taille et la conception du graphique
description: Apprenez à utiliser Aspose.Cells pour Python via .NET pour manipuler efficacement la position, la taille et la conception du graphique dans Microsoft Excel. Notre guide montrera comment ajuster ces propriétés pour une meilleure mise en page et visualisation.
keywords: Aspose.Cells pour Python via .NET, Position, Taille, Graphique de conception, Microsoft Excel, Mise en page, Visualisation.
type: docs
weight: 45
url: /fr/python-net/manipulate-position-size-and-designer-chart/
---

## **Position et taille du graphique**
Parfois, vous souhaitez changer la position ou la taille du graphique nouveau ou existant dans la feuille de calcul. Aspose.Cells pour Python via .NET fournit la propriété [Chart.chart_object](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/chart_object) pour y parvenir. Vous pouvez utiliser ses sous-propriétés pour redimensionner le graphique avec une nouvelle **hauteur** et **largeur** ou le repositionner avec de nouvelles coordonnées **X** et **Y**.
### **Contrôle de la position et la taille du graphique**
Pour changer la position (coordonnées X, Y) ou la taille (hauteur, largeur) du graphique, utilisez ces propriétés :

1. [Chart.chart_object.x](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/x)
1. [Chart.chart_object.y](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/y)
1. [Chart.chart_object.height](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/height)
1. [Chart.chart_object.width](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/width)

L'exemple suivant explique l'utilisation des API ci-dessus, il charge le classeur existant contenant un graphique dans sa première feuille de calcul. Ensuite, il redimensionne et repositionne le graphique en utilisant Aspose.Cells pour Python via .NET.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartPosition-1.py" >}}
## **Manipulation des graphiques de concepteur**
Il arrive que vous deviez manipuler ou modifier des graphiques dans des fichiers modèles de conception. Aspose.Cells pour Python via .NET prend en charge la manipulation complète du contenu et des éléments des graphiques de conception. Les données, le contenu du graphique, l'image de fond et les formats peuvent être conservés avec précision.
### **Manipulation des graphiques de concepteur dans les fichiers de modèle**
Pour manipuler des graphiques de concepteur dans des fichiers de modèle, utilisez l'API liée au graphique. Par exemple, vous pouvez utiliser la propriété Worksheet.Charts pour obtenir la collection de graphiques existante dans le fichier de modèle.
#### **Création d'un graphique**
L'exemple suivant montre comment créer un graphique en forme de pyramide. Nous manipulerons ce graphique plus tard.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-HowToCreateChart-1.py" >}}
#### **Manipulation du graphique**
L'exemple suivant montre comment manipuler le graphique existant. Dans cet exemple, nous modifions le graphique créé précédemment. Dans la sortie générée, notez que l'étiquette de date d'un point de données a été définie sur 'Royaume-Uni, 30K'.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyPieChart-1.py" >}}
#### **Manipulation d'un graphique linéaire dans le modèle de concepteur**
Dans cet exemple, nous manipulerons un graphique linéaire. Nous ajouterons des séries de données au graphique existant et changerons leurs couleurs de ligne.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyLineChart-1.py" >}}

