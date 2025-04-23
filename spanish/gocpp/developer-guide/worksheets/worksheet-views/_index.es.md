---
title: Vistas de Hoja de Cálculo
type: docs
weight: 40
url: /es/go-cpp/worksheet-views/
---

## **Vista previa de salto de página**

Todas las hojas de cálculo se pueden ver en dos modos:

- Vista normal.
- Vista previa de saltos de página.

La vista normal es la vista predeterminada de una hoja de cálculo. La vista previa de saltos de página es una vista de edición que muestra una hoja de cálculo tal como se imprimirá. La vista previa de saltos de página muestra qué datos irán en cada página para que puedas ajustar el área de impresión y los saltos de página. Utilizando Aspose.Cells los desarrolladores pueden habilitar los modos de vista normal o vista previa de saltos de página.

### **Controlando Modos de Vista**

Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una colección [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) ofrece una amplia gama de métodos para gestionar hojas de cálculo. Para habilitar los modos de vista previa normal o de salto de página, use el método [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) de la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). [IsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/ispagebreakpreview/) devuelve un valor bool, lo que significa que solo puede almacenar un valor **true** o **false**.

#### **Habilitar Vista Normal**

Establece una hoja de cálculo en vista normal configurando el método [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) de la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) en **false**.

#### **Habilitar vista previa de salto de página**

Configure cualquier hoja de cálculo en vista previa de salto de página configurando el método [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) de la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) en **true**. Al hacerlo, la hoja de cálculo cambia de vista normal a vista previa de salto de página.

A continuación se muestra un ejemplo completo que demuestra cómo usar el método [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) para habilitar el modo de vista previa del salto de página para la primera hoja de cálculo de un archivo de Excel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnablingPageBreakPreview.go" >}}

## **Factor de zoom**

### **Usar Microsoft Excel**

Microsoft Excel ofrece una función que permite a los usuarios establecer el zoom o factor de escala de una hoja de cálculo. Esta función ayuda a los usuarios a ver el contenido de la hoja de cálculo en vistas más pequeñas o más grandes. Los usuarios pueden establecer el factor de zoom en cualquier valor.

### **Aspose.Cells y el factor de zoom**

Aspose.Cells también permite a los desarrolladores configurar el factor de zoom de la hoja de cálculo. Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una colección [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) ofrece una amplia gama de métodos para gestionar hojas de cálculo. Para establecer el factor de zoom de una hoja, use el método [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) de la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). El factor de zoom se establece asignando un valor numérico (entero) al método [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/).

A continuación se muestra un ejemplo completo que demuestra cómo usar el método [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) para establecer el factor de zoom de la primera hoja de cálculo del archivo de Excel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ZoomFactor.go" >}}

## **Congelar paneles**

### **Usar Microsoft Excel**

Fijar paneles es una función proporcionada por Microsoft Excel. Al fijar paneles, puedes seleccionar datos para que permanezcan visibles al desplazarte en una hoja de cálculo.

### **Aspose.Cells y fijar paneles**

Aspose.Cells también permite a los desarrolladores aplicar paneles de congelación a las hojas de cálculo en tiempo de ejecución. Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contiene una colección [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) ofrece una amplia gama de métodos para gestionar hojas de cálculo. Para configurar paneles de congelación, llama al método [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) de la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). El método [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) toma los siguientes parámetros:

- **Fila**, el índice de la fila desde la cual se iniciará la congelación.
- **Columna**, el índice de la columna desde la cual se iniciará la congelación.
- **Filas congeladas**, el número de filas visibles en el panel superior.
- **Columnas congeladas**, el número de columnas visibles en el panel izquierdo.

A continuación se muestra un ejemplo completo que explica cómo usar el método [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) para congelar filas y columnas (empezando desde C4, representado por la cuarta fila y la tercera columna, donde las filas y columnas comienzan desde el índice 0) de la primera hoja de cálculo del archivo de Excel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FreezePanes.go" >}}

## **División de paneles**

Si necesita dividir la pantalla para obtener dos vistas diferentes en la misma hoja de cálculo, divida los paneles. Microsoft Excel ofrece una función muy útil que le permite ver más de una copia de su hoja de cálculo, y le permite desplazarse por cada panel de la hoja de cálculo de forma independiente: dividir los paneles.

Los paneles funcionan simultáneamente. Si realiza un cambio en uno, el cambio aparece simultáneamente en el otro. Aspose.Cells proporciona la función de dividir paneles para los usuarios.

### **Aplicación y eliminación de divisiones de paneles**

#### **División de paneles**

Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) ofrece una amplia gama de métodos para gestionar un archivo de Excel. Para implementar vistas divididas, utilice el método [Split](https://reference.aspose.com/cells/go-cpp/worksheet/split/) de la clase [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Para eliminar los paneles divididos, use el método [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/).

En el ejemplo, utilizamos un archivo de plantilla simple que se carga, luego se aplica la función de division de paneles en una celda de la primera hoja de cálculo. El archivo actualizado se guarda.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SplitPanes.go" >}}

#### **Eliminación de paneles**

Eliminar paneles divididos usando el método [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingPanes.go" >}}
