---
title: Sparklines en Aspose.Cells for Node.js via Java
description: Aspose.Cells es una biblioteca Node.js via Java para trabajar con archivos de hoja de cálculo que admite la creación de sparklines — gráficos en miniatura ubicados dentro de celdas de la hoja de cálculo, este artículo explica cómo agregar y personalizar sparklines de línea, columna y ganar/perder usando la biblioteca Aspose.Cells.
linktitle: Sparklines
keywords: Aspose.Cells, biblioteca Node.js via Java, hoja de cálculo, sparklines, sparkline de línea, sparkline de columna, sparkline ganar/perder, SparklineGroup, SparklineType
type: docs
weight: 195
url: /es/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite la creación de sparklines dentro de celdas de la hoja de cálculo. Los sparklines son gráficos en miniatura que caben en una sola celda, proporcionando una representación visual rápida de las tendencias de los datos. Aspose.Cells admite sparklines de línea, columna y ganar/perder, y cada uno puede personalizarse respecto al color, grosor de la línea, puntos alto/bajo y marcadores.
{{% /alert %}}

## **Introducción**
Los sparklines son pequeños gráficos dentro de celdas que son útiles cuando se desea mostrar una tendencia rápida junto a una fila o columna de datos sin ocupar el espacio de un gráfico completo. Excel admite tres tipos de sparklines: **línea**, **columna** y **ganar/perder**. Aspose.Cells replica esta capacidad a través de las API `SparklineGroup` y `SparklineGroupCollection` que se encuentran en el espacio de nombres `com.aspose.cells.Charts`.
En Aspose.Cells, cada sparkline que añades se crea mediante `worksheet.SparklineGroups.add(...)`, que devuelve un objeto `SparklineGroup`. Luego puedes usar ese objeto para establecer el tipo de sparkline, el rango de datos, la celda de destino y propiedades visuales como el color de la línea, el grosor de la línea, los marcadores y los indicadores de puntos alto/bajo.
Este artículo recorre cada uno de los tres tipos de sparkline compatibles con Aspose.Cells — **Línea**, **Columna** y **Ganar/Perder** — y muestra cómo agregarlos, personalizar sus colores y guardar el libro de trabajo resultante.

## **Sparklines de Línea**
Un sparkline de línea dibuja una línea continua a través de los puntos de datos de una serie, lo que lo convierte en la opción más natural para mostrar tendencias a lo largo del tiempo. En Aspose.Cells, un sparkline de línea se crea pasando `SparklineType.Line` al método `SparklineGroups.add`.
1. Crea un nuevo `Workbook` y accede a la primera hoja de cálculo.  
2. Llena una fila de datos fuente (por ejemplo, fila 1, columnas A a E) con los valores que deseas visualizar.  
3. Construye un `CellArea` que describa la celda de destino donde se dibujará el sparkline.  
4. Llama a `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. El tercer argumento — `false` — indica an Aspose.Cells que el rango de datos es horizontal (una fila), no vertical (una columna).  
5. Opcionalmente personaliza el `SparklineGroup` devuelto. Para un sparkline de línea puedes establecer el color de la línea usando `group.Line.Color` (que espera un `CellsColor` de `com.aspose.cells.Drawing`), ajustar el grosor de la línea y activar los marcadores de puntos alto/bajo.  
6. Guarda el libro de trabajo.
El siguiente ejemplo crea un libro de trabajo, escribe los valores 5, -3, 8, -2, 6 en las celdas A1 a E1, y agrega un sparkline de línea en la celda F1 que traza esos valores. También personaliza el color de la línea a rojo y habilita los marcadores para los puntos alto y bajo.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();
// Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Step 3: Build a CellArea pointing to destination cell F1
let dest = new AsposeCells.CellArea();
dest.StartColumn = 5;   // column F (0-indexed)
dest.EndColumn = 5;
dest.StartRow = 0;      // row 1 (0-indexed)
dest.EndRow = 0;
// Step 4: Add a Line sparkline from A1:E1 into F1
// SparklineGroups.Add returns the index of the newly added group
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.LINE, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);
// Step 5: Create a red CellsColor and assign it to the sparkline line color
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// Step 6: Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Step 7: Save the workbook
workbook.save("output_line.xlsx");
```

