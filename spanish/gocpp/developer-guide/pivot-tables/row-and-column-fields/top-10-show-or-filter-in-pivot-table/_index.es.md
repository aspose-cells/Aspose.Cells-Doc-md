---
title: Mostrar o filtrar los 10 principales en una tabla dinámica
linktitle: Mostrar o filtrar los 10 principales en una tabla dinámica
description: Aprenda a mostrar únicamente los elementos mejor o peor clasificados de un campo de una tabla dinámica en Aspose.Cells for Go via C++. Este artículo explica el método Top10AutoShow de Excel 97-2003, cómo recuperar las opciones con Top10AutoShowSettings y el filtro de los 10 principales de Excel 2007-365 mediante FilterTop10.
keywords: Aspose.Cells, Go via C++, tabla dinámica, 10 principales, mostrar automáticamente, Top10AutoShow, GetTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Go
type: docs
weight: 20
url: /es/go-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
Una tabla dinámica que enumera todos los elementos de un campo de fila puede ser difícil de leer cuando el campo tiene decenas de elementos. Un informe de los 10 principales conserva únicamente los elementos mejor o peor clasificados, que es exactamente lo que necesitan los informes de clasificación: «los 5 productos con mayores ingresos» o «las 3 regiones con menor número de ventas». Aspose.Cells admite dos mecanismos para ello, que corresponden a dos generaciones de Microsoft Excel.
- **AutoShow de Excel 97-2003** — el método `PivotField.Top10AutoShow()`. Esta es la opción clásica «Mostrar los N elementos superiores/inferiores», almacenada directamente en el campo de la tabla dinámica. Funciona en todas las versiones de Excel, tanto antiguas como modernas, porque forma parte del formato original de la tabla dinámica.
- **Filtro de los 10 principales de Excel 2007-365** — el método `PivotField.FilterTop10()`. Este es el filtro moderno de los 10 principales que se encuentra en «Filtros de valores», dentro del menú del campo. Se almacena como un objeto `PivotFilter` asociado al campo y permite clasificar por número de elementos o por porcentaje.

## **Mostrar los 10 principales en Excel 97-2003 (Top10AutoShow)**
La opción clásica de AutoShow se configura con una sola llamada a `PivotField.Top10AutoShow(isAutoShow bool, isTop bool, count int32, rankBy int32)`:
- `isAutoShow` — habilita o deshabilita la opción AutoShow en el campo.
- `isTop` — `true` conserva los elementos con la clasificación más alta (Superiores), mientras que `false` conserva los de clasificación más baja (Inferiores).
- `count` — número de elementos que conservar, por ejemplo, 10 para un informe clásico de los 10 principales.
- `rankBy` — índice de base cero del **campo de datos** cuyos valores determinan la clasificación de los elementos. Pase -1 para clasificar los elementos en función del propio campo.

La clasificación puede basarse en un campo de valores o en el propio campo. A continuación se muestran dos variantes habituales.

### **Clasificar por un campo de valores**
Ordene los elementos del campo de fila por un campo de valores estándar, como Suma de Ventas. El siguiente ejemplo crea una tabla dinámica con un campo de fila (`Sport`) y un campo de datos (`Sales`), y a continuación muestra los 2 deportes con mayores ventas. `rankBy` es 0 porque «Suma de Ventas» es el campo de datos que ocupa el índice 0.

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
	// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
	sportField.Top10AutoShow(true, true, 2, 0)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-value-field.xlsx")
}
```

### **Clasificar por el propio campo**
También se puede clasificar un campo por sí mismo: pase el valor -1 a `rankBy`. Esta variante no necesita ningún campo de datos adicional; basta con que el campo esté en el área de filas (o columnas). El siguiente ejemplo muestra los 3 deportes con la clasificación más baja, usando el propio campo para la clasificación. Al guardar esta configuración, el atributo `rankBy` se omite del XML de la tabla dinámica porque -1 es el valor predeterminado del formato, y `GetRankBy()` recupera el valor -1.

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
	// Show the bottom 3 items ranked by the field itself (rankBy = -1)
	sportField.Top10AutoShow(true, false, 3, -1)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-by-field-itself.xlsx")
}
```

