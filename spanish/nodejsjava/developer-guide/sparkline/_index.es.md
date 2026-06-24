---
title: Minigráficos en Aspose.Cells para Aspose.Cells for Node.js via Java
linktitle: Sparklines
description: Aspose.Cells es una biblioteca de Node.js via Java para trabajar con archivos de hojas de cálculo que admite la creación de minigráficos, gráficos en miniatura colocados dentro de celdas de la hoja de cálculo. Este artículo explica cómo añadir y personalizar minigráficos de línea, columna y victoria/derrota utilizando la biblioteca Aspose.Cells.
keywords: Aspose.Cells, biblioteca de Node.js via Java, hoja de cálculo, minigráficos, minigráfico de línea, minigráfico de columna, minigráfico de victoria/derrota, SparklineGroup, SparklineType
type: docs
weight: 195
url: /es/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la creación de minigráficos dentro de celdas de la hoja de cálculo. Los minigráficos son gráficos en miniatura que caben dentro de una sola celda, proporcionando una rápida representación visual de las tendencias de los datos. Aspose.Cells admite minigráficos de línea, columna y victoria/derrota, y cada uno se puede personalizar en cuanto a color, grosor de línea, puntos altos/bajos y marcadores.

{{% /alert %}}

## **Introducción**

Los minigráficos son pequeños gráficos dentro de una celda que resultan útiles cuando se desea mostrar una tendencia rápida junto a una fila o columna de datos sin ocupar el espacio de un gráfico completo. Excel admite tres tipos de minigráficos: **línea**, **columna** y **victoria/derrota**. Aspose.Cells refleja esta capacidad a través de las API `SparklineGroup` y `SparklineGroupCollection` que se encuentran en el espacio de nombres `com.aspose.cells.Charts`.

En Aspose.Cells, cada minigráfico que añada se crea mediante `worksheet.SparklineGroups.add(...)`, que devuelve un objeto `SparklineGroup`. A continuación, puede utilizar ese objeto para establecer el tipo de minigráfico, el rango de datos, la celda de destino y las propiedades visuales, como el color de la línea, el grosor de la línea, los marcadores y los indicadores de puntos altos/bajos.

{{% alert color="primary" %}}

Un único `SparklineGroup` puede contener uno o más minigráficos que comparten el mismo estilo. Cuando llama a `add` y pasa una fila de datos junto con una sola celda de destino, obtiene un minigráfico dentro de esa celda. Si su rango de destino es más ancho que una sola celda, se dibuja un minigráfico independiente en cada celda de destino, todos utilizando el mismo estilo y rango de datos.

{{% /alert %}}

Este artículo repasa cada uno de los tres tipos de minigráficos compatibles con Aspose.Cells — **Línea**, **Columna** y **Victoria/Derrota** — y muestra cómo agregarlos, personalizar sus colores y guardar el libro de trabajo resultante.

## **Minigráficos de línea**

Un minigráfico de línea dibuja una línea continua a través de los puntos de datos de una serie, lo que lo convierte en la opción más natural para mostrar tendencias a lo largo del tiempo. En Aspose.Cells, un minigráfico de línea se crea pasando `SparklineType.Line` al método `SparklineGroups.add`.

