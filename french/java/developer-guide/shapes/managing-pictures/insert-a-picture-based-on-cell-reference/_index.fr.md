---
title: Insérer une image basée sur la référence Cell
type: docs
weight: 90
url: /fr/java/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

Parfois, vous avez une image vide et devez afficher des données ou du contenu dans l'image en définissant une référence de cellule dans la barre de formule. Aspose.Cells prend en charge cette fonctionnalité (Microsoft Excel 2010).

{{% /alert %}}

## Insertion d'une image basée sur la référence Cell

Aspose.Cells prend en charge l'affichage du contenu d'une cellule de feuille de calcul sous forme d'image. Vous pouvez lier l'image à la cellule qui contient les données que vous souhaitez afficher. Étant donné que la cellule ou la plage de cellules est liée à l'objet graphique, les modifications apportées aux données apparaissent automatiquement dans l'objet graphique. Ajoutez une image à la feuille de calcul en appelant le[**Ajouter une image**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture(int,%20int,%20int,%20int,%20java.io.InputStream) ) méthode de la[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) collection (encapsulée dans le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) objet). Spécifiez la plage de cellules à l'aide de la[**setFormule**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula) méthode de la[**Image**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)objet.

Vous trouverez ci-dessous une capture d'écran du fichier généré par le code ci-dessous.

**Insertion d'une image basée sur une référence de cellule**

![tâche : image_autre_texte](insert-a-picture-based-on-cell-reference_1.png)

## Exemple de code

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
