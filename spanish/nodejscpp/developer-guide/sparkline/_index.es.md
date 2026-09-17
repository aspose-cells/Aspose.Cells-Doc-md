---
title: Minigráficos en Aspose.Cells for Node.js via C++
description: Aspose.Cells es una biblioteca de Node.js para trabajar con archivos de hojas de cálculo que admite la creación de minigráficos, pequeños gráficos colocados dentro de celdas de la hoja de cálculo. Este artículo explica cómo añadir y personalizar minigráficos de línea, columna y ganancia/pérdida utilizando la biblioteca Aspose.Cells.
linktitle: Minigráficos
keywords: Aspose.Cells, biblioteca de Node.js, hoja de cálculo, minigráficos, minigráfico de línea, minigráfico de columna, minigráfico de ganancia/pérdida, SparklineGroup, SparklineType
type: docs
weight: 195
url: /es/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite la creación de minigráficos dentro de celdas de la hoja de cálculo. Los minigráficos son pequeños gráficos que caben dentro de una sola celda, proporcionando una rápida representación visual de las tendencias de los datos. Aspose.Cells admite minigráficos de línea, columna y ganancia/pérdida, y cada uno se puede personalizar con respecto al color, el grosor de línea, los puntos alto/bajo y los marcadores.

## **Introducción**
Los minigráficos son pequeños gráficos dentro de celdas que resultan útiles cuando se desea mostrar una tendencia rápida junto a una fila o columna de datos sin ocupar el espacio de un gráfico completo. Excel admite tres tipos de minigráficos: **línea**, **columna** y **ganancia/pérdida**. Aspose.Cells refleja esta capacidad a través de las API `SparklineGroup` y `SparklineGroupCollection` que se encuentran en el espacio de nombres `Aspose.Cells.Charts`.
En Aspose.Cells, cada minigráfico que se agrega se crea a través de `worksheet.sparklineGroups.add(...)`, que devuelve un objeto `SparklineGroup`. Luego puede usar ese objeto para establecer el tipo de minigráfico, el rango de datos, la celda de destino y las propiedades visuales como el color de la línea, el grosor de la línea, los marcadores y los indicadores de puntos altos/bajos.
Este artículo recorre cada uno de los tres tipos de minigráficos admitidos por Aspose.Cells — **Línea**, **Columna** y **Ganancia/Pérdida** — y muestra cómo agregarlos, personalizar sus colores y guardar el libro de trabajo resultante.

