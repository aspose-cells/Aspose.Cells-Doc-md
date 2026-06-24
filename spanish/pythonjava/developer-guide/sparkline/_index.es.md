---
title: Minigráficos en Aspose.Cells for Python via Java
linktitle: Sparklines
description: Aspose.Cells es una biblioteca de Python via Java para trabajar con archivos de hojas de cálculo que admite la creación de minigráficos: gráficos en miniatura colocados dentro de celdas de hojas de cálculo. Este artículo explica cómo añadir y personalizar minigráficos de líneas, columnas y victorias/derrotas usando la biblioteca Aspose.Cells.
keywords: Aspose.Cells, biblioteca de Python via Java, hoja de cálculo, minigráficos, minigráfico de líneas, minigráfico de columnas, minigráfico de victorias/derrotas, SparklineGroup, SparklineType
type: docs
weight: 195
url: /es/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la creación de minigráficos dentro de celdas de hojas de cálculo. Los minigráficos son gráficos en miniatura que caben dentro de una sola celda, proporcionando una representación visual rápida de las tendencias de los datos. Aspose.Cells admite minigráficos de líneas, columnas y victorias/derrotas, y cada uno puede personalizarse en cuanto a color, grosor de línea, puntos altos/bajos y marcadores.

{{% /alert %}}

## **Introducción**

Los minigráficos son pequeños gráficos dentro de celdas que resultan útiles cuando se desea mostrar una tendencia rápida junto a una fila o columna de datos sin ocupar el espacio de un gráfico completo. Excel admite tres tipos de minigráficos: **líneas**, **columnas** y **victorias/derrotas**. Aspose.Cells refleja esta capacidad a través de las API `SparklineGroup` y `SparklineGroupCollection` que se encuentran en el espacio de nombres `Aspose.Cells.Charts`.

En Aspose.Cells, cada minigráfico que añada se crea mediante `worksheet.getSparklineGroups().add(...)`, que devuelve un objeto `SparklineGroup`. A continuación, puede usar ese objeto para establecer el tipo de minigráfico, el rango de datos, la celda de destino y propiedades visuales como el color de la línea, el grosor de la línea, los marcadores y los indicadores de puntos altos/bajos.

{{% alert color="primary" %}}

Un solo `SparklineGroup` puede contener uno o varios minigráficos que comparten el mismo estilo. Cuando llama a `add` y pasa una fila de datos más una sola celda de destino, obtiene un minigráfico dentro de esa celda. Si su rango de destino es más ancho que una celda, se dibuja un minigráfico independiente en cada celda de destino, todos usando el mismo estilo y rango de datos.

{{% /alert %}}

Este artículo repasa cada uno de los tres tipos de minigráficos admitidos por Aspose.Cells — **Línea**, **Columna** y **Victoria/Derrota** — y muestra cómo añadirlos, personalizar sus colores y guardar el libro de trabajo resultante.

## **Minigráficos de líneas**

Un minigráfico de líneas dibuja una línea continua a través de los puntos de datos de una serie, lo que lo convierte en la opción más natural para mostrar tendencias a lo largo del tiempo. En Aspose.Cells, un minigráfico de líneas se crea pasando `SparklineType.LINE` al método `add`.

El flujo de trabajo es el mismo que para cualquier otro tipo de minigráfico:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene una fila de datos de origen (por ejemplo, fila 1, columnas A a E) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino donde se dibujará el minigráfico.
4. Llame a `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. El tercer argumento — `false` — indica a Aspose.Cells que el rango de datos es horizontal (una fila), no vertical (una columna).
5. Opcionalmente, personalice el `SparklineGroup` devuelto. Para un minigráfico de líneas puede establecer el color de la línea usando `group.getLine().getColor()` (que espera un `CellsColor` de `Aspose.Cells.Drawing`), ajustar el grosor de la línea y activar o desactivar los marcadores de los puntos altos y bajos.
6. Guarde el libro de trabajo.

El siguiente ejemplo crea un libro de trabajo, escribe los valores 5, -3, 8, -2, 6 en las celdas A1 a E1, y añade un minigráfico de líneas en la celda F1 que traza esos valores. También personaliza el color de la línea a rojo y activa los marcadores para los puntos altos y bajos.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color

# Paso 1: Crear un Workbook y obtener la primera hoja de cálculo
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()

# Paso 2: Escribir los valores de muestra 5, -3, 8, -2, 6 en las celdas A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)

# Paso 3: Construir un CellArea que apunte a la celda de destino F1
dest = CellArea()
dest.setStartColumn(5)  # columna F (índice 0)
dest.setEndColumn(5)
dest.setStartRow(0)     # fila 1 (índice 0)
dest.setEndRow(0)

# Paso 4: Agregar un minigráfico de tipo Línea desde A1:E1 en F1
# SparklineGroups.add devuelve el índice del grupo recién agregado
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)

# Paso 5: Crear un CellsColor rojo y asignarlo al color de línea del minigráfico
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)

# Paso 6: Habilitar los marcadores de punto alto y punto bajo
group.setShowHighPoint(True)
group.setShowLowPoint(True)

# Paso 7: Guardar el workbook
workbook.save("output_line.xlsx")

jpype.shutdownJVM()
```

