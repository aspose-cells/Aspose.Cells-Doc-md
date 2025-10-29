---
title: Générer des images de barres de données de formatage conditionnel avec Golang via C++
linktitle: Générer des images de mise en forme conditionnelle DataBars
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers de feuilles de calcul. Elle supporte la génération de barres de données et d’images avec un formatage conditionnel, permettant aux utilisateurs de personnaliser l’affichage du classeur en fonction de la valeur des cellules. Cet article introduira comment utiliser la bibliothèque Aspose.Cells pour générer des barres de données et des images avec un formatage conditionnel.
keywords: Aspose.Cells, Mise en forme conditionnelle, Barres de données, Images, Feuilles de calcul
type: docs
weight: 40
url: /fr/go-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Parfois, vous devez générer des images de barres de données de formatage conditionnel. Vous pouvez utiliser la méthode Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/) pour générer ces images. Cet article montre comment générer une image de barre de données à l'aide d'Aspose.Cells.

{{% /alert %}}

Le code exemple suivant génère l’image de la barre de données de la cellule C1. Il accède d’abord à l’objet de condition de mise en forme de la cellule, puis depuis cet objet, il accède à l’objet [**DataBar**](https://reference.aspose.com/cells/go-cpp/databar/) et utilise sa méthode [**ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/) pour générer l’image de la cellule. Enfin, il enregistre l’image sur le disque.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GenerateConditionalFormattingDatabarsImages.go" >}}
