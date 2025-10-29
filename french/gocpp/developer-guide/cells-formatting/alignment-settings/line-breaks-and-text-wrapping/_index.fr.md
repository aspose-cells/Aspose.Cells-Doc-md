---
title: Sauts de ligne et retour à la ligne du texte avec Golang via C++
description: Comment implémenter le retour à la ligne du texte et l’enveloppement des mots en utilisant la bibliothèque Aspose.Cells en C++. En utilisant la bibliothèque Aspose.Cells, vous pouvez facilement insérer du texte dans des cellules et définir la méthode de retour à la ligne, comme le retour à la ligne manuel, le retour à la ligne automatique, etc. Ce document détaille comment implémenter ces fonctionnalités et fournit un code d’exemple pour référence.
keywords: Aspose.Cells, sauts de ligne, retours à la ligne, mise en page du texte
type: docs
weight: 60
url: /fr/go-cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Pour vous assurer que le texte dans une cellule peut être lu, des sauts de ligne explicites et un retour à la ligne du texte peuvent être appliqués. Le retour à la ligne du texte transforme une ligne en plusieurs dans une cellule, tandis que les sauts de ligne explicites insérés les mettent exactement où vous le souhaitez.

{{% /alert %}}

## **Pour retourner le texte dans une cellule**

Pour envelopper le texte dans une cellule, utilisez la propriété [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/go-cpp/style/istextwrapped/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LineBreaksAndTextWrapping.go" >}}
## **Pour utiliser des sauts de ligne explicites**

Vous pouvez utiliser ‘\n’ en C++ pour insérer des sauts de ligne explicites dans une cellule.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LineBreaksAndTextWrapping-1.go" >}}