## **Minigráficos de línea**
Un minigráfico de línea dibuja una línea continua a través de los puntos de datos en una serie, lo que lo convierte en la opción más natural para mostrar tendencias a lo largo del tiempo. En Aspose.Cells, un minigráfico de línea se crea pasando `SparklineType.Line` al método `sparklineGroups.add`.
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene una fila de datos de origen (por ejemplo, fila 1, columnas A a E) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino donde se dibujará el minigráfico.
4. Llame a `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. El tercer argumento — `false` — indica an Aspose.Cells que el rango de datos es horizontal (una fila), no vertical (una columna).
5. Opcionalmente, personalice el `SparklineGroup` devuelto. Para un minigráfico de línea puede establecer el color de la línea usando `group.line.color` (que espera un `CellsColor` de `Aspose.Cells.Drawing`), ajustar el grosor de la línea y activar los marcadores de puntos altos/bajos.
6. Guarde el libro de trabajo.
El siguiente ejemplo crea un libro de trabajo, escribe los valores 5, -3, 8, -2, 6 en las celdas A1 a E1 y agrega un minigráfico de línea en la celda F1 que traza esos valores. También personaliza el color de la línea a rojo y habilita los marcadores para los puntos altos y bajos.

```javascript
const AsposeCells = require("aspose.cells");
// Paso 1: Crear un Workbook y obtener la primera hoja de cálculo
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Paso 2: Escribir valores de muestra 5, -3, 8, -2, 6 en las celdas A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Paso 3: Construir un CellArea apuntando a la celda destino F1
const dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // columna F (índice 0)
dest.setEndColumn(5);
dest.setStartRow(0);      // fila 1 (índice 0)
dest.setEndRow(0);
// Paso 4: Agregar un minigráfico de tipo Line desde A1:E1 en F1
// SparklineGroups.Add devuelve el índice del grupo recién agregado
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);
// Paso 5: Crear un CellsColor rojo y asignarlo al color de línea del minigráfico
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// Paso 6: Habilitar los marcadores de punto alto y punto bajo
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Paso 7: Guardar el workbook
workbook.save("output_line.xlsx");
```

## **Minigráficos de columna**
Un minigráfico de columna representa cada punto de datos como una barra vertical. Esto lo hace muy adecuado para datos cuya magnitud es significativa — por ejemplo, cifras de ventas mensuales o recuentos. En Aspose.Cells, se crea un minigráfico de columna pasando `SparklineType.Column` al método `sparklineGroups.add`.
El procedimiento refleja el ejemplo del minigráfico de línea:
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene los datos de origen.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` resultante — por ejemplo, configurando `group.type` para confirmar el tipo, o ajustando el color de las barras.
6. Guarde el libro de trabajo en un archivo de salida separado para que no sobrescriba el ejemplo del minigráfico de línea.
El ejemplo siguiente escribe los valores 5, -3, 8, -2, 6 en A1:E1 y representa un minigráfico de columna en F1. Los valores negativos se dibujan como barras que van hacia abajo y los valores positivos como barras que van hacia arriba, lo que hace que las contribuciones positivas y negativas sean fáciles de detectar de un vistazo.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Paso 2: Escribir valores de muestra en A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Paso 3: Construir un CellArea que apunte a F1 (índice de columna 5, índice de fila 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Paso 4: Añadir un minigráfico de Columna a la celda de destino
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Paso 5: Confirmar el tipo de minigráfico leyendo group.Type
console.log("Sparkline Type added: " + group.getType());
// Paso 6: Guardar el libro de trabajo
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **Minigráficos de ganancia/pérdida**
Un minigráfico de ganancia/pérdida es una variante especial del minigráfico de columna diseñado para mostrar solo dos resultados: un valor positivo se dibuja como una barra "arriba" (una ganancia) y un valor cero o negativo se dibuja como una barra "abajo" (una pérdida). Los minigráficos de ganancia/pérdida se usan comúnmente para visualizar secuencias de victorias y derrotas, resultados de aprobado/no aprobado o cualquier resultado binario a lo largo del tiempo.
En Aspose.Cells, un minigráfico de ganancia/pérdida se crea pasando `SparklineType.Stacked` al método `sparklineGroups.add`. (A pesar del nombre, `SparklineType.Stacked` es el valor de enumeración utilizado para solicitar la representación de ganancia/pérdida).
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el rango de origen. Dado que los minigráficos de ganancia/pérdida tratan cada valor como una ganancia o una pérdida, la magnitud del valor no importa — solo su signo. Los valores positivos se convierten en barras arriba y los valores no positivos se convierten en barras abajo.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` devuelto, por ejemplo, configurando colores de acento para las barras de ganancia y pérdida.
6. Guarde el libro de trabajo con un nombre de archivo distinto para que los tres ejemplos puedan coexistir en el disco.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Paso 2: Poblar datos de muestra en la fila 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Paso 3: Construir un CellArea que apunte a F1 (columna 5, fila 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // fila 1
dest.setEndRow(0);
// Paso 4: Agregar un minigráfico de Ganancia/Pérdida (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Paso 5: Personalizar el grupo de minigráficos
// Habilitar marcadores de punto alto y punto bajo
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Establecer el color del punto alto en verde
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);
// Establecer el color del punto bajo en rojo
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);
// Establecer el color del punto negativo en naranja
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);
// Establecer el color de serie predeterminado (usado para barras positivas)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);
// Paso 6: Guardar el libro
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Combinando los tres tipos de minigráficos**
El ejemplo combinado a continuación crea un único libro de trabajo, rellena la fila 1 con los valores 5, -3, 8, -2, 6 y luego agrega tres grupos de minigráficos en las celdas F1, F2 y F3 — uno de cada tipo — de modo que el archivo resultante demuestre los tres estilos de minigráficos a la vez.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Paso 2: Llenar datos de muestra en la fila 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Paso 3: Agregar un grupo de minigráficos de línea en F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Personalizar el color del minigráfico de línea mediante CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);
// Paso 4: Agregar un grupo de minigráficos de columna en F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Personalizar el color de la serie del minigráfico de columna
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);
// Paso 5: Agregar un grupo de minigráficos de Ganancia/Pérdida (Apilado) en F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Personalizar el color de la serie del minigráfico de Ganancia/Pérdida
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);
// Paso 6: Guardar el libro de trabajo
workbook.save("output_all.xlsx");
```

## **Personalización de la apariencia de los minigráficos**
Una vez que se ha creado y agregado un `SparklineGroup` a `worksheet.sparklineGroups`, puede leer o modificar varias de sus propiedades visuales antes de guardar el libro de trabajo. Las propiedades personalizadas más comunes son:
- **`group.type`** — el `SparklineType` (Line, Column o Stacked). Se establece cuando se agrega el grupo, pero puede leerlo de nuevo para confirmarlo.
- **`group.line.color`** — el color de la línea, expresado como un `CellsColor` creado mediante `workbook.createCellsColor()`. Esta es la propiedad que se debe usar para el color del trazo del minigráfico de línea.
- **`group.line.weight`** — el grosor de la línea en puntos. Los valores más altos producen líneas más gruesas.
- **Marcadores de puntos altos/bajos** — indicadores que activan pequeños marcadores en los puntos de datos más altos y más bajos, útiles para resaltar los extremos.
- **Marcadores de puntos primero/último/negativo** — indicadores que activan marcadores en el primer, último y negativos puntos de datos.
Para cambiar un color, siempre cree una instancia de `CellsColor` y asígnela a la propiedad correspondiente. No asigne un `System.Drawing.Color` directamente a las propiedades de color del minigráfico — esperan el tipo `CellsColor` de `Aspose.Cells.Drawing`. El método `sparklineGroups.add` en sí mismo devuelve un objeto `SparklineGroup` completamente tipado, por lo que puede encadenar asignaciones de propiedades en el valor de retorno o almacenarlo en una variable local y personalizarlo antes de guardar.
{{% /alert %}}1. Create a new `Workbook` and access the first worksheet.
3. Build a `CellArea` describing the destination cell.
4. Call `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.javascript

{{< app/cells/assistant language="javascript" >}}