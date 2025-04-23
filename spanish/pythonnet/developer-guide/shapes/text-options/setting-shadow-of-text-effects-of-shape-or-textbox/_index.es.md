---
title: Establecer sombra de efectos de texto de forma o cuadro de texto
type: docs
weight: 250
url: /es/python-net/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}}

Puedes establecer la sombra de los efectos de texto de cualquier forma o cuadro de texto. Utiliza la propiedad [**Shape.text_body**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_body). Presenta la configuración del texto de la forma y devuelve objetos [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting). Después de acceder a él, establece la sombra a través de la propiedad [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type). Esta propiedad es del tipo [**PresetShadowType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/presetshadowtype/) que tiene varios valores. Algunos de estos son

- OFFSET_DIAGONAL_BOTTOM_RIGHT
- OFFSET_INFERIOR
- OFFSET_DIAGONAL_SUPERIOR_DERECHO
- DENTRO_IZQUIERDA
- CENTRO_INTERNO
- PERSPECTIVA_DIAGONAL_SUPERIOR_IZQUIERDA
- PERSPECTIVA_DIAGONAL_SUPERIOR_DERECHA

{{% /alert %}}

El siguiente fragmento de código demuestra el uso de la propiedad [**FontSetting.text_options.shadow.preset_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shadoweffect/preset_type) para establecer la sombra de efectos de texto de forma o cuadro de texto.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SettingTextEffectsShadowOfShapeOrTextbox-1.py" >}}
