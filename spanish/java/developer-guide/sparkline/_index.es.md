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
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // Paso 1: Crear un Workbook y obtener la primera hoja de trabajo
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();
            // Paso 2: Escribir valores de muestra 5, -3, 8, -2, 6 en las celdas A1:E1
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);
            // Paso 3: Construir un CellArea apuntando a la celda destino F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // columna F (índice basado en 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // fila 1 (índice basado en 0)
            dest.EndRow = 0;
            // Paso 4: Agregar un mini-gráfico de línea desde A1:E1 en F1
            // SparklineGroups.add devuelve el índice del grupo recién agregado
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);
            // Paso 5: Crear un CellsColor rojo y asignarlo al color de la línea del mini-gráfico
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);
            // Paso 6: Habilitar marcadores de punto alto y punto bajo
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);
            // Paso 7: Guardar el libro de trabajo
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
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
// Escribir valores de muestra en A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Construir un CellArea que apunte a F1 (índice de columna 5, índice de fila 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Agregar un minigráfico de columna a la celda de destino
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);
// Confirmar el tipo de minigráfico leyendo group.Type
System.out.println("Sparkline Type added: " + group.getType());
// Guardar el libro de trabajo
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
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Llenar datos de muestra
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Construir un CellArea que apunte a F1 (columna 5, fila 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Agregar un minigráfico de Ganancia/Pérdida (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);
// Personalizar el grupo de minigráficos
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Establecer el color del punto alto a verde
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);
// Establecer el color del punto bajo a rojo
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);
// Establecer el color del punto negativo a naranja
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);
// Establecer el color predeterminado de la serie (usado para barras positivas)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // Aproximación de SteelBlue
group.setSeriesColor(seriesColor);
// Guardar el libro de trabajo
workbook.save("output_winloss.xlsx");
System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **Combinación de los tres tipos de sparklines**
El siguiente ejemplo combinado crea un único libro de trabajo, rellena la fila 1 con los valores 5, -3, 8, -2, 6 y, a continuación, añade tres grupos de sparklines en las celdas F1, F2 y F3 — uno de cada tipo — para que el archivo resultante demuestre los tres estilos de sparklines a la vez.

```java
import com.aspose.cells.*;
// Paso 1: Crear un Workbook y obtener la primera hoja de trabajo
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Paso 2: Poblar datos de muestra en la fila 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Paso 3: Agregar un grupo de minigráficos de línea en F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // Corrección: Usar método de fábrica estática
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Personalizar el color del minigráfico de línea mediante CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Paso 4: Agregar un grupo de minigráficos de columna en F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Corrección: Usar método de fábrica estática
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Personalizar el color de la serie del minigráfico de columna
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Paso 5: Agregar un grupo de minigráficos de Ganancia/Pérdida (Apilados) en F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Corrección: Usar método de fábrica estática
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Personalizar el color de la serie del minigráfico de ganancia/pérdida
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Paso 6: Guardar el workbook
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
{{% /alert %}}

{{< app/cells/assistant language="java" >}}