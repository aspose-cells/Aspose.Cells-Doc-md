---
title: Impostazione dell ombra degli effetti di testo della forma o del riquadro di testo
type: docs
weight: 250
url: /it/python-net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

È possibile impostare l'**Ombra** degli **Effetti di testo** di qualsiasi forma o casella di testo. Si prega di utilizzare la proprietà [**Shape.text_body**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_body). Essa rappresenta l'impostazione del testo della forma e restituisce oggetti [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting). Dopo avervi accesso, si prega di impostare l'**Ombra** tramite la proprietà [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type). Questa proprietà è del tipo [**PresetShadowType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/presetshadowtype/) che ha diversi valori. Alcuni di questi sono

- OFFSET_DIAGONAL_BOTTOM_RIGHT
- OFFSET_BOTTOM
- OFFSET_DIAGONAL_TOP_RIGHT
- INSIDE_LEFT
- INSIDE_CENTER
- PERSPECTIVE_DIAGONAL_UPPER_LEFT
- PERSPECTIVE_DIAGONAL_UPPER_RIGHT

{{% /alert %}}

Il seguente frammento di codice dimostra l'uso della proprietà [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type) per impostare l'ombra degli effetti di testo della forma o della casella di testo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SettingTextEffectsShadowOfShapeOrTextbox-1.py" >}}
