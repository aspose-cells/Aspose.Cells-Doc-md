---
title: シェイプまたはテキストボックスのテキスト効果の影の設定
type: docs
weight: 250
url: /ja/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

図形またはテキストボックスの**影**や**テキストエフェクト**を設定することができます。[**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody)プロパティを使用してください。これは、図形のテキストの設定を示し、[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)のオブジェクトを返します。これにアクセスした後は、[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype)プロパティを使用して**影**を設定してください。このプロパティは、複数の値を持つ[**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype)のタイプです。

- DiagonalBottomRightのOffset
- ボトムのオフセット
- DiagonalTopRightのOffset
- 左内部
- 中央内部
- PerspectiveDiagonalUpperLeft
- PerspectiveDiagonalLowerRight

{{% /alert %}}

次のコードスニペットは、ShapeまたはTextBoxのテキストエフェクトの影を設定するための[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype)プロパティの使用方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
