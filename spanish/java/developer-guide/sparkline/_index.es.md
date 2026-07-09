---
title: Minigráficos en Aspose.Cells para Aspose.Cells for Java
linktitle: Sparklines
description: Aspose.Cells es una biblioteca Java para trabajar con archivos de hojas de cálculo que admite la creación de minigráficos, pequeños gráficos colocados dentro de celdas de hojas de cálculo. Este artículo explica cómo agregar y personalizar minigráficos de línea, columna y victorias/derrotas utilizando la biblioteca Aspose.Cells.
keywords: Aspose.Cells, biblioteca Java, hoja de cálculo, minigráficos, minigráfico de línea, minigráfico de columna, minigráfico de victorias/derrotas, SparklineGroup, SparklineType
type: docs
weight: 195
url: /es/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la creación de minigráficos dentro de celdas de hojas de cálculo. Los minigráficos son pequeños gráficos que caben dentro de una sola celda, proporcionando una representación visual rápida de las tendencias de los datos. Aspose.Cells admite minigráficos de línea, columna y victorias/derrotas, y cada uno se puede personalizar en cuanto a color, grosor de línea, puntos altos/bajos y marcadores.

{{% /alert %}}

## **Introducción**

Los minigráficos son pequeños gráficos dentro de celdas que resultan útiles cuando se desea mostrar una tendencia rápida junto a una fila o columna de datos sin ocupar el espacio de un gráfico completo. Excel admite tres tipos de minigráficos: **línea**, **columna** y **victorias/derrotas**. Aspose.Cells replica esta funcionalidad a través de las APIs `SparklineGroup` y `SparklineGroupCollection` que se encuentran en el namespace `Aspose.Cells.Charts`.

En Aspose.Cells, cada minigráfico que agregue se crea mediante `worksheet.getSparklineGroups().add(...)`, que devuelve un objeto `SparklineGroup`. Luego puede usar ese objeto para establecer el tipo de minigráfico, el rango de datos, la celda de destino y propiedades visuales como el color de la línea, el grosor de la línea, los marcadores y los indicadores de puntos altos/bajos.

{{% alert color="primary" %}}

Un solo `SparklineGroup` puede contener uno o más minigráficos que comparten el mismo estilo. Cuando llama a `add` y pasa una fila de datos más una sola celda de destino, obtiene un minigráfico dentro de esa celda. Si su rango de destino es más ancho que una celda, se dibuja un minigráfico independiente en cada celda de destino, todos usando el mismo estilo y rango de datos.

{{% /alert %}}

Este artículo recorre cada uno de los tres tipos de minigráficos admitidos por Aspose.Cells — **Línea**, **Columna** y **Victorias/Derrotas** — y muestra cómo agregarlos, personalizar sus colores y guardar el libro resultante.

## **Minigráficos de Línea**

Un minigráfico de línea dibuja una línea continua a través de los puntos de datos en una serie, lo que lo convierte en la opción más natural para mostrar tendencias a lo largo del tiempo. En Aspose.Cells, un minigráfico de línea se crea pasando `SparklineType.LINE` al método `add`.