## **Minigráficos de columnas**

Un minigráfico de columnas representa cada punto de datos como una barra vertical. Esto lo hace muy adecuado para datos cuya magnitud es significativa — por ejemplo, cifras de ventas mensuales o recuentos. En Aspose.Cells, puede crear un minigráfico de columnas pasando `SparklineType.COLUMN` al método `add`.

El procedimiento refleja el ejemplo del minigráfico de líneas:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el mismo rango de origen (A1:E1) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` resultante — por ejemplo, estableciendo `group.getType()` para confirmar el tipo, o ajustando el color de las barras.
6. Guarde el libro de trabajo en un archivo de salida independiente para que no sobrescriba el ejemplo del minigráfico de líneas.

El siguiente ejemplo escribe los valores 5, -3, 8, -2, 6 en A1:E1 y renderiza un minigráfico de columnas en F1. Los valores negativos se dibujan como barras que van hacia abajo y los valores positivos como barras que van hacia arriba, lo que facilita detectar de un vistazo las contribuciones positivas y negativas.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType

# Paso 1: Crear un Workbook y obtener la primera hoja de cálculo
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Paso 2: Escribir valores de muestra en A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])

# Paso 3: Construir un CellArea que apunte a F1 (índice de columna 5, índice de fila 0)
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)

# Paso 4: Agregar un minigráfico de columna a la celda de destino
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)

# Paso 5: Confirmar el tipo de minigráfico leyendo group.Type
print("Sparkline Type added: " + str(group.getType()))

# Paso 6: Guardar el workbook
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")

jpype.shutdownJVM()
```

## **Minigráficos de victorias/derrotas**

Un minigráfico de victorias/derrotas es una variante especial del minigráfico de columnas diseñado para mostrar solo dos resultados: un valor positivo se dibuja como una barra hacia arriba (una victoria) y un valor cero o negativo se dibuja como una barra hacia abajo (una derrota). Los minigráficos de victorias/derrotas se usan comúnmente para visualizar secuencias de victorias y derrotas, resultados de aprobado/suspenso, o cualquier resultado binario a lo largo del tiempo.

En Aspose.Cells, un minigráfico de victorias/derrotas se crea pasando `SparklineType.STACKED` al método `add`. (A pesar del nombre, `SparklineType.STACKED` es el valor de enumeración utilizado para solicitar la representación de victorias/derrotas.)

El procedimiento es el mismo que para los otros dos tipos:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el rango de origen. Dado que los minigráficos de victorias/derrotas tratan cada valor como una victoria o una derrota, la magnitud del valor no importa — solo su signo. Los valores positivos se convierten en barras hacia arriba y los valores no positivos se convierten en barras hacia abajo.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` devuelto, por ejemplo, estableciendo colores de acento para las barras de victoria y derrota.
6. Guarde el libro de trabajo con un nombre de archivo distinto para que los tres ejemplos puedan coexistir en el disco.

El siguiente ejemplo usa los mismos datos de entrada que las dos secciones anteriores. Los valores 5, -3, 8, -2, 6 se interpretan como victoria, derrota, victoria, derrota, victoria — y el minigráfico dibujado en F1 refleja exactamente ese patrón.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color

# Paso 1: Crear un Workbook y obtener la primera hoja de cálculo
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")

# Paso 2: Poblar datos de muestra en la fila 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Paso 3: Construir un CellArea que apunte a F1 (columna 5, fila 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # fila 1
dest.setEndRow(0)

# Paso 4: Agregar un minigráfico de Ganancia/Pérdida (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)

# Paso 5: Personalizar el grupo de minigráficos
# Habilitar marcadores de punto alto y punto bajo
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)

# Establecer el color del punto alto en verde
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)

# Establecer el color del punto bajo en rojo
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)

# Establecer el color del punto negativo en naranja
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)

# Establecer el color predeterminado de la serie (usado para barras positivas)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)

# Paso 6: Guardar el libro
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")

jpype.shutdownJVM()
```

