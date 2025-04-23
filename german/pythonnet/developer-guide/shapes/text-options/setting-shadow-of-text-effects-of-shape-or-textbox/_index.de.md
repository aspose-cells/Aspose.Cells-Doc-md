---
title: Einstellen des Schattens von Texteffekten von Form oder TextBox
type: docs
weight: 250
url: /de/python-net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

Sie können den **Schatten** der **Texteffekte** einer beliebigen Form oder Textbox einstellen. Bitte verwenden Sie die Eigenschaft [**Shape.text_body**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_body). Sie präsentiert die Einstellung des Texts der Form und gibt [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) Objekte zurück. Nachdem Sie darauf zugegriffen haben, legen Sie bitte über die Eigenschaft [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type) den **Schatten** fest. Diese Eigenschaft ist vom Typ [**PresetShadowType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/presetshadowtype/), der verschiedene Werte enthält. Einige davon sind

- OFFSET_DIAGONAL_BOTTOM_RIGHT
- OFFSET_BOTTOM
- OFFSET_DIAGONAL_TOP_RIGHT
- INNEN_LINKS
- INNEN_MITTIG
- PERSPEKTIVE_DIAGONAL_OBEN_LINKS
- PERSPEKTIVE_DIAGONAL_OBEN_RECHTS

{{% /alert %}}

Der folgende Codeausschnitt veranschaulicht die Verwendung der [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type) Eigenschaft zum Einstellen des Schattens von Texteffekten einer Form oder Textbox.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SettingTextEffectsShadowOfShapeOrTextbox-1.py" >}}
