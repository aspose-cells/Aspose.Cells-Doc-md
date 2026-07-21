---
title: Aplicar estilos a tablas dinámicas
linktitle: Aplicar estilos a tablas dinámicas
description: Aprenda a aplicar estilos integrados y personalizados a tablas dinámicas en Aspose.Cells for Python via Java, incluyendo autoformatos heredados de XLS, estilos con nombre modernos de Excel 2007+, estilos personalizados de tablas dinámicas y el método abreviado FormatAll.
keywords: Aspose.Cells Python via Java estilo de tabla dinámica, PivotTableStyleType, AutoFormatType, FormatAll, estilo personalizado, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /es/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la aplicación de autoformatos heredados para tablas dinámicas (destinados a archivos `.xls`) y estilos modernos con nombre o personalizados para tablas dinámicas (destinados a archivos `.xlsx`, `.xlsm` y `.xlsb`). La API que debe llamar depende del formato de archivo en el que se guarda el libro de trabajo, no del formato desde el que se cargó.

{{% /alert %}}

## **Introducción**

Aspose.Cells expone dos API de estilos paralelas para tablas dinámicas. La decisión entre ellas depende del formato de archivo en el que guarda el libro de trabajo, no del formato desde el que lo lee. Un libro de trabajo cargado desde un archivo `.xls` puede volver a guardarse como `.xlsx`, y en ese caso se aplica la API de estilo moderna en lugar de la heredada.

Para la salida heredada `.xls`, utilice el método `pivotTable.setAutoFormatType(int)` junto con la enumeración `com.aspose.cells.pivot.PivotTableAutoFormatType`. Esta API corresponde al selector de autoformato que el Excel clásico ofrecía para tablas dinámicas.

Para la salida moderna `.xlsx`, `.xlsm` y `.xlsb`, hay dos variantes de la API de estilo disponibles:

- `pivotTable.setPivotTableStyleType(int)` selecciona uno de los estilos con nombre integrados (temas claros y oscuros, incluyendo los estilos añadidos en Excel 2017). Estos preajustes son de solo lectura.
- `pivotTable.setPivotTableStyleName(String)` selecciona un estilo personalizado que usted defina a través de `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)`. Los estilos personalizados son necesarios siempre que desee modificar colores, bordes o fuentes más allá de lo que ofrecen los preajustes.

Además, `pivotTable.formatAll(Style)` es un método abreviado que aplica un único objeto `Style` a cada celda de la tabla dinámica, anulando lo que esté configurado mediante cualquiera de las API de nombre de estilo anteriores. Esto es útil cuando se requiere una apariencia uniforme independientemente del tema subyacente.

## **Aplicar un autoformato predefinido heredado de XLS**

El método `setAutoFormatType` en una tabla dinámica acepta un valor de la enumeración `com.aspose.cells.pivot.PivotTableAutoFormatType`. Los valores disponibles son `REPORT_1` a `REPORT_10`, `CLASSIC`, y `TABLE_1` a `TABLE_10`.

{{% alert color="primary" %}}

`setAutoFormatType` solo se respeta cuando el libro de trabajo se guarda como `.xls`. Cuando el mismo libro de trabajo se guarda como `.xlsx`, `.xlsm` o `.xlsb`, Excel ignora esta configuración y vuelve a las configuraciones `setPivotTableStyleType` y `setPivotTableStyleName`.

{{% /alert %}}

El siguiente ejemplo carga un libro de trabajo nuevo, completa los datos de muestra de Fruta/Año/Cantidad, añade una tabla dinámica, aplica `PivotTableAutoFormatType.REPORT_5` y guarda el resultado como `.xls`.

{{% alert color="primary" %}}

**¿Por qué no hay campos de columna?** Los autoformatos de la serie Report (`Report1` a `Report10`, `Table1` a `Table10`) se diseñaron en el Excel clásico para **tablas dinámicas unidimensionales** con solo campos de fila y valores — no tienen estilo integrado para los encabezados de campos de columna. Si tu tabla dinámica necesita campos de columna, usa los preajustes modernos `PivotTableStyleType` del Escenario 2 a continuación, que están diseñados para el diseño bidimensional que usa el Excel moderno.