## **Combinación de los tres tipos de minigráficos**

Los tres ejemplos anteriores producen cada uno su propio libro de trabajo para que los archivos de salida sean fáciles de inspeccionar de forma aislada. Sin embargo, en un escenario del mundo real, a menudo querrá comparar varias series de datos una al lado de la otra. La forma más limpia de hacerlo es colocar más de un grupo de minigráficos en la misma hoja de cálculo, con cada grupo representando un estilo diferente.

Puede añadir varios objetos `SparklineGroup` al mismo `SparklineGroupCollection`, y cada grupo puede tener como destino una celda de destino diferente o un rango diferente. Por ejemplo, podría colocar un minigráfico de líneas en F1, un minigráfico de columnas en F2 y un minigráfico de victorias/derrotas en F3 — todos leyendo desde los mismos datos de origen en la fila 1 — para que el lector pueda ver tres tratamientos visuales diferentes de los mismos números.

El siguiente ejemplo combinado crea un solo libro de trabajo, rellena la fila 1 con los valores 5, -3, 8, -2, 6, y luego añade tres grupos de minigráficos en las celdas F1, F2 y F3 — uno de cada tipo — para que el archivo resultante demuestre los tres estilos de minigráficos a la vez.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color

# Paso 1: Crear un Workbook y obtener la primera hoja de trabajo
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Paso 2: Poblar datos de muestra en la fila 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Paso 3: Agregar un grupo de minigráficos de línea en F1
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)

# Personalizar el color del minigráfico de línea mediante CellsColor
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)

# Paso 4: Agregar un grupo de minigráficos de columna en F2
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)

# Personalizar el color de la serie del minigráfico de columna
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)

# Paso 5: Agregar un grupo de minigráficos de victoria/derrota (apilados) en F3
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)

# Personalizar el color de la serie del minigráfico de victoria/derrota
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # NaranjaOscuro
stackedGroup.setSeriesColor(stackedColor)

# Paso 6: Guardar el libro de trabajo
workbook.save("output_all.xlsx")

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

Cuando combina varios grupos de minigráficos en una sola hoja de cálculo, cada grupo es independiente. Pueden compartir el mismo rango de origen o usar rangos de origen diferentes, y se pueden diseñar de forma independiente. Esto facilita la creación de un pequeño "panel" de visualizaciones dentro de celdas directamente dentro de una hoja de cálculo existente.

{{% /alert %}}

## **Personalización de la apariencia de los minigráficos**

Una vez que se ha creado un `SparklineGroup` y se ha añadido a `worksheet.getSparklineGroups()`, puede leer o modificar varias de sus propiedades visuales antes de guardar el libro de trabajo. Las propiedades personalizadas con mayor frecuencia son:

- **`group.getType()`** — el `SparklineType` (LINE, COLUMN o STACKED). Se establece cuando se añade el grupo, pero puede leerlo de nuevo para confirmarlo.
- **`group.getLine().getColor()`** — el color de la línea, expresado como un `CellsColor` creado mediante `workbook.createCellsColor()`. Esta es la propiedad que se debe usar para el color del trazo del minigráfico de líneas.
- **`group.getLine().getWeight()`** — el grosor de la línea en puntos. Los valores más altos producen líneas más gruesas.
- **Marcadores de puntos altos/bajos** — flags que activan pequeños marcadores en los puntos de datos más altos y más bajos, útiles para enfatizar los extremos.
- **Marcadores de puntos primero/último/negativo** — flags que alternan los marcadores en el primer, último y los puntos de datos negativos.

Para cambiar un color, cree siempre una instancia de `CellsColor` y asígnela a la propiedad correspondiente. No asigne un `java.awt.Color` directamente a las propiedades de color del minigráfico — esperan el tipo `CellsColor` de `Aspose.Cells.Drawing`. El propio método `add` devuelve un objeto `SparklineGroup` completamente tipado, por lo que puede encadenar asignaciones de propiedades en el valor de retorno o almacenarlo en una variable local y personalizarlo antes de guardar.



{{< app/cells/assistant language="python" >}}