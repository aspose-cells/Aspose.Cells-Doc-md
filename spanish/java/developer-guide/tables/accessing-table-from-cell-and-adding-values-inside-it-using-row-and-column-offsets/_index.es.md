---
title: Acceder a Tabla desde Celda y Agregar Valores en su Interior usando Desplazamientos de Fila y Columna
type: docs
weight: 110
url: /es/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Normalmente, agrega valores dentro de la Tabla u Objeto de Lista usando el método [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)). Pero a veces, es posible que necesite agregar valores dentro de la Tabla u Objeto de Lista usando los desplazamientos de fila y columna.

Para acceder a la Tabla u Objeto de Lista desde una celda, use el método [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--). Y para agregar valores dentro de ella usando los desplazamientos de fila y columna, use el método [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)).

{{% /alert %}}

## Ejemplo

### Capturas de pantalla que comparan los archivos fuente y de salida

La siguiente captura de pantalla muestra el archivo de Excel fuente usado dentro del código. Contiene la tabla vacía y resalta la celda D5 que se encuentra dentro de la tabla. Accederemos a esta tabla desde la celda D5 usando el método [**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable--) y luego agregaremos los valores dentro de ella usando los métodos [**Cell.putValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)) y [**ListObject.putCellValue(rowOffset,columnOffset,value)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)).

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

La siguiente captura de pantalla muestra el archivo de Excel de salida generado por el código. Como se puede ver, la celda D5 tiene un valor y la celda F6, que está en el desplazamiento 2,2 de la tabla, tiene un valor.

![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### Código Java para acceder a tabla desde celda y para agregar valores en su interior usando desplazamientos de fila y columna

El siguiente código de ejemplo carga el archivo de Excel fuente como se muestra en la captura de pantalla anterior y agrega valores dentro de la tabla, y genera el archivo de Excel de salida como se muestra arriba.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
