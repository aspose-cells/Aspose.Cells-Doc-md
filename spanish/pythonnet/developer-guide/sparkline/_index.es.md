---
title: Minigráficos en Aspose.Cells for Python via .NET
description: Aspose.Cells es una biblioteca de Python para trabajar con archivos de hojas de cálculo que admite la creación de minigráficos, pequeños gráficos colocados dentro de celdas de hojas de cálculo. Este artículo explica cómo añadir y personalizar minigráficos de líneas, columnas y de victoria/derrota usando la biblioteca Aspose.Cells.
linktitle: Sparklines
keywords: Aspose.Cells, biblioteca de Python, hoja de cálculo, minigráficos, minigráfico de líneas, minigráfico de columnas, minigráfico de victoria/derrota, SparklineGroup, SparklineType
type: docs
weight: 195
url: /es/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite la creación de minigráficos dentro de celdas de hojas de cálculo. Los minigráficos son pequeños gráficos que caben en una sola celda, ofreciendo una rápida representación visual de las tendencias de los datos. Aspose.Cells admite minigráficos de líneas, columnas y de victoria/derrota, y cada uno puede personalizarse en cuanto a color, grosor de línea, puntos altos/bajos y marcadores.

## **Introducción**
Los minigráficos son pequeños gráficos dentro de las celdas que resultan útiles cuando se desea mostrar una tendencia rápida junto a una fila o columna de datos sin ocupar el espacio de un gráfico completo. Excel admite tres tipos de minigráficos: de líneas, de columnas y de victoria/derrota. Aspose.Cells replica esta capacidad a través de las API `SparklineGroup` y `SparklineGroupCollection` que se encuentran en el espacio de nombres `aspose.cells.charts`.
En Aspose.Cells, cada minigráfico que añada se crea mediante `worksheet.sparkline_groups.add(...)`, que devuelve un objeto `SparklineGroup`. A continuación, puede usar ese objeto para establecer el tipo de minigráfico, el rango de datos, la celda de destino y las propiedades visuales como el color de la línea, el grosor de la línea, los marcadores y los indicadores de puntos altos/bajos.
Este artículo recorre cada uno de los tres tipos de minigráficos compatibles con Aspose.Cells (de líneas, de columnas y de victoria/derrota) y muestra cómo añadirlos, personalizar sus colores y guardar el libro de trabajo resultante.

## **Minigráficos de líneas**
Un minigráfico de líneas dibuja una línea continua a través de los puntos de datos de una serie, lo que lo convierte en la opción más natural para mostrar tendencias a lo largo del tiempo. En Aspose.Cells, un minigráfico de líneas se crea pasando `SparklineType.Line` al método `sparkline_groups.add`.
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene una fila de datos de origen (por ejemplo, la fila 1, columnas A a E) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino donde se dibujará el minigráfico.
4. Llame a `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)`. El tercer argumento (`False`) indica an Aspose.Cells que el rango de datos es horizontal (una fila) y no vertical (una columna).
5. Opcionalmente, personalice el `SparklineGroup` devuelto. Para un minigráfico de líneas puede establecer el color de la línea usando `group.line.color` (que espera un `CellsColor` de `aspose.cells.drawing`), ajustar el grosor de la línea y activar o desactivar los marcadores de los puntos altos/bajos.
6. Guarde el libro de trabajo.
El siguiente ejemplo crea un libro de trabajo, escribe los valores 5, -3, 8, -2, 6 en las celdas A1 a E1, y añade un minigráfico de líneas en la celda F1 que traza esos valores. También personaliza el color de la línea a rojo y habilita los marcadores para los puntos altos y bajos.

```python
import aspose.cells as ac
import System.Drawing
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # row 1
dest.end_row = 0
# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]
# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True
# Set the high-point color to green
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color
# Set the low-point color to red
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color
# Set the negative-point color to orange
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color
# Set the default series color (used for positive bars)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
```

