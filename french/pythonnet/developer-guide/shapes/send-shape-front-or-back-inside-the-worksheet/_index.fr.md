---
title: Envoyer une forme vers l avant ou vers l arrière à l intérieur de la feuille de calcul
type: docs
weight: 3400
url: /fr/python-net/send-shape-front-or-back-inside-the-worksheet/
---

## **Scénarios d'utilisation possibles**

Lorsqu’il y a plusieurs formes présentes au même endroit, leur visibilité est décidée par leur position dans l’ordre de z. Aspose.Cells pour Python via .NET propose la méthode [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back) qui modifie la position z de la forme. Si vous souhaitez envoyer une forme à l’arrière, utilisez un nombre négatif comme -1, -2, -3, etc. Et si vous souhaitez amener une forme au premier plan, utilisez un nombre positif comme 1, 2, 3, etc.

## **Envoyer la forme à l'avant ou à l'arrière dans la feuille de calcul**

Le code d'exemple suivant explique l'utilisation de la méthode [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back). Veuillez consulter le [fichier Excel d'exemple](50528330.xlsx) utilisé dans le code et le [fichier Excel de sortie](50528331.xlsx) généré par celui-ci. La capture d'écran montre l'effet du code sur le fichier Excel d'exemple à l'exécution.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-SendShapeFrontOrBackInWorksheet.py" >}}
