---
title: Minigráficos en Aspose.Cells for .NET
linktitle: Sparklines
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo que admite la creación de minigráficos: pequeños gráficos colocados dentro de las celdas de la hoja de cálculo. Este artículo explica cómo agregar y personalizar minigráficos de línea, columna y ganancia/pérdida usando la biblioteca Aspose.Cells.
keywords: Aspose.Cells, biblioteca .NET, hoja de cálculo, minigráficos, minigráfico de línea, minigráfico de columna, minigráfico de ganancia/pérdida, SparklineGroup, SparklineType
type: docs
weight: 195
url: /es/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la creación de minigráficos dentro de las celdas de la hoja de cálculo. Los minigráficos son pequeños gráficos que caben dentro de una sola celda, proporcionando una representación visual rápida de las tendencias de los datos. Aspose.Cells admite minigráficos de línea, columna y ganancia/pérdida, y cada uno se puede personalizar en cuanto a color, grosor de línea, puntos altos/bajos y marcadores.

{{% /alert %}}

## **Introducción**

Los minigráficos son pequeños gráficos dentro de celdas que resultan útiles cuando se desea mostrar una tendencia rápida junto a una fila o columna de datos sin ocupar el espacio de un gráfico completo. Excel admite tres tipos de minigráficos: **línea**, **columna** y **ganancia/pérdida**. Aspose.Cells refleja esta capacidad a través de las API `SparklineGroup` y `SparklineGroupCollection` que se encuentran en el espacio de nombres `Aspose.Cells.Charts`.

En Aspose.Cells, cada minigráfico que se agrega se crea mediante `worksheet.SparklineGroups.Add(...)`, que devuelve un objeto `SparklineGroup`. A continuación, puede usar ese objeto para establecer el tipo de minigráfico, el rango de datos, la celda de destino y propiedades visuales como el color de la línea, el grosor de la línea, los marcadores y los indicadores de puntos altos/bajos.

{{% alert color="primary" %}}

Un solo `SparklineGroup` puede contener uno o más minigráficos que comparten el mismo estilo. Cuando llama a `Add` y pasa una fila de datos más una sola celda de destino, obtiene un minigráfico dentro de esa celda. Si su rango de destino es más ancho que una celda, se dibuja un minigráfico separado en cada celda de destino, todos usando el mismo estilo y rango de datos.

{{% /alert %}}

Este artículo recorre cada uno de los tres tipos de minigráficos admitidos por Aspose.Cells — **Línea**, **Columna** y **Ganancia/Pérdida** — y muestra cómo agregarlos, personalizar sus colores y guardar el libro de trabajo resultante.

## **Minigráficos de línea**

Un minigráfico de línea dibuja una línea continua a través de los puntos de datos en una serie, lo que lo convierte en la opción más natural para mostrar tendencias a lo largo del tiempo. En Aspose.Cells, un minigráfico de línea se crea pasando `SparklineType.Line` al método `SparklineGroups.Add`.

