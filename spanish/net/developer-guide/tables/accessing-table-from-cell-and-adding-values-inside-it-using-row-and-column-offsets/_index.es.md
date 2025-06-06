---
title: Acceder a Tabla desde Celda y Agregar Valores en su Interior usando Desplazamientos de Fila y Columna
type: docs
weight: 230
url: /es/net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Normalmente, agrega valores dentro de la Tabla u Objeto de Lista usando el método [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index). Pero a veces, es posible que necesite agregar valores dentro de la Tabla u Objeto de Lista usando los desplazamientos de fila y columna.

Para acceder a una Tabla u Objeto de Lista desde una celda, utilice el método [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable). Para agregar valores dentro de ella utilizando los desplazamientos de fila y columna, use el método [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue).

{{% /alert %}}

La siguiente captura de pantalla muestra el archivo de Excel fuente usado dentro del código. Contiene la tabla vacía y resalta la celda D5 que se encuentra dentro de la tabla. Accederemos a esta tabla desde la celda D5 usando el método [**Cell.GetTable()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gettable) y luego agregaremos los valores dentro de ella usando los métodos [**Cell.PutValue()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) y [**ListObject.PutCellValue**](https://reference.aspose.com/cells/net/aspose.cells.tables/listobject/methods/putcellvalue).

## Ejemplo

### Capturas de pantalla que comparan los archivos fuente y de salida

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

La siguiente captura de pantalla muestra el archivo de Excel de salida generado por el código. Como se puede ver, la celda D5 tiene un valor y la celda F6, que está en el desplazamiento 2,2 de la tabla, tiene un valor.

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### Código C# para acceder a la tabla desde la celda y para agregar valores dentro de ella usando desplazamientos de fila y columna

El siguiente código de ejemplo carga el archivo de Excel fuente como se muestra en la captura de pantalla anterior y agrega valores dentro de la tabla, y genera el archivo de Excel de salida como se muestra arriba.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-AccessTableFromCellAndAddValue-AccessTableFromCellAndAddValue.cs" >}}
{{< app/cells/assistant language="csharp" >}}
