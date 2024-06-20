---
title: Vistas de Hoja de Cálculo
type: docs
weight: 40
url: /es/cpp/worksheet-views/
---

## **Vista previa de salto de página**
Todas las hojas de cálculo se pueden ver en dos modos:

- Vista normal.
- Vista previa de saltos de página.

La vista normal es la vista predeterminada de una hoja de cálculo. La vista previa de saltos de página es una vista de edición que muestra una hoja de cálculo tal como se imprimirá. La vista previa de saltos de página muestra qué datos irán en cada página para que puedas ajustar el área de impresión y los saltos de página. Utilizando Aspose.Cells los desarrolladores pueden habilitar los modos de vista normal o vista previa de saltos de página.
### **Controlando Modos de Vista**
Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) La clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una amplia gama de métodos para gestionar hojas de cálculo. Para habilitar los modos de vista normal o vista previa de saltos de página, utiliza el método [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) de la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) [IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) devuelve un valor bool, lo que significa que solo puede almacenar un valor **true** o **false**.
#### **Habilitar Vista Normal**
Establece una hoja de cálculo en vista normal configurando el método [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) de la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) a **false**.
#### **Habilitar vista previa de salto de página**
Configure cualquier hoja de cálculo para la vista previa de salto de página estableciendo el método [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) de la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) a **true**. Al hacerlo, cambiará la hoja de cálculo de la vista normal a la vista previa de salto de página.

A continuación se muestra un ejemplo completo que demuestra cómo utilizar el método [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) para habilitar el modo de vista previa de salto de página para la primera hoja de cálculo de un archivo de Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
## **Factor de zoom**
### **Usar Microsoft Excel**
Microsoft Excel ofrece una función que permite a los usuarios establecer el zoom o factor de escala de una hoja de cálculo. Esta función ayuda a los usuarios a ver el contenido de la hoja de cálculo en vistas más pequeñas o más grandes. Los usuarios pueden establecer el factor de zoom en cualquier valor.
### **Aspose.Cells y el factor de zoom**
Aspose.Cells también permite a los desarrolladores establecer el factor de zoom de la hoja de cálculo. Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una amplia gama de métodos para gestionar hojas de cálculo. Para establecer el factor de zoom de una hoja de cálculo, utilice el método [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) de la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). El factor de zoom se establece asignando un valor numérico (entero) al método [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/).

A continuación se muestra un ejemplo completo que demuestra cómo utilizar el método [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) para establecer el factor de zoom de la primera hoja de cálculo del archivo de Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
## **Congelar paneles**
### **Usar Microsoft Excel**
Fijar paneles es una función proporcionada por Microsoft Excel. Al fijar paneles, puedes seleccionar datos para que permanezcan visibles al desplazarte en una hoja de cálculo.
### **Aspose.Cells y fijar paneles**
Aspose.Cells también permite a los desarrolladores aplicar fijar paneles a las hojas de cálculo en tiempo de ejecución. Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona una amplia gama de métodos para gestionar hojas de cálculo. Para configurar fijar paneles, llama al método [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) de la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). El método [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) toma los siguientes parámetros:

- **Fila**, el índice de la fila desde la cual se iniciará la congelación.
- **Columna**, el índice de la columna desde la cual se iniciará la congelación.
- **Filas congeladas**, el número de filas visibles en el panel superior.
- **Columnas congeladas**, el número de columnas visibles en el panel izquierdo.

A continuación se muestra un ejemplo completo que muestra cómo usar el método [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) para congelar filas y columnas (a partir de C4, representado por la cuarta fila y tercera columna, donde las filas y columnas empiezan desde el índice 0) de la primera hoja de cálculo del archivo de Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
## **División de paneles**
Si necesita dividir la pantalla para obtener dos vistas diferentes en la misma hoja de cálculo, divida los paneles. Microsoft Excel ofrece una función muy útil que le permite ver más de una copia de su hoja de cálculo, y le permite desplazarse por cada panel de la hoja de cálculo de forma independiente: dividir los paneles.

Los paneles funcionan simultáneamente. Si realiza un cambio en uno, el cambio aparece simultáneamente en el otro. Aspose.Cells proporciona la función de dividir paneles para los usuarios.
### **Aplicación y eliminación de divisiones de paneles**
#### **División de paneles**
Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Microsoft Excel. La clase [Workbook] proporciona una amplia gama de métodos para gestionar un archivo de Excel. Para implementar vistas divididas, utilice el método [Split](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) de la clase [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Para eliminar la división de paneles, utilice el método [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/).

En el ejemplo, utilizamos un archivo de plantilla simple que se carga, luego se aplica la función de division de paneles en una celda de la primera hoja de cálculo. El archivo actualizado se guarda.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
#### **Eliminación de paneles**
Elimine las divisiones de paneles utilizando el método [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