El flujo de trabajo es el mismo que para cualquier otro tipo de minigráfico:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene una fila de datos de origen (por ejemplo, fila 1, columnas A a E) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino donde se dibujará el minigráfico.
4. Llame a `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. El tercer argumento — `false` — indica a Aspose.Cells que el rango de datos es horizontal (una fila), no vertical (una columna).
5. Opcionalmente personalice el `SparklineGroup` devuelto. Para un minigráfico de línea puede establecer el color de la línea usando `group.Line.Color` (que espera un `CellsColor` de `Aspose.Cells.Drawing`), ajustar el grosor de la línea y activar/desactivar los marcadores de puntos altos/bajos.
6. Guarde el libro de trabajo.

El siguiente ejemplo crea un libro de trabajo, escribe los valores 5, -3, 8, -2, 6 en las celdas A1 a E1, y agrega un minigráfico de línea en la celda F1 que traza esos valores. También personaliza el color de la línea a rojo y activa los marcadores para los puntos altos y bajos.

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
            // Paso 1: Crear un Workbook y obtener la primera hoja de trabajo
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;

            // Paso 2: Escribir los valores de muestra 5, -3, 8, -2, 6 en las celdas A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);

            // Paso 3: Construir un CellArea que apunte a la celda de destino F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // columna F (indexada desde 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // fila 1 (indexada desde 0)
            dest.EndRow = 0;

            // Paso 4: Agregar un minigráfico de línea desde A1:E1 en F1
            // SparklineGroups.Add devuelve el índice del grupo recién agregado
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];

            // Paso 5: Crear un CellsColor rojo y asignarlo al color de la línea del minigráfico
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;

            // Paso 6: Habilitar los marcadores de punto alto y punto bajo
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;

            // Paso 7: Guardar el libro
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **Minigráficos de columna**

Un minigráfico de columna representa cada punto de datos como una barra vertical. Esto lo hace muy adecuado para datos cuya magnitud es significativa — por ejemplo, cifras de ventas mensuales o conteos. En Aspose.Cells, crea un minigráfico de columna pasando `SparklineType.Column` al método `SparklineGroups.Add`.

El procedimiento refleja el ejemplo del minigráfico de línea:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el mismo rango de origen (A1:E1) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. Opcionalmente personalice el `SparklineGroup` resultante — por ejemplo, estableciendo `group.Type` para confirmar el tipo, o ajustando el color de la barra.
6. Guarde el libro de trabajo en un archivo de salida separado para que no sobrescriba el ejemplo del minigráfico de línea.

El ejemplo siguiente escribe los valores 5, -3, 8, -2, 6 en A1:E1 y representa un minigráfico de columna en F1. Los valores negativos se dibujan como barras que van hacia abajo y los valores positivos como barras que van hacia arriba, lo que facilita identificar de un vistazo las contribuciones positivas y negativas.

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

            // Paso 3: Construir un CellArea que apunte a F1 (índice de columna 5, índice de fila 0)
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

            // Paso 6: Guardar el workbook
            workbook.Save("output_column.xlsx");

            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **Minigráficos de ganancia/pérdida**

Un minigráfico de ganancia/pérdida es una variante especial del minigráfico de columna diseñado para mostrar solo dos resultados: un valor positivo se dibuja como una barra "arriba" (una ganancia) y un valor cero o negativo se dibuja como una barra "abajo" (una pérdida). Los minigráficos de ganancia/pérdida se usan comúnmente para visualizar secuencias de victorias y derrotas, resultados de aprobado/desaprobado, o cualquier resultado binario a lo largo del tiempo.

En Aspose.Cells, un minigráfico de ganancia/pérdida se crea pasando `SparklineType.Stacked` al método `SparklineGroups.Add`. (A pesar del nombre, `SparklineType.Stacked` es el valor de enumeración utilizado para solicitar el renderizado de ganancia/pérdida.)

El procedimiento es el mismo que para los otros dos tipos:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el rango de origen. Debido a que los minigráficos de ganancia/pérdida tratan cada valor como una ganancia o una pérdida, la magnitud del valor no importa — solo su signo. Los valores positivos se convierten en barras hacia arriba y los valores no positivos se convierten en barras hacia abajo.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Opcionalmente personalice el `SparklineGroup` devuelto, por ejemplo estableciendo colores de acento para las barras de ganancia y pérdida.
6. Guarde el libro de trabajo bajo un nombre de archivo distinto para que los tres ejemplos puedan coexistir en disco.

El ejemplo siguiente utiliza los mismos datos de entrada que las dos secciones anteriores. Los valores 5, -3, 8, -2, 6 se interpretan como ganancia, pérdida, ganancia, pérdida, ganancia — y el minigráfico dibujado en F1 refleja exactamente ese patrón.

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

            // Paso 2: Rellenar datos de muestra en la fila 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
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

            // Paso 6: Guardar el libro de trabajo
            workbook.Save("output_winloss.xlsx");

            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **Combinación de los tres tipos de minigráficos**

Los tres ejemplos anteriores producen cada uno su propio libro de trabajo para que los archivos de salida sean fáciles de inspeccionar de forma aislada. En un escenario del mundo real, sin embargo, a menudo querrá comparar varias series de datos lado a lado. La forma más limpia de hacerlo es colocar más de un grupo de minigráficos en la misma hoja de cálculo, con cada grupo representando un estilo diferente.

Puede agregar varios objetos `SparklineGroup` a la misma `SparklineGroupCollection`, y cada grupo puede tener como destino una celda de destino diferente o un rango diferente. Por ejemplo, podría colocar un minigráfico de línea en F1, un minigráfico de columna en F2, y un minigráfico de ganancia/pérdida en F3 — todos leyendo desde los mismos datos de origen en la fila 1 — para que el lector pueda ver tres tratamientos visuales diferentes de los mismos números.

El ejemplo combinado siguiente crea un único libro de trabajo, rellena la fila 1 con los valores 5, -3, 8, -2, 6, y luego agrega tres grupos de minigráficos en las celdas F1, F2 y F3 — uno de cada tipo — para que el archivo resultante demuestre los tres estilos de minigráficos a la vez.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;

// Paso 1: Crear un Workbook y obtener la primera hoja de cálculo
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Paso 2: Poblar datos de muestra en la fila 1 (A1:E1)
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

// Paso 6: Guardar el workbook
workbook.Save("output_all.xlsx");
```

