---
title: Définir les marges du commentaire ou de la forme à l intérieur de la feuille de calcul
type: docs
weight: 1500
url: /fr/net/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet de définir les marges de n'importe quelle forme ou commentaire en utilisant la propriété [**Shape.TextBody.TextAlignment**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/fontsettingcollection/properties/textalignment). Cette propriété renvoie l'objet de la classe [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment) qui possède différentes propriétés telles que [**TopMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/topmarginpt), [**LeftMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/leftmarginpt), [**BottomMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/bottommarginpt), [**RightMarginPt**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rightmarginpt), etc. qui peuvent être utilisées pour définir les marges supérieure, gauche, inférieure et droite.

## **Définir les marges du commentaire ou de la forme à l'intérieur de la feuille de calcul**

Veuillez consulter le code d'échantillon suivant. Il charge le [fichier Excel d'échantillon](61767851.xlsx) qui contient deux formes. Le code accède aux formes une par une et définit leurs marges supérieure, gauche, inférieure et droite. Veuillez consulter le [fichier Excel de sortie](61767852.xlsx) généré par le code et la capture d'écran montrant l'effet du code sur le fichier Excel de sortie.

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-SetMarginsOfCommentOrShapeInsideTheWorksheet.cs" >}}
