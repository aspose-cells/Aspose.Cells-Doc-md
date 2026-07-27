---
title: Agregar campos de filtro a una tabla dinámica en Aspose.Cells para .NET
linktitle: Agregar campos de filtro
description: Aprenda a agregar y configurar campos de filtro en tablas dinámicas usando Aspose.Cells for .NET, incluyendo cómo agregar campos de filtro, filtrado de selección única y filtrado de selección múltiple.
keywords: Aspose.Cells, .NET, tabla dinámica, campo de filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /es/net/add-filter-field-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite el ciclo de vida completo de los campos de filtro en tablas dinámicas. Puede agregar un campo de filtro mediante una API de conveniencia de alto nivel o mediante la colección de bajo nivel `PageFields`, y puede controlar el filtro de página en modo de selección única, limpiarlo para mostrar cada elemento de página, o cambiar el campo a selección múltiple para que los usuarios puedan elegir varios elementos de página a la vez a través de la interfaz de casillas de verificación en Excel.
{{% /alert %}}

## **Introducción**

Un campo de filtro es un campo dinámico que controla *qué subconjunto* de los datos de origen muestra el cuerpo de la tabla dinámica. Los usuarios finales lo ven como un menú desplegable en la parte superior de una tabla dinámica renderizada en Excel, y al seleccionar uno de los elementos de página disponibles, el cuerpo de la tabla dinámica se reconstruye de modo que solo se resumen los registros que pertenecen a ese elemento de página. Un campo dinámico se convierte en un campo de filtro cuando se registra como `PivotFieldType.Page` en lugar de `PivotFieldType.Row`, `PivotFieldType.Column` o `PivotFieldType.Data`.

Un campo de filtro puede operar con dos comportamientos. En el comportamiento predeterminado de **selección única**, solo un elemento de página es visible a la vez, por lo que el cuerpo de la tabla dinámica resume exactamente un subconjunto. En el comportamiento de **selección múltiple**, el campo expone una lista de casillas de verificación, y el cuerpo de la tabla dinámica resume la unión de cada elemento de página marcado. El mismo campo de origen puede moverse de un lado a otro entre estos comportamientos alternando una sola propiedad.

Aspose.Cells for .NET expone dos formas equivalentes de registrar un campo de filtro. La API de alto nivel es `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")`, que toma el nombre de la columna de origen y agrega el campo en una sola llamada. La API de bajo nivel es `PivotTable.PageFields.Add(PivotField)`, que se utiliza cuando ya tiene una referencia `PivotField` y desea agregar la misma instancia de campo al área de filtro. Ambas API terminan rellenando la misma colección `PageFields`, y el resto de este artículo demuestra cómo elegir entre ellas y cómo controlar cada modo de filtrado.

## **Agregar un campo de filtro**

Hay dos formas de registrar un campo dinámico en el área de filtro. La llamada de alto nivel toma el nombre de la columna de origen como una cadena de texto y es la ruta más común. La llamada de bajo nivel acepta una instancia existente de `PivotField` y es conveniente cuando el mismo objeto de campo debe reutilizarse en múltiples áreas de la tabla dinámica. Ambas llamadas colocan el campo en `PivotTable.PageFields`, después de lo cual aparece como el menú desplegable de página en la parte superior de la tabla dinámica renderizada.

### Agregar un campo de filtro con AddFieldToArea

El siguiente ejemplo crea un pequeño conjunto de datos de Fruta / Año / Cantidad, coloca una tabla dinámica en la celda E3 con `Fruit` en el área de filas, `Amount` en el área de datos y `Year` en el área de filtro, actualiza la tabla dinámica y guarda el libro de trabajo.

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

// Poblar 9 filas de datos de muestra: Fruta, Año, Cantidad
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

// Agregar campos a sus áreas: Fruta como Fila, Cantidad como Datos, Año como campo de Página
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// Actualizar y calcular los datos de la tabla dinámica
pivotTable.CalculateData();

