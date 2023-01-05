---
title: Acceder a la tabla desde Cell y agregar valores dentro de ella usando compensaciones de fila y columna
type: docs
weight: 230
url: /es/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---
{{% alert color="primary" %}}

 Normalmente, agrega valores dentro de la tabla o el objeto de lista usando[**Cell.PonerValor()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)método. Pero a veces, es posible que deba agregar valores dentro de la tabla o el objeto de lista utilizando los desplazamientos de fila y columna.

Para acceder a la tabla o lista de objetos desde una celda, use el[**Cell.ObtenerTabla()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) método. Para agregar valores dentro de él usando los desplazamientos de fila y columna, use el[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue) método.

{{% /alert %}}

 La siguiente captura de pantalla muestra el archivo fuente de Excel utilizado dentro del código. Contiene la tabla vacía y resalta la celda D5 que se encuentra dentro de la tabla. Accederemos a esta tabla desde la celda D5 usando[**Cell.ObtenerTabla()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) método y luego agregue los valores dentro de él usando ambos[**Cell.PonerValor()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) y[**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue)métodos.

## Ejemplo

### Capturas de pantalla que comparan los archivos de origen y de salida

|![todo:imagen_alternativa_texto](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
|:- |

La siguiente captura de pantalla muestra el archivo de salida de Excel generado por el código. Como puede ver, la celda D5 tiene un valor y la celda F6, que está en el desplazamiento 2,2 de la tabla, tiene un valor.

|![todo:imagen_alternativa_texto](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
|:- |

### C# código para acceder a la tabla desde la celda y agregar valores dentro de ella usando compensaciones de fila y columna

El siguiente código de ejemplo carga el archivo de origen de Excel como se muestra en la captura de pantalla anterior y agrega valores dentro de la tabla y genera el archivo de salida de Excel como se muestra arriba.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