El flujo de trabajo es el mismo que para cualquier otro tipo de minigráfico:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene una fila de datos de origen (por ejemplo, fila 1, columnas A a E) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino donde se dibujará el minigráfico.
4. Llame a `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. El tercer argumento — `false` — indica a Aspose.Cells que el rango de datos es horizontal (una fila), no vertical (una columna).
5. Opcionalmente, personalice el `SparklineGroup` devuelto. Para un minigráfico de línea, puede establecer el color de la línea usando `group.getLine().setColor(...)` (que espera un `CellsColor` de `Aspose.Cells.Drawing`), ajustar el grosor de la línea y activar/desactivar los marcadores de puntos altos/bajos.
6. Guarde el libro.

El siguiente ejemplo crea un libro, escribe los valores 5, -3, 8, -2, 6 en las celdas A1 a E1, y agrega un minigráfico de línea en la celda F1 que traza esos valores. También personaliza el color de la línea a rojo y habilita marcadores para los puntos altos y bajos.

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

            // Paso 3: Construir un CellArea que apunte a la celda de destino F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // columna F (índice 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // fila 1 (índice 0)
            dest.EndRow = 0;

            // Paso 4: Agregar un mini-gráfico de línea desde A1:E1 en F1
            // SparklineGroups.add devuelve el índice del grupo recién agregado
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);

            // Paso 5: Crear un CellsColor rojo y asignarlo al color de la línea del mini-gráfico
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);

            // Paso 6: Habilitar los marcadores de punto alto y punto bajo
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);

            // Paso 7: Guardar el workbook
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## **Minigráficos de Columna**

Un minigráfico de columna representa cada punto de datos como una barra vertical. Esto lo hace muy adecuado para datos cuya magnitud es significativa — por ejemplo, cifras de ventas mensuales o conteos. En Aspose.Cells, crea un minigráfico de columna pasando `SparklineType.COLUMN` al método `add`.

El procedimiento refleja el ejemplo del minigráfico de línea:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el mismo rango de origen (A1:E1) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` resultante — por ejemplo, estableciendo `group.getType()` para confirmar el tipo, o ajustando el color de la barra.
6. Guarde el libro en un archivo de salida separado para que no sobrescriba el ejemplo del minigráfico de línea.

El ejemplo siguiente escribe los valores 5, -3, 8, -2, 6 en A1:E1 y renderiza un minigráfico de columna en F1. Los valores negativos se dibujan como barras que van hacia abajo y los valores positivos como barras que van hacia arriba, lo que facilita identificar de un vistazo las contribuciones positivas y negativas.

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

## **Minigráficos de Victorias/Derrotas**

Un minigráfico de victorias/derrotas es una variante especial del minigráfico de columna diseñado para mostrar solo dos resultados: un valor positivo se dibuja como una barra "hacia arriba" (una victoria) y un valor cero o negativo se dibuja como una barra "hacia abajo" (una derrota). Los minigráficos de victorias/derrotas se usan comúnmente para visualizar secuencias de victorias y derrotas, resultados de aprobado/desaprobado, o cualquier resultado binario a lo largo del tiempo.

En Aspose.Cells, un minigráfico de victorias/derrotas se crea pasando `SparklineType.STACKED` al método `add`. (A pesar del nombre, `SparklineType.STACKED` es el valor de enumeración usado para solicitar el renderizado de victorias/derrotas.)

El procedimiento es el mismo que para los otros dos tipos:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el rango de origen. Debido a que los minigráficos de victorias/derrotas tratan cada valor como una victoria o una derrota, la magnitud del valor no importa — solo su signo. Los valores positivos se convierten en barras hacia arriba y los valores no positivos se convierten en barras hacia abajo.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` devuelto, por ejemplo, estableciendo colores de acento para las barras de victoria y derrota.
6. Guarde el libro con un nombre de archivo distinto para que los tres ejemplos puedan coexistir en el disco.

El ejemplo siguiente usa los mismos datos de entrada que las dos secciones anteriores. Los valores 5, -3, 8, -2, 6 se interpretan como victoria, derrota, victoria, derrota, victoria — y el minigráfico dibujado en F1 refleja exactamente ese patrón.

```java
import com.aspose.cells.*;
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// Poblar datos de muestra
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Construir un CellArea apuntando a F1 (columna 5, fila 0)
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
seriesColor.setColor(new Color(70, 130, 180)); // aproximación de SteelBlue
group.setSeriesColor(seriesColor);

// Guardar el libro
workbook.save("output_winloss.xlsx");

System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **Combinando los Tres Tipos de Minigráficos**

