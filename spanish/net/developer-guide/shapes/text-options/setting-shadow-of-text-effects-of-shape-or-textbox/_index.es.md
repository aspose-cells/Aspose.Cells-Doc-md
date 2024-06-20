---
title: Establecer sombra de efectos de texto de forma o cuadro de texto
type: docs
weight: 250
url: /es/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

Puedes establecer la sombra de los efectos de texto de cualquier forma o cuadro de texto. Utiliza la propiedad [**Shape.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody). Presenta la configuración del texto de la forma y devuelve objetos [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting). Después de acceder a él, establece la sombra a través de la propiedad [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype). Esta propiedad es del tipo [**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype) que tiene varios valores. Algunos de estos son

- Diagonal inferior derecha
- Inferior
- Diagonal superior derecha
- Interior izquierdo
- Centro interior
PerspectiveDiagonalUpperLeft
PerspectiveDiagonalLowerRight

{{% /alert %}}

El siguiente fragmento de código demuestra el uso de la propiedad [**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) para establecer la sombra de efectos de texto de forma o cuadro de texto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
