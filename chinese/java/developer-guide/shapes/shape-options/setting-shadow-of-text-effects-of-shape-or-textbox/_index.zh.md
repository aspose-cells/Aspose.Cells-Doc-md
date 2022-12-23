---
title: 设置 Shape 或 TextBox 的文字效果的阴影
type: docs
weight: 670
url: /zh/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}} 

您可以设置**阴影**的**文字效果**任何形状或文本框。请使用[形状.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody)财产。它呈现形状文本的设置并返回[字体设置集合](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection).访问后[字体设置](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting)从中，请设置**阴影**通过[FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType)财产。这个属性是类型[预设阴影类型](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType)它有几个值。其中一些是

- [抵消_对角线_底部_右侧](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [OFFSET_BOTTOM](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [抵消_对角线_右上](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [INSIDE_LEFT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [INSIDE_CENTER 内部](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [看法_对角线_左上](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [看法_对角线_右上方](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **设置 Shape 或 TextBox 的文字效果的阴影**
以下屏幕截图显示了[输出excel文件](5473446.xlsx)使用以下示例代码生成。屏幕截图还显示了**阴影**已设置为**偏移底部**.

![待办事项：图片_替代_文本](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
