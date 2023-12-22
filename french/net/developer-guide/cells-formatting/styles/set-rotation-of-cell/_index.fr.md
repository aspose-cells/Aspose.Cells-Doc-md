---
title: Comment faire pivoter le texte de Cell
type: docs
weight: 80
url: /fr/net/how-to-rotate-text-of-cell/
description: Code C# pour faire pivoter le texte de Cell avec Aspose.Cells for .NET API
keywords: c# rotate text of Cell, c# programmatically rotate text of Cell in workbook, programmatically set cell rotation angle in workbook, c# how to rotate text of Cell in excel
---
##  **Faire pivoter le texte de Cell en Aspose.Cells**

Aspose.Cells est un puissant composant .NET et Java qui permet aux développeurs de travailler avec des feuilles de calcul Excel par programmation. L'une des fonctionnalités fournies par Aspose.Cells est la possibilité de faire pivoter les cellules, vous permettant de personnaliser l'orientation du texte et d'améliorer la présentation visuelle de vos données. Dans ce document, nous explorerons comment faire pivoter les cellules à l'aide de Aspose.Cells.

##  **Comment faire pivoter le texte de Cell dans Excel**
Pour faire pivoter une cellule dans Excel, vous pouvez suivre les étapes suivantes :
1. Ouvrez Excel et sélectionnez la cellule ou la plage de cellules que vous souhaitez faire pivoter.
1. Faites un clic droit sur la ou les cellules sélectionnées et choisissez "Format Cells" dans le menu contextuel. Alternativement, vous pouvez accéder à l'onglet « Accueil » du ruban Excel, cliquer sur la liste déroulante « Format » dans le groupe « Cells » et sélectionner « Formater Cells ».
1. Dans la boîte de dialogue "Format Cells", accédez à l'onglet "Alignement".
1. Sous la section "Orientation", vous verrez les options pour faire pivoter le texte. Vous pouvez saisir directement l'angle de rotation souhaité en degrés dans la case "Degrés". Les valeurs positives font pivoter le texte dans le sens inverse des aiguilles d'une montre et les valeurs négatives le font pivoter dans le sens des aiguilles d'une montre.
<br>
![tâche : image_alt_text](alignment.png)
1. Une fois que vous avez sélectionné la rotation souhaitée, cliquez sur « OK » pour appliquer les modifications. La ou les cellules sélectionnées seront désormais pivotées en fonction de l'angle de rotation ou de l'orientation choisis.

##  **Comment faire pivoter le texte de Cell en utilisant Aspose.Cells API**

[**Style.RotationAngle**](https://reference.aspose.com/cells/net/aspose.cells/style/rotationangle/) La propriété facilite la rotation des cellules. Pour faire pivoter les cellules dans Aspose.Cells, vous devez suivre ces étapes :
1. Charger le classeur Excel
<br>
 Tout d’abord, vous devez charger le classeur Excel à l’aide de Aspose.Cells. Vous pouvez utiliser la classe Workbook pour ouvrir un fichier Excel existant ou en créer un nouveau.

1. Accéder à la feuille de travail
<br>
Une fois le classeur chargé, vous devez accéder à la feuille de calcul dans laquelle vous souhaitez faire pivoter les cellules. Vous pouvez accéder à la feuille de calcul par son index ou son nom.

1. Faire pivoter le texte du Cell
<br>
 Maintenant que vous avez accès à la feuille de calcul, vous pouvez faire pivoter les cellules en modifiant l'objet Style des cellules souhaitées. L'objet Style vous permet de définir diverses options de formatage, notamment la rotation.

1. Enregistrer le classeur
<br>
Après avoir fait pivoter les cellules, vous pouvez enregistrer le classeur modifié dans un fichier ou un flux à l'aide de la méthode Save.

##  **C# Exemple de code**

Veuillez consulter le code suivant, il crée un objet classeur et définit différents angles de rotation pour plusieurs cellules. La capture d'écran montre le résultat après l'exécution de l'exemple de code.
<br>
<img src="rotation.png" width=80% />



{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-rotate-text.cs" >}}
