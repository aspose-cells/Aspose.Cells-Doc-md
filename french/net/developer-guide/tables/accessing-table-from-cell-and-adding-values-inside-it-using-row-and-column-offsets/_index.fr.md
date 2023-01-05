---
title: Accéder au tableau à partir de Cell et y ajouter des valeurs à l'aide des décalages de ligne et de colonne
type: docs
weight: 230
url: /fr/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

 Normalement, vous ajoutez des valeurs à l'intérieur de l'objet Table ou List à l'aide de[**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)méthode. Mais parfois, vous devrez peut-être ajouter des valeurs à l'intérieur de la table ou de l'objet de liste en utilisant les décalages de ligne et de colonne.

Pour accéder à Table ou List Object à partir d'une cellule, utilisez la[**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) méthode. Pour ajouter des valeurs à l'intérieur à l'aide des décalages de ligne et de colonne, utilisez la[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) méthode.

{{% /alert %}}

 La capture d'écran suivante montre le fichier Excel source utilisé dans le code. Il contient le tableau vide et met en surbrillance la cellule D5 qui se trouve à l'intérieur du tableau. Nous accéderons à ce tableau à partir de la cellule D5 en utilisant[**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) méthode, puis ajoutez les valeurs à l'intérieur en utilisant à la fois[**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) et[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue)méthodes.

## Exemple

### Captures d'écran comparant les fichiers source et de sortie

|![tâche : image_autre_texte](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
|:- |

La capture d'écran suivante montre le fichier Excel de sortie généré par le code. Comme vous pouvez le voir, la cellule D5 a une valeur et la cellule F6 qui se trouve au décalage 2,2 du tableau a une valeur.

|![tâche : image_autre_texte](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
|:- |

### C# code pour accéder à la table à partir de la cellule et pour ajouter des valeurs à l'intérieur en utilisant les décalages de ligne et de colonne

L'exemple de code suivant charge le fichier Excel source comme indiqué dans la capture d'écran ci-dessus, ajoute des valeurs dans le tableau et génère le fichier Excel de sortie comme indiqué ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
