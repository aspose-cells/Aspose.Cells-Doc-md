---
title: Vistas de la hoja de cálculo
type: docs
weight: 40
url: /es/net/worksheet-views/
---
## **La previsualización del salto de página**

Todas las hojas de trabajo se pueden ver en dos modos:

- Vista normal.
- La previsualización del salto de página.

La vista normal es la vista predeterminada de una hoja de trabajo. La vista previa de salto de página es una vista de edición que muestra una hoja de trabajo tal como se imprimirá. La vista previa de salto de página muestra qué datos irán en cada página para que pueda ajustar el área de impresión y los saltos de página. Usando Aspose.Cells, los desarrolladores pueden habilitar la vista normal o los modos de vista previa de salto de página.

### **Modos de vista de control**

Aspose.Cells proporciona un[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite el acceso a cada hoja de trabajo en un archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo. Para habilitar los modos de vista previa normal o de salto de página, use el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase[**IsPageBreakVista previa**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) propiedad.[**IsPageBreakVista previa**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) es una propiedad booleana, lo que significa que solo puede almacenar una**verdadero** o un**falso** valor.

#### **Habilitación de la vista normal**

 Establezca una hoja de trabajo en vista normal configurando el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase[**IsPageBreakVista previa**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) propiedad a**falso**.

#### **Habilitación de la vista previa de salto de página**

 Establezca cualquier hoja de trabajo en la vista previa de salto de página configurando el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase[**IsPageBreakVista previa**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) propiedad a**verdadero**Al hacerlo, la hoja de cálculo pasa de la vista normal a la vista previa de salto de página.

 A continuación se proporciona un ejemplo completo que demuestra cómo utilizar el[**IsPageBreakVista previa**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)propiedad para habilitar el modo de vista previa de salto de página para la primera hoja de cálculo de un archivo de Excel.

El archivo book1.xls se abre creando una instancia del[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase. La vista se cambia a vista previa de salto de página para la primera hoja de trabajo configurando el[**IsPageBreakVista previa**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)propiedad a**verdadero**. El archivo modificado se guarda como salida.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **Factor de acercamiento**

### **Usando Microsoft Excel**

Microsoft Excel proporciona una función que permite a los usuarios establecer el zoom o el factor de escala de una hoja de cálculo. Esta característica ayuda a los usuarios a ver el contenido de la hoja de trabajo en vistas más pequeñas o más grandes. Los usuarios pueden establecer el factor de zoom en cualquier valor.

### **Aspose.Cells y factor de zoom**

Aspose.Cells permite a los desarrolladores establecer el factor de zoom de la hoja de trabajo.
Aspose.Cells proporciona un[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite el acceso a cada hoja de trabajo en un archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo. Para establecer el factor de zoom de una hoja de trabajo, use el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase'[**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom)propiedad. El factor de zoom se establece asignando un valor numérico (entero) al[**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) propiedad.

A continuación se proporciona un ejemplo completo que demuestra cómo utilizar el[**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) propiedad para establecer el factor de zoom de la primera hoja de cálculo del archivo de Excel.

El archivo book1.xls se abre creando una instancia del[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)clase. El factor de zoom de la primera hoja de trabajo se establece en 75 y el archivo modificado se guarda como salida.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **Congelar paneles**

### **Usando Microsoft Excel**

Congelar paneles es una función proporcionada por Microsoft Excel. La congelación de paneles le permite seleccionar datos para que permanezcan visibles al desplazarse por una hoja de trabajo.

### **Aspose.Cells y congelar paneles**

Aspose.Cells permite a los desarrolladores aplicar paneles congelados a hojas de trabajo en tiempo de ejecución.

Aspose.Cells proporciona un[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)clase que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite el acceso a cada hoja de trabajo en un archivo de Excel.

Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo. Para configurar paneles congelados, llame a la clase Worksheet'[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)método. los[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)método toma los siguientes parámetros:

- **Fila**, el índice de fila de la celda desde la que comenzará la congelación.
- **Columna**, el índice de columna de la celda desde la que comenzará la congelación.
- **filas congeladas**, el número de filas visibles en el panel superior.
- **Columnas congeladas**, el número de columnas visibles en el panel izquierdo

El archivo book1.xls se abre llamando al[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)constructor de clase mientras se crea una instancia y algunas filas y columnas se congelan en la primera hoja de trabajo. El archivo modificado se guarda como salida.xls.

 A continuación se muestra un ejemplo completo que muestra cómo utilizar el[**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)método para congelar filas y columnas (a partir de C4, representada por la cuarta fila y la tercera columna, donde las filas y columnas comienzan desde el índice 0) de la primera hoja de cálculo del archivo de Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **Paneles divididos**

Si necesita dividir la pantalla para obtener dos vistas diferentes en la misma hoja de trabajo, divida los paneles. Microsoft Excel ofrece una función muy útil que le permite ver más de una copia de su hoja de trabajo y que pueda desplazarse por cada panel de su hoja de trabajo de forma independiente: paneles divididos.

Los paneles funcionan simultáneamente. Si realiza un cambio en uno, el cambio aparece simultáneamente en el otro. Aspose.Cells proporciona la función de paneles divididos para los usuarios.

### **Aplicar y quitar paneles divididos**

#### **División de paneles**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) La clase proporciona una amplia gama de propiedades y métodos para administrar un archivo de Excel. Para implementar vistas divididas, use el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase'[**Separar**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split) . Para quitar los paneles divididos, use el[**EliminarDividir**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)método.

En el ejemplo, usamos un archivo de plantilla simple que se carga, luego se aplica la función de conjuntos de paneles divididos en una celda de la primera hoja de trabajo. El archivo actualizado se guarda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

Después de ejecutar el código anterior, el archivo generado tendrá una vista dividida.

#### **Eliminación de paneles**

 Retire los paneles divididos con el[**EliminarDividir**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)método.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **Temas avanzados**
- [Ocultar la visualización de valores cero en la hoja de trabajo](/cells/es/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Establecer el color de la pestaña de la hoja de trabajo](/cells/es/net/set-worksheet-tab-color/)
- [Mostrar y ocultar líneas de cuadrícula y encabezados de columna de fila](/cells/es/net/show-and-hide-gridlines-and-row-column-headers/)
- [Mostrar y ocultar filas, columnas y barras de desplazamiento](/cells/es/net/show-and-hide-rows-columns-and-scroll-bars/)
- [Mostrar y ocultar hojas de trabajo y pestañas](/cells/es/net/show-and-hide-worksheets-and-tabs/)
- [Mostrar fórmulas en lugar de valores en una hoja de cálculo](/cells/es/net/show-formulas-instead-of-values-in-a-worksheet/)
- [Usar opciones de comprobación de errores](/cells/es/net/use-error-checking-options/)

