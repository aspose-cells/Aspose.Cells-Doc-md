---
title: Créer, supprimer et obtenir des commentaires de cellule de la grille
type: docs
weight: 100
url: /fr/net/aspose-cells-gridweb/manage-comment/
keywords: GridWeb,comment
description: Cet article présente comment travailler avec les commentaires dans GridWeb.
---

## **Scénarios d'utilisation possibles**
L'article suivant explique comment créer, supprimer et obtenir un commentaire à partir d'une cellule (GridCell) à l'intérieur de la feuille de calcul GridWeb. Il est à noter que GridWeb affiche le commentaire sous forme de tooltip comme MS-Excel lorsque vous survolez la cellule comme indiqué dans cette capture d'écran.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **Créer un objet Commentaires à l'intérieur de la cellule**
Veuillez utiliser la méthode GridCell.CreateComment pour créer un objet commentaire à l'intérieur de la cellule. Le code d'exemple suivant crée un commentaire d'exemple dans la cellule B4 de la première feuille de calcul de GridWeb.

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Supprimer un objet Commentaires de la cellule**
Veuillez utiliser la méthode GridCell.RemoveComment pour supprimer un objet commentaire de la cellule. Le code d'exemple suivant supprime le commentaire de la cellule B4 à l'intérieur de la première feuille de calcul de GridWeb.



{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **Obtenir un objet Commentaires de la cellule**
Veuillez utiliser la méthode GridCell.GetComment() pour obtenir l'objet commentaire de la cellule. Le code d'exemple suivant récupère l'objet commentaire de la cellule B4 puis accède à ses différentes propriétés comme Auteur, Note, Visibilité, etc.

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Get comment of this cell

GridComment gridComm = cell.GetComment();

//Access its various properties

string strAuth = gridComm.Author;

string strNote = gridComm.Note;

bool isVis = gridComm.IsVisible;

{{< /highlight >}}
