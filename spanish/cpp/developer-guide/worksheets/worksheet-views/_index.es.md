---
title: Vistas de hojas de trabajo
type: docs
weight: 40
url: /es/cpp/worksheet-views/
---
##  **La previsualización del salto de página**
Todas las hojas de trabajo se pueden ver en dos modos:

- Vista normal.
- La previsualización del salto de página.

La vista Normal es la vista predeterminada de una hoja de trabajo. La vista previa de salto de página es una vista de edición que muestra una hoja de trabajo tal como se imprimirá. La vista previa de salto de página muestra qué datos irán en cada página para que pueda ajustar el área de impresión y los saltos de página. Al utilizar Aspose.Cells, los desarrolladores pueden habilitar los modos de vista normal o vista previa de salto de página.
###  **Controlar los modos de visualización**
 Aspose.Cells proporciona una clase[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo Excel Microsoft. El[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)colección que permite el acceso a cada hoja de cálculo en un archivo Excel.

Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)clase. El[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) La clase proporciona una amplia gama de métodos para administrar hojas de trabajo. Para habilitar los modos de vista previa normal o de salto de página, utilice el[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) método de la[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase.[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) devuelve un valor bool, lo que significa que sólo puede almacenar un**verdadero** o**FALSO** valor.
####  **Habilitar la vista normal**
Establezca una hoja de trabajo en vista normal configurando el[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)método de la[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)clase a *falso**.
####  **Habilitar la vista previa de salto de página**
Configure cualquier hoja de trabajo en vista previa de salto de página configurando el[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)método de la[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)clase a *verdadero**. Al hacerlo, la hoja de trabajo cambia de la vista normal a la vista previa de salto de página.

 continuación se proporciona un ejemplo completo que demuestra cómo utilizar el[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)Método para habilitar el modo de vista previa de salto de página para la primera hoja de trabajo de un archivo de Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
##  **Factor de ampliación**
###  **Usando Microsoft Excel**
Microsoft Excel proporciona una función que permite a los usuarios establecer el zoom o el factor de escala de una hoja de cálculo. Esta función ayuda a los usuarios a ver el contenido de la hoja de trabajo en vistas más pequeñas o más grandes. Los usuarios pueden establecer el factor de zoom en cualquier valor.
###  **Aspose.Cells y factor de zoom**
 Aspose.Cells también permite a los desarrolladores configurar el factor de zoom de la hoja de trabajo. Aspose.Cells proporciona una clase[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo Excel Microsoft. El[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)colección que permite el acceso a cada hoja de cálculo en un archivo Excel.

Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase. El[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)La clase proporciona una amplia gama de métodos para administrar hojas de trabajo. Para establecer el factor de zoom de una hoja de trabajo, utilice el[Establecer zoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) método de la[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase. El factor de zoom se establece asignando un valor numérico (entero) al[Establecer zoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)método.

 continuación se proporciona un ejemplo completo que demuestra cómo utilizar el[Establecer zoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)Método para establecer el factor de zoom de la primera hoja de trabajo del archivo de Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
##  **Congelar paneles**
###  **Usando Microsoft Excel**
Congelar paneles es una característica proporcionada por Microsoft Excel. Congelar paneles le permite seleccionar datos para que permanezcan visibles al desplazarse por una hoja de trabajo.
###  **Aspose.Cells y congelar paneles**
 Aspose.Cells también permite a los desarrolladores aplicar paneles congelados a las hojas de trabajo en tiempo de ejecución. Aspose.Cells proporciona una clase[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo Excel Microsoft. El[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)colección que permite el acceso a cada hoja de cálculo en un archivo Excel.

Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase. El[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)La clase proporciona una amplia gama de métodos para administrar hojas de trabajo. Para configurar paneles congelados, llame al[congelarpaneles](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)método de la[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase. El[congelarpaneles](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)El método toma los siguientes parámetros:

- *Fila**, el índice de fila de la celda desde donde comenzará la congelación.
- *Columna**, el índice de columna de la celda desde donde comenzará la congelación.
- *Filas congeladas**, el número de filas visibles en el panel superior.
- *Columnas congeladas**, el número de columnas visibles en el panel izquierdo

 A continuación se proporciona un ejemplo completo que muestra cómo utilizar el[congelarpaneles](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)método para congelar filas y columnas (a partir de C4, representada por la cuarta fila y la tercera columna, donde las filas y columnas comienzan desde el índice 0) de la primera hoja de cálculo del archivo de Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
##  **Paneles divididos**
Si necesita dividir la pantalla para obtener dos vistas diferentes en la misma hoja de trabajo, divida los paneles. Microsoft Excel ofrece una característica muy útil que le permite ver más de una copia de su hoja de cálculo y poder desplazarse por cada panel de su hoja de cálculo de forma independiente: paneles divididos.

Los paneles funcionan simultáneamente. Si realiza un cambio en uno, el cambio aparece simultáneamente en el otro. Aspose.Cells proporciona la función de paneles divididos para los usuarios.
###  **Aplicar y eliminar paneles divididos**
####  **Dividir paneles**
 Aspose.Cells proporciona una clase[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo Excel Microsoft. El[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)La clase proporciona una amplia gama de métodos para administrar un archivo de Excel. Para implementar vistas divididas, utilice el[Dividir](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) método de la[Hoja de cálculo](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) clase. Para eliminar los paneles divididos, utilice el[EliminarDividir](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)método.

En el ejemplo, usamos un archivo de plantilla simple que se carga y luego la función de establecer paneles divididos se aplica en una celda de la primera hoja de trabajo. El archivo actualizado se guarda.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
####  **Quitar paneles**
 Elimine los paneles divididos usando el[EliminarDividir](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)método.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
