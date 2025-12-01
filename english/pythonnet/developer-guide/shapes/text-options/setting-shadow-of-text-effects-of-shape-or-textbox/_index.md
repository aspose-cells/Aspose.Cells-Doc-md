---
title: Setting Shadow of Text Effects of Shape or TextBox
type: docs
weight: 250
url: /python-net/setting-shadow-of-text-effects-of-shape-or-textbox/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

You can set the **Shadow** of **Text Effects** of any Shape or TextBox. Please use the [**Shape.text_body**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_body) property. It presents the setting of the shape's text and returns [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) objects. After accessing it, please set the **Shadow** via [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type) property. This property is of the type [**PresetShadowType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/presetshadowtype/) which has several values. Some of these are

- OFFSET_DIAGONAL_BOTTOM_RIGHT
- OFFSET_BOTTOM
- OFFSET_DIAGONAL_TOP_RIGHT
- INSIDE_LEFT
- INSIDE_CENTER
- PERSPECTIVE_DIAGONAL_UPPER_LEFT
- PERSPECTIVE_DIAGONAL_UPPER_RIGHT

{{% /alert %}}

The following code snippet demonstrates the use of [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type) property to set shadow of text effects of Shape or TextBox.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SettingTextEffectsShadowOfShapeOrTextbox-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
