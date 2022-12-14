---
title: Configuración de efectos de sombra de texto de forma o cuadro de texto
type: docs
weight: 250
url: /es/net/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}}

 Puede configurar el**Sombra** de**Efectos de texto** de cualquier forma o cuadro de texto. Por favor use el[**Forma.TextBody**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textbody) propiedad. Presenta la configuración del texto de la forma y devuelve[**Configuración de fuente**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) objetos. Después de acceder, configure el**Sombra** a través de[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype) propiedad. Esta propiedad es del tipo[**PresetShadowType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/presetshadowtype)que tiene varios valores. Algunos de estos son

- DesplazamientoDiagonalInferiorDerecha
- Desplazamiento inferior
- DesplazamientoDiagonalSuperiorDerecha
- AdentroIzquierda
- InsideCenter
- PerspectivaDiagonalSuperiorIzquierda
- PerspectivaDiagonalInferiorDerecha

{{% /alert %}}

El siguiente fragmento de código demuestra el uso de[**FontSetting.TextOptions.Shadow.PresetType.PresetType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shadoweffect/properties/presettype)propiedad para establecer la sombra de los efectos de texto de Shape o TextBox.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingTextEffectsShadowOfShapeOrTextbox-1.cs" >}}
