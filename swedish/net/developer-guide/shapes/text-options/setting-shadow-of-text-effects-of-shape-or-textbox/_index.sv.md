---
title: Ställa in skugga av text Effekter av form eller textruta
type: docs
weight: 250
url: /sv/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}}

 Du kan ställa in**Skugga** av**Texteffekter** av valfri form eller textruta. Vänligen använd[**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody) fast egendom. Den presenterar inställningen av formens text och returnerar[**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) föremål. När du har kommit åt det, ställ in**Skugga** via[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) fast egendom. Denna egenskap är av typen[**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype)som har flera värden. Några av dessa är

- OffsetDiagonal BottomHöger
- OffsetBottom
- OffsetDiagonalOverhöger
- Insidan Vänster
- InsideCenter
- PerspectiveDiagonalUpperLeft
- PerspektivDiagonal Nedre Höger

{{% /alert %}}

Följande kodavsnitt visar användningen av[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype)egenskap för att ställa in skuggan av texteffekter av Shape eller TextBox.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
