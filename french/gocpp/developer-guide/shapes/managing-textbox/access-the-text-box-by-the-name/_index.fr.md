---
title: Accéder à la zone de texte par le nom via Golang en C++
linktitle: Accéder à la zone de texte par le nom
type: docs
weight: 230
url: /fr/go-cpp/access-the-text-box-by-the-name/
description: Apprenez comment accéder à une boîte de texte par son nom en utilisant Aspose.Cells for C++.
---

## Accéder à la zone de texte par le nom

Auparavant, les zones de texte étaient accessibles par index dans la collection [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/go-cpp/worksheet/gettextboxes/), mais maintenant, vous pouvez également accéder à la zone de texte par son nom dans cette collection. C'est une méthode pratique et rapide pour accéder à votre zone de texte si vous connaissez déjà son nom.

Le code d'exemple suivant crée d'abord une boîte de texte, lui assigne un texte et un nom. Ensuite, dans les lignes suivantes, nous accédons à la même boîte de texte par son nom et affichons son contenu.

### Code C++ pour accéder à la boîte de texte par nom

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessTheTextBoxByTheName.go" >}}
### Sortie de la console générée par le code d'exemple

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
