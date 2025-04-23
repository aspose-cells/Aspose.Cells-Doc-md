---
title: Exporter la plage de cellules dans une feuille de calcul en tant qu image
type: docs
weight: 130
url: /fr/java/export-range-of-cells-in-a-worksheet-to-image/
---

{{% alert color="primary" %}}

Vous pouvez faire une image d'une feuille de calcul en utilisant Aspose.Cells. Cependant, parfois, vous devez exporter seulement une plage de cellules dans une feuille de calcul vers une image. Cet article explique comment y parvenir.

{{% /alert %}}

Pour obtenir une image d'une plage, définissez la zone d'impression sur la plage souhaitée, puis définissez toutes les marges à 0. Définissez également [**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) à **true**.

Le code suivant prend une image de la plage E8:H10. Voici une capture d'écran du classeur source utilisé dans le code. Vous pouvez essayer le code avec n'importe quel classeur.

**Fichier d'entrée**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)

L'exécution du code crée uniquement une image de la plage E8:H10.

**Image de sortie**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

Vous trouverez peut-être également l'article [Conversion de feuille de calcul en différents formats d'image](/cells/fr/java/converting-worksheet-to-different-image-formats/) utile.
{{< app/cells/assistant language="java" >}}
