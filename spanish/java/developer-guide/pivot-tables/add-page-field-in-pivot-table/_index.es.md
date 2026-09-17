---
title: Agregar Campos de Filtro a una Tabla Dinámica en Aspose.Cells for Java
description: Aprenda a agregar y configurar campos de filtro en tablas dinámicas usando Aspose.Cells for Java, incluyendo la adición de campos de filtro, el filtrado de selección única y el filtrado de selección múltiple.
keywords: Aspose.Cells, Java, tabla dinámica, campo de filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /es/java/add-page-field-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
linktitle: Agregar Campos de Filtro
---

{{% alert color="primary" %}}
Aspose.Cells admite el ciclo de vida completo de los campos de filtro en las tablas dinámicas. Puede agregar un campo de filtro mediante una API de alto nivel de conveniencia o mediante la colección de bajo nivel `PageFields`, y puede controlar el filtro en modo de selección única, limpiarlo para mostrar todos los elementos del filtro, o cambiar el campo a selección múltiple para que los usuarios puedan elegir varios elementos del filtro a la vez a través de la interfaz de casillas de verificación en Excel.
{{% /alert %}}

## **Introducción**
Un campo de filtro es un campo dinámico que controla *qué subconjunto* de los datos de origen muestra el cuerpo de la tabla dinámica. Los usuarios finales lo ven como un menú desplegable en la parte superior de una tabla dinámica renderizada en Excel, y seleccionar uno de los elementos del filtro disponibles reconstruye el cuerpo de la tabla dinámica de modo que solo se resumen los registros que pertenecen a ese elemento del filtro. Un campo dinámico se convierte en un campo de filtro cuando se registra como `PivotFieldType.Page` en lugar de `PivotFieldType.Row`, `PivotFieldType.Column` o `PivotFieldType.Data`.

## **Agregar un Campo de Filtro**

### Agregar un Campo de Filtro con addFieldToArea
El siguiente ejemplo construye un pequeño conjunto de datos de Fruta / Año / Cantidad, coloca una tabla dinámica en la celda E3 con `Fruit` en el área de filas, `Amount` en el área de datos y `Year` en el área de filtro, actualiza la tabla dinámica y guarda el libro de trabajo.

```java
import com.aspose.cells.*;
// Crear un nuevo libro de trabajo
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
// Configurar la fila de encabezado
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Poblar 9 filas de datos de muestra: Fruta, Año, Cantidad
Object[][] data = new Object[][]
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
for (int i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}
// Agregar una tabla dinámica anclada en la celda E3
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Agregar campos a sus áreas: Fruta como Fila, Cantidad como Datos, Año como Campo de Página
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Actualizar y calcular los datos de la tabla dinámica
pivotTable.calculateData();
// Guardar el libro de trabajo
workbook.save("pageFieldSample.xlsx");
```

### Agregar un Campo de Filtro con PageFields.add
Cuando ya trabaja con una instancia de `PivotField`, puede pasarlo directamente a `PivotTable.PageFields.add`. La tabla dinámica y el campo de filtro se construyen exactamente como en el escenario anterior; solo el registro del área de filtro final se reemplaza con la llamada a la API de bajo nivel.

```java
import com.aspose.cells.*;
// - La tabla dinámica y el campo de página se construyen exactamente como en
//   Escenario 1a (datos Fruit/Year/Amount, pivote en E3, Fruit->Fila,
//   Amount->Datos). A continuación obtenemos el PivotField de Year desde la
//   colección BaseFields y lo pasamos a PageFields.Add - la
//   alternativa de bajo nivel a AddFieldToArea. El resultado es
//   funcionalmente idéntico al Escenario 1a.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// Encabezados
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
// Datos de muestra (9 filas)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);
// Agregar tabla dinámica en E3 cubriendo A1:C10
int pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);
// Fruit -> Fila, Amount -> Datos (Year irá a Página a continuación)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Enfoque de bajo nivel: tomar el PivotField Year existente desde BaseFields
// y registrarlo en el área Página mediante PageFields.Add(PivotField).
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);
// Actualizar para que el nuevo campo de página se refleje en el libro guardado
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **Filtrado de Selección Única (Mostrar un Elemento de Filtro)**
En el comportamiento predeterminado de selección única, el campo de filtro se renderiza como un menú desplegable único y el entero `PivotField.CurrentPageItem` selecciona qué elemento del filtro dirige el cuerpo de la tabla dinámica. Asignar un índice específico selecciona ese único elemento; asignar el valor centinela especial `0x7FFD` (decimal 32765) limpia el filtro para que cada elemento del filtro se resuma a la vez. La selección única es la predeterminada; no necesita habilitarla explícitamente.

### Mostrar Todos los Elementos
Establecer `CurrentPageItem` en el valor mágico `0x7FFD` equivale a limpiar el filtro: el cuerpo de la tabla dinámica resume cada elemento del filtro como si no se aplicara ningún filtro.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// Poblar datos de Fruta/Año/Cantidad
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
Object[][] data = new Object[][]
{
    {"Apple", 2022, 100},
    {"Apple", 2023, 150},
    {"Banana", 2022, 80},
    {"Banana", 2023, 120},
    {"Cherry", 2022, 200},
    {"Cherry", 2023, 250}
};
for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
// Crear tabla dinámica en E3
PivotTableCollection pivotTables = sheet.getPivotTables();
int index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
PivotTable pivot = pivotTables.get(index);
// Configurar campos dinámicos: Fruta a Fila, Cantidad a Datos, Año a Página
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");
pivot.calculateData();
// Limpiar el filtro de página para que cada elemento en el campo de página sea visible.
// 0x7FFD (decimal 32765) es el valor centinela especial que significa "todos los elementos",
// equivalente a seleccionar "(Todos)" en el desplegable de campo de página de Excel.
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);
workbook.save("output.xlsx");
```