## **Leer las opciones actuales de AutoShow**
El método `PivotField.GetTop10AutoShowSettings()` devuelve un objeto `PivotFieldTop10AutoShowSettings` que expone las opciones de AutoShow almacenadas actualmente en el campo. Utilícelo para comprobar cómo se mostrarán los elementos de una tabla dinámica, ya sea en un libro de trabajo existente o en una tabla dinámica que acaba de configurar. El método también se aplica a los libros de trabajo cargados desde un archivo.

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
	settings, _ := sportField.GetTop10AutoShowSettings()
	isAutoShow, _ := settings.IsAutoShow()
	isTop, _ := settings.IsTop()
	autoShowCount, _ := settings.GetAutoShowCount()
	rankBy, _ := settings.GetRankBy()
	direction := "Bottom"
	if isTop {
		direction = "Top"
	}
	fmt.Println("AutoShow enabled:", isAutoShow)
	fmt.Println("Direction:", direction)
	fmt.Println("Item count:", autoShowCount)
	fmt.Println("Ranking data field index:", rankBy)
}
```

Las opciones se corresponden con los atributos clásicos de AutoShow que se escriben en el XML de la tabla dinámica (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), por lo que los valores leídos serán respetados por cualquier versión de Excel.

## **Nota**

{{% alert color="primary" %}}
- Después de llamar a `Top10AutoShow()`, vuelva a llamar a `PivotTable.CalculateData()`: la configuración solo surtirá efecto en la disposición mostrada tras el siguiente recálculo.
- La configuración de AutoShow funciona con campos de fila y de columna. Un campo situado únicamente en el área de filtros no se puede clasificar de esta forma, ya que sus elementos no se muestran en el cuerpo de la tabla dinámica.
{{% /alert %}}

## **Excel 2007-365: filtro de los 10 principales (FilterTop10)**
Las versiones modernas de Excel ofrecen el filtro de los 10 principales como filtro de valores en el menú del campo («Filtros de valores», «10 principales...»). Aspose.Cells lo representa mediante el método `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)`, que devuelve el objeto `PivotFilter` creado:
- `valueFieldIndex` — índice de base cero del campo de datos cuyos valores agregados determinan la clasificación de los elementos.
- `type` — significado de `itemCount`. `PivotFilterType.Count` conserva una cantidad fija de elementos (la opción «Elementos» del cuadro de diálogo). `PivotFilterType.Percent` conserva un porcentaje de los elementos, por lo que `itemCount` es el propio porcentaje: 30 conserva el 30 % de los elementos con la clasificación más alta. `PivotFilterType.Sum` clasifica en función de la cobertura acumulativa de los valores.
- `isTop` — `true` para Superiores, `false` para Inferiores.
- `itemCount` — el valor N de «N principales»; su unidad depende de `type`.

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
	// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
	sportField.FilterTop10(0, PivotFilterType_Count, true, 2)
	// For a percentage-based filter instead, keep the top 30 percent of the items:
	// sportField.FilterTop10(0, PivotFilterType_Percent, true, 30)
	pivotTable.CalculateData()
	workbook.Save_String("output-top10-filter.xlsx")
}
```

{{% alert color="primary" %}}
Las opciones de AutoShow y `FilterTop10` son dos funcionalidades distintas. AutoShow escribe el atributo clásico `autoShow` en el campo de la tabla dinámica, y sus opciones se respetan en todas las versiones de Excel desde Excel 97. `FilterTop10` escribe una entrada moderna de tipo `PivotFilter`, que requiere Excel 2007 o posterior. Al abrir un libro de trabajo en una versión anterior de Excel, una tabla dinámica que utilice el filtro moderno vuelve a mostrar todos los elementos. Para los documentos que deben procesarse en ida y vuelta mediante herramientas heredadas, se recomienda `Top10AutoShow`; para los libros de trabajo modernos, se recomienda `FilterTop10` porque es compatible con los demás filtros de valores.
{{% /alert %}}

## **Artículos relacionados**
- [Agrupar campos de la tabla dinámica](/cells/es/go-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="go" >}}