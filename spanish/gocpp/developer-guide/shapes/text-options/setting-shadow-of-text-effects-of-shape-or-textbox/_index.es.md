---
title: Configurar sombra de efectos de texto de forma o cuadro de texto con Golang vía C++
linktitle: Configuración de sombra de efectos de texto
type: docs
weight: 250
url: /es/go-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/
description: Aprenda cómo configurar la sombra de efectos de texto para formas o cuadros de texto usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Puede configurar la **Sombra** de los **Efectos de texto** de cualquier forma o cuadro de texto. Por favor, utilice la propiedad [**Shape.GetTextBody()**](https://reference.aspose.com/cells/go-cpp/shape/gettextbody/). Esta presenta la configuración del texto de la forma y devuelve objetos [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/). Después de acceder a ella, configure la **Sombra** a través de la propiedad [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/). Esta propiedad es del tipo [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/) y tiene varios valores. Algunos de estos son:

- Diagonal inferior derecha
- Inferior
- Diagonal superior derecha
- Interior izquierdo
- Centro interior
PerspectiveDiagonalUpperLeft
PerspectiveDiagonalLowerRight

{{% /alert %}}

El siguiente fragmento de código demuestra el uso de la propiedad [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/go-cpp/shadoweffect/getpresettype/) para establecer la sombra de efectos de texto de Forma o Cuadro de texto.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingShadowOfTextEffectsOfShapeOrTextbox.go" >}}