Los tres ejemplos anteriores producen cada uno su propio libro para que los archivos de salida sean fáciles de inspeccionar de forma aislada. En un escenario del mundo real, sin embargo, a menudo querrá comparar varias series de datos lado a lado. La forma más limpia de hacerlo es colocar más de un grupo de minigráficos en la misma hoja de cálculo, con cada grupo renderizando un estilo diferente.

Puede agregar múltiples objetos `SparklineGroup` a la misma `SparklineGroupCollection`, y cada grupo puede tener como destino una celda de destino diferente o un rango diferente. Por ejemplo, podría colocar un minigráfico de línea en F1, un minigráfico de columna en F2 y un minigráfico de victorias/derrotas en F3 — todos leyendo de los mismos datos de origen en la fila 1 — para que el lector pueda ver tres tratamientos visuales diferentes de los mismos números.

El ejemplo combinado siguiente crea un único libro, rellena la fila 1 con los valores 5, -3, 8, -2, 6, y luego agrega tres grupos de minigráficos en las celdas F1, F2 y F3 — uno de cada tipo — para que el archivo resultante demuestre los tres estilos de minigráficos a la vez.

```java
import com.aspose.cells.*;

// Paso 1: Crear un Workbook y obtener la primera hoja de cálculo
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Paso 2: Poblar datos de muestra en la fila 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Paso 3: Agregar un grupo de minigráficos de línea en F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // Corrección: Usar el método de fábrica estático
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Personalizar el color del minigráfico de línea mediante CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// Paso 4: Agregar un grupo de minigráficos de columna en F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Corrección: Usar el método de fábrica estático
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Personalizar el color de la serie del minigráfico de columna
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// Paso 5: Agregar un grupo de minigráficos de Ganancia/Pérdida (Apilado) en F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Corrección: Usar el método de fábrica estático
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Personalizar el color de la serie del minigráfico de ganancia/pérdida
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// Paso 6: Guardar el workbook
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

Cuando combina múltiples grupos de minigráficos en una sola hoja de cálculo, cada grupo es independiente. Pueden compartir el mismo rango de origen o usar rangos de origen diferentes, y se pueden diseñar de forma independiente. Esto facilita la construcción de un pequeño "panel" de visualizaciones dentro de celdas directamente dentro de una hoja de cálculo existente.

{{% /alert %}}

## **Personalizando la Apariencia de los Minigráficos**

Una vez que se ha creado un `SparklineGroup` y se ha agregado a `worksheet.getSparklineGroups()`, puede leer o modificar varias de sus propiedades visuales antes de guardar el libro. Las propiedades más comúnmente personalizadas son:

- **`group.getType()`** — el `SparklineType` (LINE, COLUMN o STACKED). Se establece cuando se agrega el grupo, pero puede leerlo para confirmarlo.
- **`group.getLine().setColor(...)`** — el color de la línea, expresado como un `CellsColor` creado mediante `workbook.createCellsColor()`. Esta es la propiedad a usar para el color del trazo del minigráfico de línea.
- **`group.getLine().setWeight(...)`** — el grosor de la línea en puntos. Los valores más altos producen líneas más gruesas.
- **Marcadores de puntos altos/bajos** — indicadores que activan pequeños marcadores en los puntos de datos más altos y más bajos, útiles para enfatizar los extremos.
- **Marcadores de primer/último/punto negativo** — indicadores que activan/desactivan marcadores en el primer, último y puntos de datos negativos.

Para cambiar un color, siempre cree una instancia de `CellsColor` y asígnela a la propiedad correspondiente. No asigne un `java.awt.Color` directamente a las propiedades de color del minigráfico — esperan el tipo `CellsColor` de `Aspose.Cells.Drawing`. El método `add` en sí mismo devuelve un objeto `SparklineGroup` completamente tipado, por lo que puede encadenar asignaciones de propiedades en el valor de retorno o almacenarlo en una variable local y personalizarlo antes de guardar.



{{< app/cells/assistant language="java" >}}