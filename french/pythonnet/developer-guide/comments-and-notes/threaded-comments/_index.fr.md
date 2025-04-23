---
title: Commentaires en fil
type: docs
weight: 140
url: /fr/python-net/threaded-comments/
---

## **Commentaires en fil**

MS Excel 365 offre la possibilité d'ajouter des commentaires en fil. Ces commentaires fonctionnent comme des conversations et peuvent être utilisés pour des discussions. Les commentaires sont maintenant dotés d'une boîte de réponse qui permet des conversations en fil. Les anciens commentaires sont appelés Notes dans Excel 365. La capture d'écran ci-dessous montre comment les commentaires en fil sont affichés lorsqu'ils sont ouverts dans Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

Les commentaires en fil sont affichés comme ceci dans les anciennes versions d'Excel. Les images suivantes ont été prises en ouvrant le fichier d'exemple dans Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells pour Python via .NET offre également la possibilité de gérer les commentaires en fil de discussion.

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

### **Ajouter un commentaire en fil de discussion avec Aspose.Cells pour Python via .NET**

Aspose.Cells pour Python via .NET fournit la méthode [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment/) pour ajouter des commentaires en fil de discussion. La méthode [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment) accepte les trois paramètres suivants.

- Nom de la cellule : Le nom de la cellule où le commentaire sera inséré.
- Texte du commentaire : Le texte du commentaire.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentauthor) : L'auteur du commentaire

L'exemple de code suivant démontre l'utilisation de la méthode [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment) pour ajouter un commentaire enfilé à la cellule A1. Veuillez consulter le fichier Excel de sortie (89849859.xlsx) généré par le code pour référence.

#### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-AddThreadedComments-1.py" >}}

## **Lire les Commentaires enfilés**

### **Lire des commentaires enfilés avec Excel**

Pour lire des commentaires enfilés dans Excel, survolez simplement la cellule contenant les commentaires pour les afficher. La vue des commentaires ressemblera à la vue dans l'image suivante.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Lire les commentaires en fil de discussion avec Aspose.Cells pour Python via .NET**

Aspose.Cells pour Python via .NET offre la méthode [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) pour récupérer les commentaires en fil de discussion pour la colonne spécifiée. La méthode [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) accepte le nom de la colonne en paramètre et retourne le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). Vous pouvez parcourir le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) pour voir les commentaires.

L'exemple suivant démontre la lecture des commentaires de la colonne A1 en chargeant le [Fichier Excel d'exemple](89849861.xlsx). Veuillez consulter la sortie de la console générée par le code pour référence.

#### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedComments-1.py" >}}

#### **Sortie console**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Lire l'heure de création des commentaires en fil**

Aspose.Cells pour Python via .NET fournit la méthode [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) pour récupérer les commentaires en fil de discussion pour la colonne spécifiée. La méthode [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) accepte le nom de la colonne en paramètre et retourne le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). Vous pouvez parcourir le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) et utiliser la propriété [**ThreadedComment.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcomment/created_time).

L'exemple suivant démontre la lecture de l'heure de création des commentaires en fil en chargeant le [Fichier Excel d'exemple](89849861.xlsx). Veuillez consulter la sortie de la console générée par le code pour référence.

#### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedCommentCreatedTime-1.py" >}}

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

### **Modifier un commentaire en fil de discussion avec Aspose.Cells pour Python via .NET**

Aspose.Cells pour Python via .NET offre la méthode [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) pour récupérer les commentaires en fil de discussion pour la colonne spécifiée. La méthode [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) accepte le nom de la colonne en paramètre et retourne le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). Vous pouvez mettre à jour le commentaire requis dans le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) et enregistrer le classeur.

L'exemple suivant démontre l'édition du premier commentaire en fil dans la colonne A1 en chargeant le [Fichier Excel d'exemple](89849861.xlsx). Veuillez consulter le [fichier Excel de sortie](89849862.xlsx) généré par le code montrant le commentaire mis à jour pour référence.

#### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-EditThreadedComments-1.py" >}}

