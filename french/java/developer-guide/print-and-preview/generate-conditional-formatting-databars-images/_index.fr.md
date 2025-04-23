---
title: Générer des images de mise en forme conditionnelle DataBars
type: docs
weight: 170
url: /fr/java/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Parfois, vous devez générer des images de barres de données de formatage conditionnel. Vous pouvez utiliser la méthode Aspose.Cells [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage-com.aspose.cells.Cell-com.aspose.cells.ImageOrPrintOptions-) pour générer ces images. Cet article montre comment générer une image de barre de données à l'aide d'Aspose.Cells.

{{% /alert %}}

## **Exemple**

Le code d'exemple suivant génère l'image DataBar de la cellule C1. Tout d'abord, il accède à l'objet condition de formatage de la cellule, puis à partir de cet objet, il accède à l'objet DataBar et utilise sa méthode [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage-com.aspose.cells.Cell-com.aspose.cells.ImageOrPrintOptions-) pour générer l'image de la cellule. Enfin, il enregistre l'image sur le disque.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
{{< app/cells/assistant language="java" >}}
