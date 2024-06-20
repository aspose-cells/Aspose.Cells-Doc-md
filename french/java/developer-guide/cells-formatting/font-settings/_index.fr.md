---
title: Gestion des paramètres de police
linktitle: Paramètres de la police
type: docs
weight: 20
url: /fr/java/dealing-with-font-settings/
---

{{% alert color="primary" %}} 

L'apparence et le style du texte peuvent être contrôlés en modifiant ses paramètres de police. Ces paramètres de police peuvent inclure le nom, le style, la taille, la couleur et d'autres effets des polices comme indiqué ci-dessous dans la figure :

**Paramètres de police dans Microsoft Excel** 

![todo:image_alt_text](dealing-with-font-settings_1.png)

Tout comme Microsoft Excel, Aspose.Cells prend également en charge la configuration des paramètres de police des cellules.

{{% /alert %}} 
## **Configuration des paramètres de police**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contient une [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fournit une collection de [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). Chaque élément de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) représente un objet de la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Aspose.Cells fournit la méthode [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) de la classe [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell), utilisée pour définir la mise en forme d'une cellule. De plus, l'objet de la classe [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) fournit des propriétés pour configurer les paramètres de la police.

Cet article montre comment :

- [Appliquer une police spécifique au texte.](/cells/fr/java/dealing-with-font-settings/)
- [Définir le texte en gras](/cells/fr/java/dealing-with-font-settings/).
- [Définir la taille de la police](/cells/fr/java/dealing-with-font-settings/).
- [Définir la couleur de la police](/cells/fr/java/dealing-with-font-settings/).
- [Souligner le texte](/cells/fr/java/dealing-with-font-settings/).
- [Barrer le texte](/cells/fr/java/dealing-with-font-settings/).
- [Définir le texte en indice](/cells/fr/java/dealing-with-font-settings/).
- [Définir le texte en exposant](/cells/fr/java/dealing-with-font-settings/).
### **Définition du nom de la police**
Appliquer une police spécifique au texte dans les cellules en utilisant la propriété [setName](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name) de l'objet [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **Définition du style de police en gras**
Mettre le texte en gras en définissant la propriété [setBold](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) de l'objet [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) sur **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **Définition de la taille de police**
Définir la taille de la police en utilisant la propriété [setSize](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size) de l'objet [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **Définition du type de soulignement de la police**
Souligner le texte avec la propriété [setUnderline](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) de l'objet [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font). Aspose.Cells offre différents types de soulignement de police prédéfinis dans l'énumération [FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType).

|**Types de soulignement de police**|**Description**|
| :- | :- |
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|Pas de soulignement|
|[SINGLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|Un seul soulignement|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|Double souligné|
|[ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|Un seul souligné comptable|
|[DOUBLE_ACCOUNTING](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|Double souligné comptable|
|[DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|Souligné en pointillés|
|[DASH_DOT_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|Souligné épais trait-point-point|
|[DASH_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|Souligné épais trait-point|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|Souligné épais pointillé|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|Souligné long pointillé|
|[DASH_LONG_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|Souligné épais long pointillé|
|[DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|Souligné trait-point|
|[DOT_DOT_DASH](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|Souligné trait-point-point|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|Souligné en pointillés|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|Souligné épais en pointillés|
|[HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|Souligné épais|
|[WAVE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|Souligné ondulé|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|Double souligné ondulé|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|Souligné ondulé épais|
|[WORDS](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|Souligné uniquement pour les caractères non-espaces|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **Définition de la couleur de police**
Définir la couleur de la police avec l' [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objet's [setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color) propriété. Sélectionnez une couleur quelconque dans l'énumération [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)  et attribuez la couleur sélectionnée à l' [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objet's [setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **Paramétrage de l'effet de barré sur le texte**
Barrer le texte avec l'objet [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) et la propriété [setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **Paramétrage de l'indice**
Mettre le texte en exposant en utilisant l'objet [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) et la propriété [setSubscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **Paramétrage de l'indice supérieur**
Appliquer un exposant au texte avec l'objet [Font](https://reference.aspose.com/cells/java/com.aspose.cells/Font) et la propriété [setSuperscript](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **Sujets avancés**
- [Appliquer les effets exposant et bas indice sur les polices](/cells/fr/java/apply-superscript-and-subscript-effects-on-fonts/)
- [Obtenir une liste des polices utilisées dans une feuille de calcul ou un classeur](/cells/fr/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