{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType

# Escenario 1: Aplicar un autoformato preestablecido XLS heredado
# API en uso: PivotTable.AutoFormatType
# Formato de archivo de destino: .xls (heredado)
# Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Crear un nuevo libro de trabajo
workbook = Workbook()

# Obtener la primera hoja de trabajo
sheet = workbook.getWorksheets().get(0)

# Poblar los datos de origen con la fila de encabezado (Fruit, Year, Amount)
# y 9 filas de datos cubriendo grape, blueberry, kiwi, cherry a lo largo de 2020 y 2021
sheet.getCells().get(0, 0).putValue("Fruit")
sheet.getCells().get(0, 1).putValue("Year")
sheet.getCells().get(0, 2).putValue("Amount")

sheet.getCells().get(1, 0).putValue("grape")
sheet.getCells().get(1, 1).putValue(2020)
sheet.getCells().get(1, 2).putValue(50)

sheet.getCells().get(2, 0).putValue("blueberry")
sheet.getCells().get(2, 1).putValue(2020)
sheet.getCells().get(2, 2).putValue(30)

sheet.getCells().get(3, 0).putValue("kiwi")
sheet.getCells().get(3, 1).putValue(2020)
sheet.getCells().get(3, 2).putValue(25)

sheet.getCells().get(4, 0).putValue("cherry")
sheet.getCells().get(4, 1).putValue(2020)
sheet.getCells().get(4, 2).putValue(40)

sheet.getCells().get(5, 0).putValue("grape")
sheet.getCells().get(5, 1).putValue(2021)
sheet.getCells().get(5, 2).putValue(60)

sheet.getCells().get(6, 0).putValue("blueberry")
sheet.getCells().get(6, 1).putValue(2021)
sheet.getCells().get(6, 2).putValue(35)

sheet.getCells().get(7, 0).putValue("kiwi")
sheet.getCells().get(7, 1).putValue(2021)
sheet.getCells().get(7, 2).putValue(28)

sheet.getCells().get(8, 0).putValue("cherry")
sheet.getCells().get(8, 1).putValue(2021)
sheet.getCells().get(8, 2).putValue(45)

sheet.getCells().get(9, 0).putValue("grape")
sheet.getCells().get(9, 1).putValue(2020)
sheet.getCells().get(9, 2).putValue(45)

# Agregar una tabla dinámica en la celda de destino E3, llamada "Pivot1", usando el rango de origen A1:C10
pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Asignar campos: Fruit -> Filas, Year -> Columnas, Amount -> Datos
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Aplicar el autoformato preestablecido XLS heredado "Report5"
# Nota: Esta propiedad solo es significativa cuando se guarda como .xls.
# Cuando se guarda como .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
# y usa lo que PivotTableStyleType / PivotTableStyleName especifique.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.Report5)

# Guardar el libro de trabajo en formato .xls heredado
workbook.save("output.xls")

jpype.shutdownJVM()
```

## **Aplicar un estilo de tabla dinámica predefinido con nombre moderno**

El método `setPivotTableStyleType` en una tabla dinámica acepta un valor de la enumeración `com.aspose.cells.PivotTableStyleType`. La enumeración cubre los temas claros `PIVOT_TABLE_STYLE_LIGHT_1` a `PIVOT_TABLE_STYLE_LIGHT_28` y los temas oscuros `PIVOT_TABLE_STYLE_DARK_1` a `PIVOT_TABLE_STYLE_DARK_28`. Los estilos añadidos en Excel 2017 (la segunda oleada de temas claros y oscuros) son accesibles a través de la misma enumeración.

Esta es la API recomendada para cualquier formato de archivo moderno. A diferencia del autoformato heredado, el estilo seleccionado aquí se representa fielmente por Excel y sobrevive a los ciclos de ida y vuelta a través de otras herramientas de Office.

El siguiente ejemplo utiliza los mismos datos de Fruta/Año/Cantidad, crea una tabla dinámica idéntica, aplica `PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1` y guarda el libro de trabajo como `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType

# Escenario 2: Aplicar un estilo preestablecido con nombre moderno de Excel 2007+ usando PivotTableStyleType.
# Formato de archivo de destino: .xlsx. La enumeración PivotTableStyleType reside en el espacio de nombres Aspose.Cells
# (no en Aspose.Cells.Pivot) — por eso no necesitamos ninguna importación adicional.
# Referencia de GitHub: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Fila de encabezado: Fruta / Año / Cantidad
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 9 filas de datos de Fruta / Año / Cantidad
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(150)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(180)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(120)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(170)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(210)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(190)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(130)

# Agregar una tabla dinámica en E3 con el nombre "Pivot1", con origen en A1:C10
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Asignar campos de la tabla dinámica: Fruta -> área de Filas, Año -> área de Columnas, Cantidad -> área de Datos
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Aplicar un estilo preestablecido con nombre moderno de tabla dinámica de Excel 2007+.
# PivotTableStyleType es la API correcta para archivos .xlsx / .xlsm / .xlsb; AutoFormatType
# es ignorado por Excel para esos formatos. PivotTableStyleDark1 pertenece a la familia de tema oscuro
# familia (PivotTableStyleDark1..PivotTableStyleDark28), y la misma enumeración también expone los
# temas más nuevos claro/oscuro de Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PivotTableStyleDark1)

# Guardar como .xlsx moderno — este es el formato para el cual PivotTableStyleType es significativo.
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Definir y aplicar un estilo personalizado de tabla dinámica**

Los preajustes integrados no se pueden modificar. Siempre que necesite anular colores, bordes o fuentes, debe definir un estilo personalizado para tabla dinámica. El flujo de trabajo tiene tres pasos:

1. Añada un estilo personalizado a la colección `TableStyles` del libro de trabajo mediante `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. Esto devuelve el índice del estilo recién creado.
2. Configure el estilo añadiendo elementos (como `WHOLE_TABLE` o `GRAND_TOTAL_ROW`) mediante `tableStyle.getTableStyleElements().add(TableStyleElementType)`, luego asigne un `Style` a cada elemento mediante `tableStyleElement.setElementStyle(Style)`.
3. Aplique el estilo personalizado a la tabla dinámica llamando a `pivotTable.setPivotTableStyleName(String)` con el nombre del estilo. No utilice `setPivotTableStyleType` aquí, ya que ese método selecciona preajustes integrados.

{{% alert color="primary" %}}

`setPivotTableStyleName` y `setPivotTableStyleType` no son intercambiables. Utilice `setPivotTableStyleType` para preajustes integrados, y `setPivotTableStyleName` para estilos personalizados que haya definido mediante `addPivotTableStyle`. Configurar ambos es inofensivo, pero solo se representa el que coincida con el origen previsto.

{{% /alert %}}

Los valores disponibles de `TableStyleElementType` incluyen `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` y `PAGE_FIELD_VALUES`.

El siguiente ejemplo define un estilo personalizado de tabla dinámica con un borde negro fino en `WHOLE_TABLE` y una fuente roja en negrita en `GRAND_TOTAL_ROW`, luego lo aplica mediante `setPivotTableStyleName` y guarda como `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from java.awt import Color

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Poblar datos de origen: fila de encabezado + 9 filas de datos (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)

# Agregar tabla dinámica con origen en A1:C10, anclada en E3, llamada "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# Paso 1: registrar un nuevo estilo de tabla dinámica personalizado y capturar su índice
styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle")
tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex)

