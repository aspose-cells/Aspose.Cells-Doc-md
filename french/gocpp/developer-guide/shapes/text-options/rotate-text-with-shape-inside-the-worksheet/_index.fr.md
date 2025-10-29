---
title: Rotation du texte avec la forme à l intérieur de la feuille de calcul avec Golang via C++
linktitle: Tourner le texte avec la forme
type: docs
weight: 1300
url: /fr/go-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Apprenez comment contrôler la rotation du texte avec des formes dans les feuilles de calcul Excel en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez ajouter du texte à l'intérieur de n'importe quelle forme à l'aide de Microsoft Excel. Si vous ajoutez une forme avec la très ancienne version Microsoft Excel 2003, le texte ne tournera pas avec la forme. Cependant, si vous ajoutez une forme avec des versions plus récentes de Microsoft Excel, comme 2007, 2010, 2013 ou 2016, le texte tournera avec la forme. Vous pouvez contrôler si le texte doit tourner avec la forme ou non en utilisant la propriété [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/). La valeur par défaut de cette propriété est **true**, ce qui signifie que le texte tournera avec la forme. Si vous la définissez à **false**, le texte ne tournera pas avec la forme.

## **Faire pivoter le texte avec la forme à l'intérieur de la feuille de calcul**

Le code d'exemple suivant charge le [fichier Excel d'exemple](64716896.xlsx) contenant une forme triangulaire, et son texte tourne avec la forme. Si vous ouvrez le fichier Excel dans Microsoft Excel et faites pivoter la forme triangulaire, le texte tournera aussi avec elle. Le code définit ensuite la propriété [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/) sur **false** et le sauvegarde en tant que [fichier Excel de sortie](64716897.xlsx). Si vous ouvrez maintenant le fichier Excel de sortie dans Microsoft Excel et faites pivoter la forme triangulaire, le texte ne tournera pas avec elle. Veuillez voir la capture d'écran suivante montrant l'effet du code sur le fichier Excel d'exemple pour référence.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RotateTextWithShapeInsideTheWorksheet.go" >}}
