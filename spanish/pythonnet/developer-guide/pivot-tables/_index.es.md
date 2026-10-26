---
title: Insertar tabla dinámica
linktitle: Insertar tabla dinámica
description: Cree y formatee tablas dinámicas con Aspose.Cells for Python via .NET.
keywords: Crear tabla dinámica, Insertar tabla dinámica, Formatear tabla dinámica.
type: docs
weight: 160
url: /es/python-net/create-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **¿Qué es una tabla dinámica?**
Una tabla dinámica es un informe de resumen interactivo: condensa un gran bloque de datos sin procesar, organizados fila por fila, en una matriz compacta sin necesidad de usar una sola fórmula. Usted decide qué columnas se convierten en etiquetas de fila, cuáles en etiquetas de columna y cuáles se asignan al área de valores; la tabla dinámica se encarga de agrupar los datos y realizar los cálculos:
- **Resumir** — las ventas totales por producto, región o trimestre, en lugar de cadenas largas de fórmulas.
- **Comparar** — las categorías en las filas y los períodos en las columnas convierten una lista plana en un informe cruzado donde las tendencias se aprecian de un vistazo.
- **Analizar en detalle** — haga doble clic en cualquier valor de resumen para examinar las filas de origen que respaldan ese valor.
- **Actualizar** — cuando cambian los datos de origen, una actualización recalcula todo el informe.
Entre los escenarios típicos se encuentran los paneles de ventas, los desgloses de gastos y el análisis de inventario: cualquier pregunta del tipo "¿cómo se desglosan estas cifras por categoría y tiempo?". Aspose.Cells for Python via .NET crea las mismas tablas dinámicas de forma programática, de modo que los libros de trabajo que genera la aplicación pueden incluir informes listos para usar, en lugar de únicamente datos sin procesar.

### **Modelo de objetos de la tabla dinámica**
Aspose.Cells for Python via .NET proporciona un conjunto específico de clases en el namespace [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) para crear y controlar tablas dinámicas. Estas clases se utilizan para crear y configurar objetos [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/), que son los componentes fundamentales de una tabla dinámica. Los objetos son:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) representa un campo en una [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) representa una colección de todos los objetos [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) en la [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) representa una tabla dinámica en una hoja de cálculo.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) representa una colección de todos los objetos [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) en una hoja de cálculo.

### **Creación de una tabla dinámica simple con Aspose.Cells**
La creación de una tabla dinámica requiere tres pasos principales: escribir los datos de origen en las celdas de la hoja de cálculo, agregar la tabla dinámica en una posición de destino y colocar sus campos en las áreas de filas, columnas y datos.
1. Agregue datos a una hoja de cálculo mediante el método [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) del objeto [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Estos datos se utilizarán como origen de datos de la tabla dinámica.
2. Agregue una tabla dinámica a la hoja de cálculo llamando al método [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) de la colección [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection): `add(source_data, row, column)`. `source_data` es el rango de origen (por ejemplo, "A1:C8"); `row` y `column` son las coordenadas de fila y columna de la celda de destino, que se encuentra en la esquina superior izquierda de la tabla dinámica; la numeración comienza en cero (la celda E3 corresponde a la fila 2 y la columna 4). El método devuelve directamente el nuevo objeto [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
3. Coloque los campos de la tabla dinámica mediante el método `add_field_to_area` del objeto [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable): asigne el nombre de un campo al área de filas (`PivotFieldType.ROW`), al área de columnas (`PivotFieldType.COLUMN`) o al área de datos (`PivotFieldType.DATA`).
4. Guarde el libro de trabajo: la tabla dinámica se incluye en el archivo guardado.
Después de ejecutar el código de ejemplo, se agrega una tabla dinámica a la hoja de cálculo.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType

# Crear un nuevo libro de trabajo y obtener la primera hoja de cálculo
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Escribir los datos de origen: ventas por deporte y trimestre
sheet.cells.get("A1").put_value("Sport")
sheet.cells.get("B1").put_value("Quarter")
sheet.cells.get("C1").put_value("Sales")
sheet.cells.get("A2").put_value("Golf")
sheet.cells.get("B2").put_value("Qtr3")
sheet.cells.get("C2").put_value(1500)
sheet.cells.get("A3").put_value("Golf")
sheet.cells.get("B3").put_value("Qtr4")
sheet.cells.get("C3").put_value(2000)
sheet.cells.get("A4").put_value("Tennis")
sheet.cells.get("B4").put_value("Qtr3")
sheet.cells.get("C4").put_value(600)
sheet.cells.get("A5").put_value("Tennis")
sheet.cells.get("B5").put_value("Qtr4")
sheet.cells.get("C5").put_value(1500)
sheet.cells.get("A6").put_value("Tennis")
sheet.cells.get("B6").put_value("Qtr3")
sheet.cells.get("C6").put_value(4070)
sheet.cells.get("A7").put_value("Tennis")
sheet.cells.get("B7").put_value("Qtr4")
sheet.cells.get("C7").put_value(5000)
sheet.cells.get("A8").put_value("Golf")
sheet.cells.get("B8").put_value("Qtr3")
sheet.cells.get("C8").put_value(6430)

# Agregar una tabla dinámica en la celda de destino E3, utilizando A1:C8 como origen
pivot_table = sheet.pivot_tables.add("A1:C8", 2, 4)

# Asignar campos de la tabla dinámica: Sport a Filas, Quarter a Columnas y Sales a Datos
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Quarter")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")

# Guardar el libro de trabajo
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
Al asignar un rango de celdas como origen de datos, el rango debe extenderse desde la esquina superior izquierda hasta la inferior derecha. Por ejemplo, "A1:C3" es válido, pero "C3:A1" no lo es.
{{% /alert %}}

## Artículos relacionados
- [Agregar campos de filtro a una tabla dinámica en Aspose.Cells for Python via .NET](/cells/es/python-net/add-page-field-in-pivot-table/)
- [Aplicar estilos a las tablas dinámicas en Aspose.Cells for Python via .NET](/cells/es/python-net/apply-style-to-pivot-table/)
- [Modificar la disposición de los campos de página en una tabla dinámica](/cells/es/python-net/change-page-field-layout/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/python-net/filter-by-label-or-value-of-pivot-table/)
- [Administrar los campos de valor de las tablas dinámicas en Aspose.Cells for Python via .NET](/cells/es/python-net/manage-value-fields/)

{{< app/cells/assistant language="python-net" >}}