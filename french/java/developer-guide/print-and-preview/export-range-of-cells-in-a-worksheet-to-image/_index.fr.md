---
title: Exporter la plage de Cells dans une feuille de calcul vers une image
type: docs
weight: 130
url: /fr/java/export-range-of-cells-in-a-worksheet-to-image/
---
{{% alert color="primary" %}}

Vous pouvez créer une image d'une feuille de calcul à l'aide de Aspose.Cells. Cependant, vous devez parfois exporter uniquement une plage de cellules d'une feuille de calcul vers une image. Cet article explique comment y parvenir.

{{% /alert %}}

 Pour prendre une image d'une plage, définissez la zone d'impression sur la plage souhaitée, puis définissez toutes les marges sur 0. Définissez également[**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) à**vrai**.

Le code suivant prend une image de la plage E8:H10. Vous trouverez ci-dessous une capture d'écran du classeur source utilisé dans le code. Vous pouvez essayer le code avec n'importe quel classeur.

**Fichier d'entrée**

![tâche : image_autre_texte](export-range-of-cells-in-a-worksheet-to-image_1.png)

L'exécution du code crée une image de la plage E8:H10 uniquement.

**Image de sortie**

![tâche : image_autre_texte](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

 Vous pouvez également retrouver l'article[Conversion d'une feuille de calcul en différents formats d'image](/cells/fr/java/converting-worksheet-to-different-image-formats/) utile.
