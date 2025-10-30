---
title: Establecer formatos condicionales en archivos de Excel y ODS con C++
linktitle: Formatos condicionales
type: docs
weight: 60
url: /es/cpp/conditional-formatting/
description: Cómo aplicar formatos condicionales en archivos de Excel y ODS usando C++.
keywords: aplicar formatos condicionales 
---

## **Introducción**

El formato condicional es una característica avanzada de Microsoft Excel que te permite aplicar formatos a una celda o rango de celdas y que ese formato cambie dependiendo del valor de la celda o del valor de una fórmula. Por ejemplo, puedes hacer que una celda aparezca en negrita solo cuando el valor de la celda sea mayor que 500. Cuando el valor de la celda cumple la condición, se aplica el formato especificado a la celda. Si el valor de la celda no cumple la condición del formato, se utiliza el formato predeterminado de la celda. En Microsoft Excel, selecciona **Formato**, luego **Formato condicional** para abrir el cuadro de diálogo Formato condicional.

Aspose.Cells admite aplicar formato condicional a las celdas en tiempo de ejecución. Este artículo explica cómo. También explica cómo calcular el color utilizado por Excel para el formato condicional de escala de color.

## **Aplicar formato condicional**

Aspose.Cells admite el formato condicional de varias maneras:

- Usando una hoja de cálculo de diseñador
- Usando el método de copia.
- Creando formato condicional en tiempo de ejecución.

### **Usar la Hoja de Cálculo de Diseñador**

Los desarrolladores pueden crear una hoja de cálculo de diseñador que contenga formato condicional en Microsoft Excel y luego abrir esa hoja de cálculo con Aspose.Cells. Aspose.Cells carga y guarda la hoja de cálculo de diseñador, conservando cualquier configuración de formato condicional.

### **Usando el Método de Copia**

Aspose.Cells permite a los desarrolladores copiar la configuración de formato condicional de una celda a otra en la hoja de cálculo llamando al método [**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/).

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Open the Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    int totalRowCount = 0;

    // Iterate through all worksheets in the workbook
    for (int i = 0; i < workbook.GetWorksheets().GetCount(); i++)
    {
        Worksheet sourceSheet = workbook.GetWorksheets().Get(i);

        // Get the maximum display range of the source sheet
        Range sourceRange = sourceSheet.GetCells().GetMaxDisplayRange();

        // Create a destination range in the first worksheet
        Range destRange = worksheet.GetCells().CreateRange(
            sourceRange.GetFirstRow() + totalRowCount, 
            sourceRange.GetFirstColumn(),
            sourceRange.GetRowCount(), 
            sourceRange.GetColumnCount());

        // Copy data from source range to destination range
        destRange.Copy(sourceRange);

        // Update the total row count
        totalRowCount += sourceRange.GetRowCount();
    }

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Aplicar formato condicional en tiempo de ejecución**

Aspose.Cells te permite tanto agregar como eliminar formato condicional en tiempo de ejecución. Los ejemplos de código a continuación muestran cómo establecer el formato condicional:

1. Instanciar un libro de trabajo.
1. Agregar un formato condicional vacío.
1. Establecer el rango al que debe aplicarse el formato.
1. Definir las condiciones de formato.
1. Guarde el archivo.

Después de este ejemplo vienen varios ejemplos más pequeños que muestran cómo aplicar configuraciones de fuente, configuraciones de bordes y patrones.

Microsoft Excel 2007 agregó un formato condicional más avanzado que también es compatible con Aspose.Cells. Los ejemplos aquí ilustran cómo usar formatos simples. Los ejemplos de Microsoft Excel 2007 muestran cómo aplicar formatos condicionales más avanzados.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Instantiating a Workbook object
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range.
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;
    fcs.AddArea(ca);

    ca = CellArea();
    ca.StartRow = 1;
    ca.EndRow = 1;
    ca.StartColumn = 1;
    ca.EndColumn = 1;
    fcs.AddArea(ca);

    // Adds condition.
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"=A2", u"100");

    // Adds condition.
    int conditionIndex2 = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Sets the background color.
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().SetBackgroundColor(Color::Red());

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Establecer fuente**

```c++
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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style of the cell
    Style style = cell.GetStyle();

    // Set the font weight to bold
    Font font = style.GetFont();
    font.SetIsBold(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Solo puedes cambiar el estilo de la fuente, el color del texto, el subrayado y la tachadura.

{{% /alert %}}

### **Establecer borde**

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Set the conditional format range
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 5;
    ca.StartColumn = 0;
    ca.EndColumn = 3;
    fcs.AddArea(ca);

    // Add condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");

    // Set the background color
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Dashed);
    fc.GetStyle().GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Dashed);

    fc.GetStyle().GetBorders().Get(BorderType::LeftBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::RightBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::TopBorder).SetColor(Color{0, 255, 255, 255});
    fc.GetStyle().GetBorders().Get(BorderType::BottomBorder).SetColor(Color{255, 255, 0, 255});

    // Save the workbook
    workbook.Save(outDir + u"output.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Solo puedes utilizar estilos de líneas delgadas para el borde del contorno. No se permiten líneas diagonales.

{{% /alert %}}

### **Establecer patrón**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Adds an empty conditional formatting
    int index = sheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcs = sheet.GetConditionalFormattings().Get(index);

    // Sets the conditional format range
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 5;
    ca.StartColumn = 0;
    ca.EndColumn = 3;
    fcs.AddArea(ca);

    // Adds condition
    int conditionIndex = fcs.AddCondition(FormatConditionType::CellValue, OperatorType::Between, u"50", u"100");
    FormatCondition fc = fcs.Get(conditionIndex);
    fc.GetStyle().SetPattern(BackgroundType::ReverseDiagonalStripe);
    fc.GetStyle().SetForegroundColor(Color{255, 255, 0, 255});
    fc.GetStyle().SetBackgroundColor(Color{0, 255, 255, 255});

    // Save the workbook
    workbook.Save(outDir + u"output.xlsx");

    std::cout << "Conditional formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Temas avanzados**
- [Agregar escalas de colores de 2 colores y 3 colores con formato condicional](/cells/es/cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Aplicar formato condicional avanzado](/cells/es/cpp/apply-advanced-conditional-formatting/)
- [Aplicar formato condicional en hojas de cálculo](/cells/es/cpp/apply-conditional-formatting-in-worksheets/)
- [Aplicar sombreado a filas y columnas alternas con formato condicional](/cells/es/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Generar imágenes de barras de datos de formato condicional](/cells/es/cpp/generate-conditional-formatting-databars-images/)
- [Obtener conjuntos de iconos, barras de datos o escalas de colores utilizados en el formato condicional](/cells/es/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)
{{< app/cells/assistant language="cpp" >}}
