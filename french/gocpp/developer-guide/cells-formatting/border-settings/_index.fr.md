---
title: Paramètres de bordure avec Golang via C++
linktitle: Paramètres de bordure
description: Comment utiliser la bibliothèque Aspose.Cells en C++ pour définir le style et la couleur de la bordure des cellules. En ajustant la largeur, le style et la couleur de la bordure, vous avez plus de contrôle sur l’apparence des cellules.
keywords: Aspose.Cells, Paramètres de bordure des cellules, C++, Largeur de la bordure, Style de la bordure, Couleur de la bordure
type: docs
weight: 40
url: /fr/go-cpp/cells-border-settings/
---

## **Ajout de bordures aux cellules**

Microsoft Excel permet aux utilisateurs de formater les cellules en ajoutant des bordures. Le type de bordure dépend de l'endroit où elle est ajoutée. Par exemple, une bordure supérieure est celle ajoutée en haut d'une cellule. Les utilisateurs peuvent également modifier le style de ligne et la couleur des bordures.

Avec Aspose.Cells, les développeurs peuvent ajouter des bordures et personnaliser leur aspect de la même manière flexible que dans Microsoft Excel.

### **Ajout de bordures aux cellules**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) contient une collection [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fournit la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Chaque élément dans la collection [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

Aspose.Cells fournit la méthode [**GetStyle**](https://reference.aspose.com/cells/go-cpp/cell/getstyle/) dans la classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). La méthode [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) est utilisée pour définir le style de mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) fournit des propriétés pour ajouter des bordures aux cellules.

#### **Ajout de bordures à une cellule**

Les développeurs peuvent ajouter des bordures à une cellule en utilisant la collection [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) de l'objet [**Style**](https://reference.aspose.com/cells/go-cpp/style/). Le type de bordure est passé comme un index à la collection [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/). Tous les types de bordures sont prédéfinis dans l'énumération [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/).

**Énumération de bordure**

| **Types de bordure** | **Description** |
|------------------|-----------------|
| BordureInférieure     | Une ligne de bordure inférieure |
| DiagonaleVersLeBas     | Une ligne diagonale du haut gauche au bas droit |
| DiagonalUp       | Une ligne diagonale du coin inférieur gauche vers le haut droit |
| LeftBorder       | Une ligne de bordure gauche |
| RightBorder      | Une ligne de bordure droite |
| TopBorder        | Une ligne de bordure supérieure |

La collection [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) stocke toutes les bordures. Chaque bordure dans la collection [**GetBorders()**](https://reference.aspose.com/cells/go-cpp/style/getborders/) est représentée par un objet [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/) qui fournit deux propriétés, [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getcolor/) et [**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/) pour définir respectivement la couleur et le style de la ligne d'une bordure.

Pour définir la couleur d'une ligne de bordure, sélectionnez une couleur en utilisant l'énumération Color et assignez-la à la propriété Color de l'objet Border.

Le style de ligne de la bordure est défini en sélectionnant un style de ligne dans l'énumération [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/).

**Énumération de Type de Bordure Cellulaire**

| **Styles de ligne**       | **Description**               |
|------------------------|-------------------------------|
| DashDot               | Ligne mince en pointillés tirets |
| DashDotDot            | Ligne mince en pointillés tirets-dots |
| Dashed                | Ligne en pointillés |
| Dotted                | Ligne en dots |
| Double                | Double ligne |
| Hair                  | Ligne très fine |
| MediumDashDot         | Ligne moyenne en pointillés tirets |
| MediumDashDotDot      | Ligne moyenne en pointillés tirets-dots |
| MediumDashed          | Ligne moyenne en pointillés |
| None                  | Aucune ligne |
| Medium                | Ligne moyenne |
| SlantedDashDot        | Ligne oblique moyenne en pointillés tirets |
| Thick                 | Ligne épaisse |
| Thin                  | Ligne fine |

Sélectionnez l'un des styles de ligne, puis assignez-le à la propriété [**GetLineStyle()**](https://reference.aspose.com/cells/go-cpp/border/getlinestyle/) de l'objet [**Border**](https://reference.aspose.com/cells/go-cpp/border/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings.go" >}}
{{% alert color="primary" %}}

Vous devez définir à la fois le style de ligne et la couleur en même temps. Les deux lignes diagonales de la bordure doivent avoir le même style de ligne et la même couleur.

{{% /alert %}}

#### **Ajout de bordures à une plage de cellules**

Il est également possible d'ajouter des bordures à une plage de cellules plutôt qu'à une seule cellule. Pour ce faire, créez d'abord une plage de cellules en appelant la méthode [**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange/) de la collection [**Cells**](https://reference.aspose.com/cells/go-cpp/cells/). Elle prend les paramètres suivants :

- Première ligne, la première ligne de la plage.
- Première colonne, represente la première colonne de la plage.
- Nombre de lignes, le nombre de lignes dans la plage.
- Nombre de colonnes, le nombre de colonnes dans la plage.

La méthode [**CreateRange**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/) renvoie un objet [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/), qui contient la plage de cellules spécifiée. L'objet [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) fournit une méthode [**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/) qui accepte les paramètres suivants pour ajouter une bordure à cette plage de cellules :

- **Type de Bordure**, le type de bordure, sélectionné dans l'énumération [**BorderType**](https://reference.aspose.com/cells/go-cpp/bordertype/).
- **Style de Ligne**, le style de ligne de la bordure, sélectionné dans l'énumération [**CellBorderType**](https://reference.aspose.com/cells/go-cpp/cellbordertype/).
- **Couleur**, la couleur de la ligne, sélectionnée dans l'énumération Color.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-BorderSettings-1.go" >}}
