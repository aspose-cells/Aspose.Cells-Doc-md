---
title: Faire pivoter le texte avec la forme à l'intérieur de la feuille de calcul
type: docs
weight: 110
url: /fr/java/rotate-text-with-shape-inside-the-worksheet/
---
## **Scénarios d'utilisation possibles**

Vous pouvez ajouter du texte à l'intérieur de n'importe quelle forme en utilisant Microsoft Excel. Si vous ajoutez une forme à l'aide du très ancien Microsoft Excel 2003, le texte ne pivotera pas avec la forme. Mais si vous ajoutez une forme à l'aide de versions plus récentes d'Excel Microsoft, par exemple 2007, 2010, 2013 ou 2016, etc., le texte pivotera avec la forme. Vous pouvez contrôler si le texte doit pivoter avec la forme ou non en utilisant le[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape)la propriété. La valeur par défaut de celui-ci est**vrai**ce qui signifie que le texte pivotera avec la forme, mais si vous le définissez comme**faux**, le texte ne pivotera pas avec la forme.

## **Faire pivoter le texte avec la forme à l'intérieur de la feuille de calcul**

L'exemple de code suivant charge le[exemple de fichier Excel](64716919.xlsx)qui a une forme de triangle et son texte tourne avec la forme. Si vous ouvrez l'exemple de fichier Excel dans Microsoft Excel et faites pivoter la forme du triangle, le texte pivotera également avec lui. Le code définit alors le[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape)propriété comme**faux**et l'enregistre sous[fichier Excel de sortie](64716917.xlsx). Si vous ouvrez maintenant le fichier Excel de sortie dans Microsoft Excel et faites pivoter la forme du triangle, le texte ne pivotera pas avec lui. Veuillez consulter la capture d'écran suivante montrant l'effet du code sur un exemple de fichier Excel pour référence.

![tâche : image_autre_texte](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-RotateTextWithShapeInsideWorksheet.java" >}}
