---
title: Şeklin veya Metin Kutusunun Metin Efektlerinin Gölgesini Ayarlama
type: docs
weight: 670
url: /tr/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}} 

 ayarlayabilirsiniz**Gölge** nın-nin**Metin Efektleri** herhangi bir Şekil veya Metin Kutusu. lütfen[Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody) Emlak. Şeklin metninin ayarını sunar ve döndürür[FontSettingKoleksiyon](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection) . eriştikten sonra[Yazı Tipi Ayarı](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) ondan, lütfen**Gölge** aracılığıyla[FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType) Emlak. Bu özellik şu türdendir:[ÖnayarGölgeTürü](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType)birkaç değeri olan. Bunlardan bazıları

- [TELAFİ ETMEK_DİYAGONAL_SAĞ ALT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [OFFSET_BOTTOM](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [TELAFİ ETMEK_DİYAGONAL_SAĞ ÜST](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [INSIDE_LEFT](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [INSIDE_CENTER](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [PERSPEKTİF_DİYAGONAL_SOL ÜST](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [PERSPEKTİF_DİYAGONAL_SAĞ ÜST](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **Şeklin veya Metin Kutusunun Metin Efektlerinin Gölgesini Ayarlama**
 Aşağıdaki ekran görüntüsü[çıktı excel dosyası](5473446.xlsx) aşağıdaki örnek kod ile oluşturulmuştur. Ekran görüntüsü aynı zamanda değerini de gösterir.**Gölge** olarak ayarlanan**Ofset Alt**.

![yapılacaklar:resim_alternatif_Metin](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
