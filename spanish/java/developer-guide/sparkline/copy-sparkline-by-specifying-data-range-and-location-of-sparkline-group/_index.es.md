---
title: Copie Sparkline especificando el rango de datos y la ubicación del grupo Sparkline
type: docs
weight: 120
url: /es/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
Copie Sparkline especificando el rango de datos y la ubicación del grupo Sparkline en MS Excel

Microsoft Excel le permite copiar un minigráfico especificando el rango de datos y la ubicación del grupo de minigráficos. Siga estos pasos para copiar su Sparkline a otras celdas.

- Seleccione la celda que contiene su minigráfico.
-  Seleccione**Editar datos** desde el**Minigráfico** sección dentro de la**Diseño** pestaña
-  Escoger**Editar ubicación y datos del grupo...**
- Especifique el rango de datos y la ubicación y haga clic en Aceptar.

## Ejemplo

 Aspose.Cells proporciona el[**SparklineCollection.add(rango de datos, fila, columna)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection) método para especificar el rango de datos y la ubicación del Sparkline Group.

### Capturas de pantalla de los archivos fuente y de salida

La siguiente captura de pantalla muestra el archivo fuente de Excel utilizado dentro del código. El área resaltada en rojo muestra "**Editar ubicación y datos del grupo...**" opción para especificar el rango de datos y la ubicación del grupo minigráfico. La celda P4 muestra el minigráfico que se copiará en las otras cuatro celdas llenas de color amarillo usando Aspose.Cells.

![todo:imagen_alternativa_texto](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

La siguiente captura de pantalla muestra el archivo de salida de Excel generado por el código de muestra. Como puede ver, el minigráfico de la celda P4 se ha copiado en las siguientes cuatro celdas de la columna P, cada una con un rango de datos diferente.

![todo:imagen_alternativa_texto](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### Java código para copiar minigráfico especificando el rango de datos y la ubicación del grupo de minigráfico

El siguiente código de muestra carga el archivo de origen de Excel como se muestra en la captura de pantalla anterior, luego accede al primer grupo de minigráficos y agrega rangos de datos y ubicaciones dentro del grupo de minigráficos. Finalmente, escribe el archivo de salida de Excel en el disco que también se muestra en la captura de pantalla anterior.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
