---
title: 设置形状或文本框的文本效果的阴影
type: docs
weight: 250
url: /zh/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

您可以设置任何形状或文本框的文本效果的阴影。请使用[**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody)属性。它提供形状文本的设置，并返回[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)对象。访问后，请通过[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype)属性设置**阴影**。这个属性是[**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype)类型，具有多个值。其中一些是

- 偏移对角线底部右
- 偏移底部
- 偏移对角线顶部右
- 内部左
- 内部中心
- 透视对角线左上
- 透视对角线右下

{{% /alert %}}

以下代码片段演示了使用 [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) 属性来设置形状或文本框的文本效果阴影。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
