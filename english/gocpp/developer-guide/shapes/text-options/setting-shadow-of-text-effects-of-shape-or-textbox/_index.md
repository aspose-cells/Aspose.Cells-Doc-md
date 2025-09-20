---
title: Setting Shadow of Text Effects of Shape or TextBox with Golang via C++
linktitle: Setting Shadow of Text Effects
type: docs
weight: 250
url: /go-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Learn how to set the shadow of text effects for shapes or textboxes using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

You can set the **Shadow** of **Text Effects** of any Shape or TextBox. Please use the [**Shape.GetTextBody()**](https://reference.aspose.com/cells/go-cpp/shape/gettextbody/) property. It presents the setting of the shape's text and returns [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) objects. After accessing it, please set the **Shadow** via [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/) property. This property is of the type [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/) which has several values. Some of these are:

- OffsetDiagonalBottomRight
- OffsetBottom
- OffsetDiagonalTopRight
- InsideLeft
- InsideCenter
- PerspectiveDiagonalUpperLeft
- PerspectiveDiagonalLowerRight

{{% /alert %}}

The following code snippet demonstrates the use of [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/go-cpp/shadoweffect/getpresettype/) property to set shadow of text effects of Shape or TextBox.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingShadowOfTextEffectsOfShapeOrTextbox.go" >}}