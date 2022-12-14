---
title: Gestion des commentaires dans une feuille de calcul
type: docs
weight: 110
url: /fr/net/managing-comments-in-a-worksheet/
---
{{% alert color="primary" %}} 

Dans MS Excel, vous devez être familiarisé avec la fonctionnalité de commentaires qui permet aux utilisateurs d'ajouter des commentaires aux cellules. Cette fonctionnalité est utile dans les cas où il est nécessaire de fournir des informations aux utilisateurs lorsqu'ils sont sur le point d'entrer des valeurs dans les cellules. Chaque fois qu'un utilisateur place le curseur de sa souris sur une cellule commentée, un petit message contextuel apparaît pour fournir des informations à l'utilisateur. En utilisant Aspose.Cells.GridDesktop, les développeurs peuvent créer des commentaires sur les cellules. Dans cette rubrique, nous expliquerons en détail l'utilisation de cette fonctionnalité.

{{% /alert %}} 
## **Ajouter des commentaires**
Pour ajouter un commentaire à une cellule à l'aide de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

-  Ajoutez le contrôle Aspose.Cells.GridDesktop à votre**Formulaire**
-  Accédez à tout**Feuille de travail**
-  Ajouter**Commentaire** à la feuille de calcul en spécifiant la cellule (en utilisant son nom ou son numéro de ligne et de colonne) dans laquelle le commentaire serait ajouté.

 Le code ci-dessous ajoutera des commentaires au**b2** et**b4** cellules de la feuille de calcul.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


**commentaires** collecte dans le**Feuille de travail** l'objet fournit une surcharge**Ajouter** méthode. Les développeurs peuvent utiliser n'importe quelle version surchargée de**Ajouter** méthode en fonction de leurs besoins spécifiques.
## **Accéder aux commentaires**
Pour accéder à un commentaire existant dans la feuille de calcul et le modifier, les développeurs peuvent accéder au commentaire à partir du**commentaires** collecte de la**Feuille de travail** en spécifiant la cellule (en utilisant le nom de la cellule ou son emplacement en termes de numéro de ligne et de colonne) dans laquelle le commentaire est inséré. Une fois le commentaire accessible, les développeurs peuvent modifier son texte au moment de l'exécution.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **Suppression de commentaires**
 Pour supprimer un commentaire existant, les développeurs peuvent simplement accéder à une feuille de calcul souhaitée, puis**Retirer** commentaire de la**commentaires** collecte de la**Feuille de travail** en spécifiant la cellule (en utilisant son nom ou son numéro de ligne et de colonne) contenant le commentaire.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
