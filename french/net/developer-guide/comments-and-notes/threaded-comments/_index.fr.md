---
title: Commentaires filetés
type: docs
weight: 140
url: /fr/net/threaded-comments/
---
## **Commentaires filetés**

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
 - Clique le**Passer en revue** Languette
 - Clique le**Nouveau commentaire** bouton
 - Cela ouvrira une boîte de dialogue pour entrer des commentaires dans la cellule active.
  - ![tâche : image_autre_texte](threaded-comments_4.jpg)
- Méthode 2
 - Faites un clic droit sur la cellule où vous souhaitez insérer le commentaire.
 - Clique le**Nouveau commentaire** option.
 - Cela ouvrira une boîte de dialogue pour entrer des commentaires dans la cellule active.
  - ![tâche : image_autre_texte](threaded-comments_5)

### **Ajouter un commentaire fileté en utilisant Aspose.Cells**

Aspose.Cells fournit[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) méthode pour ajouter des commentaires thématiques.[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)La méthode accepte les trois paramètres suivants.

- Cell Nom : Le nom de la cellule où le commentaire sera inséré.
- Texte du commentaire : le texte du commentaire.
- [**ThreadedCommentAuteur**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthor): L'auteur du commentaire

L'exemple de code suivant illustre l'utilisation de[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)méthode pour ajouter un commentaire fileté à la cellule A1. Veuillez consulter le[fichier Excel de sortie](89849859.xlsx) généré par le code pour référence.

#### **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}

## **Lire les commentaires filetés**

### **Lire les commentaires filetés avec Excel**

Pour lire les commentaires filetés dans Excel, passez simplement votre souris sur la cellule contenant les commentaires pour afficher les commentaires. La vue des commentaires ressemblera à la vue de l'image suivante.

![tâche : image_autre_texte](threaded-comments_1.jpg)

### **Lire les commentaires filetés en utilisant Aspose.Cells**

Aspose.Cells fournit[**Commentaires.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)méthode pour récupérer les commentaires filetés pour la colonne spécifiée.[**Commentaires.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)La méthode accepte le nom de la colonne comme paramètre et renvoie le[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Vous pouvez itérer sur le[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)pour voir les commentaires.

L'exemple suivant illustre la lecture des commentaires de la colonne A1 en chargeant le[exemple de fichier Excel](89849861.xlsx). Veuillez consulter la sortie de la console générée par le code pour référence.

#### **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}

#### **Sortie console**

Commentaire : testez le commentaire fileté

Auteur : Aspose

### **Lire l'heure de création des commentaires filetés**

Aspose.Cells fournit[**Commentaires.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)méthode pour récupérer les commentaires filetés pour la colonne spécifiée.[**Commentaires.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)La méthode accepte le nom de la colonne comme paramètre et renvoie le[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Vous pouvez itérer sur le[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) et utiliser le[**ThreadedComment.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/threadedcomment/properties/createdtime) la propriété.

L'exemple suivant illustre la lecture de l'heure de création des commentaires thématiques en chargeant le[exemple de fichier Excel](89849861.xlsx). Veuillez consulter la sortie de la console générée par le code pour référence.

#### **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}

#### **Sortie console**

Commentaire : testez le commentaire fileté

Auteur : Aspose

Heure de création : 15/05/2019 12:46:23

## **Modifier les commentaires liés**

### **Modifier le commentaire fileté avec Excel**

 Pour modifier un commentaire fileté dans Excel, cliquez sur le**Éditer** lien sur le commentaire comme indiqué dans l'image suivante.

![tâche : image_autre_texte](threaded-comments_7.jpg)

### **Modifier le commentaire fileté en utilisant Aspose.Cells**

Aspose.Cells fournit[**Commentaires.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) méthode pour récupérer les commentaires filetés pour la colonne spécifiée.[**Commentaires.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)La méthode accepte le nom de la colonne comme paramètre et renvoie le[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Vous pouvez mettre à jour le commentaire requis dans le[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)et enregistrez le classeur.

L'exemple suivant illustre la modification du premier commentaire fileté dans la colonne A1 en chargeant le[exemple de fichier Excel](89849861.xlsx). Veuillez consulter le[fichier Excel de sortie](89849862.xlsx)généré par le code affichant le commentaire mis à jour pour référence.

#### **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}

## **Supprimer les commentaires filetés**

### **Supprimer les commentaires filetés avec Excel**

 Pour supprimer les commentaires filetés dans Excel, faites un clic droit sur la cellule contenant les commentaires et cliquez sur le**Supprimer le commentaire** comme indiqué dans l'image suivante.

![tâche : image_autre_texte](threaded-comments_8.jpg)

### **Supprimer les commentaires filetés en utilisant Aspose.Cells**

Aspose.Cells fournit[**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index)méthode pour supprimer les commentaires de la colonne spécifiée.[**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index)La méthode accepte le nom de la colonne en tant que paramètre supprime les commentaires de cette colonne.

L'exemple suivant illustre la suppression de commentaires dans la colonne A1 en chargeant le[exemple de fichier Excel](89849861.xlsx). Veuillez consulter le[fichier Excel de sortie](89849864.xlsx)généré par le code pour référence.

#### **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}}

 Veuillez noter qu'en supprimant le commentaire avec Aspose.Cells, l'auteur n'est pas supprimé automatiquement. Si vous devez également supprimer l'auteur, veuillez utiliser la méthode RemoveAt de[**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthorcollection) classe comme indiqué dans l'exemple ci-dessus.

{{% /alert %}}
