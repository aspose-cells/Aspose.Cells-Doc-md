---
title: Gestion des commentaires dans une feuille de calcul
type: docs
weight: 110
url: /fr/net/aspose-cells-griddesktop/manage-comments-in-a-worksheet/
keywords: GridDesktop, commentaire, commentaires
description: Cet article présente comment travailler avec les commentaires dans GridDesktop.
---

{{% alert color="primary" %}} 

Dans MS Excel, vous devez être familier avec la fonctionnalité des commentaires qui permet aux utilisateurs d'ajouter des commentaires aux cellules. Cette fonctionnalité est utile dans les cas où il est nécessaire de fournir des informations aux utilisateurs lorsqu'ils s'apprêtent à saisir des valeurs dans les cellules. Chaque fois qu'un utilisateur place son curseur de souris sur une cellule commentée, un petit message contextuel apparaît pour fournir des informations à l'utilisateur. En utilisant Aspose.Cells.GridDesktop, les développeurs peuvent créer des commentaires sur des cellules. Dans ce sujet, nous expliquerons en détail l'utilisation de cette fonctionnalité.

{{% /alert %}} 
## **Ajout de commentaires**
Pour ajouter un commentaire à une cellule en utilisant Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

- Ajoutez le contrôle Aspose.Cells.GridDesktop à votre **Form**
- Accédez à n'importe quelle **Worksheet** souhaitée
- Ajouter un **Commentaire** à la feuille de calcul en spécifiant la cellule (en utilisant son nom ou son numéro de ligne et de colonne) dans laquelle le commentaire serait ajouté.

Le code ci-dessous ajoutera des commentaires aux cellules **b2** et **b4** de la feuille de calcul.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


La collection **Comments** dans l'objet **Worksheet** fournit une méthode **Add** surchargée. Les développeurs peuvent utiliser n'importe quelle version surchargée de la méthode **Add** selon leurs besoins spécifiques.
## **Accéder aux commentaires**
Pour accéder et modifier un commentaire existant dans la feuille de calcul, les développeurs peuvent accéder au commentaire à partir de la collection **Comments** de la **Worksheet** en spécifiant la cellule (en utilisant le nom de la cellule ou son emplacement en termes de numéros de ligne et de colonne) dans laquelle le commentaire est inséré. Une fois le commentaire accessible, les développeurs peuvent modifier son texte à l'exécution.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **Supprimer les Commentaires**
Pour supprimer un commentaire existant, les développeurs peuvent simplement accéder à une feuille de calcul souhaitée et ensuite **supprimer** le commentaire de la collection **Comments** de la **Worksheet** en spécifiant la cellule (en utilisant son nom ou son numéro de ligne et de colonne) contenant le commentaire.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
