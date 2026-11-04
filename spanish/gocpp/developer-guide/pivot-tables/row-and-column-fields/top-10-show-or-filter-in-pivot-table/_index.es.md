---
title: Mostrar o filtrar los 10 principales en una tabla dinámica
linktitle: Mostrar o filtrar los 10 principales en una tabla dinámica
description: Aprenda a mostrar únicamente los elementos con mayor o menor clasificación de un campo de una tabla dinámica en Aspose.Cells for Go via C++. Este artículo cubre la configuración de AutoShow en Excel 97-2003 (SetIsAutoShow y métodos relacionados), la recuperación de las opciones y el filtro de los 10 principales de Excel 2007-365 mediante FilterTop10.
keywords: Aspose.Cells, Go via C++, tabla dinámica, 10 principales, mostrar automáticamente, SetIsAutoShow, SetIsAscendShow, SetAutoShowCount, SetAutoShowField, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /es/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
Una tabla dinámica que enumera todos los elementos de un campo de fila puede ser difícil de leer cuando el campo tiene decenas de miembros. Un informe de los 10 principales conserva únicamente los elementos con mayor o menor clasificación, que es exactamente lo que necesitan los informes de clasificación: «5 productos principales por ingresos» o «3 regiones inferiores por número de ventas». Aspose.Cells admite dos mecanismos para esta tarea, y cada uno corresponde a una generación diferente de Microsoft Excel.
- **AutoShow de Excel 97-2003** — los cuatro métodos de configuración de `PivotField`: `SetIsAutoShow`, `SetIsAscendShow`, `SetAutoShowCount` y `SetAutoShowField`. Esta es la opción clásica «Mostrar los N elementos superiores/inferiores», almacenada directamente en el campo de la tabla dinámica. Funciona en todas las versiones de Excel, tanto antiguas como modernas, porque forma parte del formato original de las tablas dinámicas.
- **Filtro de los 10 principales de Excel 2007-365** — el método `PivotField.FilterTop10()`. Este es el filtro moderno de los 10 principales, disponible en el menú del campo, en Filtros de valores. Se almacena como un objeto `PivotFilter` asociado al campo y ofrece una clasificación según el número de elementos o según porcentajes.

## **Mostrar los 10 principales en Excel 97-2003 (AutoShow)**
El AutoShow clásico se configura mediante cuatro llamadas a los métodos de configuración de `PivotField`:
- `SetIsAutoShow(bool)` — habilita o deshabilita la opción AutoShow en el campo.
- `SetIsAscendShow(bool)` — `false` conserva los elementos con mayor clasificación (Superior), mientras que `true` conserva los de menor clasificación (Inferior).
- `SetAutoShowCount(int32)` — el número de elementos que se conservarán; por ejemplo, 10 para un informe clásico de los 10 principales.
- `SetAutoShowField(int32)` — el índice basado en cero del **campo de datos** cuyos valores se utilizan para clasificar los elementos. Pase -1 para clasificar los elementos según el propio campo.
La clasificación puede determinarse mediante un campo de valores o mediante el propio campo. A continuación se muestran dos variantes habituales.

### **Clasificar por un campo de valores**
Clasifique los elementos del campo de fila según un campo de valores común, como Suma de ventas. El siguiente ejemplo crea una tabla dinámica con un campo de fila (`Sport`) y un campo de datos (`Sales`), y a continuación muestra los 2 deportes con mayores ventas. `rankBy` es 0 porque «Suma de ventas» es el campo de datos con el índice 0.

```go
package main
import (
	"strconv"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String("Qtr" + strconv.Itoa(int(quarter)))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Mostrar los 2 elementos principales clasificados por "Sum of Sales" (índice del campo de datos 0)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(false)
	sportField.SetAutoShowCount(int32(2))
	sportField.SetAutoShowField(int32(0))
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **Clasificar por el propio campo**
También se puede clasificar un campo por sí mismo: pase -1 a `SetAutoShowField`. Esta variante no necesita ningún campo de datos adicional; el campo solo debe encontrarse en el área de filas o columnas. El siguiente ejemplo muestra los 3 deportes con menor clasificación según el propio campo. Al guardar esta configuración, el atributo `rankBy` se omite del XML de la tabla dinámica porque -1 es el valor predeterminado del formato, y `GetAutoShowField()` devuelve -1.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String(fmt.Sprintf("Qtr%d", quarter))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Mostrar los 3 elementos inferiores clasificados por el propio campo (rankBy = -1)
	sportField.SetIsAutoShow(true)
	sportField.SetIsAscendShow(true)
	sportField.SetAutoShowCount(3)
	sportField.SetAutoShowField(-1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **Leer las opciones actuales de AutoShow**
Los métodos de lectura `IsAutoShow()`, `IsAscendShow()`, `GetAutoShowCount()` y `GetAutoShowField()` exponen las opciones de AutoShow almacenadas actualmente en el campo. Utilícelos para inspeccionar cómo se mostrarán los elementos de una tabla dinámica, ya se encuentre en un libro de trabajo existente o en una que acaba de configurar. También se aplican a los libros de trabajo cargados desde un archivo.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook_String("output-top10-by-value-field.xlsx")
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Get_Int(0)
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	isAutoShow, _ := sportField.IsAutoShow()
	isAscendShow, _ := sportField.IsAscendShow()
	autoShowCount, _ := sportField.GetAutoShowCount()
	autoShowField, _ := sportField.GetAutoShowField()
	direction := "Bottom"
	if !isAscendShow {
		direction = "Top"
	}
	fmt.Println("AutoShow enabled:", isAutoShow)
	fmt.Println("Direction:", direction)
	fmt.Println("Item count:", autoShowCount)
	fmt.Println("Ranking data field index:", autoShowField)
}
```

