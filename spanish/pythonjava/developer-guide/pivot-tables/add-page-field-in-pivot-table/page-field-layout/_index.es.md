---
title: Modificar el diseño del campo de página en la tabla dinámica
linktitle: Modificar el diseño del campo de página en la tabla dinámica
description: Aprenda a controlar el diseño del área de campos de página en una tabla dinámica con Aspose.Cells for Python via Java, incluida la configuración del orden de visualización, el recuento de ajuste y el orden de los campos de página en la parte superior de la tabla dinámica.
keywords: Aspose.Cells for Python via Java, biblioteca Python Java, hoja de cálculo, tabla dinámica, campo de página, orden de los campos de página, recuento de ajuste del campo de página, mover campo de página
type: docs
weight: 191
url: /es/python-java/change-page-field-layout/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Este artículo es una continuación del tema **Agregar campo de página en la tabla dinámica**. Demuestra cómo controlar el diseño del área de campos de página — la franja de controles de filtro en la parte superior de una tabla dinámica — incluido el orden de visualización, el recuento de ajuste y la reordenación de campos.
{{% /alert %}}
## **Introducción**
Una tabla dinámica en Microsoft Excel expone un **área de campos de página** dedicada que se sitúa encima del cuerpo de filas/columnas/datos de la tabla. Esta área se representa como una franja de controles de filtro desplegables (uno por cada campo de página) y es donde los usuarios finales hacen clic para segmentar la tabla dinámica según criterios como el año o la región. Aspose.Cells for Python via Java modela esta área mediante la colección `pivot_table.page_fields` y expone tres propiedades que controlan cómo se dispone visualmente la franja:
- `pivot_table.page_field_order` (un valor de `Aspose.Cells.PrintOrderType`) decide si los campos de página adicionales se colocan *junto a* los existentes o *debajo* de ellos.
- `pivot_table.page_field_wrap_count` establece cuántos campos de página se colocan por fila o columna antes de ajustar.
- `pivot_table.page_fields.move(curr_index, dest_index)` reordena los campos de página sin cambiar el modo de orden.
Este artículo recorre tres ejemplos de código que demuestran cada una de estas operaciones sobre un conjunto de datos compartido, para que pueda comparar los diseños resultantes uno junto al otro.
## **Datos de origen**
Los tres ejemplos siguientes cargan estas ocho filas de datos de ventas en una hoja de cálculo llamada `PivotData`. Los datos contienen dos candidatos a campo de página (`Year`, `Region`), un candidato a campo de fila (`Fruit`) y una medida (`Amount`), lo que hace que la franja de campos de página sea significativa para inspeccionar.
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Las ocho filas se rellenan en cada ejemplo de código, en orden idéntico, por lo que los datos de origen nunca difieren entre escenarios; solo lo hacen las propiedades de diseño del campo de página.
## **Ejemplo 1: Over Then Down**
En el primer escenario configuramos los dos campos de página (`Year`, `Region`) para que aparezcan **uno al lado del otro en una sola fila** en la parte superior de la tabla dinámica. Asignamos `Fruit` al eje de filas, ubicamos `Year` primero y `Region` segundo en el eje de página (el orden de las llamadas a `add_field_to_area` determina el índice inicial), añadimos `Amount` (Suma) como campo de datos y luego establecemos `page_field_order` en `PrintOrderType.OVER_THEN_DOWN` con `page_field_wrap_count = 2`. Con `OVER_THEN_DOWN` y un recuento de ajuste de 2, los dos campos de página se disponen horizontalmente uno al lado del otro en una sola fila en la parte superior de la tabla dinámica, por lo que la franja ocupa una fila con ancho dos.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorksheetCollection, Worksheet, Cells, PivotTableCollection, PivotTable, PivotFieldType, ConsolidationFunction, PrintOrderType

dataDir = "output"
if not os.path.exists(dataDir):
    os.makedirs(dataDir, exist_ok=True)

workbook = Workbook()
worksheets = workbook.getWorksheets()

pivotDataIdx = worksheets.add("PivotData")
pivotDataSheet = worksheets.get(pivotDataIdx)
pivotDataCells = pivotDataSheet.getCells()

# Encabezados (fila 0)
pivotDataCells.get(0, 0).putValue("Fruit")
pivotDataCells.get(0, 1).putValue("Year")
pivotDataCells.get(0, 2).putValue("Region")
pivotDataCells.get(0, 3).putValue("Amount")

