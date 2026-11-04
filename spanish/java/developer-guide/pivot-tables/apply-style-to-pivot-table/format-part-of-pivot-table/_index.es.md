---
title: Formato de una Parte de una Tabla Dinámica
description: Formatee parte de una tabla dinámica en Aspose.Cells for Java aplicando estilos a regiones semánticas PivotArea o rectángulos CellArea mediante PivotTable.format, con los formatos almacenados en PivotTable.getPivotFormats y preservados cuando la tabla dinámica se actualiza.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Java, tabla dinámica, formato, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Java
type: docs
weight: 20
url: /es/java/format-part-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de Uso Posibles**
`PivotTable.formatAll` aplica un único estilo a toda la tabla dinámica y se describe en la página principal. No distingue entre etiquetas, valores, totales ni regiones particulares del informe.  
En la práctica, solo una parte de una tabla dinámica suele necesitar resaltarse. Los objetivos comunes incluyen las etiquetas pertenecientes a un campo de fila, las celdas de valor generadas por un campo, la fila de total general o un rectángulo arbitrario como las dos primeras filas de elementos.  
Aplicar un estilo directamente a las celdas de la hoja de cálculo de una tabla dinámica no es equivalente. Excel almacena el formato de la tabla dinámica como regiones semánticas `PivotArea` en lugar de registros de estilo de celda ordinarios. Un formato de área de pivote permanece asociado a una región, como las etiquetas o los valores de datos de un campo, y se vuelve a resolver cuando la tabla dinámica se recalcula, actualiza o expande. Por otro lado, un estilo escrito directamente en una celda pertenece a la posición de esa celda y no es rastreado por el modelo de pivote.  
Aspose.Cells expone la familia completa de sobrecargas `PivotTable.format` para que ambos tipos de formato estén disponibles:
- `format(PivotArea, Style)` ancla un estilo a una región semántica que se construye con `PivotArea.select` o `PivotArea.selectField`.
- `format(CellArea, Style)` ancla un estilo a un rectángulo de hoja de cálculo dentro de la tabla dinámica.
- `format(int row, int column, Style)` se dirige a una sola celda.
- `formatAll(Style)` formatea toda la tabla dinámica.

## **Formatear un Área de Pivote**
El flujo de trabajo de área semántica es el enfoque recomendado cuando un resaltado debe seguir a un campo o una región del informe.
1. Cree un `PivotArea` con `new PivotArea(pivotTable)`. El objeto describe una región semántica que pertenece a esa tabla dinámica específica.  
2. Seleccione un campo por su posición basada en cero en un eje dado mediante `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` selecciona tanto las etiquetas como los datos del campo.  
   - `PivotTableSelectionType.LABEL_ONLY` selecciona solo las etiquetas del campo.  
   - `PivotTableSelectionType.DATA_ONLY` selecciona solo las celdas de datos del campo.  
