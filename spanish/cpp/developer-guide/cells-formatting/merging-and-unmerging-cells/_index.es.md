---
title: Fusionar y deshacer la unión de celdas con C++
linktitle: Fusionar y Desfusionar Celdas
description: Aspose.Cells es una biblioteca C++ para trabajar con archivos de hojas de cálculo, que soporta fusionar y deshacer la unión de celdas. Este artículo introducirá cómo fusionar y deshacer la unión de celdas usando la biblioteca Aspose.Cells y cómo personalizar el estilo de las celdas fusionadas.
keywords: Aspose.Cells, biblioteca C++, hoja de cálculo, fusionar celdas, deshacer unión de celdas, configuraciones de estilo, estilos personalizados
type: docs
weight: 190
url: /es/cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells admite esta función y también puede combinar celdas en una hoja de cálculo. También puedes descombinar o dividir las celdas combinadas. La referencia de celda de una celda combinada es la referencia de la celda superior izquierda en el rango original seleccionado.

{{% /alert %}} 

## **Introducción**
No siempre quieres el mismo número de celdas en cada fila o columna. Por ejemplo, es posible que desees colocar un título en una celda que abarque varias columnas. O, si estás creando una factura, es posible que desees menos columnas para el total. Para hacer una celda a partir de dos o más celdas, combínalas. Microsoft Excel permite a los usuarios seleccionar archivos y combinarlos para estructurar la hoja de cálculo según sus necesidades.

{{% alert color="primary" %}} 

Ten en cuenta que cuando las celdas se combinan, solo se conservan los datos de las celdas superiores izquierdas. Si hay datos en las otras celdas del rango, estos datos se eliminan.
Asimismo, el formato se basa en la celda de referencia, por lo que al combinar celdas, se aplican las configuraciones de formato de la celda superior izquierda en el rango a la celda combinada. Cuando la celda se divide, las nuevas celdas mantienen sus ajustes de formato originales.

{{% /alert %}} 

## **Combina celdas en una hoja de cálculo**
### **Combinar celdas en Microsoft Excel**
Los siguientes pasos describen cómo combinar celdas en la hoja de cálculo utilizando MS Excel.

1. Copie los datos que desea en la celda superior izquierda dentro del rango.
1. Seleccione las celdas que desea combinar.
1. Para combinar celdas en una fila o columna y centrar el contenido de la celda, haga clic en el icono **Combinar y centrar** en la barra de herramientas **Formato**.

### **Combinar celdas con Aspose.Cells**
 La clase `Aspose::Cells::Cells` tiene algunos métodos útiles para la tarea. Por ejemplo, el método `Merge()` fusiona las celdas en un rango especificado en una sola celda.

El siguiente ejemplo muestra cómo combinar celdas (C6:E7) en una hoja de cálculo.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Descombinar (Separar) celdas combinadas**
### **Usar Microsoft Excel**
Los siguientes pasos describen cómo separar celdas combinadas utilizando Microsoft Excel.

1. Seleccione la celda combinada.
   Cuando las celdas se han combinado, **Combinar y centrar** se selecciona en la barra de herramientas **Formato**.
1. Haga clic en **Combinar y centrar** en la barra de herramientas **Formato**.

### **Usar Aspose.Cells**
 La clase `Aspose::Cells::Cells` tiene un método llamado `UnMerge()` que divide las celdas en su estado original. El método deshace la unión de las celdas usando la referencia de la celda en el rango fusionado.

El siguiente ejemplo muestra cómo separar las celdas combinadas (C6). El ejemplo utiliza el archivo creado en el ejemplo anterior y separa las celdas combinadas.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"mergingcells.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"unmergingcells.out.xls";

    // Create a Workbook and open the excel file
    Workbook wbk(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Get the Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Unmerge the cells
    cells.UnMerge(5, 2, 2, 3);

    // Save the file
    wbk.Save(outputFilePath);

    std::cout << "Cells unmerged successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Detectar celdas combinadas en una hoja de cálculo](/cells/es/cpp/detect-merged-cells-in-a-worksheet/)