# Paso 2: agregar un elemento WholeTable y aplicar bordes negros finos en los cuatro lados
wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE)
wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex)
wholeTableStyle = workbook.createStyle()
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)
wholeTableElement.setElementStyle(wholeTableStyle)

# Paso 3: agregar un elemento GrandTotalRow y aplicar fuente roja en negrita
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.RED)
grandTotalElement.setElementStyle(grandTotalStyle)

# Paso 4: aplicar el estilo personalizado por nombre (NO por PivotTableStyleType, que es para estilos predefinidos)
pivotTable.setPivotTableStyleName("CustomPivotStyle")

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Aplicar un estilo a cada celda de la tabla dinámica con FormatAll**

`pivotTable.formatAll(Style)` es un método abreviado que aplica un único objeto `Style` a cada celda de la tabla dinámica, incluyendo el área de datos, los encabezados de filas y columnas, y los totales. Lo que se haya establecido previamente mediante `setPivotTableStyleType` o `setPivotTableStyleName` queda anulado.

{{% alert color="primary" %}}

`formatAll` anula tanto `setPivotTableStyleType` como `setPivotTableStyleName`. Utilícelo solo cuando se requiera una apariencia uniforme, independiente del tema, en toda la tabla dinámica.

{{% /alert %}}

El siguiente ejemplo crea un `Style` con un relleno sólido amarillo, una fuente azul oscuro en negrita y bordes negros finos en todos los lados, luego lo aplica con `formatAll` y guarda como `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType

# Escenario 4: Aplicar un único Estilo a cada celda de la tabla dinámica usando FormatAll
# API en uso: PivotTable.FormatAll(Style)
# Formato de destino: .xlsx
# Referencia de GitHub: ver repositorio Aspose.Cells-for-.NET — ejemplos de estilo de tablas dinámicas

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Rellenar datos fuente: fila de encabezado (fila 1) + 9 filas de datos (filas 2-10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(5000)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(3000)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(4000)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(2000)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(6000)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(3500)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(4500)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(2500)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(5500)

# Agregar tabla dinámica: rango fuente A1:C10, celda de destino E3, nombre "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Asignar campos dinámicos: Fruit -> área de filas, Year -> área de columnas, Amount -> área de datos
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# Construir un Estilo que se forzará sobre cada celda de la tabla dinámica
style = workbook.createStyle()
style.setForegroundColor(Color.YELLOW)
style.setPattern(BackgroundType.SOLID)
style.getFont().setIsBold(True)
style.getFont().setColor(Color.DARK_BLUE)
style.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)

# Aplicar FormatAll: fuerza este único estilo sobre cada celda de la tabla dinámica,
# sobrescribiendo cualquier PivotTableStyleType / PivotTableStyleName establecido previamente
pivotTable.formatAll(style)

# Guardar el libro en el formato moderno .xlsx
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **¿Qué API de estilo debo usar?**

La elección de la API de estilo depende del formato de archivo en el que está guardando. Utilice la tabla siguiente como referencia rápida.

| Formato de archivo de destino | API a utilizar | Notas |
|---|---|---|
| `.xls` (heredado) | `pivotTable.setAutoFormatType(int)` | Valores de `com.aspose.cells.pivot.PivotTableAutoFormatType` (p. ej. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Se ignora al guardar en formatos modernos. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo integrado) | `pivotTable.setPivotTableStyleType(int)` | Valores de `com.aspose.cells.PivotTableStyleType` (temas claros/oscuros, incluyendo las adiciones de Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo personalizado) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | Utilícelo cuando los preajustes integrados no sean suficientes. Configurar mediante `tableStyleElement.setElementStyle(Style)`. |
| Cualquier formato (anulación uniforme) | `pivotTable.formatAll(Style)` | Método abreviado que anula cualquier otra configuración de estilo en toda la tabla dinámica. |

En caso de duda, guarde como `.xlsx` y utilice `setPivotTableStyleType` para temas integrados, o `setPivotTableStyleName` para temas personalizados.

{{< app/cells/assistant language="python" >}}