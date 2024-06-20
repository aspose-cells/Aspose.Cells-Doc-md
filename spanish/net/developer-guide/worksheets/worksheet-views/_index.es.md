---
title: Vistas de Hoja de Cálculo
type: docs
weight: 40
url: /es/net/worksheet-views/
description: Este artículo describirá cómo usar C# y la API .NET para interactuar con la vista de salto de página de un libro de Excel y hojas de cálculo. Trabaje con divisiones de paneles, paneles congelados y factor de zoom. 
---

## **Vista previa de salto de página**

Todas las hojas de cálculo se pueden ver en dos modos:

- Vista normal.
- Vista previa de saltos de página.

La vista normal es la vista predeterminada de una hoja de cálculo. La vista previa de salto de página es una vista de edición que muestra una hoja de cálculo tal como se imprimirá. La vista previa de salto de página muestra qué datos irán en cada página para que pueda ajustar el área de impresión y los saltos de página. Usando Aspose.Cells, los desarrolladores pueden habilitar la vista normal o los modos de vista previa de salto de página.

### **Controlando Modos de Vista**

Aspose.Cells provee una clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para administrar hojas de cálculo. Para habilitar los modos de vista normal o vista previa de salto de página, use la propiedad [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) es una propiedad booleana, lo que significa que solo puede almacenar un valor **true** o un valor **false**.

#### **Habilitar Vista Normal**

Establezca una hoja de cálculo en vista normal configurando la propiedad [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) en **false**.

#### **Habilitar vista previa de salto de página**

Establezca cualquier hoja de cálculo en vista previa de salto de página configurando la propiedad [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) en **true**. Al hacerlo, cambia la hoja de cálculo de la vista normal a la vista previa de salto de página.

A continuación se muestra un ejemplo completo que demuestra cómo usar la propiedad [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) para habilitar el modo de vista previa de salto de página para la primera hoja de cálculo de un archivo de Excel.

El archivo book1.xls se abre creando una instancia de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). La vista se cambia a vista previa de salto de página para la primera hoja de cálculo configurando la propiedad [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) en **true**. El archivo modificado se guarda como output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **Factor de zoom**

### **Usar Microsoft Excel**

Microsoft Excel ofrece una función que permite a los usuarios establecer el zoom o factor de escala de una hoja de cálculo. Esta función ayuda a los usuarios a ver el contenido de la hoja de cálculo en vistas más pequeñas o más grandes. Los usuarios pueden establecer el factor de zoom en cualquier valor.

### **Aspose.Cells y el factor de zoom**

Aspose.Cells permite a los desarrolladores establecer el factor de zoom de la hoja de cálculo.
Aspose.Cells proporciona una clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para establecer el factor de zoom de una hoja de cálculo, utilice la propiedad [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) de la clase [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom). El factor de zoom se establece asignando un valor numérico (entero) a la propiedad [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) .

A continuación se muestra un ejemplo completo que demuestra cómo utilizar la propiedad [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) para establecer el factor de zoom de la primera hoja de cálculo del archivo de Excel.

El archivo book1.xls se abre creando una instancia de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). El factor de zoom de la primera hoja de cálculo se establece en 75 y el archivo modificado se guarda como output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **Congelar paneles**

### **Usar Microsoft Excel**

Fijar paneles es una función proporcionada por Microsoft Excel. Al fijar paneles, puedes seleccionar datos para que permanezcan visibles al desplazarte en una hoja de cálculo.

### **Aspose.Cells y fijar paneles**

Aspose.Cells permite a los desarrolladores aplicar bloquear paneles a las hojas de cálculo en tiempo de ejecución.

Aspose.Cells proporciona una clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para configurar bloquear paneles, llama al método [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) de la clase Hoja de cálculo. El método [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) toma los siguientes parámetros:

- **Fila**, el índice de la fila desde la cual se iniciará la congelación.
- **Columna**, el índice de la columna desde la cual se iniciará la congelación.
- **Filas congeladas**, el número de filas visibles en el panel superior.
- **Columnas congeladas**, el número de columnas visibles en el panel izquierdo.

El archivo book1.xls se abre llamando al constructor de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) mientras se instancia y se congelan algunas filas y columnas en la primera hoja de cálculo. El archivo modificado se guarda como output.xls.

A continuación se muestra un ejemplo completo que muestra cómo utilizar el método [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) para congelar filas y columnas (a partir de C4, representado por la cuarta fila y tercera columna, donde las filas y columnas empiezan desde el índice 0) de la primera hoja de cálculo del archivo de Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **División de paneles**

Si necesita dividir la pantalla para obtener dos vistas diferentes en la misma hoja de cálculo, divida los paneles. Microsoft Excel ofrece una función muy útil que le permite ver más de una copia de su hoja de cálculo, y le permite desplazarse por cada panel de la hoja de cálculo de forma independiente: dividir los paneles.

Los paneles funcionan simultáneamente. Si realiza un cambio en uno, el cambio aparece simultáneamente en el otro. Aspose.Cells proporciona la función de dividir paneles para los usuarios.

### **Aplicación y eliminación de divisiones de paneles**

#### **División de paneles**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ofrece una amplia gama de propiedades y métodos para administrar un archivo de Excel. Para implementar vistas divididas, use el [**Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Para eliminar los paneles divididos, use el método [**RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit).

En el ejemplo, utilizamos un archivo de plantilla simple que se carga, luego se aplica la función de division de paneles en una celda de la primera hoja de cálculo. El archivo actualizado se guarda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

Después de ejecutar el código anterior, el archivo generado tendrá una vista dividida.

#### **Eliminación de paneles**

Eliminar paneles divididos utilizando el método [**RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **Temas avanzados**
- [Ocultar la visualización de los valores cero en la hoja de cálculo](/cells/es/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Establecer el color de la pestaña de la hoja de cálculo](/cells/es/net/set-worksheet-tab-color/)
- [Mostrar y ocultar la cuadrícula y las cabeceras de filas y columnas](/cells/es/net/show-and-hide-gridlines-and-row-column-headers/)
- [Mostrar y ocultar filas, columnas y barras de desplazamiento](/cells/es/net/show-and-hide-rows-columns-and-scroll-bars/)
- [Mostrar y ocultar hojas de cálculo y pestañas](/cells/es/net/show-and-hide-worksheets-and-tabs/)
- [Mostrar fórmulas en lugar de valores en una hoja de cálculo](/cells/es/net/show-formulas-instead-of-values-in-a-worksheet/)
- [Utilizar opciones de verificación de errores](/cells/es/net/use-error-checking-options/)

