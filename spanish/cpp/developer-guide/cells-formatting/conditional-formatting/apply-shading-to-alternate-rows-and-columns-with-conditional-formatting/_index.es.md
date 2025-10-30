---
title: Aplicar sombreado en filas y columnas alternas con formato condicional en C++
linktitle: Aplicar sombreado en filas y columnas alternas
description: Cómo usar la biblioteca Aspose.Cells en C++ para aplicar sombras en formato condicional en filas y columnas alternas. Ajustando estos criterios, tendrás más control sobre cómo se ven y aparecen las celdas.
keywords: Aspose.Cells, Formato condicional, C++, Filas alternas, Columnas alternas, Sombras
type: docs
weight: 30
url: /es/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Las API de Aspose.Cells proporcionan los medios para agregar y manipular reglas de formato condicional para el objeto [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Estas reglas pueden adaptarse de varias maneras para obtener el formato deseado según condiciones o reglas. Este artículo demostrará el uso de las API de Aspose.Cells for C++ para aplicar sombreado en filas y columnas alternas con reglas de formato condicional y funciones integradas de Excel.

{{% /alert %}}

Este artículo utiliza las funciones integradas de Excel como ROW, COLUMN y MOD. Aquí hay algunos detalles de estas funciones para una mejor comprensión del fragmento de código proporcionado a continuación.

- La función **ROW()** devuelve el número de fila de una referencia de celda. Si se omite el parámetro de referencia, asume que la referencia es la dirección de la celda en la que se ha ingresado la función ROW.
- La función **COLUMN()** devuelve el número de columna de una referencia de celda. Si se omite el parámetro de referencia, asume que la referencia es la dirección de la celda en la que se ha ingresado la función COLUMN.
- La función **MOD()** devuelve el resto después de dividir un número por un divisor, donde el primer parámetro de la función es el valor numérico cuyo resto se desea encontrar y el segundo parámetro es el número utilizado para dividir el parámetro del número. Si el divisor es 0, devolverá el error #DIV/0!.

Comencemos a escribir algún código para lograr este objetivo con la ayuda de la API Aspose.Cells for C++.

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

    // Create an instance of Workbook
    Workbook book;

    // Access the Worksheet on which desired rule has to be applied
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add FormatConditions to the instance of Worksheet
    int idx = sheet.GetConditionalFormattings().Add();

    // Access the newly added FormatConditions via its index
    auto conditionCollection = sheet.GetConditionalFormattings().Get(idx);

    // Define a CellsArea on which conditional formatting will be applicable
    // The code creates a CellArea ranging from A1 to I20
    CellArea area = CellArea::CreateCellArea(u"A1", u"I20");

    // Add area to the instance of FormatConditions
    conditionCollection.AddArea(area);

    // Add a condition to the instance of FormatConditions
    // For this case, the condition type is expression, which is based on some formula
    idx = conditionCollection.AddCondition(FormatConditionType::Expression);

    // Access the newly added FormatCondition via its index
    FormatCondition formatCondition = conditionCollection.Get(idx);

    // Set the formula for the FormatCondition
    // Formula uses the Excel's built-in functions as discussed earlier in this article
    formatCondition.SetFormula1(u"=MOD(ROW(),2)=0");

    // Set the background color and pattern for the FormatCondition's Style
    formatCondition.GetStyle().SetBackgroundColor(Color::Blue());
    formatCondition.GetStyle().SetPattern(BackgroundType::Solid);

    // Save the result on disk
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

La siguiente captura de pantalla muestra la hoja de cálculo resultante cargada en la aplicación de Excel.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Para aplicar el sombreado a las columnas alternas, todo lo que tiene que hacer es cambiar la fórmula **=MOD(ROW(),2)=0** a **=MOD(COLUMN(),2)=0**, es decir, en lugar de obtener el índice de fila, modifique la fórmula para obtener el índice de columna. 
La hoja de cálculo resultante, en este caso, se verá como sigue.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="cpp" >}}
