---
title: Paramètres de police
type: docs
weight: 30
url: /fr/net/cells-font-settings/
---
{{% alert color="primary" %}}

L'apparence d'un texte peut être contrôlée en modifiant les paramètres de police. Les paramètres de police peuvent inclure le nom, le style, la taille, la couleur et d'autres effets des polices. Tout comme Microsoft Excel, Aspose.Cells prend également en charge la configuration des paramètres de police des cellules.

{{% /alert %}}

## **Configuration des paramètres de police**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) le recueil. Chaque élément de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection représente un objet de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classer.

 Aspose.Cells fournit le[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classer'[**ObtenirStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) et[**DéfinirStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) méthodes utilisées pour obtenir et définir le style de formatage d'une cellule. La[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)La classe fournit des propriétés pour configurer les paramètres de police.

### **Définition du nom de la police**

 Les développeurs peuvent appliquer n'importe quelle police au texte à l'intérieur d'une cellule en utilisant le[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objets[Nom](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

### **Définition du style de police en gras**

 Les développeurs peuvent mettre le texte en gras en définissant le[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objets[**EstBold**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold) propriété à**vrai**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

### **Définition de la taille de la police**

Définissez la taille de la police avec le[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)objets[**Taille**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

### **Définition de la couleur de la police**

Utilisez le[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objets[**Couleur**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)propriété pour définir la couleur de la police. Sélectionnez n'importe quelle couleur dans l'énumération des couleurs (qui fait partie du cadre .NET) et attribuez-la au[**Couleur**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

### **Définition du type de soulignement de la police**

Utilisez le[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)objets[**Souligner**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)propriété pour souligner le texte. Aspose.Cells offre divers types de soulignement de police prédéfinis dans le[**FontUnderlineType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) énumération.

|**Types de soulignement de police**|**La description**|
|:- |:- |
|Comptabilité|Un soulignement comptable unique|
|Double|Double soulignement|
|DoubleComptabilité|Double soulignement comptable|
|Aucun|Pas de soulignement|
|Seul|Un seul soulignement|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

### **Réglage de l'effet barré**

Appliquez le barré en réglant le[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objets[**EstBarré**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)propriété à**vrai**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

### **Définition de l'effet d'indice**

Appliquer l'indice en définissant le[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)objets[**EstSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript) propriété à**vrai**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

### **Définition de l'effet Exposant sur la police**

 Les développeurs peuvent appliquer l'effet d'exposant sur la police en définissant le[**EstExposant**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) propriété de la[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) s'opposer à**vrai**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

## **Sujets avancés**
- [Appliquer des effets d'exposant et d'indice sur les polices](/cells/fr/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Obtenir une liste des polices utilisées dans une feuille de calcul ou un classeur](/cells/fr/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

