---
title: Festlegen des Schattens von Texteffekten von Form oder TextBox
type: docs
weight: 670
url: /de/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}} 

 Sie können die einstellen**Schatten** von**Texteffekte** einer beliebigen Form oder TextBox. Bitte verwenden Sie die[Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody) Eigentum. Es zeigt die Einstellung des Textes der Form und kehrt zurück[FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection) . Nach dem Zugriff[Schrifteinstellung](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) daraus bitte die einstellen**Schatten** über[FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType) Eigentum. Diese Eigenschaft ist vom Typ[PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType)die mehrere Werte hat. Einige davon sind

- [VERSATZ_DIAGONALE_UNTEN RECHTS](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [OFFSET_UNTEN](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [VERSATZ_DIAGONALE_OBEN RECHTS](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [INNEN_LINKS](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [INNEN_MITTE](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [PERSPEKTIVE_DIAGONALE_OBEN LINKS](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [PERSPEKTIVE_DIAGONALE_OBEN RECHTS](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **Festlegen des Schattens von Texteffekten von Form oder TextBox**
 Der folgende Screenshot zeigt die[Excel-Datei ausgeben](5473446.xlsx) generiert mit dem folgenden Beispielcode. Der Screenshot zeigt auch den Wert der**Schatten** was eingestellt wurde als**Versatz unten**.

![todo: Bild_alt_Text](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
