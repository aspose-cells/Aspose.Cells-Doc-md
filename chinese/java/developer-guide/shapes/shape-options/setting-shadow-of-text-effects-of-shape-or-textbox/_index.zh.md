---
title: 设置形状或文本框的文本效果的阴影
type: docs
weight: 670
url: /zh/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}} 

您可以设置任何形状或文本框的**文本效果**的**阴影**。请使用[Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody)属性。它表示形状文本的设置并返回[FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection)。在访问其中的[FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting)后，请通过[FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType)属性设置**阴影**。此属性是[PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType)类型，具有多个值。其中一些是

- [斜向下右侧偏移](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET-DIAGONAL-BOTTOM-RIGHT)
- [向下偏移](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET-BOTTOM)
- [斜向上右侧偏移](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET-DIAGONAL-TOP-RIGHT)
- [内部左侧](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE-LEFT)
- [内部中心](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE-CENTER)
- [透视斜向左上](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE-DIAGONAL-UPPER-LEFT)
- [透视斜向右上](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE-DIAGONAL-UPPER-RIGHT)

{{% /alert %}} 
## **设置形状或文本框的文本效果阴影**
以下屏幕截图显示了使用以下示例代码生成的[输出Excel文件](5473446.xlsx)。屏幕截图还显示了已设置为**向下偏移**的**阴影**的值。

![todo:image_alt_text](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
{{< app/cells/assistant language="java" >}}
