---
title: Envoyer la forme avant ou arrière dans la feuille de calcul
type: docs
weight: 600
url: /fr/java/send-shape-front-or-back-inside-the-worksheet/
---
## **Scénarios d'utilisation possibles**

Lorsqu'il y a plusieurs formes présentes au même endroit, la façon dont elles seront visibles est déterminée par leurs positions dans l'ordre z. Aspose.Cells fournit[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)) méthode qui modifie la position de l'ordre z de la forme. Si vous voulez envoyer la forme à l'arrière, vous utiliserez un nombre négatif comme -1, -2, -3, etc. et si vous voulez envoyer la forme à l'avant, vous utiliserez un nombre positif comme 1, 2, 3, etc.

## **Envoyer la forme avant ou arrière dans la feuille de calcul**

L'exemple de code suivant explique l'utilisation de[**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)) méthode. Veuillez consulter le[exemple de fichier Excel](50528362.xlsx)utilisé à l'intérieur du code et le[fichier Excel de sortie](50528361.xlsx)généré par celui-ci. La capture d'écran montre l'effet du code sur l'exemple de fichier Excel lors de l'exécution.

![tâche : image_autre_texte](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
