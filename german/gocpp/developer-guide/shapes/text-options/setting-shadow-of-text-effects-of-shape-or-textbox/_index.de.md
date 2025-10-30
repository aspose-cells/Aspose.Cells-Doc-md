---
title: Schatten der Texteffekte von Shape oder TextBox mit Golang via C++ einstellen
linktitle: Schatten der Texteffekte einstellen
type: docs
weight: 250
url: /de/go-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Lernen Sie, wie man den Schatten der Texteffekte für Formen oder Textboxen mit Aspose.Cells for C++ einstellt.
---

{{% alert color="primary" %}}

Sie können den **Schatten** der **Texts-Effekte** jeder Form oder Textbox einstellen. Bitte verwenden Sie die [**Shape.GetTextBody()**](https://reference.aspose.com/cells/go-cpp/shape/gettextbody/)-Eigenschaft. Diese stellt die Einstellung des Textes der Form dar und gibt [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/)-Objekte zurück. Nachdem Sie darauf zugegriffen haben, stellen Sie bitte den **Schatten** über die [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/)-Eigenschaft ein. Diese Eigenschaft ist vom Typ [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/) und hat mehrere Werte, darunter:

- OffsetDiagonal-unten-rechts
- OffsetBottom
- OffsetDiagonal-oben-rechts
- Innen-links
- Innen-mitte
- PerspektiveDiagonalObenLinks
- PerspektiveDiagonalUntenRechts

{{% /alert %}}

Das folgende Codesnippet zeigt die Verwendung der [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/go-cpp/shadoweffect/getpresettype/)-Eigenschaft zum Festlegen des Schattens der Texteffekte von Shape oder TextBox.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingShadowOfTextEffectsOfShapeOrTextbox.go" >}}
