---
title: Uso de estilos integrados
type: docs
weight: 480
url: /es/java/using-built-in-styles/
---
{{% alert color="primary" %}} 

Aspose.Cells proporciona una amplia colección de estilos reutilizables para formatear una celda en un documento de hoja de cálculo. Podemos usar estilos incorporados en nuestro libro de trabajo y también crear estilos personalizados.

{{% /alert %}} 
## **Cómo usar estilos incorporados**
 El método[Workbook.createBuiltinStyle](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#createBuiltinStyle\(int\) ) y clase[BuiltinStyleType](https://reference.aspose.com/cells/java/com.aspose.cells/BuiltinStyleType)que sea conveniente crear estilos reutilizables. Aquí hay una lista de todos los estilos integrados posibles:

- [VEINTE_POR CIENTO_ACENTO_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_1)
- [VEINTE_POR CIENTO_ACENTO_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_2)
- [VEINTE_POR CIENTO_ACENTO_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_3)
- [VEINTE_POR CIENTO_ACENTO_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_4)
- [VEINTE_POR CIENTO_ACENTO_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_5)
- [VEINTE_POR CIENTO_ACENTO_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY_PERCENT_ACCENT_6)
- [CUARENTA_POR CIENTO_ACENTO_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_1)
- [CUARENTA_POR CIENTO_ACENTO_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_2)
- [CUARENTA_POR CIENTO_ACENTO_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_3)
- [CUARENTA_POR CIENTO_ACENTO_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_4)
- [CUARENTA_POR CIENTO_ACENTO_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_5)
- [CUARENTA_POR CIENTO_ACENTO_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY_PERCENT_ACCENT_6)
- [SESENTA_POR CIENTO_ACENTO_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_1)
- [SESENTA_POR CIENTO_ACENTO_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_2)
- [SESENTA_POR CIENTO_ACENTO_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_3)
- [SESENTA_POR CIENTO_ACENTO_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_4)
- [SESENTA_POR CIENTO_ACENTO_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_5)
- [SESENTA_POR CIENTO_ACENTO_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY_PERCENT_ACCENT_6)
- [ACENTO_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_1)
- [ACENTO_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_2)
- [ACENTO_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_3)
- [ACENTO_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_4)
- [ACENTO_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_5)
- [ACENTO_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT_6)
- [MALO](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#BAD)
- [CÁLCULO](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CALCULATION)
- [CHECK_CELL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CHECK_CELL)
- [COMA](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA)
- [COMA_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA_1)
- [DIVISA](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY)
- [MONEDA_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY_1)
- [TEXTO_EXPLICATIVO](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#EXPLANATORY_TEXT)
- [BUENO](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#GOOD)
- [CABECERA_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_1)
- [CABECERA_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_2)
- [CABECERA_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_3)
- [CABECERA_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER_4)
- [HIPERVÍNCULO](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HYPERLINK)
- [SEGUIDO_HIPERVINCULO](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FOLLOWED_HYPERLINK)
- [APORTE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#INPUT)
- [LINKED_CELL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#LINKED_CELL)
- [NEUTRAL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NEUTRAL)
- [NORMAL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NORMAL)
- [NOTA](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NOTE)
- [PRODUCCIÓN](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#OUTPUT)
- [POR CIENTO](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#PERCENT)
- [TÍTULO](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TITLE)
- [TOTAL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TOTAL)
- [ADVERTENCIA_TEXTO](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#WARNING_TEXT)
- [ROW_LEVEL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ROW_LEVEL)
- [COLUMN_LEVEL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COLUMN_LEVEL)

El código siguiente muestra cómo usar estilos integrados.

![todo:imagen_alternativa_texto](using-built-in-styles_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingBuiltinStyles-UsingBuiltinStyles.java" >}}
