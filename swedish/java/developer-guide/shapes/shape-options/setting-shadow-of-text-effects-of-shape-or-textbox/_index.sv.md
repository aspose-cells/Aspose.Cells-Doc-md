---
title: Inställning av skugga för texteffekter av form eller textruta
type: docs
weight: 670
url: /sv/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}} 

Du kan ställa in **Skugga** för **Texteffekter** av en form eller textruta. Använd egenskapen [Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody). Den representerar inställningarna för texten i formen och returnerar [FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection). Efter att ha fått åtkomst till [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) från det, ställ in **Skugga** med hjälp av [FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType) egenskapen. Denna egenskap är av typen[PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType) som har flera värden. Några av dessa är

- [OFFSET_DIAGONAL_BOTTOM_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET-DIAGONAL-BOTTOM-RIGHT)
- [OFFSET_BOTTOM](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET-BOTTOM)
- [OFFSET_DIAGONAL_TOP_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET-DIAGONAL-TOP-RIGHT)
- [INSIDE_LEFT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE-LEFT)
- [INSIDE_CENTER](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE-CENTER)
- [PERSPECTIVE_DIAGONAL_UPPER_LEFT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE-DIAGONAL-UPPER-LEFT)
- [PERSPECTIVE_DIAGONAL_UPPER_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE-DIAGONAL-UPPER-RIGHT)

{{% /alert %}} 
## **Inställning av skugga för texteffekter av form eller textruta**
Följande skärmdump visar [utfilens excel-fil](5473446.xlsx) som genererats med följande exempelkod. Skärmdumpen visar också värdet av **Skugga** som har ställts in som **Offset Bottom**.

![todo:image_alt_text](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
{{< app/cells/assistant language="java" >}}
