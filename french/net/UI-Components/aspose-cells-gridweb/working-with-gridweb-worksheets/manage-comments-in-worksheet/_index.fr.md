---
title: Gérer les commentaires dans la feuille de calcul
type: docs
weight: 110
url: /fr/net/manage-comments-in-worksheet/
---
{{% alert color="primary" %}} 

Cette rubrique traite de l'ajout, de l'accès et de la suppression de commentaires dans les feuilles de calcul. Les commentaires sont utiles pour ajouter des notes ou des informations utiles aux utilisateurs qui travailleront avec la feuille. Les développeurs ont la possibilité d'ajouter des commentaires à n'importe quelle cellule de la feuille de calcul.

{{% /alert %}} 
## **Travailler avec des commentaires**
### **Ajouter des commentaires**
Pour ajouter un commentaire à la feuille de calcul, veuillez suivre les étapes ci-dessous :

1. Ajoutez le contrôle Aspose.Cells.GridWeb au formulaire Web.
1. Accédez à la feuille de calcul à laquelle vous ajoutez des commentaires.
1. Ajouter un commentaire à une cellule.
1. Définissez une note pour le nouveau commentaire.

**Un commentaire a été ajouté à la feuille de calcul** 

![tâche : image_autre_texte](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **Accéder aux commentaires**
Pour accéder à un commentaire :

1. Accédez à la cellule qui contient le commentaire.
1. Obtenez la référence de la cellule.
1. Transmettez la référence à la collection Comment pour accéder au commentaire.
1. Il est maintenant possible de modifier les propriétés du commentaire.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **Suppression de commentaires**
Pour supprimer un commentaire :

1. Accédez à la cellule comme expliqué ci-dessus.
1. Utilisez la méthode RemoveAt de la collection Comment pour supprimer le commentaire.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
