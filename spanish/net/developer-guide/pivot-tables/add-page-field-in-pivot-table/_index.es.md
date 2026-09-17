---
title: Agregar campos de filtro a una tabla dinámica en Aspose.Cells for .NET
description: Aprenda cómo agregar y configurar campos de filtro en tablas dinámicas usando Aspose.Cells for .NET, incluida la adición de campos de filtro, el filtrado de selección única y el filtrado de selección múltiple.
keywords: Aspose.Cells, .NET, tabla dinámica, campo de filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /es/net/add-page-field-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
linktitle: Agregar campos de filtro
---

{{% alert color="primary" %}}
Aspose.Cells admite el ciclo de vida completo de los campos de filtro en las tablas dinámicas. Puede agregar un campo de filtro mediante una API de conveniencia de alto nivel o mediante la colección de bajo nivel `PageFields`, y puede controlar el filtro en modo de selección única, limpiarlo para mostrar todos los elementos del filtro o cambiar el campo a selección múltiple para que los usuarios puedan elegir varios elementos del filtro a la vez a través de la interfaz de casillas de verificación en Excel.
{{% /alert %}}

## **Introducción**
Un campo de filtro es un campo dinámico que controla *qué subconjunto* de los datos de origen muestra el cuerpo de la tabla dinámica. Los usuarios finales lo ven como un menú desplegable en la parte superior de una tabla dinámica renderizada en Excel, y al seleccionar uno de los elementos de filtro disponibles se reconstruye el cuerpo de la tabla dinámica de modo que solo se resumen los registros que pertenecen a ese elemento de filtro. Un campo dinámico se convierte en un campo de filtro cuando se registra como `PivotFieldType.Page` en lugar de `PivotFieldType.Row`, `PivotFieldType.Column` o `PivotFieldType.Data`.

## **Agregar un campo de filtro**

### Agregar un campo de filtro con AddFieldToArea
El siguiente ejemplo crea un pequeño conjunto de datos de Fruta / Año / Monto, coloca una tabla dinámica en la celda E3 con `Fruit` en el área de filas, `Amount` en el área de datos y `Year` en el área de filtro, actualiza la tabla dinámica y guarda el libro de trabajo.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Crear un nuevo libro de trabajo
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";
// Configurar la fila de encabezado
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// Rellenar 9 filas de datos de muestra: Fruta, Año, Cantidad
object[,] data = new object[,]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    worksheet.Cells[i + 1, 0].PutValue(data[i, 0]);
    worksheet.Cells[i + 1, 1].PutValue(data[i, 1]);
    worksheet.Cells[i + 1, 2].PutValue(data[i, 2]);
}
// Agregar una tabla dinámica anclada en la celda E3
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// Agregar campos a sus áreas: Fruta como Fila, Cantidad como Dato, Año como campo de Página
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// Refrescar y calcular los datos de la tabla dinámica
pivotTable.CalculateData();
// Guardar el libro de trabajo
workbook.Save("pageFieldSample.xlsx");
```

### Agregar un campo de filtro con PageFields.Add
Cuando ya trabaja con una instancia de `PivotField`, puede pasarla directamente a `PivotTable.PageFields.Add`. La tabla dinámica y el campo de filtro se construyen exactamente como en el escenario anterior; solo se reemplaza el registro final del área de filtro con la llamada a la API de bajo nivel.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// — La tabla dinámica y el campo de página se construyen exactamente como en
//   Escenario 1a (datos Fruta/Año/Monto, pivote en E3, Fruta→Fila,
//   Monto→Datos). A continuación obtenemos el PivotField de Año de la
//   colección BaseFields y lo pasamos a PageFields.Add — la
//   alternativa de bajo nivel a AddFieldToArea. El resultado es
//   funcionalmente idéntico al Escenario 1a.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
// Encabezados
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");
// Datos de muestra (9 filas)
sheet.Cells["A2"].PutValue("apple");    sheet.Cells["B2"].PutValue("2020"); sheet.Cells["C2"].PutValue(100);
sheet.Cells["A3"].PutValue("apple");    sheet.Cells["B3"].PutValue("2021"); sheet.Cells["C3"].PutValue(150);
sheet.Cells["A4"].PutValue("apple");    sheet.Cells["B4"].PutValue("2022"); sheet.Cells["C4"].PutValue(200);
sheet.Cells["A5"].PutValue("grape");    sheet.Cells["B5"].PutValue("2020"); sheet.Cells["C5"].PutValue(300);
sheet.Cells["A6"].PutValue("grape");    sheet.Cells["B6"].PutValue("2021"); sheet.Cells["C6"].PutValue(400);
sheet.Cells["A7"].PutValue("grape");    sheet.Cells["B7"].PutValue("2022"); sheet.Cells["C7"].PutValue(500);
sheet.Cells["A8"].PutValue("blueberry"); sheet.Cells["B8"].PutValue("2020"); sheet.Cells["C8"].PutValue(250);
sheet.Cells["A9"].PutValue("blueberry"); sheet.Cells["B9"].PutValue("2021"); sheet.Cells["C9"].PutValue(350);
sheet.Cells["A10"].PutValue("blueberry");sheet.Cells["B10"].PutValue("2022"); sheet.Cells["C10"].PutValue(450);
// Agregar tabla dinámica en E3 cubriendo A1:C10
int pivotIndex = sheet.PivotTables.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];
// Fruta -> Fila, Monto -> Datos (Año irá a Página abajo)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Enfoque de bajo nivel: tomar el PivotField Año existente desde BaseFields
// y registrarlo en el área Página mediante PageFields.Add(PivotField).
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);
// Actualizar para que el nuevo campo de página se refleje en el libro guardado
pivotTable.CalculateData();
workbook.Save("output.xlsx");
```

