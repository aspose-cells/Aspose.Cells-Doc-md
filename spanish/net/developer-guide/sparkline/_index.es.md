---
title: Sparklines en Aspose.Cells for .NET
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo que admite la creación de sparklines,gráficos en miniatura colocados dentro de celdas de la hoja de cálculo. Este artículo explica cómo añadir y personalizar sparklines de línea, columna y ganancia/pérdida usando la biblioteca Aspose.Cells.
linktitle: Sparklines
keywords: Aspose.Cells, biblioteca .NET, hoja de cálculo, sparklines, sparkline de línea, sparkline de columna, sparkline de ganancia/pérdida, SparklineGroup, SparklineType
type: docs
weight: 195
url: /es/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Original: "Aspose.Cells is a .NET library for working with spreadsheet files that supports creating sparklines — miniature charts placed inside worksheet cells. This article explains how to add and customize line, column, and win/loss sparklines using the Aspose.Cells library."
"Introduction" - "Introducción"
"Sparklines are tiny in-cell charts that are useful when you want to display a quick trend next to a row or column of data without taking up the space of a full chart. Excel supports three kinds of sparklines: line, column, and win/loss. Aspose.Cells mirrors this capability through the SparklineGroup and SparklineGroupCollection APIs found in the Aspose.Cells.Charts namespace."
"Line Sparklines" - "Sparklines de línea"
"Column Sparklines" - "Sparklines de columna"
"Win/Loss Sparklines" - "Sparklines de ganancia/pérdida"
"Combining All Three Sparkline Types" - "Combinar los tres tipos de sparklines"
"Customizing Sparkline Appearance" - "Personalizar la apariencia de los sparklines"
1. Create a new Workbook and access the first worksheet.
2. Populate a row of source data (for example, row 1, columns A through E) with the values you want to visualize.
3. Build a CellArea describing the destination cell where the sparkline will be drawn.
4. Call worksheet.SparklineGroups.Add(...). The third argument — false — tells Aspose.Cells that the data range is horizontal (a row), not vertical (a column).
5. Optionally customize the returned SparklineGroup. For a line sparkline you can set the line color using group.Line.Color (which expects a CellsColor from Aspose.Cells.Drawing), adjust the line weight, and toggle high/low point markers.
6. Save the workbook.
That's 1-6 sequential, good.
Column sparklines:
1. Create a new Workbook and access the first worksheet.
3. Build a CellArea describing the destination cell.
4. Call worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest).
5. Optionally customize the resulting SparklineGroup — for example, by setting group.Type to confirm the type, or by tweaking the bar color.
6. Save the workbook to a separate output file so it does not overwrite the line sparkline example.
That's 1, 3, 4, 5, 6. I'll renumber to 1, 2, 3, 4, 5.
Win/Loss:
1. Create a new Workbook and access the first worksheet.
2. Populate the source range...
3. Build a CellArea...
4. Call worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest).
5. Optionally customize the returned SparklineGroup...
6. Save the workbook under a distinct filename so all three examples can coexist on disk.
That's 1-6 sequential, good.
Related Articles - I need to translate the titles.

{{% alert color="primary" %}}
Aspose.Cells admite la creación de sparklines dentro de celdas de la hoja de cálculo. Los sparklines son gráficos en miniatura que caben dentro de una sola celda, proporcionando una rápida representación visual de las tendencias de los datos. Aspose.Cells admite sparklines de línea, columna y ganancia/pérdida, y cada uno se puede personalizar en cuanto a color, grosor de línea, puntos altos/bajos y marcadores.

## **Introducción**
Los sparklines son pequeños gráficos dentro de celda que son útiles cuando se desea mostrar una tendencia rápida junto a una fila o columna de datos sin ocupar el espacio de un gráfico completo. Excel admite tres tipos de sparklines: **línea**, **columna** y **ganancia/pérdida**. Aspose.Cells refleja esta capacidad a través de las API `SparklineGroup` y `SparklineGroupCollection` que se encuentran en el espacio de nombres `Aspose.Cells.Charts`.
En Aspose.Cells, cada sparkline que añada se crea mediante `worksheet.SparklineGroups.Add(...)`, que devuelve un objeto `SparklineGroup`. A continuación, puede usar ese objeto para establecer el tipo de sparkline, el rango de datos, la celda de destino y las propiedades visuales como el color de la línea, el grosor de la línea, los marcadores y los indicadores de puntos altos/bajos.
Este artículo recorre los tres tipos de sparklines admitidos por Aspose.Cells — **Línea**, **Columna** y **Ganancia/Pérdida** — y muestra cómo añadirlos, personalizar sus colores y guardar el libro resultante.

