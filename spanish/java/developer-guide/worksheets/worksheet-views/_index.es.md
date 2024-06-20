---
title: Vistas de Hoja de Cálculo
type: docs
weight: 10
url: /es/java/worksheet-views/
---

## **Vista previa de salto de página**
Todas las hojas de cálculo se pueden ver en dos modos:

- Vista normal.
- Vista previa de saltos de página.

Una vista normal es la vista predeterminada de una hoja de cálculo. La vista previa de salto de página es una vista de edición que muestra una hoja de cálculo tal como se imprimirá. La vista previa de salto de página muestra qué datos se colocarán en cada página para que puedas ajustar el área de impresión y los saltos de página. Usando Aspose.Cells, los desarrolladores pueden habilitar los modos de vista normal o vista previa de salto de página.
### **Controlando Modos de Vista**
Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para habilitar los modos de vista normal o vista previa de salto de página, utiliza el método [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) de la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).
#### **Habilitar Vista Normal**
Establece cualquier hoja de cálculo en vista normal utilizando el método [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) de la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) y pasando **false** como parámetro.
#### **Habilitar vista previa de salto de página**
Establece cualquier hoja de cálculo en vista previa de salto de página utilizando el método [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) de la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) y pasando **true** como parámetro.

A continuación se muestra un ejemplo completo que demuestra el uso del método [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) de la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) para habilitar el modo de vista previa de salto de página para la primera hoja de cálculo del archivo de Excel.

En la captura de pantalla a continuación, puedes ver que el archivo Book1.xls está en Vista Normal.

**Book1.xls: Hoja de cálculo antes de la modificación** 

![todo:image_alt_text](worksheet-views_1.png)

Se abre el archivo Book1.xls con la clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) y el modo se cambia a vista previa de salto de página para la primera hoja de cálculo. El archivo modificado se guarda como output.xls.

**Ouput.xls: hoja de cálculo después de la modificación** 

![todo:image_alt_text](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **Factor de zoom**
Microsoft Excel ofrece una función que permite a los usuarios establecer el zoom o factor de escala de una hoja de cálculo. Esta función ayuda a los usuarios a ver el contenido de la hoja de cálculo en vistas más pequeñas o más grandes. Los usuarios pueden establecer el factor de zoom en cualquier valor.

**Configuración del Factor de Zoom utilizando Microsoft Excel** 

![todo:image_alt_text](worksheet-views_3.png)

Aspose.Cells también permite a los desarrolladores establecer el factor de zoom de la hoja de cálculo.
### **Controlando el Factor de Zoom**
Aspose.Cells proporciona una [clase Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Microsoft Excel. La [clase Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la [clase Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La [clase Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para administrar hojas de cálculo. Para establecer el factor de zoom de una hoja de cálculo, utilice el método [setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom) de la [clase Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

A continuación, se muestra un ejemplo completo que demuestra cómo utilizar el método [setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom) para establecer el factor de zoom de la primera hoja de cálculo en un archivo de Excel.

En la captura de pantalla siguiente, puedes ver el archivo Book1.xls en la vista predeterminada.

**Book1.xls: hoja de cálculo antes de la modificación** 

![todo:image_alt_text](worksheet-views_4.png)

El archivo Book1.xls se abre con la clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) y el factor de zoom de la primera hoja de cálculo se establece en 75. El archivo modificado se guarda como output.xls.

**Output.xls: hoja de cálculo después de la modificación** 

![todo:image_alt_text](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **Congelar paneles**
Fijar paneles es una función proporcionada por Microsoft Excel. Al fijar paneles, puedes seleccionar datos para que permanezcan visibles al desplazarte en una hoja de cálculo.

**Uso de paneles congelados en Microsoft Excel** 

![todo:image_alt_text](worksheet-views_6.png)

Aspose.Cells también permite a los desarrolladores aplicar paneles congelados a las hojas de cálculo en tiempo de ejecución.

Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene una [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar las hojas de cálculo. Para configurar los paneles congelados, llama al método [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) de la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). El método [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) toma los siguientes parámetros:

- **Fila**, el índice de la fila desde la cual se iniciará la congelación.
- **Columna**, el índice de la columna desde la cual se iniciará la congelación.
- **Filas congeladas**, el número de filas visibles en el panel superior.
- **Columnas congeladas**, el número de columnas visibles en el panel izquierdo.

A continuación se muestra un ejemplo completo que muestra cómo usar el método [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) de la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) para congelar filas y columnas (a partir de C4, representado por la cuarta fila y la tercera columna, donde las filas y columnas comienzan desde índices 0) de la primera hoja de cálculo del archivo de Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


En la captura de pantalla siguiente, puedes ver el archivo Book1.xls sin paneles congelados.

**Book1.xls: vista de la hoja de cálculo antes de cualquier modificación** 

![todo:image_alt_text](worksheet-views_7.png)

El archivo Book1.xls se abre con la clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) y luego se congelan algunas filas y columnas en la primera hoja de cálculo. El archivo modificado se guarda como output.xls.

**Outlook.xls: vista de hoja de cálculo después de la modificación** 

![todo:image_alt_text](worksheet-views_8.png)
## **División de paneles**
Si necesita dividir la pantalla para obtener dos vistas diferentes en la misma hoja de cálculo, divida los paneles. Microsoft Excel ofrece una función muy útil que le permite ver más de una copia de su hoja de cálculo, y le permite desplazarse por cada panel de la hoja de cálculo de forma independiente: dividir los paneles.

Los paneles funcionan simultáneamente. Si realiza un cambio en uno, el cambio aparece simultáneamente en el otro. Aspose.Cells proporciona la función de dividir paneles para los usuarios.
### **Aplicación y eliminación de divisiones de paneles**
#### **División de paneles**
Aspose.Cells proporciona una clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) proporciona una amplia gama de propiedades y métodos para manejar archivos de Excel. Para implementar vistas divididas, utilice el método [split](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split\(\)) de la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Para eliminar divisiones de paneles, utilice el método [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)).

En el ejemplo, utilizamos un archivo de plantilla simple que se carga, luego se aplica la función de division de paneles en una celda de la primera hoja de cálculo. El archivo actualizado se guarda.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



Después de ejecutar el código anterior, el archivo generado tiene una vista dividida.

**Divisiones de paneles en el archivo de salida** 

![todo:image_alt_text](worksheet-views_9.png)
#### **Eliminación de paneles**
Los desarrolladores pueden eliminar divisiones de paneles utilizando el método [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **Temas avanzados**
- [Ocultar la visualización de los valores cero en la hoja de cálculo](/cells/es/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Establecer el color de la pestaña de la hoja de cálculo](/cells/es/java/set-worksheet-tab-color/)
- [Mostrar y ocultar elementos](/cells/es/java/show-and-hide-elements/)
- [Mostrar fórmulas en lugar de valores en una hoja de cálculo](/cells/es/java/show-formulas-instead-of-values-in-a-worksheet/)
- [Utilizar opciones de verificación de errores](/cells/es/java/use-error-checking-options/)
