---
title: Inställning av skugga för texteffekter av form eller textruta
type: docs
weight: 250
url: /sv/python-net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

Du kan ställa in **Skugga** för **Texteffekter** av vilken form eller textruta som helst. Använd egenskapen [**Shape.text_body**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_body). Den presenterar inställningen för formens text och returnerar [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) objekt. Efter åtkomst, ställ in **Skugga** via egenskapen [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type). Denna egenskap är av typen [**PresetShadowType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/presetshadowtype/) som har flera värden. Några av dessa är

- OFFSET_DIAGONAL_BOTTOM_RIGHT
- OFFSET_BOTTOM
- OFFSET_DIAGONAL_TOP_RIGHT
- INSIDE_LEFT
- INSIDE_CENTER
- PERSPECTIVE_DIAGONAL_UPPER_LEFT
- PERSPECTIVE_DIAGONAL_UPPER_RIGHT

{{% /alert %}}

Följande kodsnutt illustrerar användningen av egenskapen [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type) för att ställa in skugga för texteffekter av en form eller textruta.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SettingTextEffectsShadowOfShapeOrTextbox-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
