---
title: Einstellen des Schattens von Texteffekten von Form oder TextBox
type: docs
weight: 250
url: /de/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

Sie können den **Schatten** der **Texteffekte** einer beliebigen Form oder Textbox einstellen. Bitte verwenden Sie die Eigenschaft [**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody). Sie präsentiert die Einstellung des Texts der Form und gibt [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) Objekte zurück. Nachdem Sie darauf zugegriffen haben, legen Sie bitte über die Eigenschaft [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) den **Schatten** fest. Diese Eigenschaft ist vom Typ [**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype), der verschiedene Werte enthält. Einige davon sind

- OffsetDiagonal-unten-rechts
- OffsetBottom
- OffsetDiagonal-oben-rechts
- Innen-links
- Innen-mitte
- PerspektiveDiagonalObenLinks
- PerspektiveDiagonalUntenRechts

{{% /alert %}}

Der folgende Codeausschnitt veranschaulicht die Verwendung der [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) Eigenschaft zum Einstellen des Schattens von Texteffekten einer Form oder Textbox.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
