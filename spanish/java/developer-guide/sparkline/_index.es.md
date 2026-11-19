---
title: Sparklines en Aspose.Cells for Java
description: Aspose.Cells es una biblioteca de Java para trabajar con archivos de hojas de cálculo que admite la creación de sparklines, pequeños gráficos colocados dentro de las celdas de la hoja de cálculo. Este artículo explica cómo añadir y personalizar sparklines de línea, columna y victorias/derrotas utilizando la biblioteca Aspose.Cells.
linktitle: Sparklines
keywords: Aspose.Cells, biblioteca de Java, hoja de cálculo, sparklines, sparkline de línea, sparkline de columna, sparkline de victorias/derrotas, SparklineGroup, SparklineType
type: docs
weight: 195
url: /es/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite la creación de sparklines dentro de las celdas de la hoja de cálculo. Los sparklines son pequeños gráficos que caben en una sola celda y proporcionan una representación visual rápida de las tendencias de los datos. Aspose.Cells admite sparklines de tipo línea, columna y victorias/derrotas, y cada uno se puede personalizar en cuanto a color, grosor de línea, puntos altos/bajos y marcadores.
{{% /alert %}}

## **Introducción**
Los sparklines son pequeños gráficos dentro de celdas que resultan útiles cuando se desea mostrar una tendencia rápida junto a una fila o columna de datos sin ocupar el espacio de un gráfico completo. Excel admite tres tipos de sparklines: **línea**, **columna** y **victorias/derrotas**. Aspose.Cells replica esta capacidad mediante las API `SparklineGroup` y `SparklineGroupCollection` que se encuentran en el espacio de nombres `Aspose.Cells.Charts`.
En Aspose.Cells, cada sparkline que añade se crea mediante `worksheet.getSparklineGroups().add(...)`, que devuelve un objeto `SparklineGroup`. A continuación, puede utilizar ese objeto para establecer el tipo de sparkline, el rango de datos, la celda de destino y propiedades visuales como el color de la línea, el grosor de la línea, los marcadores y los indicadores de puntos altos/bajos.
Este artículo recorre cada uno de los tres tipos de sparklines admitidos por Aspose.Cells — **Línea**, **Columna** y **Victorias/Derrotas** — y muestra cómo añadirlos, personalizar sus colores y guardar el libro de trabajo resultante.

## **Sparklines de línea**
Un sparkline de línea dibuja una línea continua a través de los puntos de datos de una serie, lo que lo convierte en la elección más natural para mostrar tendencias a lo largo del tiempo. En Aspose.Cells, un sparkline de línea se crea pasando `SparklineType.LINE` al método `add`.
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene una fila de datos de origen (por ejemplo, fila 1, columnas A a E) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino donde se dibujará el sparkline.
4. Llame a `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. El tercer argumento — `false` — indica an Aspose.Cells que el rango de datos es horizontal (una fila), no vertical (una columna).
5. Opcionalmente personalice el `SparklineGroup` devuelto. Para un sparkline de línea puede establecer el color de la línea mediante `group.getLine().setColor(...)` (que espera un `CellsColor` de `Aspose.Cells.Drawing`), ajustar el grosor de la línea y activar los marcadores de puntos altos/bajos.
6. Guarde el libro de trabajo.
El siguiente ejemplo crea un libro de trabajo, escribe los valores 5, -3, 8, -2, 6 en las celdas A1 a E1 y añade un sparkline de línea en la celda F1 que traza esos valores. También personaliza el color de la línea a rojo y activa los marcadores para los puntos altos y bajos.

```java
import com.aspose.cells.*;
// Step 1: Create a Workbook and get the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
// Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Step 3: Build a CellArea pointing to destination cell F1
CellArea dest = new CellArea();
dest.StartColumn = 5;   // column F (0-indexed)
dest.EndColumn = 5;
dest.StartRow = 0;      // row 1 (0-indexed)
dest.EndRow = 0;
// Step 4: Add a Line sparkline from A1:E1 into F1
// SparklineGroups.add returns the index of the newly added group
int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(index);
// Step 5: Create a red CellsColor and assign it to the sparkline line color
CellsColor red = workbook.createCellsColor();
red.setColor(com.aspose.cells.Color.getRed());
group.setSeriesColor(red);
// Step 6: Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Step 7: Save the workbook
workbook.save("output_line.xlsx");
```

## **Sparklines de columna**
Un sparkline de columna representa cada punto de datos como una barra vertical. Esto lo hace muy adecuado para datos cuya magnitud es significativa, por ejemplo, cifras de ventas mensuales o recuentos. En Aspose.Cells, un sparkline de columna se crea pasando `SparklineType.COLUMN` al método `add`.
El procedimiento refleja el ejemplo del sparkline de línea:
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. Opcionalmente personalice el `SparklineGroup` resultante, por ejemplo, estableciendo `group.getType()` para confirmar el tipo o ajustando el color de las barras.
6. Guarde el libro de trabajo en un archivo de salida independiente para que no sobrescriba el ejemplo del sparkline de línea.
El siguiente ejemplo escribe los valores 5, -3, 8, -2, 6 en A1:E1 y renderiza un sparkline de columna en F1. Los valores negativos se dibujan como barras hacia abajo y los positivos como barras hacia arriba, lo que facilita la identificación de las contribuciones positivas y negativas de un vistazo.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Write sample values into A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Build a CellArea pointing to F1 (column index 5, row index 0)
CellArea dest = new CellArea();
dest.StartColumn = 5;
dest.EndColumn = 5;
dest.StartRow = 0;
dest.EndRow = 0;
// Add a Column sparkline to the destination cell
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);
// Confirm the sparkline type by reading group.Type
System.out.println("Sparkline Type added: " + group.getType());
// Save the workbook
workbook.save("output_column.xlsx");
System.out.println("Workbook saved as output_column.xlsx");
```

