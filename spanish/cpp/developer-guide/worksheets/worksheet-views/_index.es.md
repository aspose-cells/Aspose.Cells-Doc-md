---
title: Vistas de la hoja de cálculo
type: docs
weight: 40
url: /es/cpp/worksheet-views/
---
## **La previsualización del salto de página**
Todas las hojas de trabajo se pueden ver en dos modos:

- Vista normal.
- La previsualización del salto de página.

La vista Normal es la vista predeterminada de una hoja de cálculo. La vista previa de salto de página es una vista de edición que muestra una hoja de trabajo tal como se imprimirá. La vista previa de salto de página muestra qué datos irán en cada página para que pueda ajustar el área de impresión y los saltos de página. Usando Aspose.Cells, los desarrolladores pueden habilitar la vista normal o los modos de vista previa de salto de página.
### **Modos de vista de control**
 Aspose.Cells proporciona una clase[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) que representa un archivo de Excel Microsoft. los[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)colección que permite el acceso a cada hoja de trabajo en un archivo de Excel.

 Una hoja de trabajo está representada por el[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)clase. los[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) La clase proporciona una amplia gama de métodos para administrar hojas de trabajo. Para habilitar los modos de vista previa normal o de salto de página, use el[IsPageBreakVista previa](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) metodo de la[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase.[IsPageBreakVista previa](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892) devuelve un valor booleano, lo que significa que solo puede almacenar un**verdadero** o**falso** valor.
#### **Habilitación de la vista normal**
Establezca una hoja de trabajo en vista normal configurando el[IsPageBreakVista previa](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)metodo de la[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase a**falso**.
#### **Habilitación de la vista previa de salto de página**
Establezca cualquier hoja de trabajo en la vista previa de salto de página configurando el[IsPageBreakVista previa](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)metodo de la[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase a**verdadero**Al hacerlo, la hoja de cálculo pasa de la vista normal a la vista previa de salto de página.

 A continuación se proporciona un ejemplo completo que demuestra cómo utilizar el[IsPageBreakVista previa](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)para habilitar el modo de vista previa de salto de página para la primera hoja de cálculo de un archivo de Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview.cpp" >}}
## **Factor de acercamiento**
### **Usando Microsoft Excel**
Microsoft Excel proporciona una función que permite a los usuarios establecer el zoom o el factor de escala de una hoja de cálculo. Esta característica ayuda a los usuarios a ver el contenido de la hoja de trabajo en vistas más pequeñas o más grandes. Los usuarios pueden establecer el factor de zoom en cualquier valor.
### **Aspose.Cells y factor de zoom**
 Aspose.Cells también permite a los desarrolladores establecer el factor de zoom de la hoja de trabajo. Aspose.Cells proporciona una clase[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) que representa un archivo de Excel Microsoft. los[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)colección que permite el acceso a cada hoja de trabajo en un archivo de Excel.

 Una hoja de trabajo está representada por el[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase. los[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)La clase proporciona una amplia gama de métodos para administrar hojas de trabajo. Para establecer el factor de zoom de una hoja de trabajo, use el[Zoom](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec) metodo de la[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase El factor de zoom se establece asignando un valor numérico (entero) a la[Zoom](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)método.

 A continuación se proporciona un ejemplo completo que demuestra cómo utilizar el[Zoom](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)método para establecer el factor de zoom de la primera hoja de trabajo del archivo de Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor.cpp" >}}
## **Congelar paneles**
### **Usando Microsoft Excel**
Congelar paneles es una función proporcionada por Microsoft Excel. La congelación de paneles le permite seleccionar datos para que permanezcan visibles al desplazarse por una hoja de trabajo.
### **Aspose.Cells y congelar paneles**
 Aspose.Cells también permite a los desarrolladores aplicar paneles congelados a hojas de trabajo en tiempo de ejecución. Aspose.Cells proporciona una clase[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) que representa un archivo de Excel Microsoft. los[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) la clase contiene un[Hojas de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)colección que permite el acceso a cada hoja de trabajo en un archivo de Excel.

 Una hoja de trabajo está representada por el[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase. los[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)La clase proporciona una amplia gama de métodos para administrar hojas de trabajo. Para configurar los paneles congelados, llame al[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)metodo de la[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase. los[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)método toma los siguientes parámetros:

- **Fila**, el índice de fila de la celda desde la que comenzará la congelación.
- **Columna**, el índice de columna de la celda desde la que comenzará la congelación.
- **filas congeladas**, el número de filas visibles en el panel superior.
- **Columnas congeladas**, el número de columnas visibles en el panel izquierdo

 A continuación se muestra un ejemplo completo que muestra cómo utilizar el[FreezePanes](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)método para congelar filas y columnas (a partir de C4, representada por la 4.ª fila y la 3.ª columna, donde las filas y columnas comienzan desde el índice 0) de la primera hoja de cálculo del archivo de Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes.cpp" >}}
## **Paneles divididos**
Si necesita dividir la pantalla para obtener dos vistas diferentes en la misma hoja de trabajo, divida los paneles. Microsoft Excel ofrece una función muy útil que le permite ver más de una copia de su hoja de trabajo y que pueda desplazarse por cada panel de su hoja de trabajo de forma independiente: paneles divididos.

Los paneles funcionan simultáneamente. Si realiza un cambio en uno, el cambio aparece simultáneamente en el otro. Aspose.Cells proporciona la función de paneles divididos para los usuarios.
### **Aplicar y quitar paneles divididos**
#### **División de paneles**
 Aspose.Cells proporciona una clase[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) que representa un archivo de Excel Microsoft. los[ILibro de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)class proporciona una amplia gama de métodos para administrar un archivo de Excel. Para implementar vistas divididas, use el[Separar](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a0e581a3a9528a767c57008521ee02b6f) metodo de la[IHoja de trabajo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) clase. Para quitar los paneles divididos, use el[EliminarDividir](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)método.

En el ejemplo, usamos un archivo de plantilla simple que se carga, luego se aplica la función de conjuntos de paneles divididos en una celda de la primera hoja de trabajo. El archivo actualizado se guarda.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes.cpp" >}}
#### **Eliminación de paneles**
 Retire los paneles divididos con el[EliminarDividir](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)método.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes.cpp" >}}
