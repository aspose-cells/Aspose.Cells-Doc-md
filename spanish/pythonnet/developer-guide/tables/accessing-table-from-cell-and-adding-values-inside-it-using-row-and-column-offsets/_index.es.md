---
title: Acceder a Tabla desde Celda y Agregar Valores en su Interior usando Desplazamientos de Fila y Columna
type: docs
weight: 230
url: /es/python-net/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}

Normalmente, agrega valores dentro de la Tabla u Objeto de Lista usando el método [**Cell.put_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool). Pero a veces, es posible que necesite agregar valores dentro de la Tabla u Objeto de Lista usando los desplazamientos de fila y columna.

Para acceder a una Tabla u Objeto de Lista desde una celda, utilice el método [**Cell.get_table()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_table/#). Para agregar valores dentro de ella utilizando los desplazamientos de fila y columna, use el método [**ListObject.put_cell_value**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/put_cell_value/#int-int-any).

{{% /alert %}}

La siguiente captura de pantalla muestra el archivo de Excel fuente usado dentro del código. Contiene la tabla vacía y resalta la celda D5 que se encuentra dentro de la tabla. Accederemos a esta tabla desde la celda D5 usando el método [**Cell.get_table()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_table/#) y luego agregaremos los valores dentro de ella usando los métodos [**Cell.put_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#bool) y [**ListObject.put_cell_value**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listobject/put_cell_value/#int-int-any).

## Ejemplo

### Capturas de pantalla que comparan los archivos fuente y de salida

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|
| :- |

La siguiente captura de pantalla muestra el archivo de Excel de salida generado por el código. Como se puede ver, la celda D5 tiene un valor y la celda F6, que está en el desplazamiento 2,2 de la tabla, tiene un valor.

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|
| :- |

### Código Python para acceder a una tabla desde la celda y agregar valores dentro de ella usando desplazamientos de fila y columna

El siguiente código de ejemplo carga el archivo de Excel fuente como se muestra en la captura de pantalla anterior y agrega valores dentro de la tabla, y genera el archivo de Excel de salida como se muestra arriba.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-AccessTableFromCellAndAddValue.py" >}}
