---
title: Ställa in skugga av text Effekter av form eller textruta
type: docs
weight: 670
url: /sv/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}} 

 Du kan ställa in**Skugga** av**Texteffekter** av valfri form eller textruta. Vänligen använd[Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody) fast egendom. Den presenterar inställningen av formens text och returnerar[FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection) . Efter åtkomst[FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) från det, ställ in**Skugga** via[FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType) fast egendom. Denna egenskap är av typen[PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType)som har flera värden. Några av dessa är

- [OFFSET_DIAGONAL_NERE TILL HÖGER](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [OFFSET_BOTTOM](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [OFFSET_DIAGONAL_ÖVERST TILL HÖGER](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [INSIDE_LEFT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [INSIDE_CENTER](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [PERSPEKTIV_DIAGONAL_ÖVRE VÄNSTER](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [PERSPEKTIV_DIAGONAL_UPP TILL HÖGER](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **Ställa in skugga av text Effekter av form eller textruta**
 Följande skärmdump visar[output excel-fil](5473446.xlsx) genereras med följande exempelkod. Skärmdumpen visar också värdet på**Skugga** som har satts som**Offset Botten**.

![todo:image_alt_text](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
