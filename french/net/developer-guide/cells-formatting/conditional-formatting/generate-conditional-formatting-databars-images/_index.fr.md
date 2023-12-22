---
title: Générer des images de barres de données au formatage conditionnel
description: Aspose.Cells est une bibliothèque .NET permettant de travailler avec des feuilles de calcul. Il prend en charge la génération de barres de données et d'images formatées de manière conditionnelle, permettant aux utilisateurs de personnaliser l'affichage de la feuille de calcul en fonction de la valeur des cellules. Cet article explique comment utiliser la bibliothèque Aspose.Cells pour générer des barres de données et des images formatées de manière conditionnelle.
keywords: Aspose.Cells, Conditional Formatting, Data Bars, Images, Spreadsheets
type: docs
weight: 40
url: /fr/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 Parfois, vous devez générer des images de barres de données de mise en forme conditionnelle. Vous pouvez utiliser le Aspose.Cells[**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) méthode pour générer ces images. Cet article montre comment générer une image DataBar à l'aide de Aspose.Cells.

{{% /alert %}}

 L’exemple de code suivant génère l’image DataBar de la cellule C1. Tout d'abord, il accède à l'objet de condition de format de la cellule, puis à partir de cet objet, il accède à l'objet[**Barre de données**](https://reference.aspose.com/cells/net/aspose.cells/databar) objet et utilise son[**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)méthode pour générer l’image de la cellule. Enfin, il enregistre l'image sur le disque.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
