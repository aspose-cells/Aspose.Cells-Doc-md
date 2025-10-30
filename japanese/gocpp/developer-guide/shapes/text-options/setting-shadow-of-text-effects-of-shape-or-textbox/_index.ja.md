---
title: Golangを使ったC++経由でシェイプまたはテキストボックスのテキスト効果の影を設定する
linktitle: 文字効果の shadow を設定する
type: docs
weight: 250
url: /ja/go-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Aspose.Cells for C++を使用して、図形やテキストボックスの文字効果の影を設定する方法を学びます。
---

{{% alert color="primary" %}}

任意の図形やテキストボックスのテキスト効果の**Shadow**を設定できます。[**Shape.GetTextBody()**](https://reference.aspose.com/cells/go-cpp/shape/gettextbody/)プロパティを使用してください。このプロパティは図形のテキスト設定を示し、[**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/)オブジェクトを返します。アクセス後、[**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)プロパティを介して**Shadow**を設定してください。このプロパティは[**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/)型で、いくつかの値を持ちます。例として：

- DiagonalBottomRightのOffset
- ボトムのオフセット
- DiagonalTopRightのOffset
- 左内部
- 中央内部
- PerspectiveDiagonalUpperLeft
- PerspectiveDiagonalLowerRight

{{% /alert %}}

以下のコードスニペットは、[**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/go-cpp/shadoweffect/getpresettype/) プロパティを使用してShapeまたはTextBoxのテキスト効果のシャドウを設定する例です。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingShadowOfTextEffectsOfShapeOrTextbox.go" >}}
