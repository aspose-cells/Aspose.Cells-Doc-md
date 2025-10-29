---
title: Manipuler la position, la taille et le concepteur du graphique avec Golang via C++
linktitle: Manipuler la position, la taille et la conception du graphique
description: Apprenez comment utiliser Aspose.Cells for C++ pour manipuler efficacement la position, la taille et le graphique de conception dans Microsoft Excel. Notre guide démontrera comment ajuster ces propriétés pour une meilleure mise en page et visualisation.
keywords: Aspose.Cells for C++, Position, Taille, Graphique de conception, Microsoft Excel, Mise en page, Visualisation.
type: docs
weight: 45
url: /fr/go-cpp/manipulate-position-size-and-designer-chart/
---

## **Position et taille du graphique**
Parfois, vous souhaitez changer la position ou la taille du nouveau ou existant graphique à l'intérieur de la feuille de calcul. Aspose.Cells fournit la propriété [Chart.GetChartObject()](https://reference.aspose.com/cells/go-cpp/chart/getchartobject/) pour y parvenir. Vous pouvez utiliser ses sous-propriétés pour redimensionner le graphique avec une nouvelle **hauteur** et **largeur** ou le repositionner avec de nouvelles coordonnées **X** et **Y**.

### **Contrôle de la position et la taille du graphique**
Pour changer la position (coordonnées X, Y) ou la taille (hauteur, largeur) du graphique, utilisez ces propriétés :

1. [Chart.GetX()](https://reference.aspose.com/cells/go-cpp/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/go-cpp/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/go-cpp/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/go-cpp/shape/getwidth/)

L'exemple suivant explique l'utilisation des API ci-dessus, il charge le classeur existant qui contient un graphique dans sa première feuille. Ensuite, il redimensionne et repositionne le graphique en utilisant Aspose.Cells.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart.go" >}}
## **Manipulation des graphiques de concepteur**
Il y a des moments où vous avez besoin de manipuler ou de modifier des graphiques dans des fichiers de modèle de concepteur. Aspose.Cells prend en charge pleinement la manipulation des contenus et des éléments de graphique de concepteur. Les données, les contenus des graphiques, l'image de fond et les mises en forme peuvent être conservés avec précision.

### **Manipulation des graphiques de concepteur dans les fichiers de modèle**
Pour manipuler des graphiques de concepteur dans des fichiers de modèle, utilisez l'API liée au graphique. Par exemple, vous pouvez utiliser la propriété Worksheet.Charts pour obtenir la collection de graphiques existante dans le fichier de modèle.

#### **Création d'un graphique**
L'exemple suivant montre comment créer un graphique en forme de pyramide. Nous manipulerons ce graphique plus tard.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-1.go" >}}
#### **Manipulation du graphique**
L'exemple suivant montre comment manipuler le graphique existant. Dans cet exemple, nous modifions le graphique créé précédemment. Dans la sortie générée, notez que l'étiquette de date d'un point de données a été définie sur 'Royaume-Uni, 30K'.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-2.go" >}}
#### **Manipulation d'un graphique linéaire dans le modèle de concepteur**
Dans cet exemple, nous manipulerons un graphique linéaire. Nous ajouterons des séries de données au graphique existant et changerons leurs couleurs de ligne.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-3.go" >}}
