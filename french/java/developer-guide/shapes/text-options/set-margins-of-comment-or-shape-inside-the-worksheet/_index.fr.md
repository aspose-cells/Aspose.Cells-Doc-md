---
title: Définir les marges du commentaire ou de la forme à l intérieur de la feuille de calcul
type: docs
weight: 90
url: /fr/java/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet de définir les marges de n'importe quelle forme ou commentaire en utilisant la propriété [**Shape.TextBody.TextAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/fontsettingcollection#TextAlignment). Cette propriété renvoie l'objet de la classe [**ShapeTextAlignment**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeTextAlignment) qui a différentes propriétés telles que [**TopMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#TopMarginPt), [**LeftMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#LeftMarginPt), [**BottomMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#BottomMarginPt), [**RightMarginPt**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RightMarginPt), etc. qui peuvent être utilisées pour définir les marges supérieure, gauche, inférieure et droite.

## **Définir les marges du commentaire ou de la forme à l'intérieur de la feuille de calcul**

Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel d'exemple](61767867.xlsx) qui contient deux formes. Le code accède aux formes une par une et définit leurs marges supérieure, gauche, inférieure et droite. Veuillez consulter le [fichier Excel de sortie](61767866.xlsx) généré par le code et la capture d'écran montrant l'effet du code sur le fichier Excel de sortie.

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-SetMarginsOfCommentOrShapeInsideTheWorksheet.java" >}}
