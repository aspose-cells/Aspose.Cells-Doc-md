---
title: Configuración de efectos de sombra de texto de forma o cuadro de texto
type: docs
weight: 670
url: /es/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---
{{% alert color="primary" %}} 

 Puede configurar el**Sombra** de**Efectos de texto** de cualquier forma o cuadro de texto. Por favor use el[Forma.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody) propiedad. Presenta la configuración del texto de la forma y devuelve[FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection) . Después de acceder[Configuración de fuente](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) desde allí, configure el**Sombra** a través de[Configuración de fuentes.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType) propiedad. Esta propiedad es de tipo[PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType)que tiene varios valores. Algunos de estos son

- [COMPENSAR_DIAGONAL_ABAJO A LA DERECHA](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [OFFSET_BOTTOM](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [COMPENSAR_DIAGONAL_PARTE SUPERIOR DERECHA](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [INTERIOR_IZQUIERDA](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [DENTRO_CENTRO](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [PERSPECTIVA_DIAGONAL_ARRIBA A LA IZQUIERDA](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [PERSPECTIVA_DIAGONAL_SUPERIOR DERECHA](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **Configuración de efectos de sombra de texto de forma o cuadro de texto**
La siguiente captura de pantalla muestra la[archivo de salida de Excel](5473446.xlsx) generado con el siguiente código de ejemplo. La captura de pantalla también muestra el valor de la**Sombra** que se ha fijado como**Fondo compensado**.

![todo:imagen_alternativa_texto](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