Las cuatro propiedades se corresponden con los atributos clásicos de AutoShow que se escriben en el XML de la tabla dinámica (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), por lo que los valores recuperados son los que tienen en cuenta todas las versiones de Excel.

## **Nota**

{{% alert color="primary" %}}
- Después de cambiar cualquier opción de AutoShow mediante un método de configuración, vuelva a llamar a `PivotTable.CalculateData()`; la configuración solo surte efecto en la disposición visual tras el siguiente recálculo.
- Las opciones de AutoShow se aplican a los campos de fila y columna. Un campo que se encuentre únicamente en el área de página (filtro) no se puede clasificar de esta forma porque sus elementos no están distribuidos en el cuerpo de la tabla dinámica.
{{% /alert %}}

## **Excel 2007-365: filtro de los 10 principales (FilterTop10)**
Las versiones modernas de Excel presentan la opción de los 10 principales como filtro de valores en el menú del campo (Filtros de valores, 10 principales...). Aspose.Cells representa esta opción mediante el método `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`, que devuelve el `PivotFilter` creado:
- `valueFieldIndex` — el índice basado en cero del campo de datos cuyos valores agregados se utilizan para clasificar los elementos.
- `type` — el significado de `itemCount`. `PivotFilterType.Count` conserva un número fijo de elementos (la opción Elementos del cuadro de diálogo). `PivotFilterType.Percent` conserva un porcentaje de los elementos; por tanto, `itemCount` es el propio porcentaje: un valor de 30 conserva el 30 % de los elementos superiores. `PivotFilterType.Sum` establece la clasificación según la cobertura acumulada de los valores.
- `isTop` — `true` para Superior, `false` para Inferior.
- `itemCount` — el valor N en «N principales»; su unidad depende de `type`.

```go
package main
import (
	"fmt"
	. "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)
func main() {
	workbook, _ := NewWorkbook()
	wss, _ := workbook.GetWorksheets()
	worksheet, _ := wss.Get_Int(0)
	cells, _ := worksheet.GetCells()
	cell, _ := cells.Get_String("A1")
	cell.PutValue_String("Sport")
	cell, _ = cells.Get_String("B1")
	cell.PutValue_String("Quarter")
	cell, _ = cells.Get_String("C1")
	cell.PutValue_String("Sales")
	sports := []string{"Golf", "Tennis", "Rugby", "Cricket", "Boxing"}
	row := int32(2)
	for _, sport := range sports {
		for quarter := int32(1); quarter <= 3; quarter++ {
			cell, _ = cells.Get_Int_Int(row, 0)
			cell.PutValue_String(sport)
			cell, _ = cells.Get_Int_Int(row, 1)
			cell.PutValue_String(fmt.Sprintf("Qtr%d", quarter))
			cell, _ = cells.Get_Int_Int(row, 2)
			cell.PutValue_Int(1000 + 777*row)
			row++
		}
	}
	pivotTables, _ := worksheet.GetPivotTables()
	pivotTable, _ := pivotTables.Add_String_Int_Int("A1:C16", 2, 5)
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Row, "Sport")
	pivotTable.AddFieldToArea_PivotFieldType_String(PivotFieldType_Data, "Sales")
	pivotTable.CalculateData()
	rowFields, _ := pivotTable.GetRowFields()
	sportField, _ := rowFields.Get_Int(0)
	// Filtro Top 10: conservar los 2 elementos principales según "Suma de ventas" (índice 0 del campo de datos)
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// Para un filtro basado en porcentaje, conservar el 30 % superior de los elementos:
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
Las opciones de AutoShow y `FilterTop10` son dos funciones distintas. AutoShow escribe el atributo clásico `autoShow` en el campo de la tabla dinámica y se tiene en cuenta en todas las versiones de Excel, desde Excel 97. `FilterTop10` escribe una entrada moderna de tipo `PivotFilter`, que requiere Excel 2007 o una versión posterior. Al abrir un libro de trabajo en una versión anterior de Excel, una tabla dinámica que utiliza el filtro moderno vuelve a mostrar todos los elementos. Para los documentos que deben procesarse mediante herramientas heredadas sin pérdida de información, se recomienda utilizar los métodos de configuración de AutoShow; para los libros de trabajo modernos, se recomienda utilizar `FilterTop10` porque se integra con los demás filtros de valores.
{{% /alert %}}

## **Artículos relacionados**
- [Agrupar campos de la tabla dinámica](/cells/es/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}