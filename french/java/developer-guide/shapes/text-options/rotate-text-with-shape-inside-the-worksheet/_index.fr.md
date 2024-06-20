---
title: Faire pivoter le texte avec la forme à l intérieur de la feuille de calcul
type: docs
weight: 110
url: /fr/java/rotate-text-with-shape-inside-the-worksheet/
---

## **Scénarios d'utilisation possibles**

Vous pouvez ajouter du texte dans n'importe quelle forme à l'aide de Microsoft Excel. Si vous ajoutez une forme à l'aide de la très ancienne version de Microsoft Excel 2003, alors le texte ne pivotera pas avec la forme. Mais si vous ajoutez une forme à l'aide de versions plus récentes de Microsoft Excel, par exemple 2007, 2010, 2013 ou 2016, etc., alors le texte pivotera avec la forme. Vous pouvez contrôler si le texte doit pivoter avec la forme ou non en utilisant la propriété [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape). La valeur par défaut est **true**, ce qui signifie que le texte pivotera avec la forme, mais si vous la définissez sur **false**, alors le texte ne pivotera pas avec la forme.

## **Faire pivoter le texte avec la forme à l'intérieur de la feuille de calcul**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716919.xlsx) qui contient une forme de triangle et dont le texte pivote avec la forme. Si vous ouvrez le fichier Excel d'exemple dans Microsoft Excel et faites pivoter la forme du triangle, le texte pivotera également avec elle. Le code définit ensuite la propriété [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape) comme **false** et le sauvegarde sous la forme de [fichier Excel de sortie](64716917.xlsx). Si vous ouvrez maintenant le fichier Excel de sortie dans Microsoft Excel et faites pivoter la forme du triangle, le texte ne pivotera pas avec elle. Veuillez consulter la capture d'écran suivante montrant l'effet du code sur le fichier Excel d'exemple pour référence.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-RotateTextWithShapeInsideWorksheet.java" >}}
