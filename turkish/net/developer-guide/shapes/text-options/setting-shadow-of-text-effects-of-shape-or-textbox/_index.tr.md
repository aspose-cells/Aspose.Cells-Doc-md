---
title: Şekil veya Metin Kutusunun Metin Efektlerinin Gölgesini Ayarlama
type: docs
weight: 250
url: /tr/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

Herhangi bir Şekil veya Metin Kutusunun **Metin Efektlerinin Gölgesini** ayarlayabilirsiniz. Lütfen [**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody) özelliğini kullanın. Bu, şeklin metninin ayarlanmasını sunar ve [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) nesnelerini döndürür. Buna erişildikten sonra, lütfen **Gölgeyi** [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) özelliği aracılığıyla ayarlayın. Bu özellik, birkaç değere sahip olan [**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype) türündendir. Bunlardan bazıları şunlardır:

- Dikey Sağa Ofset
- Alt Ofset
- OffsetDiagonalTopRight
- InsideLeft
- InsideCenter
- PerspectiveDiagonalUpperLeft
- PerspectiveDiagonalLowerRight

{{% /alert %}}

Aşağıdaki kod örneği, Şekil veya TextBox'ın metin efekt gölgelerini ayarlamak için [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) özelliğini kullanmanın örneklerini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
