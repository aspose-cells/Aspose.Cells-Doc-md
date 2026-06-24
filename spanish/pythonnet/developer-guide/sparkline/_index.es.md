---
title: Sparklines in Aspose.Cells for Python via .NET
linktitle: Sparklines
description: Aspose.Cells es una biblioteca de Python para trabajar con archivos de hojas de cálculo que admite la creación de sparklines, minigráficos colocados dentro de las celdas de la hoja de cálculo. Este artículo explica cómo agregar y personalizar sparklines de línea, columna y victoria/derrota utilizando la biblioteca Aspose.Cells.
keywords: Aspose.Cells, biblioteca Python, hoja de cálculo, sparklines, sparkline de línea, sparkline de columna, sparkline de victoria/derrota, SparklineGroup, SparklineType
type: docs
weight: 195
url: /es/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la creación de sparklines dentro de las celdas de la hoja de cálculo. Los sparklines son minigráficos que caben dentro de una sola celda, proporcionando una representación visual rápida de las tendencias de los datos. Aspose.Cells admite sparklines de línea, columna y victoria/derrota, y cada uno se puede personalizar en cuanto a color, grosor de línea, puntos altos/bajos y marcadores.

{{% /alert %}}

## **Introducción**

Los sparklines son pequeños gráficos dentro de una celda que son útiles cuando se desea mostrar una tendencia rápida junto a una fila o columna de datos sin ocupar el espacio de un gráfico completo. Excel admite tres tipos de sparklines: **línea**, **columna** y **victoria/derrota**. Aspose.Cells refleja esta capacidad a través de las API `SparklineGroup` y `SparklineGroupCollection` que se encuentran en el espacio de nombres `aspose.cells.charts`.

En Aspose.Cells, cada sparkline que agrega se crea a través de `worksheet.sparkline_groups.add(...)`, que devuelve un objeto `SparklineGroup`. Luego puede usar ese objeto para establecer el tipo de sparkline, el rango de datos, la celda de destino y las propiedades visuales como el color de la línea, el grosor de la línea, los marcadores y los indicadores de puntos altos/bajos.

{{% alert color="primary" %}}

Un único `SparklineGroup` puede contener uno o más sparklines que comparten el mismo estilo. Cuando llama a `add` y pasa una fila de datos más una sola celda de destino, obtiene un sparkline dentro de esa celda. Si su rango de destino es más ancho que una celda, se dibuja un sparkline separado en cada celda de destino, todos usando el mismo estilo y rango de datos.

{{% /alert %}}

Este artículo recorre cada uno de los tres tipos de sparkline admitidos por Aspose.Cells: **Línea**, **Columna** y **Victoria/Derrota**, y muestra cómo agregarlos, personalizar sus colores y guardar el libro de trabajo resultante.

## **Sparklines de línea**

Un sparkline de línea dibuja una línea continua a través de los puntos de datos en una serie, lo que lo convierte en la opción más natural para mostrar tendencias a lo largo del tiempo. En Aspose.Cells, un sparkline de línea se crea pasando `SparklineType.Line` al método `sparkline_groups.add`.

El flujo de trabajo es el mismo que para cualquier otro tipo de sparkline:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene una fila de datos de origen (por ejemplo, fila 1, columnas A a E) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino donde se dibujará el sparkline.
4. Llame a `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)`. El tercer argumento — `False` — indica a Aspose.Cells que el rango de datos es horizontal (una fila), no vertical (una columna).
5. Opcionalmente, personalice el `SparklineGroup` devuelto. Para un sparkline de línea puede establecer el color de la línea usando `group.line.color` (que espera un `CellsColor` de `aspose.cells.drawing`), ajustar el grosor de la línea y alternar los marcadores de puntos altos/bajos.
6. Guarde el libro de trabajo.

El siguiente ejemplo crea un libro de trabajo, escribe los valores 5, -3, 8, -2, 6 en las celdas A1 a E1, y agrega un sparkline de línea en la celda F1 que traza esos valores. También personaliza el color de la línea a rojo y habilita marcadores para los puntos altos y bajos.

