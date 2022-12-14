---
title: Gestion des hyperliens dans une feuille de calcul
type: docs
weight: 90
url: /fr/net/managing-hyperlinks-in-a-worksheet/
---
{{% alert color="primary" %}} 

En utilisant Aspose.Cells.GridDesktop, il est également possible d'ajouter des hyperliens vers des valeurs simples stockées dans les cellules d'une feuille de calcul. Disons que dans certaines cellules, vous pourriez avoir des valeurs que vous aimeriez lier avec des informations plus détaillées sur une page Web. Dans ce cas, il serait souhaitable d'ajouter un lien hypertexte à cette cellule afin que si un utilisateur clique sur la cellule, il soit dirigé vers cette page Web. Dans cette rubrique, nous expliquerons comment les développeurs peuvent ajouter et manipuler des liens hypertexte dans leurs feuilles de calcul.

{{% /alert %}} 
## **Ajout d'hyperliens**
Pour ajouter un lien hypertexte vers une cellule à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

-  Ajoutez le contrôle Aspose.Cells.GridDesktop à votre**Formulaire**
-  Accédez à tout**Feuille de travail**
-  Accéder à un**Cell** dans la feuille de travail qui sera hyperliée
- Ajoutez de la valeur à la cellule à créer un lien hypertexte
-  Ajouter**Lien hypertexte** à la feuille de calcul en précisant le nom de la cellule sur laquelle le lien hypertexte serait appliqué

**Hyperliens** collecte dans le**Feuille de travail** l'objet fournit une surcharge**Ajouter** méthode. Les développeurs peuvent utiliser n'importe quelle version surchargée de**Ajouter** méthode en fonction de leurs besoins spécifiques.

 Le code ci-dessous ajoutera un lien hypertexte vers**B2** et**C3** cellules de la feuille de calcul.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **Accéder aux hyperliens**
Une fois qu'un lien hypertexte sera ajouté à une cellule, il peut également être nécessaire d'accéder et de modifier le lien hypertexte lors de l'exécution. Pour ce faire, les développeurs peuvent simplement accéder au lien hypertexte depuis le**Hyperliens** collecte de la**Feuille de travail** en spécifiant la cellule (en utilisant le nom de la cellule ou son emplacement en termes de numéro de ligne et de colonne) à laquelle le lien hypertexte est ajouté. Une fois le lien hypertexte accessible, les développeurs peuvent modifier son URL lors de l'exécution.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **Suppression des hyperliens**
 Pour supprimer un lien hypertexte existant, les développeurs peuvent simplement accéder à une feuille de calcul souhaitée, puis**Retirer** lien hypertexte du**Hyperliens** collecte de la**Feuille de travail** en spécifiant la cellule hyperliée (en utilisant son nom ou son numéro de ligne et de colonne).



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

Si vous souhaitez ajouter un lien hypertexte à une cellule et que vous souhaitez afficher l'URL du lien hypertexte dans la cellule au lieu d'une valeur, n'ajoutez aucune valeur à la cellule et ajoutez simplement le lien hypertexte à cette cellule. Ce faisant, la cellule sera liée par un hyperlien et l'URL du lien hypertexte sera également affichée dans la cellule en tant que valeur.

{{% /alert %}}
