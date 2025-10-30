---
title: Şekil veya Metin Kutusu Metin Efektlerinin Gölgesini Golang ve C++ ile Ayarlama
linktitle: Metin Efektleri Gölgesini Ayarlama
type: docs
weight: 250
url: /tr/go-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Aspose.Cells for C++ kullanarak şekil veya metin kutularının metin efektleri gölgesini nasıl ayarlayacağınızı öğrenin.
---

{{% alert color="primary" %}}

Herhangi bir Şekil veya Metin Kutusu'nun **Metin Efektleri**nin **Gölgesi**ni ayarlayabilirsiniz. Lütfen [**Shape.GetTextBody()**](https://reference.aspose.com/cells/go-cpp/shape/gettextbody/) özelliğini kullanın. Bu, şeklin metnini ayarlar ve [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) nesnelerini döndürür. Erişim sağladıktan sonra, [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/) özelliği aracılığıyla **Gölge**yi ayarlayın. Bu özellik, birkaç değeri olan [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/) türündedir ve bazıları şunlardır:

- Dikey Sağa Ofset
- Alt Ofset
- OffsetDiagonalTopRight
- InsideLeft
- InsideCenter
- PerspectiveDiagonalUpperLeft
- PerspectiveDiagonalLowerRight

{{% /alert %}}

Aşağıdaki kod parçası, Shape veya TextBox'un metin efektleri gölgesini ayarlamak için [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/go-cpp/shadoweffect/getpresettype/) özelliğinin kullanımını gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingShadowOfTextEffectsOfShapeOrTextbox.go" >}}
