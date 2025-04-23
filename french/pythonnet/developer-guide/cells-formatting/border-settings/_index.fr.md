---
title: Paramètres de bordure
description: Comment utiliser la bibliothèque Aspose.Cells pour Python via .NET en Python pour définir le style et la couleur de la bordure des cellules. En ajustant la largeur, le style et la couleur de la bordure, vous avez plus de contrôle sur l apparence des cellules.
keywords: Aspose.Cells pour Python via .NET, Paramètres de bordure de cellule, Largeur de la bordure Python, Style de bordure, Couleur de bordure
type: docs
weight: 40
url: /fr/python-net/cells-border-settings/
---

## **Ajout de bordures aux cellules**

Microsoft Excel permet aux utilisateurs de formater des cellules en ajoutant des bordures. Le type de bordure dépend de l'emplacement où elle est ajoutée. Par exemple, une bordure supérieure est ajoutée à la position supérieure d'une cellule. Les utilisateurs peuvent également modifier le style de ligne et la couleur des bordures.

Avec Aspose.Cells pour Python via .NET, les développeurs peuvent ajouter des bordures et personnaliser leur apparence de la même manière flexible qu’avec Microsoft Excel.

### **Ajout de bordures aux cellules**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Chaque élément de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells pour Python via .NET fournit la méthode [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) dans la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). La méthode [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) est utilisée pour définir le style de mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) fournit des propriétés pour ajouter des bordures aux cellules.

#### **Ajout de bordures à une cellule**

Les développeurs peuvent ajouter des bordures à une cellule en utilisant la collection [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) de l'objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Le type de bordure est passé en index à la collection [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders). Tous les types de bordures sont prédéfinis dans l'énumération [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype).

**Énumération de bordure**

|**Types de bordures**|**Description**|
| :- | :- |
|BORDURE_INFÉRIEURE|Une ligne de bordure en bas|
|DIAGONALE_DESCENDANTE|Une ligne diagonale du haut gauche vers le bas droit|
|DIAGONALE_MONTE|Une ligne diagonale du bas gauche vers le haut droit|
|BORDURE_GAUCHE|Une ligne de bordure à gauche|
|BORDURE_DROITE|Une ligne de bordure à droite|
|BORDURE_SUPÉRIEURE|Une ligne de bordure en haut|

The [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border) object which provides two properties, [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/border/color) and [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) to set a border's line color and style respectively.

Pour définir la couleur de la ligne de bordure, sélectionnez une couleur à l'aide de l'énumération Couleur (partie du cadre .NET) et attribuez-la à la propriété Couleur de l'objet Bordure.

Le style de la ligne de la bordure est défini en sélectionnant un style de ligne à partir de l'énumération [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype).

**Énumération de Type de Bordure Cellulaire**

|**Styles de ligne**|**Description**|
| :- | :- |
|TIRET_POINT|Ligne pointillée fine|
|TIRET_POINT_POINT|Ligne tiret-point fin|
|TACHÉ|Ligne tachetée|
|POINTILLÉ|Ligne pointillée|
|DOUBLE|Ligne double|
|CHEVEUX|Ligne très fine|
|TIRET_MOYEN_DASH_DOT|Ligne pointillée moyenne diagonale|
|TIRET_MOYEN_DASH_DOT_DOT|Ligne tiret-point moyenne pointillée|
|TIRET_MOYEN_DÉCHETÉ|Ligne tiret m-tière moyenne|
|AUCUN|Pas de ligne|
|MOYEN|Ligne moyenne|
|DIAGONALE_ENCOLLÉE_DASH_DOT|Ligne diagonale oblique tiret-point|
|ÉPAISSE|Ligne épaisse|
|FAINTE|Ligne fine|
Sélectionnez l'un des styles de ligne, puis affectez-le à la propriété [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) de l'objet [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBordersToCells-1.py" >}}

{{% alert color="primary" %}}

Vous devez définir à la fois le style de ligne et la couleur en même temps. Les deux lignes de bordure diagonales doivent avoir le même style de ligne et la même couleur.

{{% /alert %}}

#### **Ajout de bordures à une plage de cellules**

Il est également possible d'ajouter des bordures à une plage de cellules plutôt qu'à une seule cellule. Pour ce faire, créez d'abord une plage de cellules en appelant la méthode [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) de la collection [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Elle prend les paramètres suivants :

- Première ligne, la première ligne de la plage.
- Première colonne, represente la première colonne de la plage.
- Nombre de lignes, le nombre de lignes dans la plage.
- Nombre de colonnes, le nombre de colonnes dans la plage.

La méthode [**create_range**](hhttps://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str) renvoie un objet [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range), qui contient la plage de cellules spécifiée. L'objet [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) fournit une méthode [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border) qui prend les paramètres suivants pour ajouter une bordure à la plage de cellules :

- **Type de bordure**, le type de bordure, sélectionné dans l'énumération [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype).
- **Style de ligne**, le style de la bordure, sélectionné dans l'énumération [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype).
- **Couleur**, la couleur de la ligne, sélectionnée dans l'énumération Color.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBorderstoRange-1.py" >}}

