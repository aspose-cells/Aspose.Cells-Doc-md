---
title: Impostare l ombra degli effetti del testo di forma o casella di testo con Golang via C++
linktitle: Impostare l’ombra degli effetti di testo
type: docs
weight: 250
url: /it/go-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Impara come impostare l’ombra degli effetti di testo per forme o caselle di testo usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Puoi impostare l’**Ombra** degli **Effetti di testo** di qualsiasi forma o casella di testo. Usa la proprietà [**Shape.GetTextBody()**](https://reference.aspose.com/cells/go-cpp/shape/gettextbody/). Essa rappresenta la configurazione del testo della forma e restituisce oggetti [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/). Dopo averla accessata, imposta l’**Ombra** tramite la proprietà [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/). Questa proprietà è di tipo [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/) e può avere diversi valori. Alcuni di questi sono:

- DiagonaleOffsetInferioreDestra
- OffsetInferiore
- DiagonaleOffsetSuperioreDestra
- SinistraInterno
- CentroInterno
- DiagonaleSuperioreSinistraProspettiva
- DiagonaleInferioreDestraProspettiva

{{% /alert %}}

Il seguente frammento di codice dimostra l'uso della proprietà [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/go-cpp/shadoweffect/getpresettype/) per impostare l'ombra sugli effetti di testo di Forma o Casella di Testo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingShadowOfTextEffectsOfShapeOrTextbox.go" >}}
