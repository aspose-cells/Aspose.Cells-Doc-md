---
title: Agrupando y Desagrupando Filas y Columnas
type: docs
weight: 50
url: /es/net/grouping-and-ungrouping-rows-and-columns/
---

## **Introducción**

En un archivo de Microsoft Excel, puedes crear un esquema para los datos que te permita mostrar y ocultar niveles de detalle con un solo clic de ratón.

Haz clic en los **Símbolos de Esquema**, 1,2,3, + y - para mostrar rápidamente solo las filas o columnas que proporcionen resúmenes o encabezados para secciones en una hoja de cálculo, o puedes usar los símbolos para ver detalles bajo un resumen o encabezado individual como se muestra a continuación en la figura:

|**Agrupar Filas y Columnas.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gestión de Agrupación de Filas y Columnas**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) que representa todas las celdas en la hoja de cálculo.

La colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) proporciona varios métodos para gestionar filas o columnas en una hoja de cálculo, algunos de estos se discuten a continuación con más detalle.

### **Agrupar Filas y Columnas**

Es posible agrupar filas o columnas llamando a los métodos [**GroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index) y [**GroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Ambos métodos toman los siguientes parámetros:

- Índice de la primera fila/columna, la primera fila o columna del grupo.
- Índice de la última fila/columna, la última fila o columna del grupo.
- Está oculto, un parámetro booleano que especifica si ocultar o no filas/columnas después de agrupar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **Configuración de Grupo**

Microsoft Excel te permite configurar la configuración de grupo para mostrar:

- Filas resumen debajo del detalle.
- Columnas de resumen a la derecha del detalle.

Los desarrolladores pueden configurar estas configuraciones de grupo usando la propiedad [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

### **Filas de Resumen Debajo del Detalle**

Es posible controlar si se muestran las filas de resumen debajo del detalle configurando la propiedad [**SummaryRowBelow**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow) de la clase [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline) en **true** o **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **Columnas Resumen a la Derecha del Detalle**

Los desarrolladores también pueden controlar la visualización de columnas de resumen a la derecha del detalle configurando la propiedad [**SummaryColumnRight**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright) de la clase [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline) en **true** o **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **Desagrupando Filas y Columnas**

Para desagrupar filas o columnas agrupadas, llama a los métodos [**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) y [**UngroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns) de la colección [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Ambos métodos toman dos parámetros:

- Índice de la primera fila o columna, la primera fila/columna a desagrupar.
- Índice de la última fila o columna, la última fila/columna a desagrupar.

[**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) tiene una sobrecarga que toma un tercer parámetro Booleano. Configurándolo en **true** eliminará toda la información agrupada. De lo contrario, solo se eliminará la información de grupo externa.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
