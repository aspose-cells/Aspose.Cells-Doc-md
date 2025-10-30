---
title: Aplicar formato condicional en hojas de trabajo con C++
linktitle: Aplicar formato condicional
description: Cómo usar la biblioteca Aspose.Cells en C++ para aplicar formato condicional en hojas de trabajo. Ajustando estos criterios, tienes más control sobre cómo se ven y aparecen las celdas.
keywords: Aspose.Cells, Formato condicional, C++, Hoja de trabajo, Formateo
type: docs
weight: 130
url: /es/cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Este artículo está diseñado para proporcionar una comprensión detallada de cómo agregar formato condicional a un rango de celdas en una hoja de cálculo.

El formato condicional es una función avanzada en Microsoft Excel que le permite aplicar formatos a un rango de celdas, y tener ese formato cambie dependiendo del valor de la celda o el valor de una fórmula. Por ejemplo, el fondo de una celda puede ser rojo para resaltar un valor negativo, o el color del texto podría ser verde para un valor positivo. Cuando el valor de la celda cumple con la condición del formato, se aplica el formato. Si el valor de la celda no cumple con la condición de formato, se utiliza el formato predeterminado de la celda.

Es posible aplicar formato condicional con la Automatización de Office de Microsoft, pero eso tiene sus desventajas. Hay varias razones y problemas involucrados, como la seguridad, la estabilidad, la escalabilidad y la velocidad. La razón principal para encontrar otra solución es que Microsoft en sí mismo recomienda fuertemente en contra de la Automatización de Office para soluciones de software.

Este artículo muestra cómo crear una aplicación de consola, agregar formato condicional a las celdas con algunas líneas de código más simples utilizando la API de Aspose.Cells.

{{% /alert %}}

## **Usar Aspose.Cells para Aplicar Formato Condicional Basado en el Valor de la Celda**

1. **Descargar e Instalar Aspose.Cells**.
   1. Descarga Aspose.Cells for C++.
1. Instálelo en su equipo de desarrollo.
   Todos los componentes de Aspose, al instalarse, funcionan en modo de evaluación. El modo de evaluación no tiene límite de tiempo y solo inserta marcas de agua en los documentos producidos.
1. **Crear un proyecto**.
   Inicia tu entorno de desarrollo C++ y crea una nueva aplicación de consola.
1. **Agregar referencias**.
   Agrega una referencia a Aspose.Cells en tu proyecto, por ejemplo agrega una referencia a ..\Archivos de Programa\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. **Aplicar formato condicional basado en el valor de la celda**.
   A continuación se presenta el código usado para realizar la tarea. Aplica formato condicional en una celda.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the FormatConditionCollection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(0, 0, 0, 0);

    // Add the cell area to the format condition collection
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Sets the background color
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Cuando se ejecuta el código anterior, se aplica formato condicional a la celda "A1" en la primera hoja del archivo de salida (output.xls). El formato condicional aplicado a A1 depende del valor de la celda. Si el valor de A1 está entre 50 y 100, el color de fondo será rojo debido al formato condicional aplicado.

## **Usar Aspose.Cells para Aplicar Formato Condicional Basado en Fórmula**

1. **Aplicando formato condicional dependiendo de la fórmula (Fragmento de código)**
   A continuación se muestra el código para lograr la tarea. Aplica formato condicional en B3.

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

    // Create workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();

    // Get the conditional formatting collection
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca = CellArea::CreateCellArea(2, 1, 2, 1);

    // Add the area to the conditional formatting
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::Expression);

    // Get the format condition
    FormatCondition fc = fcs.Get(conditionIndex);

    // Set the formula for the condition
    fc.SetFormula1(u"=IF(SUM(B1:B2)>100,TRUE,FALSE)");

    // Set the background color
    Style style = fc.GetStyle();
    style.SetBackgroundColor(Color::Red());
    fc.SetStyle(style);

    // Set the formula for cell B3
    sheet.GetCells().Get(u"B3").SetFormula(u"=SUM(B1:B2)");

    // Set the value for cell C4
    sheet.GetCells().Get(u"C4").PutValue(u"If Sum of B1:B2 is greater than 100, B3 will have RED background");

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls", SaveFormat::Auto);

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Cuando se ejecuta el código anterior, se aplica formato condicional a la celda "B3" en la primera hoja del archivo de salida (output.xls). El formato condicional aplicado depende de la fórmula que calcula el valor de "B3" como la suma de B1 y B2.
{{< app/cells/assistant language="cpp" >}}
