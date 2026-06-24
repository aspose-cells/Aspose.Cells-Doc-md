---
title: Sparklines en Aspose.Cells for C++
linktitle: Sparklines
description: Aspose.Cells es una biblioteca de C++ para trabajar con archivos de hojas de cálculo que admite la creación de sparklines (minigráficos) colocados dentro de las celdas de la hoja de cálculo. Este artículo explica cómo agregar y personalizar sparklines de línea, columna y ganancia/pérdida usando la biblioteca Aspose.Cells.
keywords: Aspose.Cells, biblioteca de C++, hoja de cálculo, sparklines, sparkline de línea, sparkline de columna, sparkline de ganancia/pérdida, SparklineGroup, SparklineType
type: docs
weight: 195
url: /es/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la creación de sparklines dentro de celdas de hojas de cálculo. Los sparklines son minigráficos que caben dentro de una sola celda, proporcionando una representación visual rápida de las tendencias de los datos. Aspose.Cells admite sparklines de línea, columna y ganancia/pérdida, y cada uno se puede personalizar con respecto al color, grosor de línea, puntos altos/bajos y marcadores.

{{% /alert %}}

## **Introducción**

Los sparklines son pequeños gráficos dentro de celdas que son útiles cuando se desea mostrar una tendencia rápida junto a una fila o columna de datos sin ocupar el espacio de un gráfico completo. Excel admite tres tipos de sparklines: **línea**, **columna** y **ganancia/pérdida**. Aspose.Cells refleja esta capacidad a través de las API `SparklineGroup` y `SparklineGroupCollection` que se encuentran en el espacio de nombres `Aspose.Cells.Charts`.

En Aspose.Cells, cada sparkline que agregue se crea a través de `worksheet.SparklineGroups.Add(...)`, que devuelve un objeto `SparklineGroup`. Luego puede usar ese objeto para establecer el tipo de sparkline, el rango de datos, la celda de destino y las propiedades visuales como el color de la línea, el grosor de la línea, los marcadores y los indicadores de puntos altos/bajos.

{{% alert color="primary" %}}

Un único `SparklineGroup` puede contener uno o más sparklines que comparten el mismo estilo. Cuando llama a `Add` y pasa una fila de datos más una sola celda de destino, obtiene un sparkline dentro de esa celda. Si su rango de destino es más ancho que una celda, se dibuja un sparkline separado en cada celda de destino, todos usando el mismo estilo y rango de datos.

{{% /alert %}}

Este artículo recorre cada uno de los tres tipos de sparklines admitidos por Aspose.Cells — **Línea**, **Columna** y **Ganancia/Pérdida** — y muestra cómo agregarlos, personalizar sus colores y guardar el libro de trabajo resultante.

## **Sparklines de línea**

Un sparkline de línea dibuja una línea continua a través de los puntos de datos en una serie, lo que lo convierte en la opción más natural para mostrar tendencias a lo largo del tiempo. En Aspose.Cells, un sparkline de línea se crea pasando `SparklineType.Line` al método `SparklineGroups.Add`.

El flujo de trabajo es el mismo que para cualquier otro tipo de sparkline:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene una fila de datos de origen (por ejemplo, fila 1, columnas A a E) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino donde se dibujará el sparkline.
4. Llame a `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. El tercer argumento — `false` — indica a Aspose.Cells que el rango de datos es horizontal (una fila), no vertical (una columna).
5. Opcionalmente, personalice el `SparklineGroup` devuelto. Para un sparkline de línea puede establecer el color de la línea usando `group.Line.Color` (que espera un `CellsColor` de `Aspose.Cells.Drawing`), ajustar el grosor de la línea y activar/desactivar los marcadores de puntos altos/bajos.
6. Guarde el libro de trabajo.

El siguiente ejemplo crea un libro de trabajo, escribe los valores 5, -3, 8, -2, 6 en las celdas A1 a E1, y agrega un sparkline de línea en la celda F1 que traza esos valores. También personaliza el color de la línea a rojo y habilita los marcadores para los puntos altos y bajos.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Paso 1: Crear un Workbook y obtener la primera hoja de cálculo
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Paso 2: Escribir valores de muestra 5, -3, 8, -2, 6 en las celdas A1:E1
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);

    // Paso 3: Construir un CellArea apuntando a la celda de destino F1
    CellArea dest;
    dest.StartColumn = 5;   // columna F (índice base 0)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // fila 1 (índice base 0)
    dest.EndRow = 0;

    // Paso 4: Agregar un minigráfico de tipo Línea desde A1:E1 en F1
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);

    // Paso 5: Crear un CellsColor rojo y asignarlo al color de la línea del minigráfico
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);

    // Paso 6: Habilitar los marcadores de punto alto y punto bajo
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);

    // Paso 7: Guardar el libro de trabajo
    workbook.Save(u"output_line.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sparklines de columna**

Un sparkline de columna representa cada punto de datos como una barra vertical. Esto lo hace muy adecuado para datos cuya magnitud es significativa — por ejemplo, cifras de ventas mensuales o recuentos. En Aspose.Cells, se crea un sparkline de columna pasando `SparklineType.Column` al método `SparklineGroups.Add`.

El procedimiento refleja el ejemplo del sparkline de línea:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el mismo rango de origen (A1:E1) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` resultante — por ejemplo, estableciendo `group.Type` para confirmar el tipo, o ajustando el color de la barra.
6. Guarde el libro de trabajo en un archivo de salida separado para que no sobrescriba el ejemplo del sparkline de línea.

