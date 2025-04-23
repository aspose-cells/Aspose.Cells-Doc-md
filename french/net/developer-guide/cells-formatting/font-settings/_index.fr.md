---
title: Paramètres de la police
description: Aspose.Cells est une bibliothèque .NET pour travailler avec des fichiers de feuille de calcul. Il prend en charge le paramétrage des paramètres de police des cellules, permettant aux utilisateurs de personnaliser le style et les propriétés de police des cellules. Cet article présente comment utiliser la bibliothèque Aspose.Cells pour définir les paramètres de police des cellules.
keywords: Aspose.Cells, Cellules, Paramètres de police, Styles, Propriétés
type: docs
weight: 30
url: /fr/net/cells-font-settings/
---

{{% alert color="primary" %}}

L'aspect et la sensation d'un texte peuvent être contrôlés en modifiant les paramètres de la police. Les paramètres de police peuvent inclure le nom, le style, la taille, la couleur et d'autres effets des polices. Tout comme Microsoft Excel, Aspose.Cells prend également en charge la configuration des paramètres de police des cellules.

{{% /alert %}}

## **Configuration des paramètres de police**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Chaque élément de la collection [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

Aspose.Cells fournit les méthodes [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) et [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) de la classe [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) utilisées pour obtenir et définir le style de mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) fournit des propriétés pour configurer les paramètres de police.

### **Définition du nom de la police**

Les développeurs peuvent appliquer n'importe quelle police au texte à l'intérieur d'une cellule en utilisant la propriété [Name](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name) de l'objet [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **Définition du style de police en gras**

Les développeurs peuvent mettre en gras le texte en définissant la propriété [**IsBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold) de l'objet [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) sur **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **Définition de la taille de police**

Définissez la taille de la police avec la propriété [**Size**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size) de l'objet [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **Définition de la couleur de police**

Utilisez la propriété [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color) de l'objet [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) pour définir la couleur de la police. Sélectionnez une couleur dans l'énumération Color (partie du framework .NET) et attribuez-la à la propriété [**Color**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **Définition du type de soulignement de la police**

Utilisez la propriété [**Underline**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline) de l'objet [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) pour souligner le texte. Aspose.Cells propose divers types de soulignement de police prédéfinis dans l'énumération [**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype).

|**Types de soulignement de police**|**Description**|
| :- | :- |
|Accounting|Un soulignement de comptabilité unique|
|Double|Double soulignement|
|DoubleAccounting|Double soulignement de comptabilité|
|None|Pas de soulignement|
|Single|Un seul soulignement|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **Définition de l'effet Barré**

Appliquer l'effet barré en définissant la propriété [**IsStrikeout**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout) de l'objet [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) à **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **Définir l'effet de bas indice**

Appliquer le bas indice en définissant la propriété [**IsSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript) de l'objet [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) à **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **Définition de l'effet exposant sur la police**

Les développeurs peuvent appliquer l'effet exposant sur la police en définissant la propriété [**IsSuperscript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) de l'objet [**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) à **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **Sujets avancés**
- [Appliquer les effets exposant et bas indice sur les polices](/cells/fr/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Obtenir une liste des polices utilisées dans une feuille de calcul ou un classeur](/cells/fr/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

{{< app/cells/assistant language="csharp" >}}
