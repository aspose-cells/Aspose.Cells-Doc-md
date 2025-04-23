---
title: Paramètres de la police
description: Aspose.Cells est une bibliothèque Python pour travailler avec des fichiers de feuilles de calcul. Elle supporte la définition des paramètres de police des cellules, permettant aux utilisateurs de personnaliser le style et les propriétés de la police des cellules. Cet article présente comment utiliser la bibliothèque Aspose.Cells pour Python via .NET pour définir les paramètres de police des cellules.
keywords: Aspose.Cells pour Python via .NET, Cellules, Paramètres de police, Styles, Propriétés
type: docs
weight: 30
url: /fr/python-net/cells-font-settings/
---

{{% alert color="primary" %}}

L'apparence du texte peut être contrôlée en modifiant les paramètres de police. Les paramètres de police peuvent inclure le nom, le style, la taille, la couleur et autres effets de la police. Tout comme Microsoft Excel, Aspose.Cells pour Python via .NET supporte également la configuration des paramètres de police des cellules.

{{% /alert %}}

## **Configuration des paramètres de police**

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Chaque élément dans la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells fournit les méthodes [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) et [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) de la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) utilisées pour obtenir et définir le style de mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) fournit des propriétés pour configurer les paramètres de police.

### **Définition du nom de la police**

Les développeurs peuvent appliquer n'importe quelle police au texte dans une cellule en utilisant la propriété [**name**](https://reference.aspose.com/cells/python-net/aspose.cells/font/name/) de l'objet [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontName-1.py" >}}

### **Définition du style de police en gras**

Les développeurs peuvent mettre en gras le texte en définissant la propriété [**is_bold**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_bold) de l'objet [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) sur **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontStyle.py" >}}

### **Définition de la taille de police**

Définissez la taille de la police avec la propriété [**size**](https://reference.aspose.com/cells/python-net/aspose.cells/font/size) de l'objet [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontSize.py" >}}

### **Définition de la couleur de police**

Utilisez la propriété [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color) de l'objet [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) pour définir la couleur de la police. Sélectionnez une couleur dans l'énumération Color (partie du framework .NET) et attribuez-la à la propriété [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/color).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetFontColor.py" >}}

### **Définition du type de soulignement de la police**

Utilisez la propriété [**underline**](https://reference.aspose.com/cells/python-net/aspose.cells/font/underline) de l'objet [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) pour souligner le texte. Aspose.Cells pour Python via .NET offre divers types de soulignement prédéfinis dans l'énumération [**FontUnderlineType**](https://reference.aspose.com/cells/python-net/aspose.cells/fontunderlinetype).

|**Types de soulignement de police**|**Description**|
| :- | :- |
|COMPTE|Un seul soulignement comptable|
|DOUBLE|Soulignement double|
|DOUBLE_ACCOUNTING|Soulignement comptable double|
|NONE|Pas de soulignement|
|SINGLE|Un seul soulignement|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontUnderlineType-1.py" >}}

### **Définition de l'effet Barré**

Appliquer l'effet barré en définissant la propriété [**is_strikeout**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_strikeout) de l'objet [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) à **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetStrikeout.py" >}}

### **Définir l'effet de bas indice**

Appliquer le bas indice en définissant la propriété [**is_subscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_subscript/) de l'objet [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) à **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSubscript.py" >}}

### **Définition de l'effet exposant sur la police**

Les développeurs peuvent appliquer l'effet exposant sur la police en définissant la propriété [**is_superscript**](https://reference.aspose.com/cells/python-net/aspose.cells/font/is_superscript) de l'objet [**Style.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) à **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetSuperscript.py" >}}

## **Sujets avancés**
- [Appliquer les effets exposant et bas indice sur les polices](/cells/fr/python-net/apply-superscript-and-subscript-effects-on-fonts/)
- [Obtenir une liste des polices utilisées dans une feuille de calcul ou un classeur](/cells/fr/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)


