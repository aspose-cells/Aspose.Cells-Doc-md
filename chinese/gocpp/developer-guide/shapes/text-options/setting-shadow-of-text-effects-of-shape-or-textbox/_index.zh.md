---
title: 设置 Golang 通过 C++ 形状或文本框文本效果的阴影
linktitle: 设置文本效果阴影
type: docs
weight: 250
url: /zh/go-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: 学习如何使用编号Aspose.Cells for C++为形状或文本框设置文本效果的阴影。
---

{{% alert color="primary" %}}

你可以为任何形状或文本框的**文本效果**设置**阴影**。请使用[**Shape.GetTextBody()**](https://reference.aspose.com/cells/go-cpp/shape/gettextbody/)属性，它会展示形状文本的设置并返回[**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/)对象。在访问后，请通过[**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)属性设置**阴影**。该属性类型为[**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/)，具有几个值，部分如下：

- 偏移对角线底部右
- 偏移底部
- 偏移对角线顶部右
- 内部左
- 内部中心
- 透视对角线左上
- 透视对角线右下

{{% /alert %}}

以下代码片段演示了如何使用[**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/go-cpp/shadoweffect/getpresettype/)属性为形状或文本框设置文本效果的阴影。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingShadowOfTextEffectsOfShapeOrTextbox.go" >}}
