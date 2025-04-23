---
title: Şekil veya Metin Kutusunun Metin Efektlerinin Gölgesini Ayarlama
type: docs
weight: 250
url: /tr/python-net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

Herhangi bir Şekil veya Metin Kutusunun **Metin Efektlerinin Gölgesini** ayarlayabilirsiniz. Lütfen [**Shape.text_body**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_body) özelliğini kullanın. Bu, şeklin metninin ayarlanmasını sunar ve [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) nesnelerini döndürür. Buna erişildikten sonra, lütfen **Gölgeyi** [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type) özelliği aracılığıyla ayarlayın. Bu özellik, birkaç değere sahip olan [**PresetShadowType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/presetshadowtype/) türündendir. Bunlardan bazıları şunlardır:

- OFFSET_DIAGONAL_BOTTOM_RIGHT
- OFFSET_BOTTOM
- OFFSET_DIAGONAL_TOP_RIGHT
- İÇ SOL
- İÇ ORTA
- PERSPEKTİF DİKÇE ÜST SOL
- PERSPEKTİF DİKÇE ÜST SAĞ

{{% /alert %}}

Aşağıdaki kod örneği, Şekil veya TextBox'ın metin efekt gölgelerini ayarlamak için [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type) özelliğini kullanmanın örneklerini gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SettingTextEffectsShadowOfShapeOrTextbox-1.py" >}}
