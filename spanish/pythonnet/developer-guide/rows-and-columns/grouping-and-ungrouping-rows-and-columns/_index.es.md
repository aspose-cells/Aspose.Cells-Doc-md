---
title: Agrupando y Desagrupando Filas y Columnas
type: docs
weight: 50
url: /es/python-net/grouping-and-ungrouping-rows-and-columns/
description: Este artículo muestra cómo agrupar y desagrupar filas y columnas con la API de Aspose.Cells para Python via .NET.
keywords: Python Excel Library, Cómo Agrupar Filas y Columnas en Python, Cómo Desagrupar Filas y Columnas en Python, Gestión de Agrupación de Filas y Columnas en Python, Cómo establecer Filas de Resumen Debajo del Detalle, Cómo establecer Columnas de Resumen a la Derecha del Detalle en Python.
---

## **Introducción**

En un archivo de Microsoft Excel, puedes crear un esquema para los datos que te permita mostrar y ocultar niveles de detalle con un solo clic de ratón.

Haz clic en los **Símbolos de Esquema**, 1,2,3, + y - para mostrar rápidamente solo las filas o columnas que proporcionen resúmenes o encabezados para secciones en una hoja de cálculo, o puedes usar los símbolos para ver detalles bajo un resumen o encabezado individual como se muestra a continuación en la figura:

|**Agrupar Filas y Columnas.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Gestión de Agrupación de Filas y Columnas**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) que representa todas las celdas en la hoja de cálculo.

La colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) proporciona varios métodos para gestionar filas o columnas en una hoja de cálculo, algunos de estos se discuten a continuación con más detalle.

### **Cómo Agrupar Filas y Columnas**

Es posible agrupar filas o columnas llamando a los métodos [**group_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_rows/#int-int-bool) y [**group_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_columns/#int-int-bool) de la colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Ambos métodos toman los siguientes parámetros:

- Índice de la primera fila/columna, la primera fila o columna del grupo.
- Índice de la última fila/columna, la última fila o columna del grupo.
- Está oculto, un parámetro booleano que especifica si ocultar o no filas/columnas después de agrupar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-GroupingRowsAndColumns-1.py" >}}

#### **Configuración de Grupo**

Microsoft Excel te permite configurar la configuración de grupo para mostrar:

- Filas resumen debajo del detalle.
- Columnas de resumen a la derecha del detalle.

Los desarrolladores pueden configurar estas configuraciones de grupo usando la propiedad [**outline**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/outline/) de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

### **Cómo establecer las filas de resumen debajo del detalle**

Es posible controlar si se muestran las filas de resumen debajo del detalle configurando la propiedad [**summary_row_below**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_row_below/) de la clase [**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline) en **true** o **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowBelow-1.py" >}}

### **Cómo establecer las columnas de resumen a la derecha del detalle**

Los desarrolladores también pueden controlar la visualización de columnas de resumen a la derecha del detalle configurando la propiedad [**summary_column_right**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_column_right/) de la clase [**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline) en **true** o **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowRight-1.py" >}}

## **Cómo desagrupar filas y columnas**

Para desagrupar filas o columnas agrupadas, llama a los métodos [**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/) y [**ungroup_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_columns/#int-int) de la colección [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). Ambos métodos toman dos parámetros:

- Índice de la primera fila o columna, la primera fila/columna a desagrupar.
- Índice de la última fila o columna, la última fila/columna a desagrupar.

[**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/#int-int-bool) tiene una sobrecarga que toma un tercer parámetro Booleano. Configurándolo en **true** eliminará toda la información agrupada. De lo contrario, solo se eliminará la información de grupo externa.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-UngroupingRowsAndColumns-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