## **Filtrado de selección única (mostrar un solo elemento de filtro)**
En el comportamiento predeterminado de selección única, el campo de filtro se muestra como un único menú desplegable y el entero `PivotField.CurrentPageItem` selecciona qué elemento de filtro controla el cuerpo de la tabla dinámica. Asignar un índice específico selecciona ese único elemento; asignar el valor centinela especial `0x7FFD` (decimal 32765) limpia el filtro para que todos los elementos del filtro se resuman a la vez. La selección única es el valor predeterminado; no necesita habilitarla explícitamente.

### Mostrar todos los elementos
Establecer `CurrentPageItem` en el valor mágico `0x7FFD` equivale a borrar el filtro: el cuerpo de la tabla dinámica resume todos los elementos del filtro como si no se aplicara ningún filtro.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
class Program
{
    static void Main()
    {
        // Crear un nuevo libro de trabajo
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        // Poblar datos de Fruta/Año/Cantidad
        sheet.Cells["A1"].PutValue("Fruit");
        sheet.Cells["B1"].PutValue("Year");
        sheet.Cells["C1"].PutValue("Amount");
        object[,] data = new object[,]
        {
            {"Apple", 2022, 100},
            {"Apple", 2023, 150},
            {"Banana", 2022, 80},
            {"Banana", 2023, 120},
            {"Cherry", 2022, 200},
            {"Cherry", 2023, 250}
        };
        for (int r = 0; r < data.GetLength(0); r++)
        {
            for (int c = 0; c < data.GetLength(1); c++)
            {
                sheet.Cells[r + 1, c].PutValue(data[r, c]);
            }
        }
        // Crear tabla dinámica en E3
        var pivotTables = sheet.PivotTables;
        int index = pivotTables.Add("=A1:C7", "E3", "PivotTable1");
        PivotTable pivotTable = pivotTables[index];
        // Configurar campos dinámicos: Fruta→Fila, Cantidad→Datos, Año→Página
        pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
        pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
        pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
        pivotTable.CalculateData();
        // Borrar el filtro de página para que cada elemento del campo de página sea visible.
        // 0x7FFD (decimal 32765) es el valor centinela especial que significa "todos los elementos" —
        // equivalente a seleccionar "(Todos)" en el menú desplegable del campo de página de Excel.
        pivotTable.PageFields[0].CurrentPageItem = 0x7FFD;
        workbook.Save("output.xlsx");
    }
}
```

### Mostrar un elemento específico
Establecer `CurrentPageItem` en un índice real selecciona solo ese elemento de filtro. El índice es la posición del elemento en la lista ordenada de elementos del campo de filtro, por lo que, por ejemplo, `1` selecciona el segundo elemento después de ordenar.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Crear libro de trabajo
var workbook = new Workbook();
var sheet = workbook.Worksheets[0];
var cells = sheet.Cells;
// Agregar datos de muestra (Fruta/Año/Monto)
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
cells["A2"].PutValue("Apple");
cells["B2"].PutValue("2020");
cells["C2"].PutValue("100");
cells["A3"].PutValue("Apple");
cells["B3"].PutValue("2021");
cells["C3"].PutValue("150");
cells["A4"].PutValue("Banana");
cells["B4"].PutValue("2020");
cells["C4"].PutValue("200");
cells["A5"].PutValue("Banana");
cells["B5"].PutValue("2021");
cells["C5"].PutValue("250");
// Agregar tabla dinámica en E3
var pivotTables = sheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables[pivotIndex];
// Agregar campos: Fruta→Fila, Monto→Datos, Año→Página
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// Operaciones específicas del campo de página
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = segundo elemento en orden de clasificación (por ejemplo, "2021")
// Actualizar y calcular tabla dinámica
pivotTable.CalculateData();
workbook.Save("output.xlsx");
```

