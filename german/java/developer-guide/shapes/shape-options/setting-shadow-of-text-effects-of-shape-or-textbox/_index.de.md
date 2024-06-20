---
title: Einstellen des Schattens von Texteffekten von Form oder TextBox
type: docs
weight: 670
url: /de/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}} 

Sie können den **Schatten** der **Texteffekte** einer beliebigen Form oder TextBox einstellen. Bitte verwenden Sie die [Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody)-Eigenschaft. Diese stellt die Einstellung des Textes der Form dar und gibt [FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection) zurück. Nach dem Zugriff auf [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) daraus, setzen Sie bitte den **Schatten** über die [FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType)-Eigenschaft. Diese Eigenschaft ist vom Typ [PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType), der mehrere Werte hat. Einige davon sind

- [OFFSET_DIAGONAL_UNTEN_RECHTS](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [OFFSET_UNTEN](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [OFFSET_DIAGONAL_OBEN_RECHTS](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [INNEN_LINKS](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [INNEN_CENTER](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [PERSPEKTIVE_DIAGONAL_OBEN_LINKS](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [PERSPEKTIVE_DIAGONAL_OBEN_RECHTS](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **Einstellen des Schattens von Texteffekten von Shape oder TextBox**
Der folgende Screenshot zeigt die [ausgegebene Excel-Datei](5473446.xlsx), die mit dem folgenden Beispielscode generiert wurde. Der Screenshot zeigt auch den Wert des **Schattens**, der als **Offset von unten** festgelegt wurde.

![todo:image_alt_text](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
