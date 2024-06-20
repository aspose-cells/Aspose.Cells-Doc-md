---
title: Commentaires en fil
type: docs
weight: 140
url: /fr/net/threaded-comments/
---

## **Commentaires en fil**

MS Excel 365 offre la possibilité d'ajouter des commentaires en fil. Ces commentaires fonctionnent comme des conversations et peuvent être utilisés pour des discussions. Les commentaires sont maintenant dotés d'une boîte de réponse qui permet des conversations en fil. Les anciens commentaires sont appelés Notes dans Excel 365. La capture d'écran ci-dessous montre comment les commentaires en fil sont affichés lorsqu'ils sont ouverts dans Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

Les commentaires en fil sont affichés comme ceci dans les anciennes versions d'Excel. Les images suivantes ont été prises en ouvrant le fichier d'exemple dans Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells fournit également la fonctionnalité pour gérer les commentaires en fil.

## **Ajouter des commentaires en fil**

### **Ajouter un commentaire en fil avec Excel**

Pour ajouter des commentaires enfilés dans Excel 365, suivez les étapes suivantes.

- Méthode 1
  - Cliquez sur l'onglet **Révision**
  - Cliquez sur le bouton **Nouveau commentaire**
  - Cela ouvrira une boîte de dialogue pour saisir des commentaires dans la cellule active.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Méthode 2
  - Cliquez avec le bouton droit sur la cellule où vous souhaitez insérer le commentaire.
  - Cliquez sur l'option **Nouveau commentaire**
  - Cela ouvrira une boîte de dialogue pour saisir des commentaires dans la cellule active.
  - ![todo:image_alt_text](threaded-comments_5)

### **Ajouter un commentaire enfilé à l'aide d'Aspose.Cells**

Aspose.Cells fournit la méthode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) pour ajouter des commentaires enfilés. La méthode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) accepte les trois paramètres suivants.

- Nom de la cellule : Le nom de la cellule où le commentaire sera inséré.
- Texte du commentaire : Le texte du commentaire.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthor) : L'auteur du commentaire

L'exemple de code suivant démontre l'utilisation de la méthode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) pour ajouter un commentaire enfilé à la cellule A1. Veuillez consulter le fichier Excel de sortie (89849859.xlsx) généré par le code pour référence.

#### **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}

## **Lire les Commentaires enfilés**

### **Lire des commentaires enfilés avec Excel**

Pour lire des commentaires enfilés dans Excel, survolez simplement la cellule contenant les commentaires pour les afficher. La vue des commentaires ressemblera à la vue dans l'image suivante.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Lire des commentaires enfilés à l'aide d'Aspose.Cells**

Aspose.Cells fournit la méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) pour récupérer les commentaires en fil pour la colonne spécifiée. La méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) accepte le nom de colonne en tant que paramètre et retourne le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Vous pouvez itérer sur le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) pour afficher les commentaires.

L'exemple suivant démontre la lecture des commentaires de la colonne A1 en chargeant le [Fichier Excel d'exemple](89849861.xlsx). Veuillez consulter la sortie de la console générée par le code pour référence.

#### **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}

#### **Sortie console**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Lire l'heure de création des commentaires en fil**

Aspose.Cells fournit la méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) pour récupérer les commentaires en fil pour la colonne spécifiée. La méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) accepte le nom de colonne en tant que paramètre et retourne le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Vous pouvez itérer sur le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) et utiliser la propriété [**ThreadedComment.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/threadedcomment/properties/createdtime).

L'exemple suivant démontre la lecture de l'heure de création des commentaires en fil en chargeant le [Fichier Excel d'exemple](89849861.xlsx). Veuillez consulter la sortie de la console générée par le code pour référence.

#### **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}

#### **Sortie console**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **Modifier les commentaires en fil**

### **Modifier le commentaire en fil avec Excel**

Pour modifier un commentaire en fil dans Excel, cliquez sur le lien **Modifier** sur le commentaire comme indiqué dans l'image suivante.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Modifier le commentaire en fil en utilisant Aspose.Cells**

Aspose.Cells fournit la méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) pour récupérer les commentaires en fil pour la colonne spécifiée. La méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) accepte le nom de colonne en tant que paramètre et retourne le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Vous pouvez mettre à jour le commentaire requis dans le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) et enregistrer le classeur.

L'exemple suivant démontre l'édition du premier commentaire en fil dans la colonne A1 en chargeant le [Fichier Excel d'exemple](89849861.xlsx). Veuillez consulter le [fichier Excel de sortie](89849862.xlsx) généré par le code montrant le commentaire mis à jour pour référence.

#### **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}

## **Supprimer les commentaires en filigrane**

### **Supprimer les commentaires en filigrane avec Excel**

Pour supprimer les commentaires en filigrane dans Excel, cliquez avec le bouton droit sur la cellule contenant les commentaires et cliquez sur l'option **Supprimer le commentaire** comme indiqué dans l'image suivante.

![todo:image_alt_text](threaded-comments_8.jpg)

### **Supprimer les commentaires en filigrane à l'aide de Aspose.Cells**

Aspose.Cells fournit la méthode [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) pour supprimer les commentaires de la colonne spécifiée. La méthode [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) accepte le nom de la colonne en paramètre pour supprimer les commentaires dans cette colonne.

L'exemple suivant montre comment supprimer les commentaires dans la colonne A1 en chargeant le [fichier Excel d'exemple](89849861.xlsx). Veuillez consulter le [fichier Excel de sortie](89849864.xlsx) généré par le code pour référence.

#### **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}}

Veuillez noter qu'en supprimant le commentaire avec Aspose.Cells, l'auteur n'est pas automatiquement supprimé. Si vous devez également supprimer l'auteur, veuillez utiliser la méthode RemoveAt de la classe [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthorcollection) comme indiqué dans l'exemple ci-dessus.

{{% /alert %}}
