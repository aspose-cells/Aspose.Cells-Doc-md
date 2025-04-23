---
title: 设置形状或文本框的文本效果的阴影
type: docs
weight: 250
url: /zh/python-net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

您可以设置任何形状或文本框的文本效果的阴影。请使用[**Shape.text_body**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_body)属性。它提供形状文本的设置，并返回[**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting)对象。访问后，请通过[**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type)属性设置**阴影**。这个属性是[**PresetShadowType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/presetshadowtype/)类型，具有多个值。其中一些是

- OFFSET_DIAGONAL_BOTTOM_RIGHT
- OFFSET_BOTTOM
- OFFSET_DIAGONAL_TOP_RIGHT
- 内侧左侧
- 内侧中心
- 透视对角线上方左侧
- 透视角朝右上方

{{% /alert %}}

以下代码片段演示了使用 [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type) 属性来设置形状或文本框的文本效果阴影。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SettingTextEffectsShadowOfShapeOrTextbox-1.py" >}}