```python
import aspose.cells as ac
import System.Drawing

# Paso 1: Crear un Workbook y obtener la primera hoja de trabajo
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# Paso 2: Escribir los valores de muestra 5, -3, 8, -2, 6 en las celdas A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)

# Paso 3: Construir un CellArea que apunte a la celda de destino F1
dest = ac.CellArea()
dest.start_column = 5   # columna F (índice 0)
dest.end_column = 5
dest.start_row = 0      # fila 1 (índice 0)
dest.end_row = 0

# Paso 4: Agregar un minigráfico de tipo Line desde A1:E1 en F1
# SparklineGroups.Add devuelve el índice del grupo recién agregado
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]

# Paso 5: Crear un CellsColor rojo y asignarlo al color de la línea del minigráfico
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red

# Paso 6: Habilitar los marcadores de punto alto y punto bajo
group.show_high_point = True
group.show_low_point = True

# Paso 7: Guardar el workbook
workbook.save("output_line.xlsx")
```

## **Sparklines de columna**

Un sparkline de columna representa cada punto de datos como una barra vertical. Esto lo hace muy adecuado para datos cuya magnitud es significativa, por ejemplo, cifras de ventas mensuales o recuentos. En Aspose.Cells, un sparkline de columna se crea pasando `SparklineType.Column` al método `sparkline_groups.add`.

El procedimiento refleja el ejemplo del sparkline de línea:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el mismo rango de origen (A1:E1) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` resultante, por ejemplo, estableciendo `group.type` para confirmar el tipo, o ajustando el color de la barra.
6. Guarde el libro de trabajo en un archivo de salida separado para que no sobrescriba el ejemplo del sparkline de línea.

El siguiente ejemplo escribe los valores 5, -3, 8, -2, 6 en A1:E1 y renderiza un sparkline de columna en F1. Los valores negativos se dibujan como barras que van hacia abajo y los valores positivos como barras que van hacia arriba, lo que facilita detectar de un vistazo las contribuciones positivas y negativas.

```python
import aspose.cells as ac

# Paso 1: Crear un Workbook y obtener la primera hoja de cálculo
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Paso 2: Escribir valores de muestra en A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells[0, i].put_value(values[i])

# Paso 3: Construir un CellArea que apunte a F1 (índice de columna 5, índice de fila 0)
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0

# Paso 4: Agregar un minigráfico de Columna a la celda de destino
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]

# Paso 5: Confirmar el tipo de minigráfico leyendo group.Type
print("Sparkline Type added: " + str(group.type))

# Paso 6: Guardar el libro
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")
```

## **Sparklines de victoria/derrota**

Un sparkline de victoria/derrota es una variante especial del sparkline de columna diseñada para mostrar solo dos resultados: un valor positivo se dibuja como una barra "hacia arriba" (una victoria) y un valor cero o negativo se dibuja como una barra "hacia abajo" (una derrota). Los sparklines de victoria/derrota se utilizan comúnmente para visualizar secuencias de victorias y derrotas, resultados de aprobado/suspendido o cualquier resultado binario a lo largo del tiempo.

En Aspose.Cells, un sparkline de victoria/derrota se crea pasando `SparklineType.Stacked` al método `sparkline_groups.add`. (A pesar del nombre, `SparklineType.Stacked` es el valor de enumeración utilizado para solicitar la representación de victoria/derrota.)

El procedimiento es el mismo que para los otros dos tipos:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el rango de origen. Debido a que los sparklines de victoria/derrota tratan cada valor como una victoria o una derrota, la magnitud del valor no importa, solo su signo. Los valores positivos se convierten en barras hacia arriba y los valores no positivos se convierten en barras hacia abajo.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` devuelto, por ejemplo, estableciendo colores de acento para las barras de victoria y derrota.
6. Guarde el libro de trabajo con un nombre de archivo distinto para que los tres ejemplos puedan coexistir en disco.

El siguiente ejemplo utiliza los mismos datos de entrada que las dos secciones anteriores. Los valores 5, -3, 8, -2, 6 se interpretan como victoria, derrota, victoria, derrota, victoria, y el sparkline dibujado en F1 refleja exactamente ese patrón.

```python
import aspose.cells as ac
import System.Drawing

# Paso 1: Crear un Workbook y obtener la primera hoja de cálculo
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"

# Paso 2: Poblar datos de muestra en la fila 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Paso 3: Construir un CellArea apuntando a F1 (columna 5, fila 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # fila 1
dest.end_row = 0

# Paso 4: Agregar un minigráfico Win/Loss (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]

# Paso 5: Personalizar el grupo de minigráficos
# Habilitar los marcadores de punto alto y punto bajo
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True

# Establecer el color del punto alto a verde
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color

# Establecer el color del punto bajo a rojo
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color

# Establecer el color del punto negativo a naranja
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color

# Establecer el color predeterminado de la serie (usado para barras positivas)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color

# Paso 6: Guardar el workbook
workbook.save("output_winloss.xlsx")

print("Workbook guardado exitosamente: output_winloss.xlsx")
```

