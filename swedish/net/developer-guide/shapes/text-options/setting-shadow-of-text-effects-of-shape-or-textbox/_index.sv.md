---
title: Inställning av skugga för texteffekter av form eller textruta
type: docs
weight: 250
url: /sv/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

Du kan ställa in **Skugga** för **Texteffekter** av vilken form eller textruta som helst. Använd egenskapen [**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody). Den presenterar inställningen för formens text och returnerar [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) objekt. Efter åtkomst, ställ in **Skugga** via egenskapen [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype). Denna egenskap är av typen [**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype) som har flera värden. Några av dessa är

- OffsetDiagonalBottomRight
- OffsetBottom
- OffsetDiagonalTopRight
- InsideLeft
- InsideCenter
- PerspectiveDiagonalUpperLeft
- PerspectiveDiagonalLowerRight

{{% /alert %}}

Följande kodsnutt illustrerar användningen av egenskapen [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) för att ställa in skugga för texteffekter av en form eller textruta.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