El flujo de trabajo es el mismo que para cualquier otro tipo de minigráfico:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene una fila de datos de origen (por ejemplo, fila 1, columnas A a E) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino donde se dibujará el minigráfico.
4. Llame a `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. El tercer argumento — `false` — indica a Aspose.Cells que el rango de datos es horizontal (una fila), no vertical (una columna).
5. Opcionalmente, personalice el `SparklineGroup` devuelto. Para un minigráfico de línea puede establecer el color de la línea usando `group.Line.Color` (que espera un `CellsColor` de `com.aspose.cells.Drawing`), ajustar el grosor de la línea y activar o desactivar los marcadores de puntos altos/bajos.
6. Guarde el libro de trabajo.

El siguiente ejemplo crea un libro de trabajo, escribe los valores 5, -3, 8, -2, 6 en las celdas A1 a E1 y añade un minigráfico de línea en la celda F1 que traza esos valores. También personaliza el color de la línea a rojo y activa los marcadores para los puntos altos y bajos.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();

// Paso 2: Escribir los valores de muestra 5, -3, 8, -2, 6 en las celdas A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// Paso 3: Construir un CellArea que apunte a la celda de destino F1
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // columna F (índice basado en 0)
dest.setEndColumn(5);
dest.setStartRow(0);      // fila 1 (índice basado en 0)
dest.setEndRow(0);

// Paso 4: Agregar un minigráfico de tipo Línea desde A1:E1 en F1
// SparklineGroups.Add devuelve el índice del grupo recién agregado
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);

// Paso 5: Crear un CellsColor rojo y asignarlo al color de la línea del minigráfico
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// Paso 6: Habilitar los marcadores de punto alto y punto bajo
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// Paso 7: Guardar el libro de trabajo
workbook.save("output_line.xlsx");
```

## **Minigráficos de columna**

Un minigráfico de columna representa cada punto de datos como una barra vertical. Esto lo hace muy adecuado para datos cuya magnitud es significativa — por ejemplo, cifras de ventas mensuales o recuentos. En Aspose.Cells, se crea un minigráfico de columna pasando `SparklineType.Column` al método `SparklineGroups.add`.

El procedimiento refleja el ejemplo del minigráfico de línea:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el mismo rango de origen (A1:E1) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` resultante — por ejemplo, estableciendo `group.Type` para confirmar el tipo, o ajustando el color de las barras.
6. Guarde el libro de trabajo en un archivo de salida separado para que no sobrescriba el ejemplo del minigráfico de línea.

El ejemplo siguiente escribe los valores 5, -3, 8, -2, 6 en A1:E1 y renderiza un minigráfico de columna en F1. Los valores negativos se dibujan como barras hacia abajo y los valores positivos como barras hacia arriba, lo que facilita identificar de un vistazo las contribuciones positivas y negativas.

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

// Paso 4: Agregar un minigráfico de Columna a la celda de destino
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// Paso 5: Confirmar el tipo de minigráfico leyendo group.Type
console.log("Sparkline Type added: " + group.getType());

// Paso 6: Guardar el libro de trabajo
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");
```

## **Minigráficos de victoria/derrota**

Un minigráfico de victoria/derrota es una variante especial del minigráfico de columna diseñado para mostrar solo dos resultados: un valor positivo se dibuja como una barra hacia arriba (una victoria) y un valor cero o negativo se dibuja como una barra hacia abajo (una derrota). Los minigráficos de victoria/derrota se usan comúnmente para visualizar secuencias de victorias y derrotas, resultados de aprobado/suspendido o cualquier resultado binario a lo largo del tiempo.

En Aspose.Cells, un minigráfico de victoria/derrota se crea pasando `SparklineType.Stacked` al método `SparklineGroups.add`. (A pesar del nombre, `SparklineType.Stacked` es el valor de enumeración que se utiliza para solicitar el renderizado de victoria/derrota.)

