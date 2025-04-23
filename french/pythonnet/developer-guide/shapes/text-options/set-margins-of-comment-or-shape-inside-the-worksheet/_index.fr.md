---
title: Définir les marges du commentaire ou de la forme à l intérieur de la feuille de calcul
type: docs
weight: 1500
url: /fr/python-net/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells pour Python via .NET vous permet de définir les marges de n'importe quelle forme ou commentaire en utilisant la propriété [**Shape.text_body.text_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/fontsettingcollection/text_alignment). Cette propriété renvoie l'objet de la classe [**ShapeTextAlignment**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment) avec différentes propriétés, par exemple [**top_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/top_margin_pt), [**left_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/left_margin_pt), [**bottom_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/bottom_margin_pt), [**right_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/right_margin_pt), etc., qui peuvent être utilisées pour définir les marges supérieure, gauche, inférieure et droite.

## **Définir les marges du commentaire ou de la forme à l'intérieur de la feuille de calcul**

Veuillez consulter le code d'échantillon suivant. Il charge le [fichier Excel d'échantillon](61767851.xlsx) qui contient deux formes. Le code accède aux formes une par une et définit leurs marges supérieure, gauche, inférieure et droite. Veuillez consulter le [fichier Excel de sortie](61767852.xlsx) généré par le code et la capture d'écran montrant l'effet du code sur le fichier Excel de sortie.

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SetMarginsOfCommentOrShapeInsideTheWorksheet.py" >}}
