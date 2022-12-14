---
title: Impostazione dell'ombreggiatura degli effetti di testo di Shape o TextBox
type: docs
weight: 670
url: /it/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}} 

 Puoi impostare il**Ombra** di**Effetti di testo** di qualsiasi Shape o TextBox. Si prega di utilizzare il[Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody) proprietà. Presenta l'impostazione del testo della forma e ritorna[FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection) . Dopo l'accesso[Impostazione carattere](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) da esso, si prega di impostare il**Ombra** attraverso[FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType) proprietà. Questa proprietà è di tipo[PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType)che ha diversi valori. Alcuni di questi lo sono

- [COMPENSARE_DIAGONALE_IN BASSO A DESTRA](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [OFFSET_INFERIORE](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [COMPENSARE_DIAGONALE_IN ALTO A DESTRA](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [INTERNO_SINISTRA](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [INTERNO_CENTRO](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [PROSPETTIVA_DIAGONALE_SUPERIORE SINISTRO](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [PROSPETTIVA_DIAGONALE_IN ALTO A DESTRA](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **Impostazione dell'ombreggiatura degli effetti di testo di Shape o TextBox**
 Lo screenshot seguente mostra il[file excel di output](5473446.xlsx) generato con il seguente codice di esempio. Lo screenshot mostra anche il valore di**Ombra** che è stato impostato come**Scostamento inferiore**.

![cose da fare:immagine_alt_testo](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
