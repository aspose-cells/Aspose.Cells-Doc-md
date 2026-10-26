---
title: Tablas dinámicas
linktitle: Tablas dinámicas
description: Cree y formatee tablas dinámicas con Aspose.Cells for Python via Java.
keywords: Crear tabla dinámica, insertar tabla dinámica, formatear tabla dinámica.
type: docs
weight: 160
url: /es/python-java/create-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **¿Qué es una tabla dinámica?**
Una tabla dinámica es un informe de resumen interactivo: condensa un bloque grande de datos sin procesar, fila por fila, en una matriz compacta sin usar ni una sola fórmula. Usted decide qué columnas se convierten en etiquetas de fila, cuáles en etiquetas de columna y cuáles se agregan como valores; la tabla dinámica se encarga de la agrupación y de los cálculos:
- **Resumir** — las ventas totales por producto, región o trimestre, en lugar de cadenas largas de fórmulas.
- **Comparar** — las categorías en las filas y los períodos en las columnas convierten una lista plana en un informe cruzado donde las tendencias se aprecian de un vistazo.
- **Desglosar** — haga doble clic en cualquier valor de resumen para inspeccionar las filas de origen asociadas.
- **Actualizar** — cuando cambian los datos de origen, una actualización recalcula todo el informe.
Entre los escenarios habituales se encuentran los paneles de ventas, los desgloses de gastos y el análisis de inventario: cualquier pregunta sobre cómo se desglosan estas cifras por categoría y tiempo. Aspose.Cells for Python via Java crea las mismas tablas dinámicas de forma programática, de modo que los libros de trabajo que genera la aplicación puedan incluir informes listos para usar en lugar de contener únicamente datos sin procesar.

### **Modelo de objetos de la tabla dinámica**
Aspose.Cells proporciona un conjunto de clases que se utilizan para crear y controlar tablas dinámicas. Los componentes básicos son:
- `PivotField` representa un campo de una `PivotTable`.
- `PivotFieldCollection` representa la colección de todos los objetos `PivotField` de una `PivotTable`.
- `PivotTable` representa una tabla dinámica en una hoja de cálculo.
- `PivotTableCollection` representa la colección de todos los objetos `PivotTable` de una hoja de cálculo.

### **Creación de una tabla dinámica simple con Aspose.Cells**
La creación de una tabla dinámica consta de tres pasos principales: escribir los datos de origen en celdas de la hoja de cálculo, agregar la tabla dinámica en una posición de destino y colocar los campos de tabla dinámica en las áreas de filas, columnas y datos.
1. Agregue datos a una hoja de cálculo mediante el método `putValue` de la celda. Este conjunto de datos se utilizará como origen de datos de la tabla dinámica.
2. Agregue una tabla dinámica a la hoja de cálculo llamando al método `add` de la colección `PivotTables`: `add(sourceData, row, column)`. `sourceData` es el rango de datos de origen (por ejemplo, "A1:C8"); `row` y `column` son las coordenadas basadas en cero de la celda de destino en la esquina superior izquierda de la tabla dinámica (la celda E3 equivale a la fila 2 y la columna 4). El método devuelve directamente el nuevo objeto `PivotTable`.
3. Coloque los campos de tabla dinámica mediante el método `addFieldToArea` del objeto `PivotTable`: un nombre de campo se asigna al área de filas (`PivotFieldType.ROW`), al área de columnas (`PivotFieldType.COLUMN`) o al área de datos (`PivotFieldType.DATA`).
4. Guarde el libro de trabajo: la tabla dinámica se escribe en el archivo guardado.
Tras ejecutar el código de ejemplo, se agrega una tabla dinámica a la hoja de cálculo.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

# Crear un nuevo libro de trabajo y obtener la primera hoja de cálculo
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Escribir los datos de origen: ventas por deporte y trimestre
cells.get("A1").putValue("Sport")
cells.get("B1").putValue("Quarter")
cells.get("C1").putValue("Sales")
cells.get("A2").putValue("Golf")
cells.get("B2").putValue("Qtr3")
cells.get("C2").putValue(1500)
cells.get("A3").putValue("Golf")
cells.get("B3").putValue("Qtr4")
cells.get("C3").putValue(2000)
cells.get("A4").putValue("Tennis")
cells.get("B4").putValue("Qtr3")
cells.get("C4").putValue(600)
cells.get("A5").putValue("Tennis")
cells.get("B5").putValue("Qtr4")
cells.get("C5").putValue(1500)
cells.get("A6").putValue("Tennis")
cells.get("B6").putValue("Qtr3")
cells.get("C6").putValue(4070)
cells.get("A7").putValue("Tennis")
cells.get("B7").putValue("Qtr4")
cells.get("C7").putValue(5000)
cells.get("A8").putValue("Golf")
cells.get("B8").putValue("Qtr3")
cells.get("C8").putValue(6430)

# Agregar una tabla dinámica en la celda de destino E3, usando A1:C8 como origen
pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4)

# Asignar los campos de la tabla dinámica: Sport a Filas, Quarter a Columnas y Sales a Datos
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales")

# Guardar el libro de trabajo
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
Al asignar un rango de celdas como origen de datos, el rango debe extenderse desde la esquina superior izquierda hasta la inferior derecha. Por ejemplo, "A1:C3" es válido, pero "C3:A1" no lo es.
{{% /alert %}}

## Artículos relacionados
- [Agregar campos de filtro a una tabla dinámica en Aspose.Cells for Python via Java](/cells/es/python-java/add-page-field-in-pivot-table/)
- [Aplicar estilos a tablas dinámicas en Aspose.Cells for Python via Java](/cells/es/python-java/apply-style-to-pivot-table/)
- [Modificar el diseño de campos de página en una tabla dinámica](/cells/es/python-java/change-page-field-layout/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/python-java/filter-by-label-or-value-of-pivot-table/)
- [Administrar campos de valores de una tabla dinámica en Aspose.Cells for Python via Java](/cells/es/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}