# Fila 1: Manzana, 2022, Norte, 150
pivotDataCells.get(1, 0).putValue("Apple")
pivotDataCells.get(1, 1).putValue(2022)
pivotDataCells.get(1, 2).putValue("North")
pivotDataCells.get(1, 3).putValue(150)

# Fila 2: Manzana, 2023, Norte, 180
pivotDataCells.get(2, 0).putValue("Apple")
pivotDataCells.get(2, 1).putValue(2023)
pivotDataCells.get(2, 2).putValue("North")
pivotDataCells.get(2, 3).putValue(180)

# Fila 3: Plátano, 2022, Sur, 120
pivotDataCells.get(3, 0).putValue("Banana")
pivotDataCells.get(3, 1).putValue(2022)
pivotDataCells.get(3, 2).putValue("South")
pivotDataCells.get(3, 3).putValue(120)

# Fila 4: Plátano, 2023, Sur, 140
pivotDataCells.get(4, 0).putValue("Banana")
pivotDataCells.get(4, 1).putValue(2023)
pivotDataCells.get(4, 2).putValue("South")
pivotDataCells.get(4, 3).putValue(140)

# Fila 5: Cereza, 2022, Este, 200
pivotDataCells.get(5, 0).putValue("Cherry")
pivotDataCells.get(5, 1).putValue(2022)
pivotDataCells.get(5, 2).putValue("East")
pivotDataCells.get(5, 3).putValue(200)

# Fila 6: Cereza, 2023, Este, 220
pivotDataCells.get(6, 0).putValue("Cherry")
pivotDataCells.get(6, 1).putValue(2023)
pivotDataCells.get(6, 2).putValue("East")
pivotDataCells.get(6, 3).putValue(220)

# Fila 7: Uva, 2022, Oeste, 90
pivotDataCells.get(7, 0).putValue("Grape")
pivotDataCells.get(7, 1).putValue(2022)
pivotDataCells.get(7, 2).putValue("West")
pivotDataCells.get(7, 3).putValue(90)

# Fila 8: Uva, 2023, Oeste, 110
pivotDataCells.get(8, 0).putValue("Grape")
pivotDataCells.get(8, 1).putValue(2023)
pivotDataCells.get(8, 2).putValue("West")
pivotDataCells.get(8, 3).putValue(110)

# Agregar hoja PivotTableReport
pivotTableSheetIdx = worksheets.add("PivotTableReport")
pivotTableSheet = worksheets.get(pivotTableSheetIdx)
pivotTables = pivotTableSheet.getPivotTables()

# Crear tabla dinámica con origen en PivotData!A1:D9 ubicada en A1 en PivotTableReport
pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# Agregar campos
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)   # Fruta
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)  # Año
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)  # Región
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)  # Cantidad
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM)

# Configurar el diseño del área de campos de página: colocar los campos de página primero en horizontal, ajustar después de cada 2
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

# Refrescar y calcular
pivotTable.calculateData()

