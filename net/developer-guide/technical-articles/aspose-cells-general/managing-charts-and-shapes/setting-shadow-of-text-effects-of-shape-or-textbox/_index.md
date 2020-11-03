---
title: Setting Shadow of Text Effects of Shape or TextBox
type: docs
weight: 250
url: /net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

You can set the **Shadow** of **Text Effects** of any Shape or TextBox. Please use the [**Shape.TextBody**](https://apireference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody) property. It presents the setting of the shape's text and returns [**FontSetting**](https://apireference.aspose.com/cells/net/aspose.cells/fontsetting) objects. After accessing it, please set the **Shadow** via [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://apireference.aspose.com/net/cells/aspose.cells.drawing/shadoweffect/properties/presettype) property. This property is of the type [**PresetShadowType**](https://apireference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype) which has several values. Some of these are

- OffsetDiagonalBottomRight
- OffsetBottom
- OffsetDiagonalTopRight
- InsideLeft
- InsideCenter
- PerspectiveDiagonalUpperLeft
- PerspectiveDiagonalLowerRight

{{% /alert %}}

The following code snippet demonstrates the use of [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://apireference.aspose.com/net/cells/aspose.cells.drawing/shadoweffect/properties/presettype) property to set shadow of text effects of Shape or TextBox.

{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