### Mostrar un Elemento Específico
Establecer `CurrentPageItem` en un índice real selecciona solo ese elemento del filtro. El índice es la posición del elemento en la lista de elementos ordenados del campo de filtro, por lo que, por ejemplo, `1` selecciona el segundo elemento después de ordenar.

```java
import com.aspose.cells.*;
// Crear libro de trabajo
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Agregar datos de muestra (Fruta/Año/Cantidad)
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
PivotTableCollection pivotTables = sheet.getPivotTables();
int pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);
// Agregar campos: Fruta→Fila, Cantidad→Dato, Año→Página
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Operaciones específicas del campo de página
pivotTable.getPageFields().get(0).setCurrentPageItem((short) 1); // 1 = segundo elemento en orden ordenado (por ejemplo, "2021")
// Actualizar y calcular tabla dinámica
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **Filtrado de Selección Múltiple**
El filtrado de selección múltiple convierte el menú desplegable del filtro en una lista de casillas de verificación y permite al usuario final seleccionar varios elementos del filtro simultáneamente. Aspose.Cells expone dos propiedades que trabajan juntas. `PivotField.IsMultipleItemSelectionAllowed` debe establecerse en `true` antes de que la interfaz de selección múltiple surta efecto. Una vez habilitada, `PivotItem.IsHidden` controla qué elementos aparecen en la lista de casillas de verificación, por lo que puede mostrar todos los elementos o permitir solo elementos específicos.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Datos de muestra: Fruta | Año | Cantidad
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");
String[][] data = new String[][]
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
for (int i = 0; i < data.length; i++)
{
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(Integer.parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(Integer.parseInt(data[i][2]));
}
Worksheet pivotSheet = workbook.getWorksheets().add("Pivot");
PivotTableCollection pivots = pivotSheet.getPivotTables();
int pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = pivots.get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// -- Habilitar selección múltiple en el campo de página
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);
// Parte A -- seleccionar TODOS los elementos (hacer visible cada elemento)
PivotItemCollection pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (int i = 0; i < pivotItems.getCount(); i++)
{
    pivotItems.get(i).setHidden(false);
}
// Parte B -- seleccionar solo elementos específicos por valor de origen
for (int i = 0; i < pivotItems.getCount(); i++)
{
    switch (pivotItems.get(i).getStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}
pivotTable.calculateData();
workbook.save("output.xlsx");
```

> **Nota:** Cuando use el filtrado de selección múltiple a través de `PivotItem.IsHidden`, **al menos un `PivotItem` debe permanecer visible** (`IsHidden == false`). Si todos los elementos están ocultos, Excel se bloquea al abrir el archivo o renderiza una tabla dinámica en blanco. Verifique siempre que su lista de permitidos para selección múltiple incluya al menos un elemento de sus datos de origen.

## **¿Qué API y Qué Modo Debo Usar?**
La tabla a continuación resume cuándo usar cada API y modo para que pueda elegir la combinación correcta sin leer cada escenario en detalle.
| Escenario / Caso de Uso | API Recomendada | Propiedad Utilizada | Notas |
|---|---|---|---|
| Agregar un campo de filtro por nombre de columna de origen (lo más común) | `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` | n/a | Alto nivel, una línea. Use esto a menos que necesite una referencia a `PivotField`. |
| Agregar un campo de filtro cuando ya tiene un objeto `PivotField` | `PivotTable.PageFields.add(PivotField)` | n/a | Use cuando el objeto de campo se obtuvo en otro lugar o necesita reutilizarse. |
| Filtrar a un único elemento del filtro (modo predeterminado) | `PivotField.CurrentPageItem` | establecer en un índice específico | Por ejemplo, `1` muestra el segundo elemento en la lista ordenada. |
| Mostrar todos los elementos / limpiar el filtro | `PivotField.CurrentPageItem` | establecer en `0x7FFD` | El valor mágico `0x7FFD` (decimal 32765) es el centinela para "todos los elementos". |
| Habilitar la interfaz de selección múltiple en Excel | `PivotField.IsMultipleItemSelectionAllowed` | establecer en `true` | Requerido antes de que cualquier llamada a `IsHidden` surta efecto. |
| Ocultar / mostrar elementos individuales en una lista de selección múltiple | `PivotItem.IsHidden` | establecer por elemento | Al menos un elemento debe permanecer visible (`IsHidden == false`). |

{{% alert color="primary" %}}
Recuerde siempre la restricción de visibilidad al configurar el filtrado de selección múltiple. Si todos los `PivotItem` en un campo de filtro de selección múltiple están ocultos, Excel se bloquea al abrir o renderiza una tabla dinámica en blanco. Construya su lista de permitidos contra sus datos de origen para que al menos un elemento permanezca visible, y sus libros de trabajo guardados se abrirán de forma fiable en cualquier máquina.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}