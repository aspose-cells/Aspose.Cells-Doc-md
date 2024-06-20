---
title: Gestion des liens hypertexte dans une feuille de calcul
type: docs
weight: 90
url: /fr/net/aspose-cells-griddesktop/manage-hyperlinks-in-a-worksheet/
keywords: GridDesktop,lien hypertexte,hyperlien,hyperlien,hyperliens
description: Cet article présente comment travailler avec un hyperlien dans GridDesktop.
---

{{% alert color="primary" %}} 

En utilisant Aspose.Cells.GridDesktop, il est également possible d'ajouter des hyperliens à des valeurs simples stockées dans des cellules d'une feuille de calcul. Disons que dans certaines cellules, vous pourriez avoir des valeurs que vous aimeriez lier à des informations plus détaillées sur une page web. Dans ce cas, il serait souhaitable d'ajouter un hyperlien à cette cellule afin que si un utilisateur clique sur la cellule, il soit dirigé vers cette page web. Dans ce sujet, nous expliquerons comment les développeurs peuvent ajouter et manipuler des hyperliens dans leurs feuilles de calcul.

{{% /alert %}} 
## **Ajout de liens hypertexte**
Pour ajouter un hyperlien à une cellule à l'aide d'Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

- Ajoutez le contrôle Aspose.Cells.GridDesktop à votre **Form**
- Accédez à n'importe quelle **Worksheet** souhaitée
- Accéder à une **Cellule** désirée dans la feuille de calcul qui sera hyperliée
- Ajouter une valeur à la cellule à hyperlier
- Ajouter un **Hyperlien** à la feuille de calcul en spécifiant le nom de la cellule sur laquelle le lien hypertexte sera appliqué

La collection **Hyperliens** dans l'objet **Feuille de calcul** fournit une méthode **Ajouter** surchargée. Les développeurs peuvent utiliser n'importe quelle version surchargée de la méthode **Ajouter** en fonction de leurs besoins spécifiques.

Le code ci-dessous ajoutera un hyperlien aux cellules **B2** et **C3** de la feuille de calcul.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **Accès aux liens hypertexte**
Une fois qu'un hyperlien aura été ajouté à une cellule, il peut également être nécessaire d'accéder et de modifier l'hyperlien à l'exécution. Pour ce faire, les développeurs peuvent simplement accéder à l'hyperlien à partir de la collection **Hyperliens** de la **Feuille de calcul** en spécifiant la cellule (en utilisant le nom de la cellule ou son emplacement en termes de numéro de ligne et de colonne) auquel l'hyperlien est ajouté. Une fois que l'hyperlien est accessible, les développeurs peuvent modifier son URL à l'exécution.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **Suppression des hyperliens**
Pour supprimer un hyperlien existant, les développeurs peuvent simplement accéder à une feuille de calcul souhaitée, puis **Supprimer** l'hyperlien de la collection **Hyperliens** de la **Feuille de calcul** en spécifiant la cellule hyperliée (en utilisant son nom ou son numéro de ligne et de colonne).



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

Si vous souhaitez ajouter un hyperlien à une cellule et souhaitez afficher l'URL du lien hypertexte dans la cellule au lieu d'une valeur, ne pas ajouter de valeur à la cellule et ajouter simplement le lien hypertexte à cette cellule. En agissant ainsi, la cellule sera hyperliée et l'URL du lien hypertexte sera également affichée dans la cellule en tant que valeur.

{{% /alert %}}
