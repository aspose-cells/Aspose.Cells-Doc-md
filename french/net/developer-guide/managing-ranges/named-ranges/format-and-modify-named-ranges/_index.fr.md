---
title: Formater et modifier des plages nommées
type: docs
weight: 85
url: /fr/net/format-and-modify-named-ranges/
---
## **Plages de formats**

### **Définition de la couleur d'arrière-plan et des attributs de police sur une plage nommée**

 Pour appliquer le formatage, définissez un[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objet pour spécifier les paramètres de style et l'appliquer à l'objet[**Intervalle**](https://reference.aspose.com/cells/net/aspose.cells/range)objet.

L'exemple suivant montre comment définir la couleur de remplissage unie (couleur d'ombrage) avec les paramètres de police sur une plage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **Ajout de bordures à une plage nommée**

 Il est possible d'ajouter des bordures à une plage de cellules au lieu d'une seule cellule. La[**Intervalle**](https://reference.aspose.com/cells/net/aspose.cells/range) l'objet fournit un[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)méthode qui prend les paramètres suivants pour ajouter une bordure à la plage de cellules :

-  Type de bordure, le type de bordure, sélectionné dans le[**Type de bordure**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)énumération.
-  Style de ligne, le style de ligne, sélectionné dans le[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)énumération.
- Color, la couleur de la ligne, sélectionnée dans l'énumération Color.

L'exemple suivant montre comment définir une bordure de contour sur une plage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

L'exemple suivant montre comment définir des bordures autour de chaque cellule de la plage.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **Renommer une plage nommée**

 Aspose.Cells vous permet de renommer une plage nommée selon vos besoins. Vous pouvez obtenir la plage nommée et la renommer en utilisant[**Nom.Texte**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text)attribut. L'exemple suivant montre comment renommer une plage nommée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **Union des gammes**

 Aspose.Cells fournit[**Gamme.Union**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union)méthode pour prendre l'union pour les plages, la méthode renvoie un[*Liste des tableaux*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8)objet. L'exemple suivant montre comment prendre union pour les plages.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **Intersection des gammes**

 Aspose.Cells fournit le[**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) méthode pour croiser deux plages. La méthode retourne un[**Intervalle**](https://reference.aspose.com/cells/net/aspose.cells/range) objet. Pour vérifier si une plage intersecte une autre plage, utilisez la[**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)méthode qui renvoie une valeur booléenne. L'exemple suivant montre comment croiser les plages.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **Fusionner Cells dans la plage nommée**

 Aspose.Cells fournit[**Plage. Fusionner()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)méthode pour fusionner les cellules de la plage. L'exemple suivant montre comment fusionner les cellules individuelles d'une plage nommée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **Supprimer une plage nommée**

 Aspose.Cells fournit le[**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) méthode pour effacer le nom de la plage. Pour effacer le contenu de la plage, utilisez[**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index)méthode. L'exemple suivant montre comment supprimer une plage nommée avec son contenu.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
