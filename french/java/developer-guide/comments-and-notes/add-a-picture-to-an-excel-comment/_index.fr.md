---
title: Ajouter une image à un commentaire Excel
type: docs
weight: 60
url: /fr/java/add-a-picture-to-an-excel-comment/
---

{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs de personnaliser l'apparence des feuilles de calcul de manière importante. Il est même possible d'ajouter des images en arrière-plan aux commentaires.

Des commentaires sont ajoutés aux cellules pour enregistrer des commentaires, des détails sur le fonctionnement d'une formule, l'origine d'une valeur ou des questions des relecteurs. Ajouter une image en arrière-plan peut être un choix esthétique ou renforcer l'identité visuelle.

{{% /alert %}}

## Ajouter une image au commentaire Excel avec Microsoft Excel

Avec Microsoft Excel 2007, il est possible d'avoir une image en arrière-plan d'un commentaire de cellule. Dans Excel 2007, ceci est accompli (en supposant que le commentaire a déjà été ajouté) de la manière suivante :

1. Faites un clic droit sur la cellule contenant le commentaire.
1. Choisissez **Afficher/Masquer les commentaires** et effacez tout texte du commentaire.
1. Cliquez sur le bord du commentaire pour le sélectionner.
1. Choisissez **Format**, puis **Commentaire**.
1. Dans l'onglet Couleurs et Traits, cliquez sur la flèche pour **Couleur**.
1. Cliquez sur **Remplissage**.
1. Dans l'onglet Image, cliquez sur **Sélectionner une image**.
1. Localisez et sélectionnez l'image
1. Cliquez sur **OK**.

## Ajouter une image au commentaire Excel avec Aspose.Cells

Aspose.Cells fournit cette fonctionnalité précieuse.

Le code d'exemple ci-dessous crée un fichier XLSX à partir de zéro et ajoute un commentaire avec un arrière-plan d'image à la cellule A1.

Après avoir exécuté le code, A1 a un commentaire avec une image en arrière-plan.

**Le fichier de sortie**

![todo:image_alt_text](add-a-picture-to-an-excel-comment_1.png)

## Code d'exemple

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddPicturetoExcelComment-AddPicturetoExcelComment.java" >}}
