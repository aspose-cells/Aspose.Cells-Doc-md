---
title: 设置形状或文本框的文本效果阴影
type: docs
weight: 250
url: /zh/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

您可以设置任何形状或文本框的**文本效果**的**阴影**。请使用[**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody)属性。它呈现形状文本的设置，并返回[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)对象。访问后，请使用[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype)属性设置**阴影**。此属性是[**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype)类型，具有多个值。其中一些是

- OffsetDiagonalBottomRight
- OffsetBottom
- OffsetDiagonalTopRight
- InsideLeft
- InsideCenter
- PerspectiveDiagonalUpperLeft
- PerspectiveDiagonalLowerRight

{{% /alert %}}

以下代码片段演示了使用[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype)属性设置形状或文本框的文本效果阴影。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
