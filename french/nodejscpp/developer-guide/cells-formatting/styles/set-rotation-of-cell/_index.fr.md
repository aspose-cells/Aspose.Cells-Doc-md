---  
title: Comment faire pivoter le texte de la cellule
linktitle: Comment faire pivoter le texte de la cellule  
type: docs  
weight: 80  
url: /fr/nodejs-cpp/how-to-rotate-text-of-cell/  
description: Apprenez comment faire pivoter le texte d une cellule de manière programmatique avec Aspose.Cells for Node.js via C++.  
keywords: node.js faire pivoter le texte de Cell, faire pivoter le texte de Cell dans un classeur de manière programmatique, définir l angle de rotation de la cellule dans le classeur, comment faire pivoter du texte dans Excel avec node.js  
---  

## ** Rotation du texte de la cellule dans Aspose.Cells for Node.js via C++**

Aspose.Cells est un composant puissant pour Node.js qui permet aux développeurs de travailler avec des feuilles de calcul Excel de manière programmatique. L'une des fonctionnalités proposées par Aspose.Cells est la rotation des cellules, permettant de personnaliser l'orientation du texte et d'améliorer la présentation visuelle de vos données. Dans ce document, nous explorerons comment faire pivoter des cellules avec Aspose.Cells.

## **Comment faire pivoter le texte d'une cellule dans Excel**
Pour faire pivoter une cellule dans Excel, vous pouvez suivre les étapes suivantes :
1. Ouvrez Excel et sélectionnez la cellule ou la plage de cellules que vous souhaitez faire pivoter.
1. Cliquez avec le bouton droit sur la(des) cellule(s) sélectionnée(s) et choisissez "Format de cellule" dans le menu contextuel. Vous pouvez également accéder à l'onglet "Accueil" dans le ruban Excel, cliquer sur le menu déroulant "Format" dans le groupe "Cellules" et sélectionner "Format de cellule".
1. Dans la boîte de dialogue "Format de cellule", accédez à l'onglet "Alignement".
1. Sous la section "Orientation", vous verrez les options pour faire pivoter le texte. Vous pouvez directement saisir l'angle de rotation souhaité en degrés dans la zone "Degrés". Les valeurs positives font pivoter le texte dans le sens inverse des aiguilles d'une montre, et les valeurs négatives le font pivoter dans le sens des aiguilles d'une montre.
<br>
![todo:image_alt_text](alignment.png)
1. Une fois que vous avez sélectionné la rotation souhaitée, cliquez sur "OK" pour appliquer les modifications. La(des) cellule(s) sélectionnée(s) sera(seront) maintenant pivotée(s) en fonction de l'angle de rotation ou de l'orientation choisi(e).

## **Comment faire pivoter le texte d'une cellule en utilisant l'API Aspose.Cells**

La propriété [**Style.setRotationAngle(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setRotationAngle-number-) facilite la rotation des cellules. Pour faire pivoter les cellules dans Aspose.Cells, vous devez suivre ces étapes :
1. Charger le classeur Excel  
<br>
Tout d'abord, vous devez charger le classeur Excel en utilisant Aspose.Cells. Vous pouvez utiliser la classe Workbook pour ouvrir un fichier Excel existant ou en créer un nouveau. 

1. Accéder à la feuille de calcul  
<br>
Une fois le classeur chargé, vous devez accéder à la feuille de calcul où vous souhaitez faire pivoter les cellules. Vous pouvez accéder à la feuille de calcul soit par son index, soit par son nom. 

1. Faire pivoter le texte de la cellule  
<br>
Maintenant que vous avez accès à la feuille de calcul, vous pouvez faire pivoter les cellules en modifiant l'objet Style des cellules désirées. L'objet Style vous permet de définir diverses options de mise en forme, y compris la rotation. 

1. Enregistrer le classeur  
<br>
Après avoir fait pivoter les cellules, vous pouvez enregistrer le classeur modifié dans un fichier ou un flux en utilisant la méthode Save.

## **Code d'exemple Node.js**

Veuillez voir le code suivant, il crée un objet classeur et définit différents angles de rotation pour plusieurs cellules. La capture d'écran montre le résultat après l'exécution de l'exemple.
<br>
<img src="rotation.png" width=80% />

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-SetRotationOfCell.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