## **Minigráficos de columnas**
Un minigráfico de columnas representa cada punto de datos como una barra vertical. Esto lo hace muy adecuado para datos cuya magnitud es significativa, por ejemplo, las cifras de ventas mensuales o recuentos. En Aspose.Cells, se crea un minigráfico de columnas pasando `SparklineType.Column` al método `sparkline_groups.add`.
El procedimiento es similar al ejemplo del minigráfico de líneas:
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene una fila de datos de origen (por ejemplo, la fila 1, columnas A a E) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` resultante, por ejemplo, estableciendo `group.type` para confirmar el tipo, o ajustando el color de la barra.
6. Guarde el libro de trabajo en un archivo de salida separado para que no sobrescriba el ejemplo del minigráfico de líneas.
El siguiente ejemplo escribe los valores 5, -3, 8, -2, 6 en A1:E1 y representa un minigráfico de columnas en F1. Los valores negativos se dibujan como barras que van hacia abajo y los valores positivos como barras que van hacia arriba, lo que facilita identificar de un vistazo las contribuciones positivas y negativas.

```python
import aspose.cells as ac
# Paso 1: Crear un Workbook y obtener la primera hoja de trabajo
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Paso 2: Escribir valores de muestra en A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells[0, i].put_value(values[i])
# Paso 3: Construir un CellArea apuntando a F1 (índice de columna 5, índice de fila 0)
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0
# Paso 4: Añadir un minigráfico de columna (Column) a la celda de destino
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]
# Paso 5: Confirmar el tipo de minigráfico leyendo group.Type
print("Sparkline Type added: " + str(group.type))
# Paso 6: Guardar el libro de trabajo
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
```

## **Minigráficos de victoria/derrota**
Un minigráfico de victoria/derrota es una variante especial del minigráfico de columnas diseñada para mostrar solo dos resultados: un valor positivo se dibuja como una barra hacia arriba (una victoria) y un valor cero o negativo se dibuja como una barra hacia abajo (una derrota). Los minigráficos de victoria/derrota se usan comúnmente para visualizar secuencias de victorias y derrotas, resultados de aprobado/suspenso, o cualquier resultado binario a lo largo del tiempo.
En Aspose.Cells, un minigráfico de victoria/derrota se crea pasando `SparklineType.Stacked` al método `sparkline_groups.add`. (A pesar del nombre, `SparklineType.Stacked` es el valor de enumeración utilizado para solicitar el renderizado de victoria/derrota.)
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el rango de origen. Dado que los minigráficos de victoria/derrota tratan cada valor como una victoria o una derrota, la magnitud del valor no importa, solo su signo. Los valores positivos se convierten en barras hacia arriba y los valores no positivos en barras hacia abajo.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` devuelto, por ejemplo, estableciendo colores de acento para las barras de victoria y derrota.
6. Guarde el libro de trabajo con un nombre de archivo distinto para que los tres ejemplos puedan coexistir en disco.

```python
import aspose.cells as ac
import System.Drawing
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = ac.CellArea()
dest.start_column = 5   # column F (0-indexed)
dest.end_column = 5
dest.start_row = 0      # row 1 (0-indexed)
dest.end_row = 0
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.Add returns the index of the newly added group
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red
# Step 6: Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
```

## **Combinación de los tres tipos de minigráficos**
El siguiente ejemplo combinado crea un único libro de trabajo, rellena la fila 1 con los valores 5, -3, 8, -2, 6 y luego añade tres grupos de minigráficos en las celdas F1, F2 y F3 (uno de cada tipo), de modo que el archivo resultante muestra los tres estilos de minigráficos a la vez.

```python
import aspose.cells as ac
import System.Drawing
# Paso 1: Crear un Workbook y obtener la primera hoja de trabajo
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
# Paso 5: Agregar un grupo de minigráficos de Ganancia/Pérdida (Apilado) en F3
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]
# Personalizar el color de la serie del minigráfico de ganancia/pérdida
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color
# Paso 6: Guardar el workbook
workbook.save("output_all.xlsx")
```

## **Personalización de la apariencia de los minigráficos**
Una vez que se ha creado y añadido un `SparklineGroup` a `worksheet.sparkline_groups`, puede leer o modificar varias de sus propiedades visuales antes de guardar el libro de trabajo. Las propiedades que se personalizan con más frecuencia son:
- **`group.type`** — el `SparklineType` (Line, Column o Stacked). Se establece al añadir el grupo, pero puede leerlo de nuevo para confirmarlo.
- **`group.line.color`** — el color de la línea, expresado como un `CellsColor` creado mediante `workbook.create_cells_color()`. Esta es la propiedad que se debe usar para el color del trazo del minigráfico de líneas.
- **`group.line.weight`** — el grosor de la línea en puntos. Los valores más altos producen líneas más gruesas.
- **Marcadores de puntos altos/bajos** — indicadores que activan pequeños marcadores en los puntos de datos más altos y más bajos, útiles para resaltar los extremos.
- **Marcadores de primer/último/punto negativo** — indicadores que activan marcadores en el primer, último y los puntos de datos negativos.
Para cambiar un color, cree siempre una instancia de `CellsColor` y asígnela a la propiedad correspondiente. Las propiedades de color del minigráfico esperan el tipo `CellsColor` de `aspose.cells.drawing`; no les asigne directamente un valor de color sin procesar. El propio método `sparkline_groups.add` devuelve un objeto `SparklineGroup` completamente tipado, por lo que puede encadenar asignaciones de propiedades en el valor devuelto o almacenarlo en una variable local y personalizarlo antes de guardar.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}