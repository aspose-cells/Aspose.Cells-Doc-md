---
title: Festlegen des Schattens von Texteffekten von Form oder TextBox
type: docs
weight: 250
url: /de/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}}

 Sie können die einstellen**Schatten** von**Texteffekte** einer beliebigen Form oder TextBox. Bitte verwenden Sie die[**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody) Eigentum. Es zeigt die Einstellung des Textes der Form und kehrt zurück[**Schrifteinstellung**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) Objekte. Nachdem Sie darauf zugegriffen haben, stellen Sie bitte die**Schatten** über[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) Eigentum. Diese Eigenschaft ist vom Typ[**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype)die mehrere Werte hat. Einige davon sind

- OffsetDiagonalUntenRechts
- OffsetUnten
- OffsetDiagonalObenRechts
- InnenLinks
- InsideCenter
- PerspektiveDiagonalObenLinks
- PerspektiveDiagonalLowerRight

{{% /alert %}}

Das folgende Code-Snippet demonstriert die Verwendung von[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype)-Eigenschaft zum Festlegen des Schattens von Texteffekten von Shape oder TextBox.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
