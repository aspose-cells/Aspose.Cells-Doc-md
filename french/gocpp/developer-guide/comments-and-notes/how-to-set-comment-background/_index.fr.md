---
title: Comment changer l arrière plan du commentaire dans Excel avec Golang via C++
linktitle: Arrière plan du commentaire
type: docs
weight: 190
url: /fr/go-cpp/how-to-set-comment-background/
description: Comment changer la couleur dans un commentaire dans Excel. Comment insérer une image ou une photo dans un commentaire dans Excel en utilisant C++.
keywords: ajouter une image en inset, une couleur de commentaire, arrière plan excel
---

{{% alert color="primary" %}}

Les commentaires sont ajoutés aux cellules pour enregistrer des remarques, allant des détails sur le fonctionnement d'une formule, de l'origine d'une valeur ou de questions des réviseurs. Les commentaires jouent un rôle extrêmement important lorsque plusieurs personnes discutent ou révisent le même document à différents moments. Comment distinguer les commentaires de différentes personnes ? Oui, nous pouvons définir une couleur d'arrière-plan différente pour chaque commentaire. Mais lorsque nous devons traiter beaucoup de documents et de nombreux commentaires, faire cela manuellement est un désastre. Heureusement, [**Aspose.Cells**](https://products.aspose.com/cells/go-cpp/) offre une API qui vous permet de faire cela dans le code.

{{% /alert %}}

## **Comment changer la couleur dans le commentaire dans Excel**

Lorsque vous n'avez pas besoin de la couleur de fond par défaut pour les commentaires, vous pouvez la remplacer par une couleur qui vous intéresse. Comment puis-je changer la couleur de l'arrière-plan de la boîte de commentaires dans Excel ?

Le code suivant vous guidera sur la façon d'utiliser [**Aspose.Cells**](https://products.aspose.com/cells/go-cpp/) pour ajouter votre couleur d'arrière-plan préférée aux commentaires de votre choix.

Voici un [fichier d'exemple](exmaple.xlsx) préparé pour vous. Ce fichier sert à initialiser l'objet Workbook dans le code ci-dessous.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetCommentBackground.go" >}}
Exécutez le code ci-dessus, et vous obtiendrez un [fichier de sortie](result.xlsx).

## **Comment insérer une image ou une photo dans le commentaire dans Excel**

Microsoft Excel permet aux utilisateurs de personnaliser considérablement l'apparence des feuilles de calcul. Il est même possible d'ajouter des images de fond aux commentaires. L'ajout d'une image d'arrière-plan peut être un choix esthétique ou utilisé pour renforcer la marque.

Le code d'exemple ci-dessous crée un fichier XLSX à partir de zéro en utilisant l'API [**Aspose.Cells**](https://products.aspose.com/cells/go-cpp/), et ajoute un commentaire avec une image d'arrière-plan à la cellule A1.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetCommentBackground-1.go" >}}
