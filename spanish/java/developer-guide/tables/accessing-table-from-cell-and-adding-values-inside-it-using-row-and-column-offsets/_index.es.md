---
title: Acceder a la tabla desde Cell y agregar valores dentro de ella usando compensaciones de fila y columna
type: docs
weight: 110
url: /es/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

 Normalmente, agrega valores dentro de la tabla o el objeto de lista usando[**Cell.ponerValor()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean)) método. Pero a veces, es posible que deba agregar valores dentro de la tabla o el objeto de lista utilizando los desplazamientos de fila y columna.

Para acceder a la tabla o lista de objetos desde una celda, use el[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ) método. Y para agregar valores dentro de él usando los desplazamientos de fila y columna, use el[**ListObject.putCellValue(rowOffset,columnOffset,valor)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) método.

{{% /alert %}}

## Ejemplo

### Capturas de pantalla que comparan los archivos de origen y de salida

 La siguiente captura de pantalla muestra el archivo fuente de Excel utilizado dentro del código. Contiene la tabla vacía y resalta la celda D5 que se encuentra dentro de la tabla. Accederemos a esta tabla desde la celda D5 usando[**Cell.getTable()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getTable() ) y luego agregue los valores dentro de él usando ambos[**Cell.ponerValor()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#putValue(boolean) ) y[**ListObject.putCellValue(rowOffset,columnOffset,valor)**](https://reference.aspose.com/cells/java/com.aspose.cells/listobject#putCellValue(int,%20int,%20java.lang.Object)) métodos.

![todo:imagen_alternativa_texto](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)

La siguiente captura de pantalla muestra el archivo de salida de Excel generado por el código. Como puede ver, la celda D5 tiene un valor y la celda F6, que está en el desplazamiento 2,2 de la tabla, tiene un valor.

![todo:imagen_alternativa_texto](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)

### Java código para acceder a la tabla desde la celda y agregar valores dentro de ella usando compensaciones de fila y columna

El siguiente código de ejemplo carga el archivo de origen de Excel como se muestra en la captura de pantalla anterior y agrega valores dentro de la tabla y genera el archivo de salida de Excel como se muestra arriba.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessingTablefromCell-AccessingTablefromCell.java" >}}
