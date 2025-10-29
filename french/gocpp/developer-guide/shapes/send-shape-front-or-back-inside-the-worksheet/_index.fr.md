---
title: Envoyer la forme au premier plan ou à l arrière plan dans la feuille de calcul avec Golang via C++
linktitle: Envoyer une forme vers l avant ou vers l arrière à l intérieur de la feuille de calcul
type: docs
weight: 3400
url: /fr/go-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Apprenez comment changer la position z order des formes dans une feuille de calcul en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Lorsque plusieurs formes sont présentes au même endroit, leur visibilité est déterminée par leur position dans l'ordre z. Aspose.Cells fournit la méthode [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/), qui modifie la position z de la forme. Si vous souhaitez envoyer une forme en arrière-plan, utilisez un nombre négatif comme -1, -2, -3, etc. Si vous souhaitez amener une forme en avant-plan, utilisez un nombre positif comme 1, 2, 3, etc.

## **Envoyer la forme à l'avant ou à l'arrière dans la feuille de calcul**

Le code d'exemple suivant montre comment utiliser la méthode [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/). Veuillez voir le [fichier Excel d'exemple](50528330.xlsx) utilisé dans le code et le [fichier Excel en sortie](50528331.xlsx) généré par celui-ci. La capture d'écran montre l'effet du code sur le fichier Excel d'exemple lors de l'exécution.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SendShapeFrontOrBackInsideTheWorksheet.go" >}}
