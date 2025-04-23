---
title: Şekil veya Metin Kutusunun Metin Efektlerinin Gölgesini Ayarlama
type: docs
weight: 670
url: /tr/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}} 

Herhangi bir Şekil veya Metin Kutusunun **Gölgesi**'ni ayarlayabilirsiniz. Lütfen [Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody) özelliğini kullanın. Bu, şeklin metninin ayarlarını sunar ve [FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection) döndürür. Bundan [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting)'e eriştikten sonra, **Gölge**'yi [FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType) özelliği üzerinden ayarlayın. Bu özellik [PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType) türündedir ve birkaç değere sahiptir. Bunlardan bazıları

- [OFFSET_DIAGONAL_BOTTOM_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET-DIAGONAL-BOTTOM-RIGHT)
- [OFFSET_BOTTOM](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET-BOTTOM)
- [OFFSET_DIAGONAL_TOP_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET-DIAGONAL-TOP-RIGHT)
- [INSIDE_LEFT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE-LEFT)
- [INSIDE_CENTER](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE-CENTER)
- [PERSPECTIVE_DIAGONAL_UPPER_LEFT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE-DIAGONAL-UPPER-LEFT)
- [PERSPECTIVE_DIAGONAL_UPPER_RIGHT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE-DIAGONAL-UPPER-RIGHT)

{{% /alert %}} 
## **Şekil veya Metin Kutusunun Metin Efektlerinin Gölgesini Ayarlama**
Aşağıdaki ekran görüntüsü, aşağıdaki örnek kod ile oluşturulan [çıktı excel dosyasını](5473446.xlsx) gösterir. Ekran görüntüsü ayrıca **Gölgelendirme** olarak ayarlanmış olan **Alt Kenar** değerini de gösterir.

![todo:image_alt_text](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
{{< app/cells/assistant language="java" >}}
