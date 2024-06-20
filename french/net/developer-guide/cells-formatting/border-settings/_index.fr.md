---
title: Paramètres de bordure
description: Comment utiliser la bibliothèque Aspose.Cells en C# pour définir le style et la couleur des bordures des cellules. En ajustant la largeur, le style et la couleur de la bordure, vous avez plus de contrôle sur l apparence des cellules.
keywords: Aspose.Cells, Paramètres de la bordure de cellule, C#, Largeur de la bordure, Style de la bordure, Couleur de la bordure
type: docs
weight: 40
url: /fr/net/cells-border-settings/
---

## **Ajout de bordures aux cellules**

Microsoft Excel permet aux utilisateurs de formater des cellules en ajoutant des bordures. Le type de bordure dépend de l'emplacement où elle est ajoutée. Par exemple, une bordure supérieure est ajoutée à la position supérieure d'une cellule. Les utilisateurs peuvent également modifier le style de ligne et la couleur des bordures.

Avec Aspose.Cells, les développeurs peuvent ajouter des bordures et personnaliser leur aspect de la même manière flexible que dans Microsoft Excel.

### **Ajout de bordures aux cellules**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Chaque élément de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells fournit la méthode [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) dans la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). La méthode [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) est utilisée pour définir le style de formatage d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) fournit des propriétés pour ajouter des bordures aux cellules.

#### **Ajout de bordures à une cellule**

Les développeurs peuvent ajouter des bordures à une cellule en utilisant la collection [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) de l'objet [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). Le type de bordure est passé en index à la collection [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders). Tous les types de bordures sont prédéfinis dans l'énumération [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype).

**Énumération de bordure**

|**Types de bordures**|**Description**|
| :- | :- |
|BottomBorder|Une ligne de bordure inférieure|
|DiagonalDown|Une ligne diagonale de haut gauche à bas droite|
|DiagonalUp|Une ligne diagonale de bas gauche à haut droit|
|LeftBorder|Une ligne de bordure gauche|
|RightBorder|Une ligne de bordure droite|
|TopBorder|Une ligne de bordure supérieure|

The [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border) object which provides two properties, [**Color**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) and [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) to set a border's line color and style respectively.

Pour définir la couleur de la ligne de bordure, sélectionnez une couleur à l'aide de l'énumération Couleur (partie du cadre .NET) et attribuez-la à la propriété Couleur de l'objet Bordure.

Le style de la ligne de la bordure est défini en sélectionnant un style de ligne à partir de l'énumération [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype).

**Énumération de Type de Bordure Cellulaire**

|**Styles de ligne**|**Description**|
| :- | :- |
|DashDot|Ligne pointillée fine|
|DashDotDot|Ligne pointillée fine avec point|
|Dashed|Ligne en tirets|
|Dotted|Ligne en pointillés|
|Double|Ligne double|
|Hair|Ligne fine|
|MediumDashDot|Ligne mixte pointillée|
|MediumDashDotDot|Ligne mixte pointillée-traitée|
|MediumDashed|Ligne en pointillés moyens|
|None|Aucune ligne|
|Medium|Ligne moyenne|
|SlantedDashDot|Ligne mixte pointillée inclinée moyenne|
|Thick|Ligne épaisse|
|Thin|Ligne fine|
Sélectionnez l'un des styles de ligne, puis affectez-le à la propriété [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) de l'objet [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

Vous devez définir à la fois le style de ligne et la couleur en même temps. Les deux lignes de bordure diagonales doivent avoir le même style de ligne et la même couleur.

{{% /alert %}}

#### **Ajout de bordures à une plage de cellules**

Il est également possible d'ajouter des bordures à une plage de cellules plutôt qu'à une seule cellule. Pour ce faire, créez d'abord une plage de cellules en appelant la méthode [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Elle prend les paramètres suivants :

- Première ligne, la première ligne de la plage.
- Première colonne, represente la première colonne de la plage.
- Nombre de lignes, le nombre de lignes dans la plage.
- Nombre de colonnes, le nombre de colonnes dans la plage.

La méthode [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) renvoie un objet [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range), qui contient la plage de cellules spécifiée. L'objet [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) fournit une méthode [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) qui prend les paramètres suivants pour ajouter une bordure à la plage de cellules :

- **Type de bordure**, le type de bordure, sélectionné dans l'énumération [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype).
- **Style de ligne**, le style de la bordure, sélectionné dans l'énumération [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype).
- **Couleur**, la couleur de la ligne, sélectionnée dans l'énumération Color.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