## **Filtrado de selección múltiple**
El filtrado de selección múltiple convierte el menú desplegable del filtro en una lista de casillas de verificación y permite al usuario final elegir varios elementos del filtro simultáneamente. Aspose.Cells expone dos propiedades que funcionan en conjunto. `PivotField.IsMultipleItemSelectionAllowed` debe establecerse en `true` antes de que la interfaz de selección múltiple surta efecto. Una vez habilitada, `PivotItem.IsHidden` controla qué elementos aparecen en la lista de casillas de verificación, por lo que puede mostrar todos los elementos o permitir solo elementos específicos en una lista blanca.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// — La tabla dinámica y el campo de página se construyen exactamente como en
//   Escenario 1a (datos Fruit/Year/Amount, pivote en E3, Fruit→Row,
//   Amount→Data, Year→Page mediante AddFieldToArea).
//   A continuación aplicamos filtrado de selección múltiple en el campo de página.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
// Datos de muestra: Fruit | Year | Amount
cells[0, 0].PutValue("Fruit");
cells[0, 1].PutValue("Year");
cells[0, 2].PutValue("Amount");
string[,] data = new string[,]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    cells[i + 1, 0].PutValue(data[i, 0]);
    cells[i + 1, 1].PutValue(Convert.ToInt32(data[i, 1]));
    cells[i + 1, 2].PutValue(Convert.ToInt32(data[i, 2]));
}
Worksheet pivotSheet = workbook.Worksheets.Add("Pivot");
PivotTableCollection pivots = pivotSheet.PivotTables;
int pivotIndex = pivots.Add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = pivots[pivotIndex];
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// — Habilitar selección múltiple en el campo de página
pivotTable.PageFields[0].IsMultipleItemSelectionAllowed = true;
// Parte A — seleccionar TODOS los elementos (hacer que cada elemento sea visible)
PivotItemCollection pivotItems = pivotTable.PageFields[0].PivotItems;
for (int i = 0; i < pivotItems.Count; i++)
{
    pivotItems[i].IsHidden = false;
}
// Parte B — seleccionar solo elementos específicos por valor de origen
for (int i = 0; i < pivotItems.Count; i++)
{
    switch (pivotItems[i].GetStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems[i].IsHidden = false;
            break;
        default:
            pivotItems[i].IsHidden = true;
            break;
    }
}
pivotTable.CalculateData();
workbook.Save("output.xlsx");
```

> **Nota:** Al utilizar el filtrado de selección múltiple a través de `PivotItem.IsHidden`, **al menos un `PivotItem` debe permanecer visible** (`IsHidden == false`). Si todos los elementos están ocultos, Excel se bloquea al abrir el archivo o muestra una tabla dinámica en blanco. Verifique siempre que su lista blanca de selección múltiple incluya al menos un elemento de sus datos de origen.

## **¿Qué API y qué modo debo usar?**
La tabla siguiente resume cuándo usar cada API y modo para que pueda elegir la combinación adecuada sin necesidad de leer cada escenario en detalle.
| Escenario / Caso de uso | API recomendada | Propiedad utilizada | Notas |
|---|---|---|---|
| Agregar un campo de filtro por nombre de columna de origen (más común) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Alto nivel, en una sola línea. Use esta opción a menos que necesite una referencia a `PivotField`. |
| Agregar un campo de filtro cuando ya tiene un objeto `PivotField` | `PivotTable.PageFields.Add(PivotField)` | n/a | Úselo cuando el objeto de campo se obtuvo en otro lugar o necesita reutilizarse. |
| Filtrar a un solo elemento de filtro (modo predeterminado) | `PivotField.CurrentPageItem` | establecido en un índice específico | Por ejemplo, `1` muestra el segundo elemento de la lista ordenada. |
| Mostrar todos los elementos / borrar el filtro | `PivotField.CurrentPageItem` | establecido en `0x7FFD` | El valor mágico `0x7FFD` (decimal 32765) es el centinela de "todos los elementos". |
| Habilitar la interfaz de selección múltiple en Excel | `PivotField.IsMultipleItemSelectionAllowed` | establecido en `true` | Necesario antes de que cualquier llamada a `IsHidden` surta efecto. |
| Ocultar / mostrar elementos individuales en una lista de selección múltiple | `PivotItem.IsHidden` | establecido por elemento | Al menos un elemento debe permanecer visible (`IsHidden == false`). |

{{% alert color="primary" %}}
Recuerde siempre la restricción de visibilidad al configurar el filtrado de selección múltiple. Si todos los `PivotItem` de un campo de filtro de selección múltiple están ocultos, Excel se bloquea al abrir o muestra una tabla dinámica en blanco. Construya su lista blanca con base en sus datos de origen para que al menos un elemento permanezca visible, y sus libros de trabajo guardados se abrirán de forma fiable en cualquier equipo.
{{% /alert %}}

## **Artículos relacionados**
- [Actualización de tablas dinámicas en Aspose.Cells for .NET](/cells/es/net/refresh-pivot-table/)
- [Aplicar estilos a tablas dinámicas](/cells/es/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}