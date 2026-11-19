---
title: Agrupar campos pivote en la tabla dinámica con Golang mediante C++
linktitle: Agrupar campos pivote en la tabla dinámica con Golang mediante C++
description: Aprenda a agrupar campos pivote de filas y columnas de una tabla dinámica en períodos de fecha, como meses y trimestres, y en rangos numéricos mediante PivotField.Group y PivotFieldGroupOptions en Aspose.Cells for Go via C++.
keywords: Aspose.Cells, Aspose.Cells for Go via C++, tabla dinámica, campo pivote, agrupar campos pivote, Group, Group_PivotFieldGroupOptions, PivotFieldGroupOptions, agrupación de fechas, rango numérico, Go
type: docs
weight: 80
url: /es/go-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
- Agrupar campos pivote resulta útil cuando un campo de fila o de columna de una tabla dinámica contiene muchos elementos distintos, como un campo de fecha con cientos de fechas o un campo numérico con muchos valores dispersos. La agrupación condensa estos elementos en secciones significativas: las fechas, en meses, trimestres y años, y los números, en rangos como 0-1, 2-3 y 4-5. Así, una tabla dinámica grande se vuelve más compacta y fácil de analizar. Aspose.Cells ofrece esta capacidad mediante el método `PivotField.Group()` (agrupación automática por tipo de datos) y `PivotField.Group(PivotFieldGroupOptions)` (opciones de agrupación personalizada).
- La agrupación por fechas convierte las fechas individuales en períodos más amplios, como días, meses, trimestres y años, y construye una jerarquía temporal (por ejemplo, Años, Trimestres y Meses). Las tendencias a lo largo del tiempo se hacen visibles de un vistazo y cada nivel de período se convierte en su propio campo pivote en el área de filas o de columnas de la tabla dinámica.
- La agrupación solo está disponible para campos colocados en el área ROW o COLUMN de una tabla dinámica. Un campo de datos (valor) no se puede agrupar directamente. Para agrupar dicho campo, primero debe agregarse al área de filas o de columnas de la tabla dinámica.

