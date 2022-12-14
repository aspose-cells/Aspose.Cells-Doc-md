---
title: Gérer les commentaires et les notes
linktitle: Commentaires et remarques
type: docs
weight: 128
url: /fr/net/comments-and-notes/
description: Insérez et gérez des commentaires ou des notes avec Aspose.Cells pour .Net.
keywords: insert comments, insert notes
---
## **Introduction**

Les commentaires sont utilisés pour ajouter des informations supplémentaires aux cellules. Aspose.Cells fournit deux méthodes pour ajouter des commentaires aux cellules. La première consiste à créer manuellement des commentaires dans un fichier de concepteur. Ces commentaires sont ensuite importés à l'aide de Aspose.Cells. La seconde consiste à ajouter des commentaires à l'aide de Aspose.Cells API au moment de l'exécution. Cette rubrique traite de l'ajout de commentaires aux cellules à l'aide du Aspose.Cells API. La mise en forme des commentaires sera également expliquée.

## **Ajout d'un commentaire**

 Ajouter un commentaire à une cellule en appelant le[**commentaires**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection) de la collection[**Ajouter**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/add/index) méthode (encapsulée dans la[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) objet). Le nouveau[**Commentaire**](https://reference.aspose.com/cells/net/aspose.cells/comment) l'objet est accessible depuis le[**commentaires**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection) collection en passant l'index de commentaire. Après avoir accédé au[**Commentaire**](https://reference.aspose.com/cells/net/aspose.cells/comment) objet, personnalisez la note de commentaire à l'aide de[**Commentaire**](https://reference.aspose.com/cells/net/aspose.cells/comment) objets[**Noter**](https://reference.aspose.com/cells/net/aspose.cells/comment/properties/note)propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddingComment-1.cs" >}}

## **Formatage des commentaires**

Il est également possible de formater l'apparence des commentaires en configurant leurs paramètres de hauteur, de largeur et de police.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-CommentFormatting-1.cs" >}}

## **Ajouter une image au commentaire**

Avec Microsoft Excel 2007, il est également possible d'avoir une image comme arrière-plan d'un commentaire de cellule. Dans Excel 2007, cela se fait en procédant comme suit. (Ils supposent que vous avez déjà ajouté un commentaire de cellule.)

1. Cliquez avec le bouton droit sur la cellule qui contient le commentaire.
1.  Sélectionner**Afficher/Masquer les commentaires**, et effacez tout texte du commentaire.
1. Cliquez sur la bordure du commentaire pour le sélectionner.
1.  Sélectionner**Format** , alors**Commentaire**.
1.  Sur le**Couleurs et lignes** onglet, développez l'onglet**Couleur** liste.
1.  Cliquez sur**Effets de remplissage**.
1.  Sur le**Image** onglet, cliquez**Sélectionnez l'image**.
1. Localisez et sélectionnez l'image.
1.  Cliquez sur**D'ACCORD** jusqu'à ce que toutes les boîtes de dialogue soient fermées.

Aspose.Cells fournit également cette fonctionnalité. Vous trouverez ci-dessous un exemple de code qui crée un fichier XLSX à partir de zéro, en ajoutant un commentaire à la cellule "A1" avec une image définie comme arrière-plan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddImageToComment-1.cs" >}}

## **Sujets avancés**
- [Changer la direction du texte du commentaire](/cells/fr/net/change-text-direction-of-the-comment/)
- [Comment changer la couleur de la police des commentaires](/cells/fr/net/how-to-change-the-comment-font-color/)
- [Comment définir l'arrière-plan des commentaires](/cells/fr/net/how-to-set-comment-background/)
- [Commentaires filetés](/cells/fr/net/threaded-comments/)

