---
title: Accéder au tableau à partir de Cell et y ajouter des valeurs à l'aide des décalages de ligne et de colonne
type: docs
weight: 110
url: /fr/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

 Normalement, vous ajoutez des valeurs à l'intérieur de l'objet Table ou List à l'aide de[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)) méthode. Mais parfois, vous devrez peut-être ajouter des valeurs à l'intérieur de la table ou de l'objet de liste en utilisant les décalages de ligne et de colonne.

Pour accéder à Table ou List Object à partir d'une cellule, utilisez la[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ) méthode. Et pour ajouter des valeurs à l'intérieur en utilisant les décalages de ligne et de colonne, utilisez le[**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) méthode.

{{% /alert %}}

## Exemple

### Captures d'écran comparant les fichiers source et de sortie

 La capture d'écran suivante montre le fichier Excel source utilisé dans le code. Il contient le tableau vide et met en surbrillance la cellule D5 qui se trouve à l'intérieur du tableau. Nous accéderons à ce tableau à partir de la cellule D5 en utilisant[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ), puis ajoutez les valeurs à l'intérieur en utilisant à la fois[**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean) ) et[**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) méthodes.

![tâche : image_autre_texte](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

La capture d'écran suivante montre le fichier Excel de sortie généré par le code. Comme vous pouvez le voir, la cellule D5 a une valeur et la cellule F6 qui se trouve au décalage 2,2 du tableau a une valeur.

![tâche : image_autre_texte](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### Java code pour accéder à la table à partir de la cellule et pour ajouter des valeurs à l'intérieur en utilisant les décalages de ligne et de colonne

L'exemple de code suivant charge le fichier Excel source comme indiqué dans la capture d'écran ci-dessus, ajoute des valeurs dans le tableau et génère le fichier Excel de sortie comme indiqué ci-dessus.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
