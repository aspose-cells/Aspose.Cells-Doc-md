---
title: Envoyer une forme vers l avant ou vers l arrière à l intérieur de la feuille de calcul
type: docs
weight: 3400
url: /fr/net/send-shape-front-or-back-inside-the-worksheet/
---

## **Scénarios d'utilisation possibles**

Lorsque plusieurs formes sont présentes au même emplacement, leur visibilité est décidée par leurs positions dans l'ordre z. Aspose.Cells fournit la méthode [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback) qui change la position dans l'ordre z de la forme. Si vous souhaitez envoyer une forme vers l'arrière, vous utiliserez un nombre négatif comme -1, -2, -3, etc. et si vous souhaitez envoyer une forme vers l'avant, vous utiliserez un nombre positif comme 1, 2, 3, etc.

## **Envoyer la forme à l'avant ou à l'arrière dans la feuille de calcul**

Le code d'exemple suivant explique l'utilisation de la méthode [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback). Veuillez consulter le [fichier Excel d'exemple](50528330.xlsx) utilisé dans le code et le [fichier Excel de sortie](50528331.xlsx) généré par celui-ci. La capture d'écran montre l'effet du code sur le fichier Excel d'exemple à l'exécution.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-SendShapeFrontOrBackInWorksheet.cs" >}}
