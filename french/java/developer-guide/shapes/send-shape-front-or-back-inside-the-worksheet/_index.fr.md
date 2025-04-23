---
title: Envoyer une forme vers l avant ou vers l arrière à l intérieur de la feuille de calcul
type: docs
weight: 600
url: /fr/java/send-shape-front-or-back-inside-the-worksheet/
---

## **Scénarios d'utilisation possibles**

Lorsqu'il y a plusieurs formes présentes au même endroit, leur visibilité est décidée par leurs positions d'ordre Z. Aspose.Cells fournit la méthode [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack-int-) qui change la position de l'ordre Z de la forme. Si vous voulez envoyer la forme en arrière, vous utiliserez un nombre négatif comme -1, -2, -3, etc. et si vous voulez envoyer la forme au premier plan, vous utiliserez un nombre positif comme 1, 2, 3, etc.

## **Envoyer la forme à l'avant ou à l'arrière dans la feuille de calcul**

Le code d'exemple suivant explique l'utilisation de la méthode [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack-int-). Veuillez consulter le [fichier Excel d'exemple](50528362.xlsx) utilisé dans le code et le [fichier Excel de sortie](50528361.xlsx) généré par celui-ci. La capture d'écran montre l'effet du code sur le fichier Excel d'exemple à l'exécution.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
