---
title: Générer des images de mise en forme conditionnelle DataBars
linktitle: Générer des images de mise en forme conditionnelle DataBars
description: Aspose.Cells est une bibliothèque Node.js permettant de travailler avec des fichiers de feuilles de calcul. Elle supporte la génération de barres de données et d images avec une mise en forme conditionnelle, permettant aux utilisateurs de personnaliser l affichage de la feuille en fonction de la valeur des cellules. Cet article introduira comment utiliser la bibliothèque Aspose.Cells pour générer des barres de données et des images avec une mise en forme conditionnelle.
keywords: Aspose.Cells, Mise en forme conditionnelle, Barres de données, Images, Feuilles de calcul, Node.js via C++
type: docs
weight: 40
url: /fr/nodejs-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Parfois, vous devez générer des images de barres de données de formatage conditionnel. Vous pouvez utiliser la méthode Aspose.Cells [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) pour générer ces images. Cet article montre comment générer une image de barre de données à l'aide d'Aspose.Cells.

{{% /alert %}}

Le code exemple suivant génère l’image de la barre de données de la cellule C1. Il accède d’abord à l’objet de condition de mise en forme de la cellule, puis depuis cet objet, il accède à l’objet [**DataBar**](https://reference.aspose.com/cells/nodejs-cpp/databar) et utilise sa méthode [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/nodejs-cpp/databar/#toImage-cell-imageorprintoptions-) pour générer l’image de la cellule. Enfin, il enregistre l’image sur le disque.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-GenerateConditionalFormattingDataBars.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
