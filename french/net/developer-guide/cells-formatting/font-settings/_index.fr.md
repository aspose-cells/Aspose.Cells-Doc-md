---
title: Paramètres de police
description: Aspose.Cells est une bibliothèque .NET permettant de travailler avec des feuilles de calcul. Il prend en charge la définition des paramètres de police des cellules, permettant aux utilisateurs de personnaliser le style de police et les propriétés des cellules. Cet article explique comment utiliser la bibliothèque Aspose.Cells pour définir les paramètres de police des cellules.
keywords: Aspose.Cells, Cells, Font Settings, Styles, Properties
type: docs
weight: 30
url: /fr/net/cells-font-settings/
---
{{% alert color="primary" %}}

L'apparence et la convivialité d'un texte peuvent être contrôlées en modifiant les paramètres de police. Les paramètres de police peuvent inclure le nom, le style, la taille, la couleur et d'autres effets des polices. Tout comme Microsoft Excel, Aspose.Cells prend également en charge la configuration des paramètres de police des cellules.

{{% /alert %}}

##  **Configuration des paramètres de police**

 Aspose.Cells propose un cours,[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. Le[**Cahier d'exercices**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fournit un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection. Chaque élément du[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) la collection représente un objet de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Aspose.Cells fournit le[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe'[**ObtenirStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) et[**Définir le style**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) méthodes utilisées pour obtenir et définir le style de formatage d’une cellule. Le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)La classe fournit des propriétés pour configurer les paramètres de police.

###  **Définition du nom de la police**

 Les développeurs peuvent appliquer n'importe quelle police au texte à l'intérieur d'une cellule en utilisant l'option[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objets[Nom](https://reference.aspose.com/cells/net/aspose.cells/font/properties/name)propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontName-1.cs" >}}

###  **Définition du style de police sur Gras**

 Les développeurs peuvent mettre le texte en gras en définissant le[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objets[**EstGras**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isbold)propriété à *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-SetFontStyle.cs" >}}

###  **Définition de la taille de la police**

Définissez la taille de la police avec le[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)objets[**Taille**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/size)propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontSize-SetFontSize.cs" >}}

###  **Définition de la couleur de la police**

Utilisez le[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objets[**Couleur**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)propriété pour définir la couleur de la police. Sélectionnez n'importe quelle couleur dans l'énumération Couleur (qui fait partie du framework .NET) et attribuez-la au[**Couleur**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/color)propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontColor-SetFontColor.cs" >}}

###  **Définition du type de soulignement de police**

Utilisez le[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)objets[**Souligner**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/underline)propriété pour souligner le texte. Aspose.Cells propose différents types de soulignement de police prédéfinis dans le[**PoliceSous-ligneType**](https://reference.aspose.com/cells/net/aspose.cells/fontunderlinetype) énumération.

|**Types de soulignement de police**|**Description**|
| :- | :- |
|Comptabilité|Un seul soulignement comptable|
|Double|Double soulignement|
|Double Comptabilité|Double comptabilité soulignée|
|Aucun|Pas de soulignement|
|Célibataire|Un seul soulignement|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontUnderlineType-1.cs" >}}

###  **Définition de l'effet de barré**

Appliquez le barré en définissant le[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) objets[**EstBiffé**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/isstrikeout)propriété à *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingStrikeOutEffect-SetStrikeout.cs" >}}

###  **Définition de l'effet d'indice**

Appliquez l'indice en définissant le[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)objets[**EstSubScript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issubscript)propriété à *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSubScriptEffect-SetSubscript.cs" >}}

###  **Définition de l'effet exposant sur la police**

 Les développeurs peuvent appliquer l'effet exposant sur la police en définissant le[**EstSuperscript**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/issuperscript) propriété du[**Style.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)s'opposer à *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingSuperScriptEffect-SetSuperscript.cs" >}}

##  **Sujets avancés**
- [Appliquer des effets d'exposant et d'indice aux polices](/cells/fr/net/apply-superscript-and-subscript-effects-on-fonts/)
- [Obtenir une liste des polices utilisées dans une feuille de calcul ou un classeur](/cells/fr/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)