## **Agrupar campos pivote automáticamente**
La sobrecarga `PivotField.Group()` sin parámetros examina el tipo de datos del campo y lo agrupa automáticamente. Un campo que contiene solo fechas (y valores en blanco) se agrupa por meses. Un campo que contiene solo números (y valores en blanco) se agrupa en rangos numéricos mediante un intervalo automático.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// Group the first row field automatically by its data type
	rowFields, _ := pivotTable.GetRowFields()
	field, _ := rowFields.Get_Int(0)
	field.Group()
	pivotTable.CalculateData()
	workbook.Save_String("outputAutoGroupPivotField.xlsx")
}
```

## **Agrupar campos pivote con opciones personalizadas**
La clase `PivotFieldGroupOptions` ofrece una configuración de agrupación personalizada. Para los campos de fecha, establezca `StartDate`, `EndDate` y `GroupTypes` (las fechas se pasan como valores `time.Time` de Go). Para los campos numéricos, establezca `StartNumber`, `EndNumber` y `Interval`. El comportamiento `newPivotField` controla si la agrupación crea nuevos campos pivote junto al original (consulte la sección Nota al final de este artículo).

### **Agrupar un campo de fecha por meses y trimestres**
El siguiente ejemplo agrupa por meses y trimestres el campo de fecha del área de filas de la tabla dinámica de ejemplo, entre una fecha de inicio y una de fin. El código carga el [archivo Excel de ejemplo](sampleGroupPivotFieldsInPivotTable.xlsx), realiza la agrupación, calcula los datos de la tabla dinámica y guarda el resultado agrupado. La captura de pantalla muestra el efecto: el campo de fecha del área de filas ahora está agrupado por trimestres y meses.
Tenga en cuenta que se ignora el orden de los valores de `GroupTypes`. Independientemente del orden en que se indiquen los tipos de agrupación, los campos agrupados siempre se muestran desde el período más amplio hasta el más pequeño: años, trimestres, meses, días, horas, minutos y segundos. En este ejemplo, los meses se indican antes que los trimestres en `GroupTypes`; sin embargo, los trimestres se muestran como el nivel exterior y los meses como el nivel interior.

```go
package main
import (
	"time"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// Group the date row field by months and quarters between the given dates
	options, _ := NewPivotFieldGroupOptions()
	options.SetStartDate(time.Date(2008, 1, 1, 0, 0, 0, 0, time.UTC))
	options.SetEndDate(time.Date(2008, 9, 5, 0, 0, 0, 0, time.UTC))
	options.SetGroupTypes([]PivotGroupByType{PivotGroupByType_Months, PivotGroupByType_Quarters})
	rowFields, _ := pivotTable.GetRowFields()
	dateField, _ := rowFields.Get_Int(0)
	dateField.Group_PivotFieldGroupOptions(options)
	pivotTable.CalculateData()
	workbook.Save_String("outputGroupPivotFieldsInPivotTable.xlsx")
}
```

![Tabla dinámica agrupada por meses y trimestres](group-pivot-fields-in-the-pivot-table_1.png)

### **Agrupar un campo numérico en rangos**
`FieldTwo` de la tabla dinámica de ejemplo es inicialmente un campo de datos (valor). Como solo los campos de fila o columna se pueden agrupar, el código primero llama a `PivotTable.AddFieldToArea(PivotFieldType_Row, "FieldTwo")` para mover `FieldTwo` al área de filas, actualiza la tabla dinámica y, a continuación, agrupa el campo numérico en los rangos 0-1, 2-3 y 4-5 mediante `StartNumber = 0`, `EndNumber = 5` e `Interval = 2`.

```go
package main
import (
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	// Load the sample workbook containing the pivot table
	workbook, _ := NewWorkbook_String("sampleGroupPivotFieldsInPivotTable.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(1)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	// FieldTwo is a data field: move it to the row area first,
	// because only row/column fields can be grouped
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "FieldTwo")
	pivotTable.CalculateData()
	// Group the numeric field into the ranges 0-1, 2-3, 4-5
	options, _ := NewPivotFieldGroupOptions()
	options.SetStartNumber(0)
	options.SetEndNumber(5)
	options.SetInterval(2)
	rowFields, _ := pivotTable.GetRowFields()
	numericField, _ := rowFields.Get_Int(1)
	numericField.Group_PivotFieldGroupOptions(options)
	pivotTable.CalculateData()
	workbook.Save_String("outputNumberGroupPivotField.xlsx")
}
```

## **Nota**

{{% alert color="primary" %}}
- Las sobrecargas del método `PivotField.GroupBy()` están obsoletas y se han eliminado de la superficie de la API. `PivotField.Group()` y `PivotField.Group(PivotFieldGroupOptions)` son sus sustitutos.
- En Microsoft Excel, agrupar un campo numérico REEMPLAZA el campo pivote original por los rangos agrupados, mientras que agrupar un campo de fecha crea NUEVOS campos pivote (uno por nivel de agrupación, por ejemplo, Trimestres y Meses) junto al campo original. A partir de Aspose.Cells 26.10, los métodos `PivotField.Group()` siguen el mismo comportamiento que Excel.
- La propiedad `PivotFieldGroupOptions.Interval` solo surte efecto en la agrupación numérica y en la agrupación de fechas por días (por ejemplo, al agrupar fechas en períodos de 7 días); se ignora cuando las fechas se agrupan por meses, trimestres o años.
{{% /alert %}}

## **Artículos relacionados**
- [Mostrar o filtrar los 10 principales en la tabla dinámica](/cells/es/go-cpp/top-10-show-or-filter-in-pivot-table/)
- [Mostrar valores como en la tabla dinámica](/cells/es/go-cpp/show-values-as-in-pivot-table/)
- [Formatear parte de la tabla dinámica](/cells/es/go-cpp/format-part-of-pivot-table/)
- [Agregar formato condicional a la tabla dinámica](/cells/es/go-cpp/add-conditional-formatting-to-pivot-table/)

{{< app/cells/assistant language="go" >}}