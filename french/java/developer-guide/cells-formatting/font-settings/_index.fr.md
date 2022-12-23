---
title: Gestion des paramètres de police
linktitle: Paramètres de police
type: docs
weight: 20
url: /fr/java/dealing-with-font-settings/
---
{{% alert color="primary" %}} 

L'aspect et la convivialité du texte peuvent être contrôlés en modifiant ses paramètres de police. Ces paramètres de police peuvent inclure le nom, le style, la taille, la couleur et d'autres effets des polices, comme indiqué ci-dessous dans la figure :

**Paramètres de police dans Microsoft Excel** 

![tâche : image_autre_texte](dealing-with-font-settings_1.png)

Tout comme Microsoft Excel, Aspose.Cells prend également en charge la configuration des paramètres de police des cellules.

{{% /alert %}} 
## **Configuration des paramètres de police**
 Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) qui représente un fichier Excel Microsoft. Le[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) classe contient un[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classe. Le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe offre une[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) le recueil. Chaque élément de la[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) collection représente un objet de la[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classe.

 Aspose.Cells fournit le[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe'[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ), utilisée pour définir la mise en forme d'une cellule. Aussi, l'objet de la[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)La classe fournit des propriétés pour configurer les paramètres de police.

Cet article montre comment :

- [Appliquer une police spécifique au texte.](/cells/fr/java/dealing-with-font-settings/)
- [Mettre le texte en gras](/cells/fr/java/dealing-with-font-settings/).
- [Définir la taille de la police](/cells/fr/java/dealing-with-font-settings/).
- [Définir la couleur de la police](/cells/fr/java/dealing-with-font-settings/).
- [Texte souligné](/cells/fr/java/dealing-with-font-settings/).
- [Texte barré](/cells/fr/java/dealing-with-font-settings/).
- [Définir le texte en indice](/cells/fr/java/dealing-with-font-settings/).
- [Mettre le texte en exposant](/cells/fr/java/dealing-with-font-settings/).
### **Définition du nom de la police**
 Appliquer une police spécifique au texte des cellules à l'aide de la[Police de caractère](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objets[setName](https://reference.aspose.com/cells/java/com.aspose.cells/font#Name)la propriété.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontName-SettingFontName.java" >}}
### **Définition du style de police en gras**
 Mettez le texte en gras en définissant le[Police de caractère](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objets[setBold](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsBold) propriété à**vrai**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-SettingFontStyle-1.java" >}}
### **Définition de la taille de la police**
 Définissez la taille de la police à l'aide de la[Police de caractère](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objets[setSize](https://reference.aspose.com/cells/java/com.aspose.cells/font#Size)la propriété.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontSize-SetFontSize.java" >}}
### **Définition du type de soulignement de la police**
 Souligner le texte avec le[Police de caractère](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objets[setUnderline](https://reference.aspose.com/cells/java/com.aspose.cells/font#Underline) la propriété. Aspose.Cells offre divers types de soulignement de police prédéfinis dans le[FontUnderlineType](https://reference.aspose.com/cells/java/com.aspose.cells/FontUnderlineType)énumération.

|**Types de soulignement de police**|**Description**|
|:- |:- |
|[RIEN](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#NONE)|Pas de soulignement|
|[CÉLIBATAIRE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#SINGLE)|Un seul soulignement|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE)|Double soulignement|
|[COMPTABILITÉ](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#ACCOUNTING)|Un soulignement comptable unique|
|[DOUBLE_COMPTE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOUBLE_ACCOUNTING)|Double soulignement comptable|
|[SE PRÉCIPITER](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH)|Souligné en pointillé|
|[SE PRÉCIPITER_POINT_DOT_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_DOT_HEAVY)|Soulignement épais tiret-point-point|
|[SE PRÉCIPITER_POINT_LOURD](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_DOT_HEAVY)|Soulignement épais tiret-point|
|[DASHED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASHED_HEAVY)|Soulignement épais en pointillés|
|[DASH_LONG](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG)|Long souligné en pointillés|
|[SE PRÉCIPITER_LONG_LOURD](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DASH_LONG_HEAVY)|Soulignement long et épais en pointillés|
|[POINT_TIRET](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DASH)|Souligné tiret-point|
|[POINT_POINT_SE PRÉCIPITER](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOT_DOT_DASH)|Tiret-Point-Point Souligné|
|[POINTÉ](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED)|Souligné en pointillé|
|[DOTTED_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#DOTTED_HEAVY)|Soulignement pointillé épais|
|[LOURD](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#HEAVY)|Soulignement épais|
|[VAGUE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVE)|Soulignement ondulé|
|[WAVY_DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_DOUBLE)|Souligné double vague|
|[WAVY_HEAVY](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WAVY_HEAVY)|Soulignement de vague lourde|
|` `[MOTS](https://reference.aspose.com/cells/java/com.aspose.cells/fontunderlinetype#WORDS)|Souligner les caractères autres que l'espace uniquement|
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontUnderlineType-SettingFontUnderlineType.java" >}}



### **Définition de la couleur de la police**
 Définissez la couleur de la police avec le[Police de caractère](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objets[setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color) la propriété. Sélectionnez n'importe quelle couleur dans la[Couleur](https://reference.aspose.com/cells/java/com.aspose.cells/Color) énumération et affecter la couleur sélectionnée à la[Police de caractère](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objets[setColor](https://reference.aspose.com/cells/java/com.aspose.cells/font#Color).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetFontColor-SetFontColor.java" >}}



### **Définition de l'effet barré sur le texte**
 Texte barré avec le[Police de caractère](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objets[setStrikeout](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsStrikeout)la propriété.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingStrikeOutEffect-SettingStrikeOutEffect.java" >}}



### **Définition de l'indice**
 Mettre le texte en exposant en utilisant le[Police de caractère](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objets[setIndice](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSubscript)la propriété.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSubscript-SetSubscript.java" >}}



### **Définition de l'exposant**
 Appliquer un exposant au texte avec le[Police de caractère](https://reference.aspose.com/cells/java/com.aspose.cells/Font) objets[setExposant](https://reference.aspose.com/cells/java/com.aspose.cells/font#IsSuperscript)la propriété.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetSuperscript-SetSuperscript.java" >}}

## **Sujets avancés**
- [Appliquer des effets d'exposant et d'indice sur les polices](/cells/fr/java/apply-superscript-and-subscript-effects-on-fonts/)
- [Obtenir une liste des polices utilisées dans une feuille de calcul ou un classeur](/cells/fr/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
