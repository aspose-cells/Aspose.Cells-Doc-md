---
title: Créer supprimer et obtenir des commentaires GridCell
type: docs
weight: 10
url: /fr/java/create-remove-and-get-gridcell-comments/
---
## **Scénarios d'utilisation possibles**
L'article suivant explique comment créer, supprimer et obtenir des commentaires GridCell dans la feuille de calcul GridWeb. Il convient de noter que GridWeb affiche un commentaire sous forme d'info-bulle comme MS-Excel lorsque vous passez la souris sur la cellule, comme indiqué dans cette capture d'écran.

![tâche : image_autre_texte](create-remove-and-get-gridcell-comments_1.png)
## **Créer un objet de commentaire à l'intérieur de Cell**
Veuillez utiliser la méthode GridCell.CreateComment pour créer un objet de commentaire dans la cellule. L'exemple de code suivant crée un exemple de commentaire dans la cellule B4 de la première feuille de calcul de GridWeb.

{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Supprimer l'objet Commentaire de Cell**
Veuillez utiliser la méthode GridCell.RemoveComment pour supprimer un objet de commentaire de la cellule. L'exemple de code suivant supprime le commentaire de la cellule B4 dans la première feuille de calcul de GridWeb.



{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
## **Obtenir l'objet Commentaire de Cell**
Veuillez utiliser la méthode GridCell.GetComment() pour obtenir l'objet commentaire de la cellule. L'exemple de code suivant obtient l'objet de commentaire de la cellule B4, puis accède à ses différentes propriétés telles que Auteur, Note, Visibilité, etc.

{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Get comment of this cell

GridComment gridComm = cell.getComment();

// Access its various properties

String strAuth = gridComm.getAuthor();

String strNote = gridComm.getNote();

boolean isVis = gridComm.isVisible();


{{< /highlight >}}




