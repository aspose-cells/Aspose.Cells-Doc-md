---
title: Générer des images de mise en forme conditionnelle DataBars
description: Aspose.Cells est une bibliothèque .NET pour travailler avec des fichiers de feuille de calcul. Elle prend en charge la génération de barres de données formatées de manière conditionnelle et d images, permettant aux utilisateurs de personnaliser l affichage de la feuille de calcul en fonction de la valeur des cellules. Cet article présentera comment utiliser la bibliothèque Aspose.Cells pour générer des barres de données formatées de manière conditionnelle et des images.
keywords: Aspose.Cells, Mise en forme conditionnelle, Barres de données, Images, Feuilles de calcul
type: docs
weight: 40
url: /fr/net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Parfois, vous devez générer des images de barres de données de formatage conditionnel. Vous pouvez utiliser la méthode Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) pour générer ces images. Cet article montre comment générer une image de barre de données à l'aide d'Aspose.Cells.

{{% /alert %}}

Le code d'exemple suivant génère l'image DataBar de la cellule C1. Tout d'abord, il accède à l'objet de condition de format de la cellule, puis à partir de cet objet, il accède à l'objet [**DataBar**](https://reference.aspose.com/cells/net/aspose.cells/databar) et utilise sa méthode [**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) pour générer l'image de la cellule. Enfin, il enregistre l'image sur le disque.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