El siguiente ejemplo escribe los valores 5, -3, 8, -2, 6 en A1:E1 y representa un sparkline de columna en F1. Los valores negativos se dibujan como barras hacia abajo y los valores positivos como barras hacia arriba, lo que hace que las contribuciones positivas y negativas sean fáciles de identificar de un vistazo.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Paso 1: Crear un Workbook y obtener la primera hoja de cálculo
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Paso 2: Escribir valores de muestra en A1:E1
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }

    // Paso 3: Construir un CellArea que apunte a F1 (índice de columna 5, índice de fila 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;

    // Paso 4: Agregar un minigráfico de Columna a la celda de destino
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);

    // Paso 5: Confirmar el tipo de minigráfico leyendo group.Type
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;

    // Paso 6: Guardar el libro de trabajo
    wb.Save(u"output_column.xlsx");

    std::cout << "Workbook saved as output_column.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sparklines de ganancia/pérdida**

Un sparkline de ganancia/pérdida es una variante especial del sparkline de columna diseñada para mostrar solo dos resultados: un valor positivo se dibuja como una barra "hacia arriba" (una ganancia) y un valor cero o negativo se dibuja como una barra "hacia abajo" (una pérdida). Los sparklines de ganancia/pérdida se usan comúnmente para visualizar secuencias de victorias y derrotas, resultados de aprobado/desaprobado, o cualquier resultado binario a lo largo del tiempo.

En Aspose.Cells, un sparkline de ganancia/pérdida se crea pasando `SparklineType.Stacked` al método `SparklineGroups.Add`. (A pesar del nombre, `SparklineType.Stacked` es el valor de enumeración utilizado para solicitar el renderizado de ganancia/pérdida.)

El procedimiento es el mismo que para los otros dos tipos:

