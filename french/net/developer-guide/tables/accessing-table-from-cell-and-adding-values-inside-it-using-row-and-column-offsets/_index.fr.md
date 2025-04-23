---
title: Accéder à un tableau depuis une cellule et ajouter des valeurs à l intérieur en utilisant des décalages de ligne et de colonne
type: docs
weight: 230
url: /fr/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Normalement, vous ajoutez des valeurs à l'intérieur de l'objet Table ou Liste en utilisant la méthode [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index). Mais parfois, vous pourriez avoir besoin d'ajouter des valeurs à l'intérieur de l'objet Table ou Liste en utilisant les décalages de ligne et de colonne.

Pour accéder à la table ou à l'objet liste à partir d'une cellule, utilisez la méthode [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable). Pour ajouter des valeurs à l'intérieur en utilisant les décalages de ligne et de colonne, utilisez la méthode [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue).

{{% /alert %}}

La capture d'écran suivante montre le fichier Excel source utilisé dans le code. Il contient le tableau vide et met en évidence la cellule D5 qui se trouve à l'intérieur du tableau. Nous accéderons à ce tableau depuis la cellule D5 en utilisant la méthode [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) et ajouterons ensuite les valeurs à l'intérieur en utilisant les méthodes [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) et [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue).

## Exemple

### Captures d'écran comparant les fichiers source et de sortie

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

La capture d'écran suivante montre le fichier Excel de sortie généré par le code. Comme vous pouvez le voir, la cellule D5 a une valeur et la cellule F6, qui est située à l'emplacement 2,2 du tableau, a une valeur.

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### Code C# pour accéder à la table à partir de la cellule et pour ajouter des valeurs à l'intérieur en utilisant des décalages de ligne et de colonne.

Le code d'exemple suivant charge le fichier Excel source tel que montré dans la capture d'écran ci-dessus et ajoute des valeurs à l'intérieur du tableau, puis génère le fichier Excel de sortie tel qu'indiqué ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
{{< app/cells/assistant language="csharp" >}}
