---
title: Agregar campos de filtro a una tabla dinámica en Aspose.Cells para .NET
linktitle: Agregar campos de filtro
description: Aprenda cómo agregar y configurar campos de filtro en tablas dinámicas usando Aspose.Cells for Node.js via C++, incluyendo cómo agregar campos de filtro, filtrado de selección única y filtrado de selección múltiple.
keywords: Aspose.Cells, Node.js via C++, tabla dinámica, campo de filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /es/nodejs-cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite el ciclo de vida completo de los campos de filtro en las tablas dinámicas. Puede agregar un campo de filtro mediante una API de conveniencia de alto nivel o mediante la colección de bajo nivel `PageFields`, y puede controlar el filtro de página en modo de selección única, limpiarlo para mostrar todos los elementos de la página o cambiar el campo a selección múltiple para que los usuarios puedan elegir varios elementos de página a la vez a través de la interfaz de casillas de verificación en Excel.
{{% /alert %}}

## **Introducción**

Un campo de filtro es un campo dinámico que controla *qué subconjunto* de los datos de origen muestra el cuerpo de la tabla dinámica. Los usuarios finales lo ven como una lista desplegable en la parte superior de una tabla dinámica renderizada en Excel, y al seleccionar uno de los elementos de página disponibles, el cuerpo de la tabla dinámica se reconstruye de manera que solo se resumen los registros que pertenecen a ese elemento de página. Un campo dinámico se convierte en un campo de filtro cuando se registra como `PivotFieldType.Page` en lugar de `PivotFieldType.Row`, `PivotFieldType.Column` o `PivotFieldType.Data`.

Un campo de filtro puede operar en dos comportamientos. En el comportamiento predeterminado de **selección única**, solo un elemento de página es visible a la vez, por lo que el cuerpo de la tabla dinámica resume exactamente un subconjunto. En el comportamiento de **selección múltiple**, el campo expone una lista de casillas de verificación, y el cuerpo de la tabla dinámica resume la unión de cada elemento de página marcado. El mismo campo de origen puede moverse hacia adelante y hacia atrás entre estos comportamientos alternando una sola propiedad.

Aspose.Cells for Node.js via C++ expone dos formas equivalentes de registrar un campo de filtro. La API de alto nivel es `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")`, que toma el nombre de la columna de origen y agrega el campo en una sola llamada. La API de bajo nivel es `PivotTable.pageFields.add(PivotField)`, que se utiliza cuando ya tiene una referencia `PivotField` y desea agregar la misma instancia de campo al área de filtro. Ambas APIs terminan poblando la misma colección `PageFields`, y el resto de este artículo demuestra cómo elegir entre ellas y cómo controlar cada modo de filtrado.

## **Agregar un campo de filtro**

Hay dos formas de registrar un campo dinámico en el área de filtro. La llamada de alto nivel toma el nombre de la columna de origen como una cadena y es la ruta más común. La llamada de bajo nivel acepta una instancia existente de `PivotField` y es conveniente cuando la misma instancia de campo debe reutilizarse en múltiples áreas dinámicas. Ambas llamadas colocan el campo en `PivotTable.pageFields`, tras lo cual aparece como la lista desplegable de página en la parte superior de la tabla dinámica renderizada.

### Agregar un campo de filtro con addFieldToArea

El siguiente ejemplo construye un pequeño conjunto de datos de Fruta / Año / Cantidad, coloca una tabla dinámica en la celda E3 con `Fruit` en el área de filas, `Amount` en el área de datos y `Year` en el área de filtro, actualiza la tabla dinámica y guarda el libro de trabajo.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// Configurar la fila de encabezados
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// Poblar 9 filas de datos de muestra: Fruta, Año, Cantidad
var data = [
    [ "apple", 2020, 100 ],
    [ "banana", 2021, 200 ],
    [ "apple", 2021, 150 ],
    [ "grape", 2020, 120 ],
    [ "orange", 2022, 180 ],
    [ "banana", 2020, 90 ],
    [ "grape", 2021, 130 ],
    [ "apple", 2022, 170 ],
    [ "orange", 2021, 110 ]
];

for (var i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}

