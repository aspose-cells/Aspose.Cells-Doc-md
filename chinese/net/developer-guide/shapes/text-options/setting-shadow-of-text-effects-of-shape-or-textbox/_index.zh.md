---
title: 设置 Shape 或 TextBox 的文字效果的阴影
type: docs
weight: 250
url: /zh/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}}

您可以设置**阴影**的**文字效果**任何形状或文本框。请使用[**形状.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody)财产。它呈现形状文本的设置并返回[**字体设置**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)对象。访问后，请设置**阴影**通过[**字体设置.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype)财产。该属性属于[**预设阴影类型**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype)它有几个值。其中一些是

- 偏移对角线底部右
- 偏移底部
- 偏移对角线右上角
- 内左
- 内部中心
- 透视对角线左上角
- 透视对角线下右

{{% /alert %}}

下面的代码片段演示了使用[**字体设置.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype)属性设置 Shape 或 TextBox 的文本效果的阴影。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
