---
title: Establecer sombra de efectos de texto de forma o cuadro de texto
type: docs
weight: 670
url: /es/java/setting-shadow-of-text-effects-of-shape-or-textbox/
---

{{% alert color="primary" %}} 

Puede establecer la **sombra** de los **efectos de texto** de cualquier forma o cuadro de texto. Por favor, use la propiedad [Shape.TextBody](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TextBody). Presenta la configuración del texto de la forma y devuelve [FontSettingCollection](https://reference.aspose.com/cells/java/com.aspose.cells/FontSettingCollection). Después de acceder a [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) desde éste, por favor configure la **sombra** a través de la propiedad [FontSetting.getTextOptions().getShadow().setPresetType()](https://reference.aspose.com/cells/java/com.aspose.cells/shadoweffect#PresetType). Esta propiedad es de tipo [PresetShadowType](https://reference.aspose.com/cells/java/com.aspose.cells/PresetShadowType) que tiene varios valores. Algunos de ellos son

- [OFFSET_DIAGONAL_INFERIOR_DERECHO](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_BOTTOM_RIGHT)
- [OFFSET_INFERIOR](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_BOTTOM)
- [OFFSET_DIAGONAL_SUPERIOR_DERECHO](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#OFFSET_DIAGONAL_TOP_RIGHT)
- [INTERIOR_IZQUIERDA](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_LEFT)
- [INTERIOR_CENTRO](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#INSIDE_CENTER)
- [PERSPECTIVA_DIAGONAL_SUPERIOR_IZQUIERDA](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_LEFT)
- [PERSPECTIVA_DIAGONAL_SUPERIOR_DERECHA](https://reference.aspose.com/cells/java/com.aspose.cells/presetshadowtype#PERSPECTIVE_DIAGONAL_UPPER_RIGHT)

{{% /alert %}} 
## **Estableciendo la sombra de los efectos de texto de una forma o cuadro de texto**
La siguiente captura de pantalla muestra el [archivo de Excel de salida](5473446.xlsx) generado con el siguiente código de ejemplo. La captura de pantalla también muestra el valor de la **sombra** que se ha establecido como **Offset Inferior**.

![todo:image_alt_text](setting-shadow-of-text-effects-of-shape-or-textbox_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingTextEffectsShadowOfShapeOrTextbox-SettingTextEffectsShadowOfShapeOrTextbox.java" >}}