# Guardar
workbook.save(os.path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"))

jpype.shutdownJVM()
```
## **Ejemplo 2: Down Then Over**
En este ejemplo ubicamos `Fruit` en el eje de filas, `Year` y `Region` en el eje de página (con `Year` primero) y `Amount` (Suma) como campo de datos, exactamente como en el Ejemplo 1. Luego establecemos `page_field_order` en `PrintOrderType.DOWN_THEN_OVER` y `page_field_wrap_count` en `2`. Con `DOWN_THEN_OVER` y un recuento de ajuste de 2, los dos campos de página se apilan verticalmente: `Year` arriba, `Region` directamente debajo, formando una sola columna en la parte superior de la tabla dinámica. Por lo tanto, la franja ocupa dos filas de ancho uno, en contraste con el Ejemplo 1.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PrintOrderType

workbook = Workbook()
pivotData = workbook.getWorksheets().get(0)
pivotData.setName("PivotData")
pivotReportIdx = workbook.getWorksheets().add("PivotTableReport")
pivotReport = workbook.getWorksheets().get(pivotReportIdx)

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivotData.getCells().get(0, c).putValue(headers[c])

data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        pivotData.getCells().get(r + 1, c).putValue(data[r][c])

idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable")
pivotTable = pivotReport.getPivotTables().get(idx)

pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)

pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)
pivotTable.setPageFieldWrapCount(2)

pivotTable.calculateData()

workbook.save("pageFieldLayout_downThenOver.xlsx")

jpype.shutdownJVM()
```
## **Ejemplo 3: Mover un campo de página**
En el tercer escenario mantenemos este conjunto de datos y la asignación de campos, establecemos un diseño neutral (`OVER_THEN_DOWN` con recuento de ajuste `2`) y luego demostramos la operación `page_fields.move`. La llamada `move(0, 1)` mueve el campo de página en el índice 0 (`Year`) a la posición 1, y el campo de página que estaba en la posición 1 (`Region`) se desplaza a la posición 0. Tras esta llamada, `Region` es el primer campo de página y `Year` es el segundo. El modo de ajuste y de orden no se modifican, por lo que la franja aún se representa horizontalmente una al lado de la otra; solo se ha intercambiado el orden de los dos desplegables.
```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PrintOrderType

workbook = Workbook()

dataSheet = workbook.getWorksheets().get(0)
dataSheet.setName("PivotData")

dataSheet.getCells().get("A1").putValue("Fruit")
dataSheet.getCells().get("B1").putValue("Year")
dataSheet.getCells().get("C1").putValue("Region")
dataSheet.getCells().get("D1").putValue("Amount")

dataSheet.getCells().get("A2").putValue("Apple")
dataSheet.getCells().get("B2").putValue(2022)
dataSheet.getCells().get("C2").putValue("North")
dataSheet.getCells().get("D2").putValue(150)

dataSheet.getCells().get("A3").putValue("Apple")
dataSheet.getCells().get("B3").putValue(2023)
dataSheet.getCells().get("C3").putValue("North")
dataSheet.getCells().get("D3").putValue(180)

dataSheet.getCells().get("A4").putValue("Banana")
dataSheet.getCells().get("B4").putValue(2022)
dataSheet.getCells().get("C4").putValue("South")
dataSheet.getCells().get("D4").putValue(120)

dataSheet.getCells().get("A5").putValue("Banana")
dataSheet.getCells().get("B5").putValue(2023)
dataSheet.getCells().get("C5").putValue("South")
dataSheet.getCells().get("D5").putValue(140)

dataSheet.getCells().get("A6").putValue("Cherry")
dataSheet.getCells().get("B6").putValue(2022)
dataSheet.getCells().get("C6").putValue("East")
dataSheet.getCells().get("D6").putValue(200)

dataSheet.getCells().get("A7").putValue("Cherry")
dataSheet.getCells().get("B7").putValue(2023)
dataSheet.getCells().get("C7").putValue("East")
dataSheet.getCells().get("D7").putValue(220)

dataSheet.getCells().get("A8").putValue("Grape")
dataSheet.getCells().get("B8").putValue(2022)
dataSheet.getCells().get("C8").putValue("West")
dataSheet.getCells().get("D8").putValue(90)

dataSheet.getCells().get("A9").putValue("Grape")
dataSheet.getCells().get("B9").putValue(2023)
dataSheet.getCells().get("C9").putValue("West")
dataSheet.getCells().get("D9").putValue(110)

pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport")
pivotSheet = workbook.getWorksheets().get(pivotSheetIdx)

pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable")
pivotTable = pivotSheet.getPivotTables().get(pivotIdx)

pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)

pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

pivotTable.getPageFields().move(0, 1)

pivotTable.calculateData()

workbook.save("pageFieldLayout_move.xlsx")

jpype.shutdownJVM()
```
## **Artículos relacionados**
- [Agregar campo de página en la tabla dinámica](/cells/es/python-java/add-page-field-in-pivot-table/) — la página principal que introduce cómo se agregan los campos de página a una tabla dinámica.
- [Campos de fila y columna en la tabla dinámica](/cells/es/python-java/row-and-column-fields/) — trata la asignación de campos a los ejes de fila y columna, complementando el trabajo del eje de página mostrado aquí.
- [Administrar campos de valor en la tabla dinámica](/cells/es/python-java/manage-value-fields/) — describe cómo configurar el área de datos (valores), incluida la agregación `SUM` utilizada en este artículo.
- [Actualizar la tabla dinámica](/cells/es/python-java/refresh-pivot-table/) — explica `refresh_data` y `calculate_data`, que son necesarios después de reordenar los campos de página.
- [Aplicar estilo a la tabla dinámica](/cells/es/python-java/apply-style-to-pivot-table/) — muestra cómo dar formato a la tabla dinámica representada después de haber dispuesto la franja de campos de página.
{{< app/cells/assistant language="python" >}}