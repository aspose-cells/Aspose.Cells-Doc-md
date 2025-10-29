---
title: Gérer les commentaires et notes avec Golang via C++
linktitle: Commentaires et notes
type: docs
weight: 128
url: /fr/go-cpp/comments-and-notes/
description: Insérer et gérer des commentaires ou notes avec Aspose.Cells for C++.
keywords: insérer des commentaires, insérer des notes
---

## **Introduction**

Les commentaires sont utilisés pour ajouter des informations supplémentaires aux cellules. Aspose.Cells propose deux méthodes pour ajouter des commentaires aux cellules. La première consiste à créer des commentaires dans un fichier du concepteur manuellement. Ces commentaires sont ensuite importés en utilisant Aspose.Cells. La seconde consiste à ajouter des commentaires en utilisant l'API Aspose.Cells à l'exécution. Ce sujet traite de l'ajout de commentaires aux cellules en utilisant l'API Aspose.Cells. La mise en forme des commentaires sera également expliquée.

## **Ajouter un commentaire**

Ajoutez un commentaire à une cellule en appelant la méthode [**Add**](https://reference.aspose.com/cells/go-cpp/commentcollection/add/) de la collection [**Comments**](https://reference.aspose.com/cells/go-cpp/commentcollection/) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Le nouvel objet [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/) peut être accédé à partir de la collection [**Comments**](https://reference.aspose.com/cells/go-cpp/commentcollection/) en passant l'indice du commentaire. Après avoir accédé à l'objet [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/), personnalisez la note du commentaire en utilisant la propriété [**GetNote()**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/getnote/) de l'objet [**Comment**](https://reference.aspose.com/cells/cpp/aspose.cells/comment/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CommentsAndNotes.go" >}}
## **Mise en forme des commentaires**

Il est également possible de formater l'apparence des commentaires en configurant leur hauteur, leur largeur et leurs paramètres de police.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CommentsAndNotes-1.go" >}}
## **Ajouter une image au commentaire**

Avec Microsoft Excel 2007, il est également possible d'avoir une image en arrière-plan d'un commentaire de cellule. Dans Excel 2007, cela se fait en suivant les étapes suivantes. (Ils supposent que vous avez déjà ajouté un commentaire de cellule.)

1. Faites un clic droit sur la cellule qui contient le commentaire.
1. Sélectionnez **Afficher/masquer les commentaires**, et effacez tout texte du commentaire.
1. Cliquez sur le bord du commentaire pour le sélectionner.
1. Sélectionnez **Format**, puis **Commentaire**.
1. Sur l'onglet **Couleurs et traits**, développez la liste **Couleur**.
1. Cliquez sur **Remplissage**.
1. Sur l'onglet **Image**, cliquez sur **Sélectionner une image**.
1. Localisez et sélectionnez l'image.
1. Cliquez sur **OK** jusqu'à ce que tous les dialogues se ferment.

Aspose.Cells propose également cette fonctionnalité. Ci-dessous se trouve un exemple de code qui crée un fichier XLSX à partir de zéro, en ajoutant un commentaire à la cellule "A1" avec une image définie comme arrière-plan.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CommentsAndNotes-2.go" >}}
## **Sujets avancés**
- [Modifier la direction du texte du commentaire](/cells/fr/cpp/change-text-direction-of-the-comment/)
- [Comment changer la couleur de police du commentaire](/cells/fr/cpp/how-to-change-the-comment-font-color/)
- [Comment définir l'arrière-plan du commentaire](/cells/fr/cpp/how-to-set-comment-background/)
- [Commentaires en fil](/cells/fr/cpp/threaded-comments/)