// Agregar una tabla dinámica anclada en la celda E3
var pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Agregar campos a sus áreas: Fruta como Fila, Cantidad como Dato, Año como campo de Página
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Actualizar y calcular los datos de la tabla dinámica
pivotTable.calculateData();

// Guardar el libro
workbook.save("pageFieldSample.xlsx");
```

### Agregar un campo de filtro con pageFields.add

Cuando ya trabaja con una instancia `PivotField`, puede pasarla directamente a `PivotTable.pageFields.add`. La tabla dinámica y el campo de filtro se construyen exactamente como en el escenario anterior; solo se reemplaza el registro final del área de filtro con la llamada API de bajo nivel.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Encabezados
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

// Datos de muestra (9 filas)
sheet.getCells().get("A2").putValue("apple");     sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");     sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");     sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");     sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");     sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");     sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);

// Agregar tabla dinámica en E3 cubriendo A1:C10
let pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Fruta -> Fila, Cantidad -> Datos (Año irá a Página abajo)
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Enfoque de bajo nivel: obtener el PivotField de Año existente desde BaseFields
// y registrarlo en el área de Página mediante PageFields.Add(PivotField).
let yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);

// Actualizar para que el nuevo campo de página se refleje en el libro guardado
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Filtrado de selección única (mostrar un elemento de página)**

En el comportamiento predeterminado de selección única, el campo de filtro se renderiza como una sola lista desplegable y el entero `PivotField.currentPageItem` selecciona qué elemento de página controla el cuerpo de la tabla dinámica. Asignar un índice específico elige ese único elemento; asignar el centinela especial `0x7FFD` (decimal 32765) limpia el filtro para que todos los elementos de página se resuman a la vez. La selección única es el valor predeterminado; no necesita habilitarla explícitamente.

### Mostrar todos los elementos

Establecer `currentPageItem` en el valor mágico `0x7FFD` equivale a limpiar el filtro de página: el cuerpo de la tabla dinámica resume todos los elementos de página como si no se aplicara ningún filtro.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Rellenar datos de Fruta/Año/Cantidad
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

let data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
];

for (let r = 0; r < data.length; r++) {
    for (let c = 0; c < data[r].length; c++) {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

// Crear tabla dinámica en E3
let pivotTables = sheet.getPivotTables();
let index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
let pivotTable = pivotTables.get(index);

// Configurar campos dinámicos: Fruta→Fila, Cantidad→Datos, Año→Página
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

pivotTable.calculateData();

// Limpiar el filtro de página para que cada elemento del campo de página sea visible.
// 0x7FFD (decimal 32765) es el valor centinela especial que significa "todos los elementos" —
// equivalente a seleccionar "(Todos)" en el menú desplegable del campo de página de Excel.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD);

workbook.save("output.xlsx");
```

### Mostrar un elemento específico

Establecer `currentPageItem` en un índice real selecciona solo ese elemento de página. El índice es la posición del elemento en la lista de elementos ordenada del campo de filtro, por lo que, por ejemplo, `1` selecciona el segundo elemento después de ordenar.

