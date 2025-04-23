---
title: Insérer une image basée sur la référence de cellule
type: docs
weight: 90
url: /fr/java/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

Parfois, vous avez une image vide et vous devez afficher des données ou du contenu dans l'image en définissant une référence de cellule dans la barre de formule. Aspose.Cells prend en charge cette fonctionnalité (Microsoft Excel 2010).

{{% /alert %}}

## Insertion d'une image basée sur la référence de la cellule

Aspose.Cells prend en charge l'affichage du contenu d'une cellule de feuille de calcul dans une forme d'image. Vous pouvez lier l'image à la cellule qui contient les données que vous souhaitez afficher. Comme la cellule ou la plage de cellules est liée à l'objet graphique, les modifications apportées aux données apparaissent automatiquement dans l'objet graphique. Ajoutez une image à la feuille de calcul en appelant la méthode [**addPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture-int-int-int-int-java.io.InputStream-) de la collection [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)). Spécifiez la plage de cellules en utilisant la méthode [**setFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula) de l'objet [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture).

Ci-dessous se trouve une capture d'écran du fichier généré par le code ci-dessous.

**Insérer une image basée sur la référence de cellule**

![todo:image_alt_text](insert-a-picture-based-on-cell-reference_1.png)

## Code d'exemple

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
{{< app/cells/assistant language="java" >}}
