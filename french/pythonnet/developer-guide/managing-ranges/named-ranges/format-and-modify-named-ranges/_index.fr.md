---
title: Formater et modifier des plages nommées
type: docs
weight: 85
url: /fr/python-net/format-and-modify-named-ranges/
description: Cet article montre comment formater et modifier les plages nommées avec l API Aspose.Cells pour Python via .NET.
keywords: Python Excel Library, Python Format and Modify Named Ranges, Python Set Background Color and Font Attributes to a Named Range, Python Add Borders to a Named Range, Python Rename a Named Range, Python Union of Ranges, Python Intersection of Ranges, Python Merge Cells in the Named Range.
---

## **Format des plages**

### **Comment définir la couleur de fond et les attributs de police sur une plage nommée**

Pour appliquer le formatage, définissez un objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) pour spécifier les paramètres de style et appliquez-le à l'objet [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range).

L'exemple suivant montre comment définir la couleur de remplissage pleine (couleur d'ombrage) avec des paramètres de police à une plage.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges1-1.py" >}}

### **Comment ajouter des bordures à une plage nommée**

Il est possible d'ajouter des bordures à une plage de cellules au lieu d'une seule cellule. L'objet [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) fournit une méthode [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border/#aspose.cells.BorderType-aspose.cells.CellBorderType-aspose.cells.CellsColor) qui prend les paramètres suivants pour ajouter une bordure à la plage de cellules:

- Type de bordure, le type de bordure, sélectionné de l'énumération [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype).
- Style de ligne, le style de ligne, sélectionné de l'énumération [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype).
- Couleur, la couleur de la ligne, sélectionnée dans l'énumération de couleur.

L'exemple suivant montre comment définir une bordure de contour à une plage.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges2-1.py" >}}


## **Comment Renommer une Plage Nommée**

Aspose.Cells vous permet de renommer une plage nommée selon vos besoins. Vous pouvez obtenir la plage nommée et la renommer en utilisant l'attribut [**Name.text**](https://reference.aspose.com/cells/python-net/aspose.cells/name/text). L'exemple suivant montre comment renommer une plage nommée.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-RenameNamedRange-1.py" >}}

## **Comment Réaliser l'Union des Plages**

Aspose.Cells fournit la méthode [**Range.union**](https://reference.aspose.com/cells/python-net/aspose.cells/range/union/#aspose.cells.Range) pour réaliser l'union des plages. L'exemple suivant montre comment réaliser l'union des plages.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-UnionOfRanges-1.py" >}}

## **Comment Intersectionner les Plages**

Aspose.Cells fournit la méthode [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) pour intersecter deux plages. La méthode renvoie un objet [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range). Pour vérifier si une plage intersecte une autre plage, utilisez la méthode [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) qui renvoie une valeur booléenne. L'exemple suivant montre comment intersecter les plages.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IntersectionofRanges-1.py" >}}

## **Comment Fusionner les Cellules dans la Plage Nommée**

Aspose.Cells fournit la méthode [**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#) pour fusionner les cellules dans la plage. L'exemple suivant montre comment fusionner les cellules individuelles d'une plage nommée.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-MergeCellsInNamedRange-1.py" >}}
