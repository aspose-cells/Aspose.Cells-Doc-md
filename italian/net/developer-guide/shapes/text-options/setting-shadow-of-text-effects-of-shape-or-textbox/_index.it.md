---
title: Impostazione dell ombra degli effetti di testo della forma o del riquadro di testo
type: docs
weight: 250
url: /it/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

È possibile impostare l'**Ombra** degli **Effetti di testo** di qualsiasi forma o casella di testo. Si prega di utilizzare la proprietà [**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody). Essa rappresenta l'impostazione del testo della forma e restituisce oggetti [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting). Dopo avervi accesso, si prega di impostare l'**Ombra** tramite la proprietà [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype). Questa proprietà è del tipo [**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype) che ha diversi valori. Alcuni di questi sono

- DiagonaleOffsetInferioreDestra
- OffsetInferiore
- DiagonaleOffsetSuperioreDestra
- SinistraInterno
- CentroInterno
- DiagonaleSuperioreSinistraProspettiva
- DiagonaleInferioreDestraProspettiva

{{% /alert %}}

Il seguente frammento di codice dimostra l'uso della proprietà [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) per impostare l'ombra degli effetti di testo della forma o della casella di testo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
