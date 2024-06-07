---
title: 设置形状或文本框的文本效果阴影
type: docs
weight: 670
url: /zh/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}} 

您可以设置任何形状或文本框的**文本效果**的**阴影**。请使用[Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody)属性。它提供了形状文本的设置，并返回[FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection)。从中访问[FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting)，然后通过[FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType)属性设置**阴影**。该属性是[PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType)类型，具有多个值。其中一些是

- [OFFSET_DIAGONAL_BOTTOM_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [OFFSET_BOTTOM](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [OFFSET_DIAGONAL_TOP_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [INSIDE_LEFT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [INSIDE_CENTER](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [PERSPECTIVE_DIAGONAL_UPPER_LEFT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [PERSPECTIVE_DIAGONAL_UPPER_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **设置形状或文本框的文字效果的阴影**
以下屏幕截图显示了使用以下示例代码生成的[输出Excel文件](5473446.xlsx)。屏幕截图还显示了已设置为**偏移底部**的**阴影**的值。

![todo:image_alt_text](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
