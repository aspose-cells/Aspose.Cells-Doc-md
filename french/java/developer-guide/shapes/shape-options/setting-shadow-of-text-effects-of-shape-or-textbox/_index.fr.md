---
title: Définir l ombre des effets de texte de la forme ou de la zone de texte
type: docs
weight: 670
url: /fr/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}} 

Vous pouvez définir l'**ombre** des **effets de texte** de n'importe quelle forme ou zone de texte. Veuillez utiliser la propriété [Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody). Elle présente le réglage du texte de la forme et renvoie [FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection). Après avoir accédé à [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) à partir de celui-ci, veuillez définir l'**ombre** via la propriété [FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType). Cette propriété est de type [PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType) qui a plusieurs valeurs. Certaines de celles-ci sont

- [OFFSET_DIAGONAL_BOTTOM_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [OFFSET_BOTTOM](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [OFFSET_DIAGONAL_TOP_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [INSIDE_LEFT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [INSIDE_CENTER](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [PERSPECTIVE_DIAGONAL_UPPER_LEFT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [PERSPECTIVE_DIAGONAL_UPPER_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **Définir l'ombre des effets de texte de forme ou de zone de texte**
La capture d'écran suivante montre le [fichier Excel de sortie](5473446.xlsx) généré avec le code d'exemple suivant. La capture d'écran montre également la valeur de l'**Ombre** qui a été définie comme **Décalage vers le bas**.

![todo:image_alt_text](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
