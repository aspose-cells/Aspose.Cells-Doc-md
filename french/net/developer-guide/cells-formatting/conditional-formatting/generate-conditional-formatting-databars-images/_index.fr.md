---
title: Générer des images de barres de données de mise en forme conditionnelle
type: docs
weight: 40
url: /fr/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 Parfois, vous devez générer des images de DataBars de mise en forme conditionnelle. Vous pouvez utiliser le Aspose.Cells[**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) méthode pour générer ces images. Cet article explique comment générer une image DataBar à l'aide de Aspose.Cells.

{{% /alert %}}

L'exemple de code suivant génère l'image DataBar de la cellule C1. Tout d'abord, il accède à l'objet de condition de format de la cellule, puis à partir de cet objet, il accède à la[**Barre de données**](https://reference.aspose.com/cells/net/aspose.cells/databar) objet et utilise son[**VersImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)méthode pour générer l'image de la cellule. Enfin, il enregistre l'image sur disque.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