## **Sparklines de línea**
Un sparkline de línea dibuja una línea continua a través de los puntos de datos de una serie, lo que lo convierte en la elección más natural para mostrar tendencias a lo largo del tiempo. En Aspose.Cells, un sparkline de línea se crea pasando `SparklineType.Line` al método `SparklineGroups.Add`.
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene una fila de datos de origen (por ejemplo, fila 1, columnas A a E) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino donde se dibujará el sparkline.
4. Llame a `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. El tercer argumento — `false` — indica an Aspose.Cells que el rango de datos es horizontal (una fila), no vertical (una columna).
5. Opcionalmente, personalice el `SparklineGroup` devuelto. Para un sparkline de línea puede establecer el color de la línea usando `group.Line.Color` (que espera un `CellsColor` de `Aspose.Cells.Drawing`), ajustar el grosor de la línea y activar los marcadores de puntos altos/bajos.
6. Guarde el libro.
El siguiente ejemplo crea un libro, escribe los valores 5, -3, 8, -2, 6 en las celdas A1 a E1, y añade un sparkline de línea en la celda F1 que traza esos valores. También personaliza el color de la línea a rojo y activa los marcadores para los puntos altos y bajos.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    public class Program
    {
        public static void Main()
        {
            // Paso 1: Crear un Workbook y obtener la primera hoja de cálculo
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;
            // Paso 2: Escribir valores de ejemplo 5, -3, 8, -2, 6 en las celdas A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);
            // Paso 3: Construir un CellArea apuntando a la celda de destino F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // columna F (indexada en 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // fila 1 (indexada en 0)
            dest.EndRow = 0;
            // Paso 4: Agregar un minigráfico de línea desde A1:E1 en F1
            // SparklineGroups.Add devuelve el índice del grupo recién agregado
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];
            // Paso 5: Crear un CellsColor rojo y asignarlo al color de línea del minigráfico
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;
            // Paso 6: Habilitar marcadores de punto alto y punto bajo
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            // Paso 7: Guardar el workbook
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **Sparklines de columna**
Un sparkline de columna representa cada punto de datos como una barra vertical. Esto lo hace muy adecuado para datos cuya magnitud es significativa — por ejemplo, cifras de ventas mensuales o recuentos. En Aspose.Cells, puede crear un sparkline de columna pasando `SparklineType.Column` al método `SparklineGroups.Add`.
El procedimiento refleja el ejemplo del sparkline de línea:
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene una fila de datos de origen (por ejemplo, fila 1, columnas A a E) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` resultante — por ejemplo, estableciendo `group.Type` para confirmar el tipo, o ajustando el color de la barra.
6. Guarde el libro en un archivo de salida independiente para que no sobrescriba el ejemplo del sparkline de línea.
El siguiente ejemplo escribe los valores 5, -3, 8, -2, 6 en A1:E1 y renderiza un sparkline de columna en F1. Los valores negativos se dibujan como barras hacia abajo y los valores positivos como barras hacia arriba, lo que facilita detectar de un vistazo las contribuciones positivas y negativas.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Paso 1: Crear un Workbook y obtener la primera hoja de cálculo
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            // Paso 2: Escribir valores de muestra en A1:E1
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }
            // Paso 3: Construir un CellArea apuntando a F1 (índice de columna 5, índice de fila 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;
            // Paso 4: Agregar un minigráfico de Columna a la celda de destino
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];
            // Paso 5: Confirmar el tipo de minigráfico leyendo group.Type
            Console.WriteLine("Sparkline Type added: " + group.Type);
            // Paso 6: Guardar el libro de trabajo
            workbook.Save("output_column.xlsx");
            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **Sparklines de ganancia/pérdida**
