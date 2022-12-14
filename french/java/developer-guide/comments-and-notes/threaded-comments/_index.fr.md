---
title: Commentaires filetés
type: docs
weight: 140
url: /fr/java/threaded-comments/
---
# **Commentaires filetés**
MS Excel 365 fournit une fonctionnalité pour ajouter des commentaires filetés. Ces commentaires fonctionnent comme des conversations et peuvent être utilisés pour des discussions. Les commentaires sont désormais accompagnés d'une boîte de réponse qui permet des conversations en fil de discussion. Les anciens commentaires sont appelés Notes dans Excel 365. La capture d'écran ci-dessous montre comment les commentaires thématiques sont affichés lorsqu'ils sont ouverts dans Excel.

![tâche : image_autre_texte](threaded-comments_1.jpg)

Les commentaires filetés sont affichés comme ceci dans les anciennes versions d'Excel. Les images suivantes ont été prises en ouvrant le fichier d'exemple dans Excel 2016.

![tâche : image_autre_texte](threaded-comments_2.jpg)



![tâche : image_autre_texte](threaded-comments_3.jpg)



Aspose.Cells fournit également la fonctionnalité de gestion des commentaires filetés.
## **Ajouter des commentaires filetés**
### **Ajouter un commentaire fileté avec Excel**
Pour ajouter des commentaires filetés dans Excel 365, procédez comme suit.

- Méthode 1
 - Clique le**Examen**Languette
 - Clique le**Nouveau commentaire**bouton
 - Cela ouvrira une boîte de dialogue pour entrer des commentaires dans la cellule active.
  - ![tâche : image_autre_texte](threaded-comments_4.jpg)
- Méthode 2
 - Faites un clic droit sur la cellule où vous souhaitez insérer le commentaire.
 - Clique le**Nouveau commentaire**option.
 - Cela ouvrira une boîte de dialogue pour entrer des commentaires dans la cellule active.
  - ![tâche : image_autre_texte](threaded-comments_5)
### **Ajouter un commentaire fileté en utilisant Aspose.Cells**
Aspose.Cells fournit[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) pour ajouter des commentaires thématiques.[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) accepte les trois paramètres suivants.

- Cell Nom : Le nom de la cellule où le commentaire sera inséré.
- Texte du commentaire : le texte du commentaire.
- [ThreadedCommentAuteur](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor): L'auteur du commentaire

L'exemple de code suivant illustre l'utilisation de[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) méthode pour ajouter un commentaire fileté à la cellule A1. Veuillez consulter le[fichier Excel de sortie](AddThreadedComments_out.xlsx)généré par le code pour référence.
#### **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **Lire les commentaires filetés**
### **Lire les commentaires filetés avec Excel**
Pour lire les commentaires filetés dans Excel, passez simplement votre souris sur la cellule contenant les commentaires pour afficher les commentaires. La vue des commentaires ressemblera à la vue de l'image suivante.

![tâche : image_autre_texte](threaded-comments_1.jpg)
### **Lire les commentaires filetés en utilisant Aspose.Cells**
Aspose.Cells fournit[Commentaires.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) pour récupérer les commentaires thématiques pour la colonne spécifiée.[Commentaires.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) accepte le nom de la colonne comme paramètre et renvoie le[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Vous pouvez itérer sur le[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)pour voir les commentaires.

L'exemple suivant illustre la lecture des commentaires de la colonne A1 en chargeant le[exemple de fichier Excel](ThreadedCommentsSample.xlsx). Veuillez consulter la sortie de la console générée par le code pour référence.
#### **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **Sortie console**
Commentaire : testez le commentaire fileté

Auteur : Aspose
### **Lire l'heure de création des commentaires filetés**
Aspose.Cells fournit[Commentaires.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) pour récupérer les commentaires thématiques pour la colonne spécifiée.[Commentaires.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) accepte le nom de la colonne comme paramètre et renvoie le[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Vous pouvez itérer sur le[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)et utiliser le[ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime)propriété.

L'exemple suivant illustre la lecture de l'heure de création des commentaires thématiques en chargeant le[exemple de fichier Excel](ThreadedCommentsSample.xlsx). Veuillez consulter la sortie de la console générée par le code pour référence.
#### **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **Sortie console**
Commentaire : testez le commentaire fileté

Auteur : Aspose

Heure de création : 2019-05-15T12:46:23
## **Modifier les commentaires liés**
### **Modifier le commentaire fileté avec Excel**
Pour modifier un commentaire fileté dans Excel, cliquez sur le**Éditer**lien sur le commentaire comme indiqué dans l'image suivante.

![tâche : image_autre_texte](threaded-comments_7.jpg)
### **Modifier le commentaire fileté en utilisant Aspose.Cells**
Aspose.Cells fournit[Commentaires.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) pour récupérer les commentaires thématiques pour la colonne spécifiée.[Commentaires.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) accepte le nom de la colonne comme paramètre et renvoie le[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Vous pouvez mettre à jour le commentaire requis dans le[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)et enregistrez le classeur.

L'exemple suivant illustre la modification du premier commentaire fileté dans la colonne A1 en chargeant le[exemple de fichier Excel](ThreadedCommentsSample.xlsx). Veuillez consulter le[fichier Excel de sortie](EditThreadedComments.xlsx)généré par le code affichant le commentaire mis à jour pour référence.
#### **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **Supprimer les commentaires filetés**
### **Supprimer les commentaires filetés avec Excel**
Pour supprimer les commentaires filetés dans Excel, faites un clic droit sur la cellule contenant les commentaires et cliquez sur le**Supprimer le commentaire**comme indiqué dans l'image suivante.

![tâche : image_autre_texte](threaded-comments_8.jpg)
### **Supprimer les commentaires filetés en utilisant Aspose.Cells**
Aspose.Cells fournit[Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) pour supprimer les commentaires de la colonne spécifiée.[Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) accepte le nom de la colonne en tant que paramètre supprime les commentaires dans cette colonne.

L'exemple suivant illustre la suppression de commentaires dans la colonne A1 en chargeant le[exemple de fichier Excel](ThreadedCommentsSample.xlsx). Veuillez consulter le[fichier Excel de sortie](ThreadedCommentsSample_Out.xlsx)généré par le code pour référence.
#### **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

 Veuillez noter qu'en supprimant le commentaire avec Aspose.Cells, l'auteur n'est pas supprimé automatiquement. Si vous devez également supprimer l'auteur, veuillez utiliser le[ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt\(int\)) méthode comme indiqué dans l'exemple ci-dessus.

{{% /alert %}}
