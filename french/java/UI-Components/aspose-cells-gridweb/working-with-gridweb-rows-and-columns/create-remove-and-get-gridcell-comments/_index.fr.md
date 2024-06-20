---
title: Créer, supprimer et obtenir des commentaires de cellule de la grille
type: docs
weight: 10
url: /fr/java/create-remove-and-get-gridcell-comments/
---

## **Scénarios d'utilisation possibles**
L'article suivant explique comment créer, supprimer et obtenir des commentaires de cellule de la grille à l'intérieur de la feuille de calcul GridWeb. Il convient de noter que GridWeb affiche le commentaire sous forme de tooltip comme MS-Excel lorsque vous survolez la souris sur la cellule, comme illustré dans cette capture d'écran.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **Créer un objet Commentaires à l'intérieur de la cellule**
Veuillez utiliser la méthode GridCell.CreateComment pour créer un objet commentaire à l'intérieur de la cellule. Le code d'exemple suivant crée un commentaire d'exemple dans la cellule B4 de la première feuille de calcul de GridWeb.

{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Supprimer un objet Commentaires de la cellule**
Veuillez utiliser la méthode GridCell.RemoveComment pour supprimer un objet commentaire de la cellule. Le code d'exemple suivant supprime le commentaire de la cellule B4 à l'intérieur de la première feuille de calcul de GridWeb.



{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
## **Obtenir un objet Commentaires de la cellule**
Veuillez utiliser la méthode GridCell.GetComment() pour obtenir l'objet commentaire de la cellule. Le code d'exemple suivant obtient l'objet commentaire de la cellule B4 puis accède à ses différentes propriétés telles que Auteur, Note, Visibilité, etc.

{{< highlight java >}}

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




