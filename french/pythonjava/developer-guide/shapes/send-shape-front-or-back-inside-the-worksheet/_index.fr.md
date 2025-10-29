---
title: Amener les formes en avant ou en arrière dans une feuille de calcul
type: docs
weight: 3400
url: /fr/python-java/send-shape-front-or-back-inside-the-worksheet/
---

## **Scénarios d'utilisation possibles**

Lorsque plusieurs formes sont présentes au même emplacement, leur visibilité est décidée par leurs positions dans l'ordre z. Aspose.Cells fournit la méthode [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)) qui change la position dans l'ordre z de la forme. Si vous souhaitez envoyer une forme vers l'arrière, vous utiliserez un nombre négatif comme -1, -2, -3, etc. et si vous souhaitez envoyer une forme vers l'avant, vous utiliserez un nombre positif comme 1, 2, 3, etc.

## **Amener la forme en avant ou en arrière dans la feuille de calcul**

Le code d'exemple suivant explique l'utilisation de la méthode [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)). Veuillez voir le [fichier Excel d'exemple](sampleToFrontOrBack.xlsx) utilisé dans le code et le [fichier Excel de sortie](50528331.xlsx) généré par celui-ci. La capture d'écran montre l'effet du code sur le fichier Excel d'exemple lors de l'exécution.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-BringShapeFrontOrBackInWorksheet.py" >}}
{{< app/cells/assistant language="csharp" >}}