```javascript
var workbook = new AsposeCells.Workbook();
var sheet = workbook.getWorksheets().get(0);
var cells = sheet.getCells();

// Agregar datos de muestra (Fruta/Año/Monto)
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");

cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");

cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");

cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");

cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");

// Agregar tabla dinámica en E3
var pivotTables = sheet.getPivotTables();
var pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables.get(pivotIndex);

// Agregar campos: Fruta→Fila, Monto→Datos, Año→Página
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// Operaciones específicas del campo de página
pivotTable.getPageFields().get(0).setCurrentPageItem(1); // 1 = segundo elemento en orden de clasificación (por ejemplo, "2021")

// Actualizar y calcular la tabla dinámica
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Filtrado de selección múltiple**

El filtrado de selección múltiple convierte la lista desplegable de la página en una lista de casillas de verificación y permite al usuario final elegir varios elementos de página simultáneamente. Aspose.Cells expone dos propiedades que funcionan juntas. `PivotField.isMultipleItemSelectionAllowed` debe establecerse en `true` antes de que la interfaz de selección múltiple surta efecto. Una vez habilitada, `PivotItem.isHidden` controla qué elementos aparecen en la lista de casillas de verificación, por lo que puede mostrar todos los elementos o permitir solo elementos específicos.

El código a continuación habilita la selección múltiple en el mismo campo de filtro Year construido en el Escenario 1a, y luego muestra dos patrones: la Parte A revela cada elemento de página al dejar `isHidden` establecido en `false` para cada entrada, mientras que la Parte B permite solo los valores de origen que elija y oculta todo lo demás mediante un bloque `switch (pivotItems[i].getStringValue())`.

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cells = sheet.getCells();

// Datos de muestra: Fruta | Año | Cantidad
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");

let data = [
    ["apple", "2019", "100"],
    ["apple", "2020", "150"],
    ["apple", "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape", "2019", "120"],
    ["grape", "2020", "170"],
    ["grape", "2021", "220"]
];

for (let i = 0; i < data.length; i++) {
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(parseInt(data[i][2]));
}

let pivotSheet = workbook.getWorksheets().add("Pivot");
let pivots = pivotSheet.getPivotTables();
let pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
let pivotTable = pivots.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");

// — Habilitar selección múltiple en el campo de página
pivotTable.getPageFields().get(0).setIsMultipleItemSelectionAllowed(true);

// Parte A — seleccionar TODOS los elementos (hacer visible cada elemento)
let pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (let i = 0; i < pivotItems.getCount(); i++) {
    pivotItems.get(i).setIsHidden(false);
}

// Parte B — seleccionar solo elementos específicos por valor de origen
for (let i = 0; i < pivotItems.getCount(); i++) {
    switch (pivotItems.get(i).getStringValue()) {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setIsHidden(false);
            break;
        default:
            pivotItems.get(i).setIsHidden(true);
            break;
    }
}

pivotTable.calculateData();

workbook.save("output.xlsx");
```

> **Nota:** Al usar el filtrado de selección múltiple a través de `PivotItem.isHidden`, **al menos un `PivotItem` debe permanecer visible** (`isHidden == false`). Si todos los elementos están ocultos, Excel se bloquea al abrir el archivo o renderiza una tabla dinámica en blanco. Siempre verifique que su lista permitida de selección múltiple incluya al menos un elemento de sus datos de origen.

## **¿Qué API y qué modo debo usar?**

La tabla a continuación resume cuándo usar cada API y modo para que pueda elegir la combinación correcta sin leer cada escenario en detalle.

| Escenario / Caso de uso | API recomendada | Propiedad utilizada | Notas |
|---|---|---|---|
| Agregar un campo de filtro por nombre de columna de origen (lo más común) | `PivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | n/a | Alto nivel, una sola línea. Use esto a menos que necesite una referencia `PivotField`. |
| Agregar un campo de filtro cuando ya tiene un objeto `PivotField` | `PivotTable.pageFields.add(PivotField)` | n/a | Use cuando el objeto de campo se obtuvo en otro lugar o necesita reutilizarse. |
| Filtrar a un solo elemento de página (modo predeterminado) | `PivotField.currentPageItem` | establecer en un índice específico | Por ejemplo, `1` muestra el segundo elemento en la lista ordenada. |
| Mostrar todos los elementos / limpiar el filtro de página | `PivotField.currentPageItem` | establecer en `0x7FFD` | El valor mágico `0x7FFD` (decimal 32765) es el centinela para "todos los elementos". |
| Habilitar la interfaz de selección múltiple en Excel | `PivotField.isMultipleItemSelectionAllowed` | establecer en `true` | Requerido antes de que cualquier llamada a `isHidden` surta efecto. |
| Ocultar / mostrar elementos individuales en una lista de selección múltiple | `PivotItem.isHidden` | establecer por elemento | Al menos un elemento debe permanecer visible (`isHidden == false`). |

{{% alert color="primary" %}}
Recuerde siempre la restricción de visibilidad al configurar el filtrado de selección múltiple. Si todos los `PivotItem` en un campo de filtro de selección múltiple están ocultos, Excel se bloquea al abrir o renderiza una tabla dinámica en blanco. Construya su lista permitida contra sus datos de origen para que al menos un elemento permanezca visible, y sus libros de trabajo guardados se abrirán de manera confiable en cualquier máquina.
{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}
