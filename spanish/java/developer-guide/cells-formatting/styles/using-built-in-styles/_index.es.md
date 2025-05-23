---
title: Utilizando Estilos Incorporados
type: docs
weight: 480
url: /es/java/using-built-in-styles/
---

{{% alert color="primary" %}} 

Aspose.Cells ofrece una vasta colección de estilos reutilizables para formatear una celda en un documento de hoja de cálculo. Podemos utilizar estilos incorporados en nuestro libro de trabajo y también crear estilos personalizados.

{{% /alert %}} 
## **Cómo utilizar Estilos Incorporados**
El método [Workbook.createBuiltinStyle](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#createBuiltinStyle-int-) y la clase [BuiltinStyleType](https://reference.aspose.com/cells/java/com.aspose.cells/BuiltinStyleType) facilitan la creación de estilos reutilizables. Aquí hay una lista de todos los estilos incorporados posibles:

- [TWENTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-1)
- [TWENTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-2)
- [TWENTY_PERCENT_ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-3)
- [TWENTY_PERCENT_ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-4)
- [TWENTY_PERCENT_ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-5)
- [TWENTY_PERCENT_ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TWENTY-PERCENT-ACCENT-6)
- [FORTY_PERCENT_ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-1)
- [FORTY_PERCENT_ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-2)
- [CUARENTA_PORCIENTO_RESALTADO_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-3)
- [CUARENTA_PORCIENTO_RESALTADO_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-4)
- [CUARENTA_PORCIENTO_RESALTADO_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-5)
- [CUARENTA_PORCIENTO_RESALTADO_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FORTY-PERCENT-ACCENT-6)
- [SESENTA_PORCIENTO_RESALTADO_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-1)
- [SESENTA_PORCIENTO_RESALTADO_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-2)
- [SESENTA_POR_CIENTO_ACENTO_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-3)
- [SESENTA_POR_CIENTO_ACENTO_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-4)
- [SESENTA_POR_CIENTO_ACENTO_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-5)
- [SESENTA_POR_CIENTO_ACENTO_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#SIXTY-PERCENT-ACCENT-6)
- [ACCENT_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-1)
- [ACCENT_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-2)
- [ACCENT_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-3)
- [ACCENT_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-4)
- [ACCENT_5](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-5)
- [ACCENT_6](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ACCENT-6)
- [MAL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#BAD)
- [CÁLCULO](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CALCULATION)
- [VERIFICAR_CELDA](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CHECK-CELL)
- [COMA](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA)
- [COMA_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COMMA-1)
- [MONEDA](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY)
- [MONEDA_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#CURRENCY-1)
- [TEXTO_EXPLICATIVO](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#EXPLANATORY-TEXT)
- [BUENO](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#GOOD)
- [ENCABEZADO_1](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER-1)
- [ENCABEZADO_2](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER-2)
- [ENCABEZADO_3](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER-3)
- [ENCABEZADO_4](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HEADER-4)
- [VINCULO](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#HYPERLINK)
- [VINCULO_SEGUIDO](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#FOLLOWED-HYPERLINK)
- [ENTRADA](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#INPUT)
- [CELDA_VINCULADA](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#LINKED-CELL)
- [NEUTRAL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NEUTRAL)
- [NORMAL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NORMAL)
- [NOTA](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#NOTE)
- [SALIDA](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#OUTPUT)
- [PORCENTAJE](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#PERCENT)
- [TITULO](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TITLE)
- [TOTAL](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#TOTAL)
- [TEXTO_ADVERTENCIA](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#WARNING-TEXT)
- [NIVEL_FILA](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#ROW-LEVEL)
- [NIVEL_COLUMNA](https://reference.aspose.com/cells/java/com.aspose.cells/builtinstyletype#COLUMN-LEVEL)

El siguiente código demuestra cómo utilizar estilos integrados.

![todo:image_alt_text](using-built-in-styles_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingBuiltinStyles-UsingBuiltinStyles.java" >}}
{{< app/cells/assistant language="java" >}}
