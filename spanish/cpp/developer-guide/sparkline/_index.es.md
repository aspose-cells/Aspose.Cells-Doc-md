---
title: Sparklines en Aspose.Cells for C++
description: Aspose.Cells es una biblioteca de C++ para trabajar con archivos de hojas de cálculo que admite la creación de sparklines, pequeños minigráficos ubicados dentro de las celdas de la hoja de cálculo. Este artículo explica cómo añadir y personalizar sparklines de línea, columna y ganar/perder utilizando la biblioteca Aspose.Cells.
linktitle: Sparklines
keywords: Aspose.Cells, biblioteca de C++, hoja de cálculo, sparklines, sparkline de línea, sparkline de columna, sparkline de ganar/perder, SparklineGroup, SparklineType
type: docs
weight: 195
url: /es/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite la creación de sparklines dentro de las celdas de la hoja de cálculo. Las sparklines son minigráficos que caben dentro de una sola celda, ofreciendo una representación visual rápida de las tendencias de los datos. Aspose.Cells admite sparklines de línea, columna y ganar/perder, y cada una se puede personalizar en cuanto a color, grosor de línea, puntos altos/bajos y marcadores.

## **Introducción**
Las sparklines son pequeños gráficos dentro de la celda que resultan útiles cuando se desea mostrar una tendencia rápida junto a una fila o columna de datos sin ocupar el espacio de un gráfico completo. Excel admite tres tipos de sparklines: **línea**, **columna** y **ganar/perder**. Aspose.Cells replica esta funcionalidad a través de las API `SparklineGroup` y `SparklineGroupCollection` que se encuentran en el espacio de nombres `Aspose.Cells.Charts`.
En Aspose.Cells, cada sparkline que añada se crea mediante `worksheet.SparklineGroups.Add(...)`, que devuelve un objeto `SparklineGroup`. Luego puede usar ese objeto para establecer el tipo de sparkline, el rango de datos, la celda de destino y propiedades visuales como el color de la línea, el grosor de la línea, los marcadores y los indicadores de puntos altos/bajos.
Este artículo recorre los tres tipos de sparklines admitidos por Aspose.Cells — **Línea**, **Columna** y **Ganar/Perder** — y muestra cómo añadirlos, personalizar sus colores y guardar el libro resultante.

## **Sparklines de línea**
Una sparkline de línea dibuja una línea continua a través de los puntos de datos de una serie, lo que la convierte en la opción más natural para mostrar tendencias a lo largo del tiempo. En Aspose.Cells, una sparkline de línea se crea pasando `SparklineType.Line` al método `SparklineGroups.Add`.
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene una fila de datos de origen (por ejemplo, fila 1, columnas A a E) con los valores que desea visualizar.
3. Construya un `CellArea` que describa la celda de destino donde se dibujará la sparkline.
4. Llame a `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. El tercer argumento — `false` — indica an Aspose.Cells que el rango de datos es horizontal (una fila), no vertical (una columna).
5. Opcionalmente, personalice el `SparklineGroup` devuelto. Para una sparkline de línea, puede establecer el color de la línea usando `group.Line.Color` (que espera un `CellsColor` de `Aspose.Cells.Drawing`), ajustar el grosor de la línea y activar los marcadores de los puntos altos y bajos.
6. Guarde el libro.
El siguiente ejemplo crea un libro, escribe los valores 5, -3, 8, -2, 6 en las celdas A1 a E1 y añade una sparkline de línea en la celda F1 que traza esos valores. También personaliza el color de la línea a rojo y activa los marcadores para los puntos altos y bajos.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Paso 1: Crear un Workbook y obtener la primera hoja de trabajo
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Paso 2: Escribir los valores de muestra 5, -3, 8, -2, 6 en las celdas A1:E1
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);
    // Paso 3: Construir un CellArea que apunte a la celda de destino F1
    CellArea dest;
    dest.StartColumn = 5;   // columna F (índice 0)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // fila 1 (índice 0)
    dest.EndRow = 0;
    // Paso 4: Agregar un minigráfico de tipo Line desde A1:E1 en F1
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);
    // Paso 5: Crear un CellsColor rojo y asignarlo al color de la línea del minigráfico
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);
    // Paso 6: Habilitar los marcadores de punto alto y punto bajo
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    // Paso 7: Guardar el workbook
    workbook.Save(u"output_line.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sparklines de columna**
Una sparkline de columna representa cada punto de datos como una barra vertical. Esto la hace muy adecuada para datos cuya magnitud es significativa — por ejemplo, cifras de ventas mensuales o recuentos. En Aspose.Cells, se crea una sparkline de columna pasando `SparklineType.Column` al método `SparklineGroups.Add`.
El procedimiento refleja el ejemplo de la sparkline de línea:
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene una fila de datos de origen.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` resultante — por ejemplo, estableciendo `group.Type` para confirmar el tipo, o ajustando el color de las barras.
6. Guarde el libro en un archivo de salida independiente para que no sobrescriba el ejemplo de la sparkline de línea.
El siguiente ejemplo escribe los valores 5, -3, 8, -2, 6 en A1:E1 y dibuja una sparkline de columna en F1. Los valores negativos se dibujan como barras hacia abajo y los valores positivos como barras hacia arriba, lo que facilita la identificación de las contribuciones positivas y negativas de un vistazo.

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
    // Paso 3: Construir un CellArea apuntando a F1 (índice de columna 5, índice de fila 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;
    // Paso 4: Agregar un minigráfico de columna a la celda de destino
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