Un sparkline de ganancia/pérdida es una variante especial del sparkline de columna diseñada para mostrar solo dos resultados: un valor positivo se dibuja como una barra "hacia arriba" (una ganancia) y un valor cero o negativo se dibuja como una barra "hacia abajo" (una pérdida). Los sparklines de ganancia/pérdida se usan comúnmente para visualizar secuencias de victorias y derrotas, resultados de aprobado/desaprobado, o cualquier resultado binario a lo largo del tiempo.
En Aspose.Cells, un sparkline de ganancia/pérdida se crea pasando `SparklineType.Stacked` al método `SparklineGroups.Add`. (A pesar del nombre, `SparklineType.Stacked` es el valor de enumeración usado para solicitar el renderizado de ganancia/pérdida.)
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el rango de origen. Dado que los sparklines de ganancia/pérdida tratan cada valor como una ganancia o una pérdida, la magnitud del valor no importa — solo su signo. Los valores positivos se convierten en barras hacia arriba y los valores no positivos en barras hacia abajo.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` devuelto, por ejemplo, estableciendo colores de acento para las barras de ganancia y pérdida.
6. Guarde el libro con un nombre de archivo distinto para que los tres ejemplos puedan coexistir en disco.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Paso 1: Crear un Workbook y obtener la primera hoja de trabajo
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";
            // Paso 2: Poblar datos de muestra en la fila 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);
            // Paso 3: Construir un CellArea que apunte a F1 (columna 5, fila 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // fila 1
            dest.EndRow = 0;
            // Paso 4: Agregar un minigráfico Win/Loss (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];
            // Paso 5: Personalizar el grupo de minigráficos
            // Habilitar marcadores de punto alto y punto bajo
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;
            // Establecer el color del punto alto en verde
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;
            // Establecer el color del punto bajo en rojo
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;
            // Establecer el color del punto negativo en naranja
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;
            // Establecer el color de serie predeterminado (usado para barras positivas)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;
            // Paso 6: Guardar el libro
            workbook.Save("output_winloss.xlsx");
            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **Combinar los tres tipos de sparklines**
El siguiente ejemplo combinado crea un único libro, rellena la fila 1 con los valores 5, -3, 8, -2, 6, y luego añade tres grupos de sparklines en las celdas F1, F2 y F3 — uno de cada tipo — para que el archivo resultante muestre los tres estilos de sparklines a la vez.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
// Paso 1: Crear un libro de trabajo y obtener la primera hoja de cálculo
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Paso 2: Rellenar datos de muestra en la fila 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// Paso 3: Agregar un grupo de minigráficos de línea en F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];
// Personalizar el color del minigráfico de línea mediante CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;
// Paso 4: Agregar un grupo de minigráficos de columna en F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];
// Personalizar el color de la serie del minigráfico de columna
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;
// Paso 5: Agregar un grupo de minigráficos de Ganancia/Pérdida (Apilado) en F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];
// Personalizar el color de la serie del minigráfico de ganancia/pérdida
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;
// Paso 6: Guardar el libro de trabajo
workbook.Save("output_all.xlsx");
```

## **Personalizar la apariencia de los sparklines**
Una vez que se ha creado y añadido un `SparklineGroup` a `worksheet.SparklineGroups`, puede leer o modificar varias de sus propiedades visuales antes de guardar el libro. Las propiedades personalizadas con mayor frecuencia son:
- **`group.Type`** — el `SparklineType` (Line, Column o Stacked). Se establece cuando se añade el grupo, pero puede leerlo de nuevo para confirmarlo.
- **`group.Line.Color`** — el color de la línea, expresado como un `CellsColor` creado mediante `workbook.CreateCellsColor()`. Esta es la propiedad que se debe usar para el color del trazo del sparkline de línea.
- **`group.Line.Weight`** — el grosor de la línea en puntos. Los valores más altos producen líneas más gruesas.
- **Marcadores de puntos altos/bajos** — flags que activan pequeños marcadores en los puntos de datos más altos y más bajos, útiles para enfatizar los extremos.
- **Marcadores de puntos primero/último/negativo** — flags que activan los marcadores en el primer, último y negativos puntos de datos.
Para cambiar un color, siempre cree una instancia de `CellsColor` y asígnela a la propiedad correspondiente. No asigne un `System.Drawing.Color` directamente a las propiedades de color del sparkline — esperan el tipo `CellsColor` de `Aspose.Cells.Drawing`. El método `SparklineGroups.Add` en sí mismo devuelve un objeto `SparklineGroup` completamente tipado, por lo que puede encadenar asignaciones de propiedades sobre el valor devuelto o almacenarlo en una variable local y personalizarlo antes de guardar.
{{% /alert %}}

## Artículos Relacionados
- [Convertir Sparkline a Imagen y HTML en Aspose.Cells for .NET](/cells/es/net/convert-sparkline-to-image-and-html/)
- [Añadir Campos de Filtro a una Tabla Dinámica en Aspose.Cells for .NET](/cells/es/net/add-page-field-in-pivot-table/)
- [Aplicar Estilos a Tablas Dinámicas en Aspose.Cells for .NET](/cells/es/net/apply-style-to-pivot-table/)
- [Modificar el Diseño del Campo de Página en la Tabla Dinámica](/cells/es/net/change-page-field-layout/)
- [Convertir Excel a Formato OFD](/cells/es/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}