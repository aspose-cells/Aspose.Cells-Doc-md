---
title: Agrupación y desagrupación de filas y columnas
type: docs
weight: 50
url: /es/net/grouping-and-ungrouping-rows-and-columns/
---
## **Introducción**

En un archivo de Excel Microsoft, puede crear un esquema para los datos que le permita mostrar y ocultar niveles de detalle con un solo clic del mouse.

 Haga clic en el**Símbolos de contorno**, 1, 2, 3, + y - para mostrar rápidamente solo las filas o columnas que proporcionan resúmenes o encabezados para las secciones de una hoja de trabajo, o puede usar los símbolos para ver los detalles bajo un resumen o encabezado individual como se muestra a continuación en la figura :

|**Agrupación de Filas y Columnas.**|
|:- |
|![todo:imagen_alternativa_texto](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gestión de grupos de filas y columnas**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)colección que representa todas las celdas de la hoja de trabajo.

 los[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection proporciona varios métodos para administrar filas o columnas en una hoja de trabajo, algunos de estos se analizan a continuación con más detalle.

### **Agrupación de filas y columnas**

 Es posible agrupar filas o columnas llamando al[**Filas de grupo**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index) y[**GrupoColumnas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index) métodos de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) recopilación. Ambos métodos toman los siguientes parámetros:

- Índice de la primera fila/columna, la primera fila o columna del grupo.
- Índice de última fila/columna, la última fila o columna del grupo.
- Está oculto, un parámetro booleano que especifica si ocultar filas/columnas después de la agrupación o no.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **Configuración de grupo**

Microsoft Excel le permite configurar ajustes de grupo para mostrar:

- Filas de resumen debajo del detalle.
- Columnas de resumen a la derecha del detalle.

 Los desarrolladores pueden configurar estos ajustes de grupo usando el[**Esquema**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline) propiedad de la[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)clase.

### **Filas de resumen hasta debajo del detalle**

 Es posible controlar si las filas de resumen se muestran debajo del detalle configurando el[**Esquema**](https://reference.aspose.com/cells/net/aspose.cells/outline) clase'[**ResumenFilaDebajo**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow) propiedad a**verdadero** o**falso**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **Columnas de resumen a la derecha del detalle**

 Los desarrolladores también pueden controlar la visualización de columnas de resumen a la derecha del detalle configurando el[**ResumenColumnaDerecha**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright) propiedad de[**Esquema**](https://reference.aspose.com/cells/net/aspose.cells/outline) clase a**verdadero** o**falso**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **Desagrupar filas y columnas**

 Para desagrupar filas o columnas agrupadas, llame al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) colección[**Desagrupar filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) y[**DesagruparColumnas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns)métodos. Ambos métodos toman dos parámetros:

- Índice de la primera fila o columna, la primera fila/columna a desagrupar.
- Índice de la última fila o columna, la última fila/columna a desagrupar.

[**Desagrupar filas**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) tiene una sobrecarga que toma un tercer parámetro booleano. Configurándolo en**verdadero**elimina toda la información agrupada. De lo contrario, solo se elimina la información del grupo externo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
