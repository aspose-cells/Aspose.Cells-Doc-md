---
title: Minigráficos en Aspose.Cells for Python via Java
description: Aspose.Cells es una biblioteca Python via Java para trabajar con archivos de hojas de cálculo que admite la creación de minigráficos, es decir, gráficos en miniatura colocados dentro de celdas de la hoja de cálculo. Este artículo explica cómo agregar y personalizar minigráficos de líneas, columnas y victorias/derrotas utilizando la biblioteca Aspose.Cells.
linktitle: Minigráficos
keywords: Aspose.Cells, biblioteca Python via Java, hoja de cálculo, minigráficos, minigráfico de líneas, minigráfico de columnas, minigráfico de victorias/derrotas, SparklineGroup, SparklineType
type: docs
weight: 195
url: /es/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite la creación de minigráficos dentro de celdas de la hoja de cálculo. Los minigráficos son gráficos en miniatura que caben dentro de una sola celda y proporcionan una representación visual rápida de las tendencias de los datos. Aspose.Cells admite minigráficos de líneas, columnas y victorias/derrotas, y cada uno se puede personalizar en cuanto a color, grosor de línea, puntos altos/bajos y marcadores.

## **Introducción**
Los minigráficos son pequeños gráficos dentro de una celda que resultan útiles cuando se desea mostrar una tendencia rápida junto a una fila o columna de datos sin ocupar el espacio de un gráfico completo. Excel admite tres tipos de minigráficos: **de líneas**, **de columnas** y **de victorias/derrotas**. Aspose.Cells refleja esta capacidad a través de las API `SparklineGroup` y `SparklineGroupCollection` que se encuentran en el espacio de nombres `Aspose.Cells.Charts`.
En Aspose.Cells, cada minigráfico que agregue se crea mediante `worksheet.getSparklineGroups().add(...)`, que devuelve un objeto `SparklineGroup`. A continuación, puede utilizar ese objeto para establecer el tipo de minigráfico, el rango de datos, la celda de destino y propiedades visuales como el color de la línea, el grosor de la línea, los marcadores y los indicadores de puntos altos/bajos.
Este artículo recorre cada uno de los tres tipos de minigráficos admitidos por Aspose.Cells: **Líneas**, **Columnas** y **Victorias/Derrotas**, y muestra cómo agregarlos, personalizar sus colores y guardar el libro de trabajo resultante.

## **Minigráficos de líneas**
Un minigráfico de líneas dibuja una línea continua a través de los puntos de datos de una serie, lo que lo convierte en la opción más natural para mostrar tendencias a lo largo del tiempo. En Aspose.Cells, un minigráfico de líneas se crea pasando `SparklineType.LINE` al método `add`.
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene una fila de datos de origen (por ejemplo, fila 1, columnas A a E) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino donde se dibujará el minigráfico.
4. Llame a `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. El tercer argumento, `false`, indica an Aspose.Cells que el rango de datos es horizontal (una fila), no vertical (una columna).
5. Opcionalmente, personalice el `SparklineGroup` devuelto. Para un minigráfico de líneas puede establecer el color de la línea usando `group.getLine().getColor()` (que espera un `CellsColor` de `Aspose.Cells.Drawing`), ajustar el grosor de la línea y activar los marcadores de puntos altos/bajos.
6. Guarde el libro de trabajo.
El siguiente ejemplo crea un libro de trabajo, escribe los valores 5, -3, 8, -2, 6 en las celdas A1 a E1 y agrega un minigráfico de líneas en la celda F1 que traza esos valores. También personaliza el color de la línea a rojo y habilita los marcadores para los puntos altos y bajos.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Step 3: Add a Line sparkline group at F1
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)
# Customize the line sparkline color via CellsColor
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)
# Step 4: Add a Column sparkline group at F2
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)
# Customize the column sparkline series color
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)
# Step 5: Add a Win/Loss (Stacked) sparkline group at F3
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)
# Customize the win/loss sparkline series color
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # DarkOrange
stackedGroup.setSeriesColor(stackedColor)
# Step 6: Save the workbook
workbook.save("output_all.xlsx")
jpype.shutdownJVM()
```