// Guardar el libro de trabajo
workbook.Save("pageFieldSample.xlsx");
```

### Agregar un campo de filtro con PageFields.Add

Cuando ya trabaja con una instancia de `PivotField`, puede pasarla directamente a `PivotTable.PageFields.Add`. La tabla dinámica y el campo de filtro se construyen exactamente como en el escenario anterior; solo el registro final del área de filtro se reemplaza con la llamada a la API de bajo nivel.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — La tabla dinámica y el campo de página se construyen exactamente como en
//   Escenario 1a (datos de Fruta/Año/Cantidad, pivote en E3, Fruta→Fila,
//   Cantidad→Datos). A continuación obtenemos el PivotField Año desde la
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

// Fruta -> Fila, Cantidad -> Datos (Año irá a Página abajo)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Enfoque de bajo nivel: tomar el PivotField Año existente de BaseFields
// y registrarlo en el área Página mediante PageFields.Add(PivotField).
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);

// Actualizar para que el nuevo campo de página se refleje en el libro guardado
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **Filtrado de selección única (mostrar un elemento de página)**

En el comportamiento predeterminado de selección única, el campo de filtro se renderiza como un único menú desplegable y el entero `PivotField.CurrentPageItem` selecciona qué elemento de página dirige el cuerpo de la tabla dinámica. Asignar un índice específico elige ese único elemento; asignar el centinela especial `0x7FFD` (decimal 32765) limpia el filtro para que cada elemento de página se resuma de una vez. La selección única es la predeterminada; no necesita habilitarla explícitamente.

### Mostrar todos los elementos

Establecer `CurrentPageItem` en el valor mágico `0x7FFD` equivale a limpiar el filtro de página: el cuerpo de la tabla dinámica resume cada elemento de página como si no se aplicara ningún filtro.

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

        // Rellenar datos de Fruta/Año/Cantidad
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

        // Configurar campos dinámicos: Fruta→Fila, Cantidad→Dato, Año→Página
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

Establecer `CurrentPageItem` en un índice real selecciona solo ese elemento de página. El índice es la posición del elemento en la lista ordenada de elementos del campo de filtro, por ejemplo, `1` selecciona el segundo elemento después de ordenar.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Crear libro de trabajo
var workbook = new Workbook();
var sheet = workbook.Worksheets[0];
var cells = sheet.Cells;

// Agregar datos de muestra (Fruta/Año/Cantidad)
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

// Agregar campos: Fruta→Fila, Cantidad→Datos, Año→Página
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// Operaciones específicas del campo de página
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = segundo elemento en orden ordenado (por ejemplo, "2021")

// Refrescar y calcular tabla dinámica
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **Filtrado de selección múltiple**

El filtrado de selección múltiple convierte el menú desplegable de página en una lista de casillas de verificación y permite al usuario final elegir varios elementos de página simultáneamente. Aspose.Cells expone dos propiedades que trabajan juntas. `PivotField.IsMultipleItemSelectionAllowed` debe establecerse en `true` antes de que la interfaz de selección múltiple surta efecto. Después de habilitarla, `PivotItem.IsHidden` controla qué elementos aparecen en la lista de casillas de verificación, por lo que puede mostrar cada elemento o incluir en la lista blanca solo elementos específicos.

El código siguiente habilita la selección múltiple en el mismo campo de filtro Year construido en el escenario 1a, y luego muestra dos patrones: la Parte A revela cada elemento de página dejando `IsHidden` establecido en `false` para cada entrada, mientras que la Parte B incluye en la lista blanca solo los valores de origen que elija y oculta todo lo demás mediante un bloque `switch (pivotItems[i].GetStringValue())`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — La tabla dinámica y el campo de página se construyen exactamente como en
//   Escenario 1a (datos de Fruta/Año/Cantidad, pivote en E3, Fruta→Fila,
//   Cantidad→Datos, Año→Página vía AddFieldToArea).
//   A continuación aplicamos el filtrado de selección múltiple en el campo de página.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;

// Datos de muestra: Fruta | Año | Cantidad
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
int pivotIndex = pivots.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = pivots[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// — Habilitar selección múltiple en el campo de página
pivotTable.PageFields[0].IsMultipleItemSelectionAllowed = true;

// Parte A — seleccionar TODOS los elementos (hacer visible cada elemento)
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

> **Nota:** Cuando use el filtrado de selección múltiple a través de `PivotItem.IsHidden`, **al menos un `PivotItem` debe permanecer visible** (`IsHidden == false`). Si cada elemento está oculto, Excel se bloquea al abrir el archivo o renderiza una tabla dinámica en blanco. Siempre verifique que su lista blanca de selección múltiple incluya al menos un elemento de sus datos de origen.

## **¿Qué API y qué modo debo usar?**

La tabla siguiente resume cuándo usar cada API y modo para que pueda elegir la combinación correcta sin leer cada escenario en detalle.

| Escenario / Caso de uso | API recomendada | Propiedad utilizada | Notas |
|---|---|---|---|
| Agregar un campo de filtro por nombre de columna de origen (más común) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Alto nivel, una sola línea. Use esto a menos que necesite una referencia `PivotField`. |
| Agregar un campo de filtro cuando ya tiene un objeto `PivotField` | `PivotTable.PageFields.Add(PivotField)` | n/a | Use cuando el objeto de campo se obtuvo en otro lugar o necesita reutilizarse. |
| Filtrar a un único elemento de página (modo predeterminado) | `PivotField.CurrentPageItem` | establecer en un índice específico | Por ejemplo, `1` muestra el segundo elemento en la lista ordenada. |
| Mostrar todos los elementos / limpiar el filtro de página | `PivotField.CurrentPageItem` | establecer en `0x7FFD` | El valor mágico `0x7FFD` (decimal 32765) es el centinela para "todos los elementos". |
| Habilitar la interfaz de selección múltiple en Excel | `PivotField.IsMultipleItemSelectionAllowed` | establecer en `true` | Requerido antes de que cualquier llamada a `IsHidden` surta efecto. |
| Ocultar / mostrar elementos individuales en una lista de selección múltiple | `PivotItem.IsHidden` | establecer por elemento | Al menos un elemento debe permanecer visible (`IsHidden == false`). |

{{% alert color="primary" %}}
Recuerde siempre la restricción de visibilidad al configurar el filtrado de selección múltiple. Si cada `PivotItem` en un campo de filtro de selección múltiple está oculto, Excel se bloquea al abrir o renderiza una tabla dinámica en blanco. Construya su lista blanca contra sus datos de origen para que al menos un elemento permanezca visible, y sus libros de trabajo guardados se abrirán de manera confiable en cualquier máquina.
{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}
