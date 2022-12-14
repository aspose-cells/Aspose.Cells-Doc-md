---
title: Impostazione dell'ombreggiatura degli effetti di testo di Shape o TextBox
type: docs
weight: 250
url: /it/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}}

 Puoi impostare il**Ombra** di**Effetti di testo** di qualsiasi Shape o TextBox. Si prega di utilizzare il[**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody) proprietà. Presenta l'impostazione del testo della forma e ritorna[**Impostazione carattere**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) oggetti. Dopo l'accesso, impostare il file**Ombra** attraverso[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) proprietà. Questa proprietà è del tipo[**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype)che ha diversi valori. Alcuni di questi lo sono

- OffsetDiagonalBottomRight
- OffsetBasso
- OffsetDiagonalTopRight
- DentroSinistra
- DentroCentro
- Prospettiva Diagonale Superiore Sinistra
- Prospettiva Diagonale Inferiore Destra

{{% /alert %}}

Il seguente frammento di codice illustra l'uso di[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype)proprietà per impostare l'ombreggiatura degli effetti di testo di Shape o TextBox.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