3. Seleccione un campo por nombre con `PivotArea.selectField(PivotFieldType axisType, String fieldName)`. Cuando se selecciona un campo de fila por nombre, la región se resuelve en las celdas de valor generadas por los elementos de ese campo.  
4. Cree un `Style` con `Workbook.createStyle()`, configure su fuente, color de primer plano y patrón de fondo sólido, y pase el estilo a `PivotTable.format(area, style)`.  
5. Cada llamada a la sobrecarga `PivotArea` añade una entrada `PivotTableFormat` a `PivotTable.getPivotFormats()`.  
6. Los formatos anclados al campo se aplican cuando se calculan los datos de la tabla dinámica. Por lo tanto, llame a `PivotTable.calculateData()` después de aplicar los formatos para que los estilos se vuelvan visibles.  
El siguiente ejemplo crea una pequeña tabla dinámica de ventas de frutas, aplica estilo a las etiquetas de fila `Fruit` con `PivotArea.select` y `PivotTableSelectionType.LABEL_ONLY`, aplica estilo a las celdas de valor generadas por ese mismo campo de fila con `PivotArea.selectField`, y luego recalcula la tabla dinámica para que ambos estilos se apliquen.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Fruit sales data
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(Color.getYellow());
labelStyle.setPattern(BackgroundType.SOLID);
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(Color.getLightGreen());
valueStyle.setPattern(BackgroundType.SOLID);
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.selectField(PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Formatear un Área de Celda de la Tabla Dinámica**
Utilice `PivotTable.format(CellArea, Style)` cuando la región de interés sea un simple rectángulo de hoja de cálculo en lugar de una región semántica de pivote.  
Un `CellArea` se describe mediante las propiedades `getStartRow()`, `getStartColumn()`, `getEndRow()` y `getEndColumn()`. Los valores son coordenadas de hoja de cálculo basadas en cero, y las coordenadas finales identifican la última fila y columna incluidas en el rectángulo, de modo que el área cubre las celdas desde la posición inicial hasta la posición final inclusive.  
A diferencia de un formato anclado a un campo, un formato `CellArea` se aplica a las celdas de inmediato. No se necesita otra llamada a `calculateData()` para que el estilo aparezca.  
Un rectángulo `CellArea` puede contener celdas de etiqueta y celdas de valor juntas. La siguiente sección describe cómo Aspose.Cells y Excel representan internamente ese rectángulo.  
El siguiente ejemplo formatea el rectángulo `E4:F5` de la tabla dinámica con un estilo cursiva y azul claro, y guarda el libro de trabajo sin ningún recálculo adicional.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Cómo Se Mapean las Áreas de Pivote y las Áreas de Celda**
Excel almacena el formato de la tabla dinámica como registros `pivotArea` en lugar de registros de estilo de celda ordinarios de la hoja de cálculo. El mismo modelo es utilizado por Aspose.Cells, por lo que una solicitud de formato se traduce en áreas de pivote cuando se registra.  
La relación entre el `CellArea` proporcionado por el usuario y las áreas de pivote almacenadas internamente es de muchos a muchos en ambas direcciones.  
- Un `CellArea` puede generar varias áreas de pivote. Si el rectángulo abarca tanto celdas de etiqueta como celdas de valor, se descompone en reglas separadas de etiqueta y datos, porque el modelo de pivote trata el formato de etiquetas y de datos de forma independiente.  
- Una área de pivote puede resolverse en varias instancias `CellArea` disjuntas. Una región semántica como una fila de total general, o un campo cuyos elementos no son contiguos, puede cubrir múltiples rectángulos. Por eso `PivotArea.getCellAreas()` devuelve una colección en lugar de un solo rectángulo.  
Cada operación de formato realizada a través de `PivotTable.format` se registra en `PivotTable.getPivotFormats()`. Cada entrada `PivotTableFormat` expone el `PivotArea` asociado y el `Style` que se le aplica. La sobrecarga `PivotArea` agrega exactamente una entrada por llamada, mientras que un `CellArea` que contiene diferentes regiones semánticas puede agregar múltiples entradas.  
Para distinguir las regiones almacenadas, cada `PivotArea` expone las banderas `getOnlyLabel()` y `getOnlyData()`. El ejemplo a continuación formatea un único rectángulo que cubre tanto etiquetas como valores, inspecciona `PivotTable.getPivotFormats()` y muestra las coordenadas `CellArea` a las que cada área de pivote almacenada se resuelve.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
// ONE rectangle in...
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
System.out.println("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (int i = 0; i < pivotTable.getPivotFormats().getCount(); i++)
{
    PivotArea storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    System.out.println("Format " + i + ": OnlyLabel=" + storedArea.getOnlyLabel()
            + ", OnlyData=" + storedArea.getOnlyData());
    for (CellArea resolved : storedArea.getCellAreas())
    {
        System.out.println("    rows " + (resolved.StartRow + 1) + "-" + (resolved.EndRow + 1)
                + ", columns " + (resolved.StartColumn + 1) + "-" + (resolved.EndColumn + 1));
    }
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=true, OnlyData=false
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=false, OnlyData=true
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Porque los formatos se almacenan como áreas de pivote en lugar de como estilos de celda ordinarios, sobreviven a la recalculación y actualización. Cuando la tabla dinámica se actualiza con `PivotTable.refreshData`, se recalcula con `calculateData`, o se guarda y se vuelve a cargar, cada área de pivote almacenada se vuelve a resolver a la posición actual de su región y su estilo se vuelve a aplicar.
{{% /alert %}}

Utilice un `PivotArea` creado con `select` o `selectField` cuando un resaltado deba permanecer anclado a un campo o una región semántica a través de actualizaciones, y utilice un `CellArea` cuando sea suficiente formatear un rectángulo fijo en el diseño actual de la tabla dinámica. La sobrecarga de una sola celda `format(int row, int column, Style)` se dirige a una celda individual. Use `formatAll`, descrito en la página principal, cuando toda la tabla dinámica deba reformatearse de una sola vez.

## **Artículos Relacionados**
- [Aplicar Estilo a la Tabla Dinámica](/cells/es/java/apply-style-to-pivot-table/)
- [Agregar Campos de Fila y Columna a la Tabla Dinámica](/cells/es/java/pivot-table-add-row-and-column-fields/)
- [Administrar Campos de Valor en la Tabla Dinámica](/cells/es/java/manage-value-fields/)
- [Actualizar la Tabla Dinámica](/cells/es/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}