## **Sparklines de Columna**
Un sparkline de columna representa cada punto de datos como una barra vertical. Esto lo hace adecuado para datos cuya magnitud es significativa — por ejemplo, cifras de ventas mensuales o recuentos. En Aspose.Cells, creas un sparkline de columna pasando `SparklineType.Column` al método `SparklineGroups.add`.
El procedimiento replica el ejemplo del sparkline de línea:
1. Crea un nuevo `Workbook` y accede a la primera hoja de cálculo.  
3. Construye un `CellArea` que describa la celda de destino.  
4. Llama a `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.  
5. Opcionalmente personaliza el `SparklineGroup` resultante — por ejemplo, estableciendo `group.Type` para confirmar el tipo, o ajustando el color de la barra.  
6. Guarda el libro de trabajo en un archivo de salida separado para que no sobrescriba el ejemplo del sparkline de línea.
El ejemplo a continuación escribe los valores 5, -3, 8, -2, 6 en A1:E1 y renderiza un sparkline de columna en F1. Los valores negativos se dibujan como barras que bajan y los positivos como barras que suben, lo que facilita identificar rápidamente las contribuciones positivas y negativas.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Write sample values into A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
let dest = new AsposeCells.CellArea();
dest.StartColumn = 5;
dest.EndColumn = 5;
dest.StartRow = 0;
dest.EndRow = 0;
// Step 4: Add a Column sparkline to the destination cell
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.COLUMN, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Step 5: Confirm the sparkline type by reading group.Type
console.log("Sparkline Type added: " + group.getType());
// Step 6: Save the workbook
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **Sparklines Ganar/Perder**
Un sparkline ganar/perder es una variante especial del sparkline de columna diseñada para mostrar solo dos resultados: un valor positivo se dibuja como una barra "arriba" (una victoria) y un valor cero o negativo se dibuja como una barra "abajo" (una derrota). Los sparklines ganar/perder se utilizan comúnmente para visualizar secuencias de victorias y derrotas, resultados de aprobar/reprobar, o cualquier resultado binario a lo largo del tiempo.
En Aspose.Cells, un sparkline ganar/perder se crea pasando `SparklineType.Stacked` al método `SparklineGroups.add`. (A pesar del nombre, `SparklineType.Stacked` es el valor de enum utilizado para solicitar la representación ganar/perder.)
1. Crea un nuevo `Workbook` y accede a la primera hoja de cálculo.  
2. Rellena el rango fuente. Debido a que los sparklines ganar/perder tratan cada valor como una victoria o una derrota, la magnitud del valor no importa — solo su signo. Los valores positivos se convierten en barras ascendentes y los valores no positivos en barras descendentes.  
3. Construye un `CellArea` que describa la celda de destino.  
4. Llama a `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.  
5. Opcionalmente personaliza el `SparklineGroup` devuelto, por ejemplo, estableciendo colores de acento para las barras de victoria y de derrota.  
6. Guarda el libro de trabajo bajo un nombre de archivo distinto para que los tres ejemplos puedan coexistir en el disco.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Build a CellArea pointing to F1 (column 5, row 0)
let dest = new AsposeCells.CellArea();
dest.StartColumn = 5;   // F
dest.EndColumn = 5;
dest.StartRow = 0;      // row 1
dest.EndRow = 0;
// Step 4: Add a Win/Loss sparkline (SparklineType.STACKED)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.STACKED,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Step 5: Customize the sparkline group
// Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Set the high-point color to green
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);
// Set the low-point color to red
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);
// Set the negative-point color to orange
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);
// Set the default series color (used for positive bars)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);
// Step 6: Save the workbook
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Combinando los Tres Tipos de Sparkline**
El ejemplo combinado a continuación crea un único libro de trabajo, llena la fila 1 con los valores 5, -3, 8, -2, 6, y luego agrega tres grupos de sparkline en las celdas F1, F2 y F3 — uno de cada tipo — de modo que el archivo resultante demuestre los tres estilos de sparkline a la vez.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Add a Line sparkline group at F1
let lineArea = new AsposeCells.CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.LINE, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Customize the line sparkline color via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Step 4: Add a Column sparkline group at F2
let columnArea = new AsposeCells.CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.COLUMN, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Customize the column sparkline series color
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.STACKED, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Customize the win/loss sparkline series color
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Step 6: Save the workbook
workbook.save("output_all.xlsx");
```

## **Personalizando la Apariencia del Sparkline**
Una vez que se ha creado y agregado un `SparklineGroup` a `worksheet.SparklineGroups`, puedes leer o modificar varias de sus propiedades visuales antes de guardar el libro de trabajo. Las propiedades más comúnmente personalizadas son:
- **`group.Type`** — el `SparklineType` (Line, Column o Stacked). Se establece al agregar el grupo, pero puedes leerlo de nuevo para confirmar.  
- **`group.Line.Color`** — el color de la línea, expresado como un `CellsColor` creado mediante `workbook.createCellsColor()`. Esta es la propiedad que se debe usar para el color del trazo del sparkline de línea.  
- **`group.Line.Weight`** — el grosor de la línea en puntos. Valores más altos producen líneas más gruesas.  
- **Marcadores de punto Alto/Bajo** — indicadores que activan pequeños marcadores en los puntos de datos más altos y más bajos, útiles para enfatizar los extremos.  
- **Marcadores de punto Primero/Último/Negativo** — indicadores que activan marcadores en los primeros, últimos y negativos puntos de datos.
Para cambiar un color, siempre crea una instancia de `CellsColor` y asígnala a la propiedad correspondiente. No asignes un `java.awt.Color` directamente a las propiedades de color del sparkline — esperan el tipo `CellsColor` de `com.aspose.cells.Drawing`. El método `SparklineGroups.add` devuelve un objeto `SparklineGroup` totalmente tipado, por lo que puedes encadenar asignaciones de propiedades en el valor de retorno o almacenarlo en una variable local y personalizarlo antes de guardar.

{{< app/cells/assistant language="nodejs-java" >}}