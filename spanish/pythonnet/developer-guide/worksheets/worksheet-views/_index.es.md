---
title: Vistas de Hoja de Cálculo
type: docs
weight: 40
url: /es/python-net/worksheet-views/
description: Este artículo describirá cómo usar la API de Aspose.Cells para Python via .NET para interactuar con la vista previa de salto de página de un libro de trabajo y hojas de cálculo de Excel. Trabajar con paneles divididos, paneles congelados y factor de zoom también. 
keywords: Biblioteca de Excel en Python, Cómo configurar Vista previa de saltos de página en Python, Cómo habilitar vista normal en Python, Cómo establecer el factor de zoom en Python, Cómo congelar paneles en Python, Cómo dividir paneles en Python, Cómo eliminar paneles en Python.
---

## **Vista previa de salto de página**

Todas las hojas de cálculo se pueden ver en dos modos:

- Vista normal.
- Vista previa de saltos de página.

La vista normal es la vista predeterminada de una hoja de cálculo. La vista previa de saltos de página es una vista de edición que muestra una hoja de cálculo tal como se imprimirá. La vista previa de saltos de página muestra qué datos irán en cada página para que puedas ajustar el área de impresión y los saltos de página. Usando Aspose.Cells para Python via .NET, los desarrolladores pueden habilitar modos de vista normal o vista previa de saltos de página.

### **Controlando Modos de Vista**

Aspose.Cells para Python via .NET ofrece una clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para administrar hojas de cálculo. Para habilitar los modos de vista normal o vista previa de salto de página, use la propiedad [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) es una propiedad booleana, lo que significa que solo puede almacenar un valor **true** o un valor **false**.

#### **Habilitar Vista Normal**

Establezca una hoja de cálculo en vista normal configurando la propiedad [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) en **false**.

#### **Habilitar vista previa de salto de página**

Establezca cualquier hoja de cálculo en vista previa de salto de página configurando la propiedad [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) en **true**. Al hacerlo, cambia la hoja de cálculo de la vista normal a la vista previa de salto de página.

A continuación se muestra un ejemplo completo que demuestra cómo usar la propiedad [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) para habilitar el modo de vista previa de salto de página para la primera hoja de cálculo de un archivo de Excel.

El archivo book1.xls se abre creando una instancia de la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). La vista se cambia a vista previa de salto de página para la primera hoja de cálculo configurando la propiedad [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) en **true**. El archivo modificado se guarda como output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-PageBreakPreview-1.py" >}}

## **Factor de zoom**

### **Usar Microsoft Excel**

Microsoft Excel ofrece una función que permite a los usuarios establecer el zoom o factor de escala de una hoja de cálculo. Esta función ayuda a los usuarios a ver el contenido de la hoja de cálculo en vistas más pequeñas o más grandes. Los usuarios pueden establecer el factor de zoom en cualquier valor.

### **Aspose.Cells y el factor de zoom**

Aspose.Cells permite a los desarrolladores establecer el factor de zoom de la hoja de cálculo.
Aspose.Cells proporciona una clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para establecer el factor de zoom de una hoja de cálculo, utilice la propiedad [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) de la clase [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom). El factor de zoom se establece asignando un valor numérico (entero) a la propiedad [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) .

A continuación se muestra un ejemplo completo que demuestra cómo utilizar la propiedad [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) para establecer el factor de zoom de la primera hoja de cálculo del archivo de Excel.

El archivo book1.xls se abre creando una instancia de la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). El factor de zoom de la primera hoja de cálculo se establece en 75 y el archivo modificado se guarda como output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ZoomFactor-1.py" >}}

## **Congelar paneles**

### **Usar Microsoft Excel**

Fijar paneles es una función proporcionada por Microsoft Excel. Al fijar paneles, puedes seleccionar datos para que permanezcan visibles al desplazarte en una hoja de cálculo.

### **Aspose.Cells y fijar paneles**

Aspose.Cells permite a los desarrolladores aplicar bloquear paneles a las hojas de cálculo en tiempo de ejecución.

Aspose.Cells proporciona una clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para configurar bloquear paneles, llama al método [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int) de la clase Hoja de cálculo. El método [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int) toma los siguientes parámetros:

- **fila**, el índice de fila desde donde comenzará el congelamiento.
- **columna**, el índice de columna desde donde comenzará el congelamiento.
- **filas congeladas**, el número de filas visibles en el panel superior.
- **columnas congeladas**, el número de columnas visibles en el panel izquierdo.

El archivo book1.xls se abre llamando al constructor de la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) mientras se instancia y se congelan algunas filas y columnas en la primera hoja de cálculo. El archivo modificado se guarda como output.xls.

A continuación se muestra un ejemplo completo que muestra cómo utilizar el método [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) para congelar filas y columnas (a partir de C4, representado por la cuarta fila y tercera columna, donde las filas y columnas empiezan desde el índice 0) de la primera hoja de cálculo del archivo de Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-FreezePanes-1.py" >}}

## **División de paneles**

Si necesita dividir la pantalla para obtener dos vistas diferentes en la misma hoja de cálculo, divida los paneles. Microsoft Excel ofrece una función muy útil que le permite ver más de una copia de su hoja de cálculo, y le permite desplazarse por cada panel de la hoja de cálculo de forma independiente: dividir los paneles.

Los paneles funcionan simultáneamente. Si realiza un cambio en uno, el cambio aparece simultáneamente en el otro. Aspose.Cells proporciona la función de dividir paneles para los usuarios.

### **Aplicación y eliminación de divisiones de paneles**

#### **División de paneles**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) ofrece una amplia gama de propiedades y métodos para administrar un archivo de Excel. Para implementar vistas divididas, use el [**split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split) de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Para eliminar los paneles divididos, use el método [**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split).

En el ejemplo, utilizamos un archivo de plantilla simple que se carga, luego se aplica la función de division de paneles en una celda de la primera hoja de cálculo. El archivo actualizado se guarda.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-SplitPanes-1.py" >}}

Después de ejecutar el código anterior, el archivo generado tendrá una vista dividida.

#### **Eliminación de paneles**

Eliminar paneles divididos utilizando el método [**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-RemovePanes-1.py" >}}

## **Temas avanzados**
- [Ocultar la visualización de los valores cero en la hoja de cálculo](/cells/es/python-net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Establecer el color de la pestaña de la hoja de cálculo](/cells/es/python-net/set-worksheet-tab-color/)
- [Mostrar y ocultar la cuadrícula y las cabeceras de filas y columnas](/cells/es/python-net/show-and-hide-gridlines-and-row-column-headers/)
- [Mostrar y ocultar filas, columnas y barras de desplazamiento](/cells/es/python-net/show-and-hide-rows-columns-and-scroll-bars/)
- [Mostrar y ocultar hojas de cálculo y pestañas](/cells/es/python-net/show-and-hide-worksheets-and-tabs/)
- [Mostrar fórmulas en lugar de valores en una hoja de cálculo](/cells/es/python-net/show-formulas-instead-of-values-in-a-worksheet/)
- [Utilizar opciones de verificación de errores](/cells/es/python-net/use-error-checking-options/)

{{< app/cells/assistant language="python-net" >}}