## **Sparklines de ganar/perder**
Una sparkline de ganar/perder es una variante especial de la sparkline de columna diseñada para mostrar solo dos resultados: un valor positivo se dibuja como una barra "hacia arriba" (una victoria) y un valor cero o negativo se dibuja como una barra "hacia abajo" (una pérdida). Las sparklines de ganar/perder se usan comúnmente para visualizar secuencias de victorias y derrotas, resultados de aprobado/suspenso o cualquier resultado binario a lo largo del tiempo.
En Aspose.Cells, una sparkline de ganar/perder se crea pasando `SparklineType.Stacked` al método `SparklineGroups.Add`. (A pesar del nombre, `SparklineType.Stacked` es el valor de enumeración usado para solicitar el renderizado de ganar/perder.)
1. Cree un nuevo `Workbook` y acceda a la primera hoja de cálculo.
2. Rellene el rango de origen. Dado que las sparklines de ganar/perder tratan cada valor como una victoria o una pérdida, la magnitud del valor no importa — solo su signo. Los valores positivos se convierten en barras hacia arriba y los valores no positivos se convierten en barras hacia abajo.
3. Construya un `CellArea` que describa la celda de destino.
4. Llame a `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Opcionalmente, personalice el `SparklineGroup` devuelto, por ejemplo, estableciendo colores de acento para las barras de victoria y pérdida.
6. Guarde el libro con un nombre de archivo distinto para que los tres ejemplos puedan coexistir en disco.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Paso 1: Crear un Workbook y obtener la primera hoja de cálculo
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");
    // Paso 2: Poblar datos de muestra en la fila 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // Paso 3: Construir un CellArea que apunte a F1 (columna 5, fila 0)
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // fila 1
    dest.EndRow = 0;
    // Paso 4: Agregar un minigráfico Win/Loss (SparklineType.Stacked)
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
El siguiente ejemplo combinado crea un único libro, rellena la fila 1 con los valores 5, -3, 8, -2, 6 y luego añade tres grupos de sparklines en las celdas F1, F2 y F3 — uno de cada tipo — de modo que el archivo resultante muestra los tres estilos de sparklines a la vez.

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
    // Paso 3: Agregar un grupo de minigráficos de línea en F1
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
    // Paso 4: Agregar un grupo de minigráficos de columna en F2
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
    // Paso 5: Agregar un grupo de minigráficos de Ganancia/Pérdida (Apilados) en F3
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
    // Paso 6: Guardar el libro
    workbook.Save(u"output_all.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Personalización del aspecto de la sparkline**
Una vez que un `SparklineGroup` ha sido creado y añadido a `worksheet.SparklineGroups`, puede leer o modificar varias de sus propiedades visuales antes de guardar el libro. Las propiedades personalizadas con mayor frecuencia son:
- **`group.Type`** — el `SparklineType` (Línea, Columna o Apilada). Se establece cuando se añade el grupo, pero puede leerlo de nuevo para confirmarlo.
- **`group.Line.Color`** — el color de la línea, expresado como un `CellsColor` creado mediante `workbook.CreateCellsColor()`. Esta es la propiedad que se debe usar para el color del trazo de la sparkline de línea.
- **`group.Line.Weight`** — el grosor de la línea en puntos. Los valores más altos producen líneas más gruesas.
- **Marcadores de puntos altos/bajos** — indicadores que activan pequeños marcadores en los puntos de datos más altos y más bajos, útiles para enfatizar los extremos.
- **Marcadores de primer/último/punto negativo** — indicadores que alternan los marcadores en el primer, último y negativos puntos de datos.
Para cambiar un color, cree siempre una instancia de `CellsColor` y asígnela a la propiedad correspondiente. No asigne un valor de color sin procesar directamente a las propiedades de color de la sparkline — esperan el tipo `CellsColor` de `Aspose.Cells.Drawing`. El propio método `SparklineGroups.Add` devuelve un objeto `SparklineGroup` totalmente tipado, por lo que puede encadenar asignaciones de propiedades sobre el valor de retorno o almacenarlo en una variable local y personalizarlo antes de guardar.
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}