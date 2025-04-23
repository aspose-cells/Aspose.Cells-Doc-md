---
title: シェイプまたはテキストボックスのテキスト効果の影の設定
type: docs
weight: 250
url: /ja/python-net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

図形またはテキストボックスの**影**や**テキストエフェクト**を設定することができます。[**Shape.text_body**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_body)プロパティを使用してください。これは、図形のテキストの設定を示し、[**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting)のオブジェクトを返します。これにアクセスした後は、[**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type)プロパティを使用して**影**を設定してください。このプロパティは、複数の値を持つ[**PresetShadowType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/presetshadowtype/)のタイプです。

- OFFSET_DIAGONAL_BOTTOM_RIGHT
- OFFSET_BOTTOM
- OFFSET_DIAGONAL_TOP_RIGHT
- INSIDE_LEFT
- INSIDE_CENTER
- PERSPECTIVE_DIAGONAL_UPPER_LEFT
- PERSPECTIVE_DIAGONAL_UPPER_RIGHT

{{% /alert %}}

次のコードスニペットは、ShapeまたはTextBoxのテキストエフェクトの影を設定するための[**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type)プロパティの使用方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SettingTextEffectsShadowOfShapeOrTextbox-1.py" >}}
