---
title: Vistas de la hoja de cálculo
type: docs
weight: 10
url: /es/java/worksheet-views/
---
## **La previsualización del salto de página**
Todas las hojas de trabajo se pueden ver en dos modos:

- Vista normal.
- La previsualización del salto de página.

Una vista normal es la vista predeterminada de una hoja de trabajo. La vista previa de salto de página es una vista de edición que muestra una hoja de trabajo tal como se imprimirá. La vista previa de salto de página muestra qué datos irán en cada página para que pueda ajustar el área de impresión y los saltos de página. Usando Aspose.Cells, los desarrolladores pueden habilitar la vista normal o los modos de vista previa de salto de página.
### **Modos de vista de control**
 Aspose.Cells proporciona un[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) clase que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)que permite el acceso a cada hoja de trabajo en un archivo de Excel.

 Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase. los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo. Para habilitar los modos de vista previa normal o de salto de página, use el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase'[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)método.
#### **Habilitación de la vista normal**
Establezca cualquier hoja de trabajo en vista normal usando el[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) metodo de la[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase y aprobación**falso** como parámetro.
#### **Habilitación de la vista previa de salto de página**
Establezca cualquier hoja de trabajo en vista previa de salto de página usando el[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)metodo de la[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase y aprobación**verdadero**como parámetro.

 A continuación se muestra un ejemplo completo que demuestra el uso de la[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase'[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)para habilitar el modo de vista previa de salto de página para la primera hoja de cálculo del archivo de Excel.

En la captura de pantalla a continuación, puede ver que el archivo Book1.xls está en Vista normal.

**Book1.xls: Hoja de trabajo antes de la modificación** 

![todo:imagen_alternativa_texto](worksheet-views_1.png)

 Book1.xls se abre con el[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class y el modo se cambia a vista previa de salto de página para la primera hoja de trabajo. El archivo modificado se guarda como salida.xls.

**Ouput.xls: hoja de trabajo después de la modificación** 

![todo:imagen_alternativa_texto](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **Factor de acercamiento**
Microsoft Excel proporciona una función que permite a los usuarios establecer el zoom o el factor de escala de una hoja de cálculo. Esta característica ayuda a los usuarios a ver el contenido de la hoja de trabajo en vistas más pequeñas o más grandes. Los usuarios pueden establecer el factor de zoom en cualquier valor.

**Configuración del factor de zoom usando Microsoft Excel** 

![todo:imagen_alternativa_texto](worksheet-views_3.png)

Aspose.Cells también permite a los desarrolladores establecer el factor de zoom de la hoja de trabajo.
### **Controlar el factor de zoom**
Aspose.Cells proporciona un[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) clase que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)que permite el acceso a cada hoja de trabajo en un archivo de Excel.

 Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase. los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo. Para establecer el factor de zoom de una hoja de trabajo, use el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase'[establecerZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)método.

 A continuación se proporciona un ejemplo completo que demuestra cómo utilizar el[establecerZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)método para establecer el factor de zoom de la primera hoja de trabajo en un archivo de Excel.

En la siguiente captura de pantalla, puede ver el archivo Book1.xls en la vista predeterminada.

**Book1.xls: hoja de trabajo antes de la modificación** 

![todo:imagen_alternativa_texto](worksheet-views_4.png)

 El archivo Book1.xls se abre con el[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class y el factor de zoom de la primera hoja de trabajo se establece en 75. El archivo modificado se guarda como salida.xls.

**Output.xls: hoja de trabajo después de la modificación** 

![todo:imagen_alternativa_texto](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **Congelar paneles**
Congelar paneles es una función proporcionada por Microsoft Excel. La congelación de paneles le permite seleccionar datos para que permanezcan visibles al desplazarse por una hoja de cálculo.

**Uso de paneles congelados en Microsoft Excel** 

![todo:imagen_alternativa_texto](worksheet-views_6.png)

Aspose.Cells también permite a los desarrolladores aplicar paneles congelados a hojas de trabajo en tiempo de ejecución.

Aspose.Cells proporciona un[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) clase que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)que permite el acceso a cada hoja de trabajo en un archivo de Excel.

 Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase. los[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo. Para configurar los paneles congelados, llame al[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase'[congelar paneles](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\) ) método. los[congelar paneles](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) método toma los siguientes parámetros:

- **Fila**, el índice de fila de la celda desde la que comenzará la congelación.
- **Columna**, el índice de columna de la celda desde la que comenzará la congelación.
- **filas congeladas**, el número de filas visibles en el panel superior.
- **Columnas congeladas**, el número de columnas visibles en el panel izquierdo

 A continuación se muestra un ejemplo completo que muestra cómo utilizar el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase'[congelar paneles](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) para congelar filas y columnas (a partir de C4, representada por la 4.ª fila y la 3.ª columna, donde las filas y columnas comienzan desde 0 índices) de la primera hoja de cálculo del archivo de Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


En la captura de pantalla a continuación, puede ver el archivo Book1.xls sin paneles congelados.

**Book1.xls: vista de la hoja de trabajo antes de cualquier modificación** 

![todo:imagen_alternativa_texto](worksheet-views_7.png)

 El archivo Book1.xls se abre con el[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class y luego algunas filas y columnas se congelan en la primera hoja de trabajo. El archivo modificado se guarda como salida.xls.

**Outlook.xls: vista de hoja de trabajo después de la modificación** 

![todo:imagen_alternativa_texto](worksheet-views_8.png)
## **Paneles divididos**
Si necesita dividir la pantalla para obtener dos vistas diferentes en la misma hoja de trabajo, divida los paneles. Microsoft Excel ofrece una función muy útil que le permite ver más de una copia de su hoja de trabajo y que pueda desplazarse por cada panel de su hoja de trabajo de forma independiente: paneles divididos.

Los paneles funcionan simultáneamente. Si realiza un cambio en uno, el cambio aparece simultáneamente en el otro. Aspose.Cells proporciona la función de paneles divididos para los usuarios.
### **Aplicar y quitar paneles divididos**
#### **División de paneles**
Aspose.Cells proporciona un[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) clase que representa un archivo de Excel Microsoft. los[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)La clase proporciona una amplia gama de propiedades y métodos para administrar archivos de Excel. Para implementar vistas divididas, use el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase'[separar](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split\(\) ) método. Para eliminar los paneles divididos, use el[eliminarDividir](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) método.

En el ejemplo, usamos un archivo de plantilla simple que se carga, luego se aplica la función de conjuntos de paneles divididos en una celda de la primera hoja de cálculo. El archivo actualizado se guarda.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



Después de ejecutar el código anterior, el archivo generado tiene una vista dividida.

**Dividir paneles en el archivo de salida** 

![todo:imagen_alternativa_texto](worksheet-views_9.png)
#### **Eliminación de paneles**
 Los desarrolladores pueden eliminar paneles divididos usando el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase'[eliminarDividir](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) método.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **Temas avanzados**
- [Ocultar la visualización de valores cero en la hoja de trabajo](/cells/es/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Establecer el color de la pestaña de la hoja de trabajo](/cells/es/java/set-worksheet-tab-color/)
- [Mostrar y ocultar elementos](/cells/es/java/show-and-hide-elements/)
- [Mostrar fórmulas en lugar de valores en una hoja de trabajo](/cells/es/java/show-formulas-instead-of-values-in-a-worksheet/)
- [Usar opciones de comprobación de errores](/cells/es/java/use-error-checking-options/)
