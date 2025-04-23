---
title: Formater et modifier des plages nommées
type: docs
weight: 85
url: /fr/net/format-and-modify-named-ranges/
---

## **Format des plages**

### **Définir la couleur d'arrière-plan et les attributs de police à une plage nommée**

Pour appliquer le formatage, définissez un objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) pour spécifier les paramètres de style et appliquez-le à l'objet [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range).

L'exemple suivant montre comment définir la couleur de remplissage pleine (couleur d'ombrage) avec des paramètres de police à une plage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **Ajout de bordures à une plage nommée**

Il est possible d'ajouter des bordures à une plage de cellules au lieu d'une seule cellule. L'objet [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) fournit une méthode [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) qui prend les paramètres suivants pour ajouter une bordure à la plage de cellules:

- Type de bordure, le type de bordure, sélectionné de l'énumération [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype).
- Style de ligne, le style de ligne, sélectionné de l'énumération [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype).
- Couleur, la couleur de la ligne, sélectionnée dans l'énumération de couleur.

L'exemple suivant montre comment définir une bordure de contour à une plage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

L'exemple suivant montre comment définir des bordures autour de chaque cellule de la plage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **Renommer une plage nommée**

Aspose.Cells vous permet de renommer une plage nommée selon vos besoins. Vous pouvez obtenir la plage nommée et la renommer en utilisant l'attribut [**Name.Text**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text). L'exemple suivant montre comment renommer une plage nommée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **Union des plages**

Aspose.Cells fournit la méthode [**Range.Union**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union) pour réaliser l'union des plages, la méthode renvoie un objet [*ArrayList*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8). L'exemple suivant montre comment réaliser l'union des plages.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **Intersection des plages**

Aspose.Cells fournit la méthode [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) pour intersecter deux plages. La méthode renvoie un objet [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range). Pour vérifier si une plage intersecte une autre plage, utilisez la méthode [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) qui renvoie une valeur booléenne. L'exemple suivant montre comment intersecter les plages.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **Fusionner les cellules dans la plage nommée**

Aspose.Cells fournit la méthode [**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) pour fusionner les cellules dans la plage. L'exemple suivant montre comment fusionner les cellules individuelles d'une plage nommée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **Supprimer une Plage Nommée**

Aspose.Cells fournit la méthode [**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) pour effacer le nom de la plage. Pour effacer le contenu de la plage, utilisez la méthode [**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index). L'exemple suivant montre comment supprimer une plage nommée avec son contenu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
