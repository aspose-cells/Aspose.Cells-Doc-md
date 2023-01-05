---
title: Générer des images de barres de données de mise en forme conditionnelle
type: docs
weight: 170
url: /fr/java/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 Parfois, vous devez générer des images de DataBars de mise en forme conditionnelle. Vous pouvez utiliser le Aspose.Cells[**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)méthode pour générer ces images. Cet article explique comment générer une image DataBar à l'aide de Aspose.Cells.

{{% /alert %}}

## **Exemple**

 L'exemple de code suivant génère l'image DataBar de la cellule C1. Tout d'abord, il accède à l'objet de condition de format de la cellule, puis à partir de cet objet, il accède à l'objet DataBar et utilise son[**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)) méthode pour générer l'image de la cellule. Enfin, il enregistre l'image sur disque.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