{{% alert color="primary" %}}

Cuando combina varios grupos de minigráficos en una sola hoja de cálculo, cada grupo es independiente. Pueden compartir el mismo rango de origen o usar rangos de origen diferentes, y se pueden estilizar de forma independiente. Esto facilita la creación de un pequeño "panel" de visualizaciones dentro de celdas directamente dentro de una hoja de cálculo existente.

{{% /alert %}}

## **Personalización de la apariencia de los minigráficos**

Una vez que se ha creado un `SparklineGroup` y se ha agregado a `worksheet.SparklineGroups`, puede leer o modificar varias de sus propiedades visuales antes de guardar el libro de trabajo. Las propiedades personalizadas con más frecuencia son:

- **`group.Type`** — el `SparklineType` (Line, Column o Stacked). Se establece cuando se agrega el grupo, pero puede leerlo de nuevo para confirmarlo.
- **`group.Line.Color`** — el color de la línea, expresado como un `CellsColor` creado mediante `workbook.CreateCellsColor()`. Esta es la propiedad que se debe usar para el color del trazo del minigráfico de línea.
- **`group.Line.Weight`** — el grosor de la línea en puntos. Los valores más altos producen líneas más gruesas.
- **Marcadores de puntos altos/bajos** — flags que activan pequeños marcadores en los puntos de datos más altos y más bajos, útiles para enfatizar los extremos.
- **Marcadores de puntos primero/último/negativo** — flags que alternan los marcadores en los puntos de datos primero, último y negativo.

Para cambiar un color, siempre cree una instancia de `CellsColor` y asígnela a la propiedad correspondiente. No asigne un `System.Drawing.Color` directamente a las propiedades de color del minigráfico — esperan el tipo `CellsColor` de `Aspose.Cells.Drawing`. El método `SparklineGroups.Add` en sí mismo devuelve un objeto `SparklineGroup` completamente tipado, por lo que puede encadenar asignaciones de propiedades en el valor de retorno o almacenarlo en una variable local y personalizarlo antes de guardar.

## **Artículos relacionados**

- [Acceso a las celdas de una hoja de cálculo](/cells/es/net/accessing-cells-of-a-worksheet/)
- [Formato de celdas de hoja de cálculo en un libro de trabajo](/cells/es/net/format-worksheet-cells-in-a-workbook/)
- [Personalización de gráficos](/cells/es/net/customizing-charts/)
- [Crear gráficos dinámicos](/cells/es/net/create-dynamic-charts/)
- [Administrar datos de archivos Excel](/cells/es/net/cells-data/)

{{< app/cells/assistant language="csharp" >}}