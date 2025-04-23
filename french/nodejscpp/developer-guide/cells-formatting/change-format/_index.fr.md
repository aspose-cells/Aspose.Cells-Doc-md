---
title: Modifier le format d une cellule
linktitle: Modifier le format d une cellule
description: Comment utiliser la bibliothèque Aspose.Cells dans Node.js via C++ pour changer la mise en forme des cellules, y compris la police, la couleur, la bordure, etc. En ajustant ces propriétés, vous avez plus de contrôle sur l apparence des cellules.
keywords: Aspose.Cells, mise en forme des cellules, Node.js via C++, police, couleur, bordure
type: docs
weight: 20
url: /fr/nodejs-cpp/how-to-change-format-of-cell/
---

## **Scénarios d'utilisation possibles**
Lorsque vous voulez mettre en évidence certaines données, vous pouvez changer le style des cellules.

## **Comment changer le format d'une cellule dans Excel**

Pour changer le format d'une seule cellule dans Excel, suivez ces étapes :

1. Ouvrez Excel et ouvrez le classeur contenant la cellule que vous souhaitez formater.

2. Repérez la cellule que vous voulez formater.

3. Cliquez avec le bouton droit sur la cellule et sélectionnez "Format de cellule" dans le menu contextuel. Vous pouvez également sélectionner la cellule, vous rendre à l'onglet Accueil dans le ruban Excel, cliquer sur le menu déroulant "Format" dans le groupe "Cellules", et sélectionner "Format de cellules".

4. La boîte de dialogue "Format de cellules" apparaîtra. Ici, vous pouvez choisir diverses options de mise en forme à appliquer à la cellule sélectionnée. Par exemple, vous pouvez modifier le style de police, la taille de police, la couleur de police, le format de nombre, les bordures, la couleur de fond, etc. Explorez les différents onglets de la boîte de dialogue pour accéder à diverses options de mise en forme.

5. Après avoir apporté les modifications de mise en forme souhaitées, cliquez sur le bouton "OK" pour appliquer la mise en forme à la cellule sélectionnée.


## **Comment changer le format d'une cellule en utilisant Node.js**

Pour changer le format d'une cellule en utilisant Aspose.Cells, vous pouvez utiliser les méthodes suivantes :
1. [Cell.setStyle(Style)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)
2. [Cell.setStyle(Style, explicitFlag)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-boolean-)
3. [Cell.setStyle(Style, StyleFlag)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-styleflag-)


## **Code d'exemple**
Dans cet exemple, nous créons un classeur Excel, ajoutons des données d'exemple, accédons à la première feuille de calcul, et obtenons deux cellules ("A2" et "B3"). Ensuite, nous récupérons le style de la cellule, définissons diverses options de mise en forme (par exemple, couleur de police, gras), et changeons le format de la cellule. Enfin, nous enregistrons le classeur dans un nouveau fichier.
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ChangeFormat.js" >}}
