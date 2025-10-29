---
title: Faire pivoter le texte avec la forme à l intérieur de la feuille de calcul
type: docs
weight: 1300
url: /fr/python-net/rotate-text-with-shape-inside-the-worksheet/
---

## **Scénarios d'utilisation possibles**

Vous pouvez ajouter du texte à l'intérieur de n'importe quelle forme en utilisant Microsoft Excel. Si vous ajoutez une forme à l'aide de la très ancienne version de Microsoft Excel 2003, le texte ne pivotera pas avec la forme. Mais si vous ajoutez une forme à l'aide de versions plus récentes de Microsoft Excel, par exemple 2007, 2010, 2013 ou 2016, etc., le texte pivotera avec la forme. Vous pouvez contrôler si le texte doit pivoter avec la forme ou non en utilisant la propriété [**ShapeTextAlignment.rotate_text_with_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/rotate_text_with_shape). Sa valeur par défaut est **true** ce qui signifie que le texte pivotera avec la forme, mais si vous le définissez sur **false**, le texte ne pivotera pas avec la forme.

## **Faire pivoter le texte avec la forme à l'intérieur de la feuille de calcul**

Le code d'échantillon suivant charge le [fichier Excel d'exemple](64716896.xlsx) qui contient une forme de triangle et son texte pivote avec la forme. Si vous ouvrez le fichier Excel d'exemple dans Microsoft Excel et faites pivoter la forme de triangle, le texte pivotera également avec elle. Le code définit ensuite la propriété [**ShapeTextAlignment.rotate_text_with_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/rotate_text_with_shape) sur **false** et l'enregistre en tant que [fichier Excel de sortie](64716897.xlsx). Si vous ouvrez maintenant le fichier Excel de sortie dans Microsoft Excel et faites pivoter la forme de triangle, le texte ne pivotera pas avec elle. Veuillez voir la capture d'écran suivante montrant l'effet du code sur le fichier Excel d'exemple pour référence.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-RotateTextWithShapeInsideWorksheet.py" >}}
{{< app/cells/assistant language="python-net" >}}
