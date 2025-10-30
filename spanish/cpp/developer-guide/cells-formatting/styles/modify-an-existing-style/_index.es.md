---
title: Modificar un estilo existente con C++
description: Aspose.Cells es una biblioteca en C++ para trabajar con archivos de hojas de cálculo que permite a los usuarios modificar estilos de celdas existentes. Este artículo presentará cómo modificar un estilo de celda existente con la biblioteca Aspose.Cells para que los usuarios puedan cambiar la apariencia de las celdas según lo requieran.
keywords: Modificar estilos existentes, personalizar la apariencia de su aplicación, guías, tutoriales, documentación de ayuda, documentación de desarrollo, referencias de API, código de muestra, descargas, soporte.
type: docs
weight: 90
url: /es/cpp/modify-an-existing-style/
---

{{% alert color="primary" %}}

Para aplicar las mismas opciones de formateo a las celdas, cree un nuevo objeto de estilo de formateo. Un objeto de estilo de formateo es una combinación de características de formateo, como la fuente, el tamaño de la fuente, la indentación, el número, los bordes, los patrones, etc., nombrados y almacenados como un conjunto. Cuando se aplica, se aplican todas las características de formato en ese estilo.

También puede utilizar un estilo existente, guardarlo con el libro y utilizarlo para formatear la información con las mismas características.

Cuando las celdas no tienen formato explícito, se aplica el **Estilo Normal** (el estilo predeterminado del libro). Microsoft Excel predefine varios estilos además del estilo Normal, incluyendo Coma, Moneda y Porcentaje.

Aspose.Cells permite modificar cualquiera de estos estilos u cualquier otro estilo que defina con las características deseadas.

{{% /alert %}}

## **Usar Microsoft Excel**

Para actualizar un estilo en Microsoft Excel 97-2003:

1. En el menú **Formato**, haga clic en **Estilo**.
1. Seleccione el estilo que desea modificar de la lista **Nombre del estilo**.
1. Haga clic en **Modificar**.
1. Seleccione las opciones de estilo que desee utilizando las pestañas en el cuadro de diálogo Formato de celdas.
1. Haz clic en **Aceptar**.
1. En **El estilo incluye**, especifique las características del estilo que desee.
1. Haga clic en **Aceptar** para guardar el estilo y aplicarlo al rango seleccionado.

## **Usar Aspose.Cells**

Los siguientes ejemplos muestran cómo usar el método [**Style.Update**](https://reference.aspose.com/cells/cpp/aspose.cells/style/update/).

### **Creación y Modificación de un Estilo**

Este ejemplo crea un objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/), lo aplica a un rango de celdas y modifica el objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Las modificaciones se aplican automáticamente a la celda y al rango al que se aplicó el estilo.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook workbook;

    // Create a new style object.
    Style style = workbook.CreateStyle();

    // Set the number format.
    style.SetNumber(14);

    // Set the font color to red color.
    style.GetFont().SetColor(Color::Red());

    // Name the style.
    style.SetName(u"Date1");

    // Get the first worksheet cells.
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Specify the style (described above) to A1 cell.
    cells.Get(u"A1").SetStyle(style);

    // Create a range (B1:D1).
    Range range = cells.CreateRange(u"B1", u"D1");

    // Initialize styleflag object.
    StyleFlag flag;

    // Set all formatting attributes on.
    flag.SetAll(true);

    // Apply the style (described above) to the range.
    range.ApplyStyle(style, flag);

    // Modify the style (described above) and change the font color from red to black.
    style.GetFont().SetColor(Color::Black());

    // Done! Since the named style (described above) has been set to a cell and range,
    // The change would be reflected (new modification is implemented) to cell (A1) and range (B1:D1).
    style.Update();

    // Save the excel file.
    U16String dataDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(dataDir + u"book_styles.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Modificación de un Estilo Existente**

Este ejemplo utiliza un archivo de Excel de plantilla simple en el que ya se ha aplicado un estilo llamado Porcentaje a un rango. El ejemplo:

1. obtiene el estilo,
1. crea un objeto de estilo y
1. modifica el formato del estilo.

Las modificaciones se aplican automáticamente al rango al que se aplicó el estilo.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"book1.xlsx";

    /*
     * Create a workbook.
     * Open a template file. 
     * In the book1.xlsx file, we have applied Ms Excel's 
     * Named style i.e., "Percent" to the range "A1:C8".
    */
    Workbook workbook(inputPath);

    // We get the Percent style and create a style object.
    Style style = workbook.GetNamedStyle(u"Percent");

    // Change the number format to "0.00%".
    style.SetNumber(11);

    // Set the font color.
    Color redColor = Color::Red();
    style.GetFont().SetColor(redColor);

    // Update the style. so, the style of range "A1:C8" will be changed too.
    style.Update();

    // Save the excel file.	
    U16String outputPath = srcDir + u"book2.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
