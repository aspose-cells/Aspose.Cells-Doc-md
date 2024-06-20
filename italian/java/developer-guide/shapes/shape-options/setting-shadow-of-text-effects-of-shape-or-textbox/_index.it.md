---
title: Impostazione dell ombra degli effetti di testo della forma o del riquadro di testo
type: docs
weight: 670
url: /it/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}} 

Puoi impostare l'**ombra** degli **effetti di testo** di qualsiasi forma o riquadro di testo. Si prega di utilizzare la proprietà [Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody). Essa presenta le impostazioni del testo della forma e restituisce [FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection). Dopo aver accesso a [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) da essa, si prega di impostare l'**ombra** tramite la proprietà [FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType). Questa proprietà è di tipo [PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType) che ha diversi valori. Alcuni di questi sono

- [SPAZIO_DIAGONALE_INFERIORE_DESTRO](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [SPAZIO_INFERIORE](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [SPAZIO_DIAGONALE_SUPERIORE_DESTRO](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [INTERNO_SINISTRO](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [INTERNO_CENTRO](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [PROSPETTIVA_DIAGONALE_SUPERIORE_SINISTRA](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [PROSPETTIVA_DIAGONALE_SUPERIORE_DESTRA](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **Impostazione dell'ombra degli effetti di testo della forma o del riquadro di testo**
La seguente schermata mostra il [file excel di output](5473446.xlsx) generato con il seguente esempio di codice. La schermata mostra anche il valore dell'**ombra** che è stato impostato come **Offset in basso**.

![todo:image_alt_text](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