## **Combinación de los tres tipos de sparkline**

Los tres ejemplos anteriores producen cada uno su propio libro de trabajo para que los archivos de salida sean fáciles de inspeccionar de forma aislada. Sin embargo, en un escenario del mundo real, a menudo querrá comparar varias series de datos una al lado de la otra. La forma más limpia de hacerlo es colocar más de un grupo de sparklines en la misma hoja de cálculo, con cada grupo renderizando un estilo diferente.

Puede agregar múltiples objetos `SparklineGroup` a la misma `SparklineGroupCollection`, y cada grupo puede apuntar a una celda de destino diferente o a un rango diferente. Por ejemplo, podría colocar un sparkline de línea en F1, un sparkline de columna en F2 y un sparkline de victoria/derrota en F3, todos leyendo desde los mismos datos de origen en la fila 1, de modo que el lector pueda ver tres tratamientos visuales diferentes de los mismos números.

El siguiente ejemplo combinado crea un único libro de trabajo, rellena la fila 1 con los valores 5, -3, 8, -2, 6, y luego agrega tres grupos de sparklines en las celdas F1, F2 y F3, uno de cada tipo, para que el archivo resultante demuestre los tres estilos de sparkline a la vez.

```python
import aspose.cells as ac
import System.Drawing

# Paso 1: Crear un Workbook y obtener la primera hoja de cálculo
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Paso 2: Poblar datos de muestra en la fila 1 (A1:E1)
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Paso 3: Agregar un grupo de minigráficos de línea en F1
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]

# Personalizar el color del minigráfico de línea mediante CellsColor
line_color = workbook.create_cells_color()
line_color.color = System.Drawing.Color.Blue
line_group.series_color = line_color

# Paso 4: Agregar un grupo de minigráficos de columna en F2
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]

# Personalizar el color de la serie del minigráfico de columna
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color

# Paso 5: Agregar un grupo de minigráficos de victoria/derrota (apilados) en F3
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]

# Personalizar el color de la serie del minigráfico de victoria/derrota
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color

# Paso 6: Guardar el workbook
workbook.save("output_all.xlsx")
```

{{% alert color="primary" %}}

Cuando combina múltiples grupos de sparklines en una sola hoja de cálculo, cada grupo es independiente. Pueden compartir el mismo rango de origen o usar diferentes rangos de origen, y se pueden estilizar de forma independiente. Esto facilita la creación de un pequeño "panel" de visualizaciones dentro de una celda directamente dentro de una hoja de cálculo existente.

{{% /alert %}}

## **Personalización de la apariencia del sparkline**

Una vez que se ha creado un `SparklineGroup` y se ha agregado a `worksheet.sparkline_groups`, puede leer o modificar varias de sus propiedades visuales antes de guardar el libro de trabajo. Las propiedades que se personalizan con más frecuencia son:

- **`group.type`** — el `SparklineType` (Línea, Columna o Apilado). Se establece cuando se agrega el grupo, pero puede leerlo de nuevo para confirmarlo.
- **`group.line.color`** — el color de la línea, expresado como un `CellsColor` creado a través de `workbook.create_cells_color()`. Esta es la propiedad que se debe usar para el color del trazo del sparkline de línea.
- **`group.line.weight`** — el grosor de la línea en puntos. Los valores más altos producen líneas más gruesas.
- **Marcadores de puntos altos/bajos** — indicadores que activan pequeños marcadores en los puntos de datos más altos y más bajos, útiles para enfatizar los extremos.
- **Marcadores de puntos primero/último/negativo** — indicadores que alternan marcadores en los puntos de datos primero, último y negativo.

Para cambiar un color, siempre cree una instancia de `CellsColor` y asígnela a la propiedad correspondiente. Las propiedades de color del sparkline esperan el tipo `CellsColor` de `aspose.cells.drawing` — no asigne un valor de color sin procesar directamente a ellas. El método `sparkline_groups.add` en sí mismo devuelve un objeto `SparklineGroup` completamente tipado, por lo que puede encadenar asignaciones de propiedades en el valor de retorno o almacenarlo en una variable local y personalizarlo antes de guardar.



{{< app/cells/assistant language="python" >}}