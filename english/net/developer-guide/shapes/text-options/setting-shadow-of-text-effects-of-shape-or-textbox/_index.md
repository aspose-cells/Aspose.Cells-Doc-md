---
title: Setting Shadow of Text Effects of Shape or TextBox
type: docs
weight: 250
url: /net/setting-shadow-of-text-effects-of-shape-or-textbox/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

You can set the **Shadow** of **Text Effects** for any Shape or TextBox. Please use the [**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody) property. It provides the settings of the shape's text and returns [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) objects. After accessing it, set the **Shadow** via the [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) property. This property is of the type [**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype), which has several values. Some of these are:

- OffsetDiagonalBottomRight
- OffsetBottom
- OffsetDiagonalTopRight
- InsideLeft
- InsideCenter
- PerspectiveDiagonalUpperLeft
- PerspectiveDiagonalLowerRight

{{% /alert %}}

The following code snippet demonstrates the use of the [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) property to set the shadow of text effects for a Shape or TextBox.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
