---
title: Gérer les commentaires dans la feuille de calcul
type: docs
weight: 110
url: /fr/net/aspose-cells-gridweb/manage-comment-in-worksheet/
keywords: GridWeb,comment
description: Cet article présente comment travailler avec les commentaires dans GridWeb.
---

{{% alert color="primary" %}} 

Ce sujet traite de l'ajout, de l'accès et de la suppression de commentaires dans les feuilles de calcul. Les commentaires sont utiles pour ajouter des notes ou des informations utiles aux utilisateurs qui travailleront avec la feuille. Les développeurs ont la flexibilité d'ajouter des commentaires à n'importe quelle cellule de la feuille de calcul.

{{% /alert %}} 
## **Travailler avec des commentaires**
### **Ajout de commentaires**
Pour ajouter un commentaire à la feuille de calcul, veuillez suivre les étapes ci-dessous :

1. Ajoutez le contrôle Aspose.Cells.GridWeb au formulaire Web.
1. Accédez à la feuille de calcul à laquelle vous souhaitez ajouter des commentaires.
1. Ajoutez un commentaire à une cellule.
1. Définissez une note pour le nouveau commentaire.

**Un commentaire a été ajouté à la feuille de calcul** 

![todo:image_alt_text](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **Accéder aux commentaires**
Pour accéder à un commentaire :

1. Accédez à la cellule qui contient le commentaire.
1. Obtenez la référence de la cellule.
1. Passez la référence à la collection de commentaires pour accéder au commentaire.
1. Il est désormais possible de modifier les propriétés du commentaire.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **Supprimer les Commentaires**
Pour supprimer un commentaire :

1. Accédez à la cellule comme expliqué ci-dessus.
1. Utilisez la méthode RemoveAt de la collection Comment pour supprimer le commentaire.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
