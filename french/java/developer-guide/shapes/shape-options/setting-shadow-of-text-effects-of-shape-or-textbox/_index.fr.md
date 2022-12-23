---
title: Définition de l'ombre des effets de texte de Shape ou TextBox
type: docs
weight: 670
url: /fr/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}} 

 Vous pouvez régler le**Ombre** de**Effets de texte** de n'importe quelle forme ou zone de texte. Veuillez utiliser le[Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody) la propriété. Il présente le réglage du texte de la forme et renvoie[FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection) . Après avoir accédé[FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) à partir de celui-ci, veuillez régler le**Ombre** via[FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType) la propriété. Cette propriété est de type[Type d'ombre prédéfini](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType)qui a plusieurs valeurs. Certains d'entre eux sont

- [DÉCALAGE_DIAGONALE_EN BAS À DROITE](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [OFFSET_BOTTOM](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [DÉCALAGE_DIAGONALE_EN HAUT À DROITE](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [À L'INTÉRIEUR_GAUCHE](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [INSIDE_CENTER](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [LA PERSPECTIVE_DIAGONALE_EN HAUT À GAUCHE](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [LA PERSPECTIVE_DIAGONALE_EN HAUT À DROITE](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **Définition de l'ombre des effets de texte de Shape ou TextBox**
La capture d'écran suivante montre le[fichier excel de sortie](5473446.xlsx) généré avec l'exemple de code suivant. La capture d'écran montre également la valeur du**Ombre** qui a été défini comme**Bas décalé**.

![tâche : image_autre_texte](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