## **Minigráficos de columnas**
Un minigráfico de columnas representa cada punto de datos como una barra vertical. Esto lo hace muy adecuado para datos cuya magnitud es significativa, por ejemplo, cifras de ventas mensuales o recuentos. En Aspose.Cells, se crea un minigráfico de columnas pasando `SparklineType.COLUMN` al método `add`.
El procedimiento refleja el ejemplo del minigráfico de líneas:
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` resultante; por ejemplo, estableciendo `group.getType()` para confirmar el tipo, o ajustando el color de las barras.
6. Guarde el libro de trabajo en un archivo de salida separado para que no sobrescriba el ejemplo del minigráfico de líneas.
El siguiente ejemplo escribe los valores 5, -3, 8, -2, 6 en A1:E1 y representa un minigráfico de columnas en F1. Los valores negativos se dibujan como barras que van hacia abajo y los valores positivos como barras que van hacia arriba, lo que permite distinguir fácilmente las contribuciones positivas y negativas de un vistazo.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType
# Paso 1: Crear un Workbook y obtener la primera hoja de trabajo
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Paso 2: Escribir valores de muestra en A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])
# Paso 3: Construir un CellArea apuntando a F1 (índice de columna 5, índice de fila 0)
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)
# Paso 4: Agregar un minigráfico de Columna a la celda de destino
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)
# Paso 5: Confirmar el tipo de minigráfico leyendo group.Type
print("Sparkline Type added: " + str(group.getType()))
# Paso 6: Guardar el libro
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
jpype.shutdownJVM()
```

## **Minigráficos de victorias/derrotas**
Un minigráfico de victorias/derrotas es una variante especial del minigráfico de columnas diseñado para mostrar solo dos resultados: un valor positivo se dibuja como una barra "hacia arriba" (una victoria) y un valor cero o negativo se dibuja como una barra "hacia abajo" (una derrota). Los minigráficos de victorias/derrotas se utilizan comúnmente para visualizar secuencias de victorias y derrotas, resultados de aprobado/suspenso o cualquier resultado binario a lo largo del tiempo.
En Aspose.Cells, un minigráfico de victorias/derrotas se crea pasando `SparklineType.STACKED` al método `add`. (A pesar del nombre, `SparklineType.STACKED` es el valor de enumeración utilizado para solicitar la representación de victorias/derrotas).
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el rango de origen. Dado que los minigráficos de victorias/derrotas tratan cada valor como una victoria o una derrota, la magnitud del valor no importa, solo su signo. Los valores positivos se convierten en barras hacia arriba y los valores no positivos en barras hacia abajo.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` devuelto, por ejemplo, estableciendo colores de acento para las barras de victoria y derrota.
6. Guarde el libro de trabajo con un nombre de archivo distinto para que los tres ejemplos puedan coexistir en disco.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # row 1
dest.setEndRow(0)
# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)
# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)
# Set the high-point color to green
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)
# Set the low-point color to red
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)
# Set the negative-point color to orange
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)
# Set the default series color (used for positive bars)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
jpype.shutdownJVM()
```

## **Combinación de los tres tipos de minigráficos**
El siguiente ejemplo combinado crea un único libro de trabajo, rellena la fila 1 con los valores 5, -3, 8, -2, 6 y luego agrega tres grupos de minigráficos en las celdas F1, F2 y F3 (uno de cada tipo), de modo que el archivo resultante demuestra los tres estilos de minigráficos a la vez.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = CellArea()
dest.setStartColumn(5)  # column F (0-indexed)
dest.setEndColumn(5)
dest.setStartRow(0)     # row 1 (0-indexed)
dest.setEndRow(0)
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.add returns the index of the newly added group
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)
# Step 6: Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
jpype.shutdownJVM()
```

## **Personalización de la apariencia de los minigráficos**
Una vez que se ha creado y agregado un `SparklineGroup` a `worksheet.getSparklineGroups()`, puede leer o modificar varias de sus propiedades visuales antes de guardar el libro de trabajo. Las propiedades más comúnmente personalizadas son:
- **`group.getType()`**: el `SparklineType` (LINE, COLUMN o STACKED). Se establece cuando se agrega el grupo, pero puede leerlo de nuevo para confirmarlo.
- **`group.getLine().getColor()`**: el color de la línea, expresado como un `CellsColor` creado mediante `workbook.createCellsColor()`. Esta es la propiedad que se debe usar para el color del trazo del minigráfico de líneas.
- **`group.getLine().getWeight()`**: el grosor de la línea en puntos. Los valores más altos producen líneas más gruesas.
- **Marcadores de puntos altos/bajos**: indicadores que activan pequeños marcadores en los puntos de datos más altos y más bajos, útiles para resaltar los extremos.
- **Marcadores de puntos primero/último/negativo**: indicadores que activan o desactivan marcadores en los puntos de datos primero, último y negativo.
Para cambiar un color, cree siempre una instancia de `CellsColor` y asígnela a la propiedad correspondiente. No asigne un `java.awt.Color` directamente a las propiedades de color del minigráfico, ya que esperan el tipo `CellsColor` de `Aspose.Cells.Drawing`. El método `add` en sí mismo devuelve un objeto `SparklineGroup` completamente tipado, por lo que puede encadenar asignaciones de propiedades sobre el valor de retorno o almacenarlo en una variable local y personalizarlo antes de guardar.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}