1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el rango de origen. Dado que los sparklines de ganancia/pérdida tratan cada valor como una ganancia o una pérdida, la magnitud del valor no importa — solo su signo. Los valores positivos se convierten en barras hacia arriba y los valores no positivos en barras hacia abajo.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` devuelto, por ejemplo, estableciendo colores de acento para las barras de ganancia y pérdida.
6. Guarde el libro de trabajo con un nombre de archivo distinto para que los tres ejemplos puedan coexistir en disco.

El siguiente ejemplo usa los mismos datos de entrada que las dos secciones anteriores. Los valores 5, -3, 8, -2, 6 se interpretan como ganancia, pérdida, ganancia, pérdida, ganancia — y el sparkline dibujado en F1 refleja exactamente ese patrón.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Paso 1: Crear un Workbook y obtener la primera hoja de trabajo
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");

    // Paso 2: Rellenar datos de muestra en la fila 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // Paso 3: Construir un CellArea apuntando a F1 (columna 5, fila 0)
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // fila 1
    dest.EndRow = 0;

    // Paso 4: Agregar un minigráfico de Ganancia/Pérdida (SparklineType.Stacked)
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);

    // Paso 5: Personalizar el grupo de minigráficos
    // Habilitar marcadores de punto alto y punto bajo
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);

    // Establecer el color del punto alto en verde
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);

    // Establecer el color del punto bajo en rojo
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);

    // Establecer el color del punto negativo en naranja
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);

    // Establecer el color predeterminado de la serie (usado para barras positivas)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);

    // Paso 6: Guardar el libro de trabajo
    workbook.Save(u"output_winloss.xlsx");

    std::cout << "Workbook saved successfully: output_winloss.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Combinación de los tres tipos de sparklines**

Los tres ejemplos anteriores producen cada uno su propio libro de trabajo para que los archivos de salida sean fáciles de inspeccionar de forma aislada. En un escenario del mundo real, sin embargo, a menudo querrá comparar varias series de datos una al lado de la otra. La forma más limpia de hacerlo es colocar más de un grupo de sparklines en la misma hoja de cálculo, donde cada grupo representa un estilo diferente.

Puede agregar múltiples objetos `SparklineGroup` a la misma `SparklineGroupCollection`, y cada grupo puede tener como destino una celda de destino diferente o un rango diferente. Por ejemplo, podría colocar un sparkline de línea en F1, un sparkline de columna en F2, y un sparkline de ganancia/pérdida en F3 — todos leyendo desde los mismos datos de origen en la fila 1 — de modo que el lector pueda ver tres tratamientos visuales diferentes de los mismos números.

El ejemplo combinado a continuación crea un único libro de trabajo, rellena la fila 1 con los valores 5, -3, 8, -2, 6, y luego agrega tres grupos de sparklines en las celdas F1, F2 y F3 — uno de cada tipo — de modo que el archivo resultante demuestre los tres estilos de sparkline a la vez.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Paso 1: Crear un Workbook y obtener la primera hoja de cálculo
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Paso 2: Poblar datos de muestra en la fila 1 (A1:E1)
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // Paso 3: Agregar un grupo de minigráficos de Línea en F1
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);

    // Personalizar el color del minigráfico de línea mediante CellsColor
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);

    // Paso 4: Agregar un grupo de minigráficos de Columna en F2
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);

    // Personalizar el color de la serie del minigráfico de columna
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);

    // Paso 5: Agregar un grupo de minigráficos de Ganancia/Pérdida (Apilado) en F3
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);

    // Personalizar el color de la serie del minigráfico de ganancia/pérdida
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);

    // Paso 6: Guardar el workbook
    workbook.Save(u"output_all.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Cuando combina múltiples grupos de sparklines en una sola hoja de cálculo, cada grupo es independiente. Pueden compartir el mismo rango de origen o usar diferentes rangos de origen, y se pueden estilizar de forma independiente. Esto facilita la creación de un pequeño "panel" de visualizaciones dentro de celdas directamente dentro de una hoja de cálculo existente.

{{% /alert %}}

## **Personalización de la apariencia de los sparklines**

Una vez que se ha creado y agregado un `SparklineGroup` a `worksheet.SparklineGroups`, puede leer o modificar varias de sus propiedades visuales antes de guardar el libro de trabajo. Las propiedades personalizadas más comunes son:

- **`group.Type`** — el `SparklineType` (Línea, Columna o Apilado). Se establece cuando se agrega el grupo, pero puede leerlo de nuevo para confirmarlo.
- **`group.Line.Color`** — el color de la línea, expresado como un `CellsColor` creado mediante `workbook.CreateCellsColor()`. Esta es la propiedad a usar para el color del trazo del sparkline de línea.
- **`group.Line.Weight`** — el grosor de la línea en puntos. Valores más altos producen líneas más gruesas.
- **Marcadores de puntos altos/bajos** — indicadores que activan pequeños marcadores en los puntos de datos más altos y más bajos, útiles para enfatizar los extremos.
- **Marcadores de puntos primero/último/negativo** — indicadores que activan/desactivan marcadores en los puntos de datos primero, último y negativos.

Para cambiar un color, siempre cree una instancia de `CellsColor` y asígnela a la propiedad correspondiente. No asigne un valor de color sin procesar directamente a las propiedades de color del sparkline — esperan el tipo `CellsColor` de `Aspose.Cells.Drawing`. El método `SparklineGroups.Add` en sí mismo devuelve un objeto `SparklineGroup` completamente tipado, por lo que puede encadenar asignaciones de propiedades en el valor de retorno o almacenarlo en una variable local y personalizarlo antes de guardar.



{{< app/cells/assistant language="cpp" >}}