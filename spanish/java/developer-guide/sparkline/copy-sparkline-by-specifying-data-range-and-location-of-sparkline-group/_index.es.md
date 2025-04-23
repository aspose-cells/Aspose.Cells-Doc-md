---
title: Copiar Sparkline especificando el rango de datos y la ubicación del grupo de sparkline
type: docs
weight: 120
url: /es/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

Copiar Sparkline especificando el rango de datos y la ubicación del grupo de sparkline en MS Excel

Microsoft Excel te permite copiar un sparkline especificando el rango de datos y la ubicación del grupo de sparkline. Sigue estos pasos para copiar tu sparkline a otras celdas.

- Selecciona la celda que contiene tu sparkline.
- Selecciona **Editar datos** en la sección **Sparkline** dentro de la pestaña **Diseño**
- Elige **Editar ubicación del grupo y datos...**
- Especifica el rango de datos y la ubicación y haz clic en Aceptar.

## Ejemplo

Aspose.Cells proporciona el método [**SparklineCollection.add(dataRange, row, column)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection) para especificar el rango de datos y la ubicación del grupo de sparkline.

### Capturas de pantalla de los archivos fuente y de salida

La siguiente captura de pantalla muestra el archivo de Excel fuente utilizado en el código. El área destacada en rojo muestra la opción "**Editar ubicación del grupo y datos...**" para especificar el rango de datos y la ubicación del grupo de sparkline. La celda P4 muestra el sparkline que se copiará a las otras cuatro celdas rellenadas con color amarillo usando Aspose.Cells.

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

La siguiente captura de pantalla muestra el archivo de Excel de salida generado por el código de ejemplo. Como se puede ver, el sparkline en la celda P4 se ha copiado a las próximas cuatro celdas en la columna P, cada una con un rango de datos diferente.

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### Código Java para copiar mini gráfico especificando rango de datos y ubicación del grupo de mini gráficos

El siguiente código de ejemplo carga el archivo de Excel fuente como se muestra en la captura de pantalla de arriba, luego accede al primer grupo de mini gráficos y agrega rangos de datos y ubicaciones dentro del grupo de mini gráficos. Finalmente, escribe el archivo de Excel de salida en disco que también se muestra en la captura de pantalla de arriba.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
{{< app/cells/assistant language="java" >}}