## **Sparklines de victorias/derrotas**
Un sparkline de victorias/derrotas es una variante especial del sparkline de columna diseñada para mostrar solo dos resultados: un valor positivo se dibuja como una barra "hacia arriba" (una victoria) y un valor cero o negativo se dibuja como una barra "hacia abajo" (una derrota). Los sparklines de victorias/derrotas se utilizan comúnmente para visualizar secuencias de victorias y derrotas, resultados de aprobado/suspenso o cualquier resultado binario a lo largo del tiempo.
En Aspose.Cells, un sparkline de victorias/derrotas se crea pasando `SparklineType.STACKED` al método `add`. (A pesar del nombre, `SparklineType.STACKED` es el valor de enumeración utilizado para solicitar el renderizado de victorias/derrotas.)
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el rango de origen. Dado que los sparklines de victorias/derrotas tratan cada valor como una victoria o una derrota, la magnitud del valor no importa, solo su signo. Los valores positivos se convierten en barras hacia arriba y los valores no positivos en barras hacia abajo.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Opcionalmente personalice el `SparklineGroup` devuelto, por ejemplo, estableciendo colores de acento para las barras de victoria y derrota.
6. Guarde el libro de trabajo con un nombre de archivo distinto para que los tres ejemplos puedan coexistir en disco.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Populate sample data
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Build a CellArea pointing to F1 (column 5, row 0)
CellArea dest = new CellArea();
dest.StartColumn = 5;
dest.EndColumn = 5;
dest.StartRow = 0;
dest.EndRow = 0;
// Add a Win/Loss sparkline (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);
// Customize the sparkline group
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Set the high-point color to green
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.getGreen());
group.setHighPointColor(highColor);
// Set the low-point color to red
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.getRed());
group.setLowPointColor(lowColor);
// Set the negative-point color to orange
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.getOrange());
group.setNegativePointsColor(negColor);
// Set the default series color (used for positive bars)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(Color.fromArgb(70, 130, 180)); // SteelBlue approximation
group.setSeriesColor(seriesColor);
// Save the workbook
workbook.save("output_winloss.xlsx");
System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **Combinación de los tres tipos de sparklines**
El siguiente ejemplo combinado crea un único libro de trabajo, rellena la fila 1 con los valores 5, -3, 8, -2, 6 y, a continuación, añade tres grupos de sparklines en las celdas F1, F2 y F3 — uno de cada tipo — para que el archivo resultante demuestre los tres estilos de sparklines a la vez.

```java
import com.aspose.cells.*;
// Step 1: Create a Workbook and get the first worksheet
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Add a Line sparkline group at F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // Fix: Use static factory method
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Customize the line sparkline color via CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Step 4: Add a Column sparkline group at F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Fix: Use static factory method
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Customize the column sparkline series color
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Fix: Use static factory method
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Customize the win/loss sparkline series color
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Step 6: Save the workbook
workbook.save("output_all.xlsx");
```

## **Personalización de la apariencia de los sparklines**
Una vez que se ha creado y añadido un `SparklineGroup` a `worksheet.getSparklineGroups()`, puede leer o modificar varias de sus propiedades visuales antes de guardar el libro de trabajo. Las propiedades personalizadas con mayor frecuencia son:
- **`group.getType()`** — el `SparklineType` (LINE, COLUMN o STACKED). Se establece cuando se añade el grupo, pero puede leerlo de nuevo para confirmarlo.
- **`group.getLine().setColor(...)`** — el color de la línea, expresado como un `CellsColor` creado mediante `workbook.createCellsColor()`. Esta es la propiedad que se debe utilizar para el color del trazo del sparkline de línea.
- **`group.getLine().setWeight(...)`** — el grosor de la línea en puntos. Los valores más altos producen líneas más gruesas.
- **Marcadores de puntos altos/bajos** — indicadores que activan pequeños marcadores en los puntos de datos más altos y más bajos, útiles para resaltar los extremos.
- **Marcadores de puntos primero/último/negativo** — indicadores que activan o desactivan los marcadores en los puntos de datos primero, último y negativo.
Para cambiar un color, cree siempre una instancia de `CellsColor` y asígnela a la propiedad correspondiente. No asigne un `java.awt.Color` directamente a las propiedades de color del sparkline; esperan el tipo `CellsColor` de `Aspose.Cells.Drawing`. El propio método `add` devuelve un objeto `SparklineGroup` completamente tipado, por lo que puede encadenar asignaciones de propiedades sobre el valor devuelto o almacenarlo en una variable local y personalizarlo antes de guardar.

{{< app/cells/assistant language="java" >}}