El procedimiento es el mismo que para los otros dos tipos:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el rango de origen. Dado que los minigráficos de victoria/derrota tratan cada valor como una victoria o una derrota, la magnitud del valor no importa — solo su signo. Los valores positivos se convierten en barras hacia arriba y los valores no positivos se convierten en barras hacia abajo.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` devuelto, por ejemplo, estableciendo colores de acento para las barras de victoria y derrota.
6. Guarde el libro de trabajo con un nombre de archivo distinto para que los tres ejemplos puedan coexistir en disco.

El ejemplo siguiente utiliza los mismos datos de entrada que las dos secciones anteriores. Los valores 5, -3, 8, -2, 6 se interpretan como victoria, derrota, victoria, derrota, victoria — y el minigráfico dibujado en F1 refleja exactamente ese patrón.

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

// Paso 4: Agregar un minigráfico Win/Loss (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);

// Paso 5: Personalizar el grupo de minigráficos
// Habilitar marcadores de punto alto y punto bajo
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Establecer el color del punto alto en verde
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);

// Establecer el color del punto bajo en rojo
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);

// Establecer el color del punto negativo en naranja
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);

// Establecer el color predeterminado de la serie (usado para barras positivas)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);

// Paso 6: Guardar el libro
workbook.save("output_winloss.xlsx");

console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Combinación de los tres tipos de minigráficos**

Los tres ejemplos anteriores producen cada uno su propio libro de trabajo para que los archivos de salida sean fáciles de inspeccionar de forma aislada. Sin embargo, en un escenario real, a menudo querrá comparar varias series de datos lado a lado. La forma más limpia de hacerlo es colocar más de un grupo de minigráficos en la misma hoja de cálculo, representando cada grupo un estilo diferente.

Puede añadir varios objetos `SparklineGroup` a la misma `SparklineGroupCollection`, y cada grupo puede tener como destino una celda de destino diferente o un rango diferente. Por ejemplo, podría colocar un minigráfico de línea en F1, un minigráfico de columna en F2 y un minigráfico de victoria/derrota en F3 — todos leyendo desde los mismos datos de origen en la fila 1 — de modo que el lector pueda ver tres tratamientos visuales diferentes de los mismos números.

El ejemplo combinado siguiente crea un único libro de trabajo, rellena la fila 1 con los valores 5, -3, 8, -2, 6 y luego añade tres grupos de minigráficos en las celdas F1, F2 y F3 — uno de cada tipo — de modo que el archivo resultante muestre los tres estilos de minigráficos a la vez.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Paso 2: Poblar datos de muestra en la fila 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Paso 3: Agregar un grupo de minigráficos de líneas en F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Personalizar el color del minigráfico de líneas mediante CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// Paso 4: Agregar un grupo de minigráficos de columnas en F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Personalizar el color de la serie del minigráfico de columnas
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// Paso 5: Agregar un grupo de minigráficos de victoria/derrota (apilados) en F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Personalizar el color de la serie del minigráfico de victoria/derrota
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// Paso 6: Guardar el libro
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

Cuando combina varios grupos de minigráficos en una sola hoja de cálculo, cada grupo es independiente. Pueden compartir el mismo rango de origen o usar rangos de origen diferentes, y se pueden estilizar de forma independiente. Esto facilita la creación de un pequeño "panel" de visualizaciones dentro de las celdas directamente dentro de una hoja de cálculo existente.

{{% /alert %}}

## **Personalización de la apariencia de los minigráficos**

Una vez que se ha creado un `SparklineGroup` y se ha añadido a `worksheet.SparklineGroups`, puede leer o modificar varias de sus propiedades visuales antes de guardar el libro de trabajo. Las propiedades más comúnmente personalizadas son:

- **`group.Type`** — el `SparklineType` (Línea, Columna o Apilado). Se establece cuando se añade el grupo, pero puede leerlo de nuevo para confirmarlo.
- **`group.Line.Color`** — el color de la línea, expresado como un `CellsColor` creado mediante `workbook.createCellsColor()`. Esta es la propiedad que se debe usar para el color del trazo del minigráfico de línea.
- **`group.Line.Weight`** — el grosor de la línea en puntos. Valores más altos producen líneas más gruesas.
- **Marcadores de puntos altos/bajos** — indicadores que activan pequeños marcadores en los puntos de datos más altos y más bajos, útiles para resaltar los extremos.
- **Marcadores de primer/último/punto negativo** — indicadores que activan o desactivan marcadores en el primer, último y negativo puntos de datos.

Para cambiar un color, siempre cree una instancia de `CellsColor` y asígnela a la propiedad correspondiente. No asigne un `java.awt.Color` directamente a las propiedades de color de los minigráficos — esperan el tipo `CellsColor` de `com.aspose.cells.Drawing`. El método `SparklineGroups.add` en sí mismo devuelve un objeto `SparklineGroup` completamente tipado, por lo que puede encadenar asignaciones de propiedades sobre el valor de retorno o almacenarlo en una variable local y personalizarlo antes de guardar.



{{< app/cells/assistant language="javascript" >}}