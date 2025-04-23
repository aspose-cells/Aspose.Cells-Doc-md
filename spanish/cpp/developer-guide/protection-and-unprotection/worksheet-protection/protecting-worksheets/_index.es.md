---
title: Proteger hojas de cálculo con C++
linktitle: Protección de hojas de cálculo
type: docs
weight: 10
url: /es/cpp/protecting-worksheets/
description: Aprenda cómo proteger hojas de cálculo, filas, columnas y celdas específicas en archivos de Microsoft Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Cuando una hoja de cálculo está protegida, las acciones que un usuario puede realizar están restringidas. Por ejemplo, no pueden ingresar datos, insertar o eliminar filas o columnas, etc.

{{% /alert %}}

## **Proteger hojas de cálculo**

### **Introducción**

Las opciones generales de protección en Microsoft Excel son:

- Contenidos
- Objetos
- Escenarios

Las hojas de cálculo protegidas no ocultan ni protegen datos sensibles, por lo que es diferente del cifrado de archivos. Generalmente, la protección de la hoja de cálculo es adecuada para fines de presentación. Evita que el usuario final modifique los datos, el contenido y el formato en la hoja de cálculo.

### **Proteger una hoja de cálculo**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

La clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) proporciona el método [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) que se utiliza para aplicar protección en la hoja de cálculo. El método [**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) acepta los siguientes parámetros:

- Tipo de protección, el tipo de protección a aplicar en la hoja de cálculo. El tipo de protección se aplica con la ayuda de la enumeración [**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/).
- Nueva contraseña, la nueva contraseña utilizada para proteger la hoja de cálculo.
- Contraseña antigua, la contraseña antigua, si la hoja de cálculo ya está protegida con contraseña. Si la hoja de cálculo no está protegida, simplemente pase nula.

La enumeración [**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/) contiene los siguientes tipos de protecciones predefinidos:

|**Tipos de protección**|**Descripción**|
| :- | :- |
|All|El usuario no puede modificar nada en esta hoja de cálculo|
|Contents|El usuario no puede introducir datos en esta hoja de cálculo|
|Objects|El usuario no puede modificar objetos de dibujo|
|Scenarios|El usuario no puede modificar escenarios guardados|
|Structure|El usuario no puede modificar la estructura|
|Windows|La protección se aplica a las ventanas|
|None|No se aplica protección|

El ejemplo a continuación muestra cómo proteger una hoja de cálculo con una contraseña.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook from the input file
    Workbook excel(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Protecting the worksheet with a password
    worksheet.Protect(ProtectionType::All, u"aspose", nullptr);

    // Saving the modified Excel file in default format
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    std::cout << "Worksheet protected and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Después de que se use el código anterior para proteger la hoja de cálculo, puede verificar la protección en la hoja de cálculo abriéndola. Una vez que abra el archivo e intente agregar datos a la hoja de cálculo, verá el siguiente cuadro de diálogo:

|**Un aviso de diálogo de que el usuario no puede modificar la hoja de cálculo**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Para trabajar en la hoja de cálculo, desprotege la hoja de cálculo seleccionando **Protección**, luego **Desproteger hoja** del elemento de menú **Herramientas**.

Después de seleccionar la opción Desproteger hoja, se abrirá un cuadro de diálogo que te pedirá que ingreses la contraseña para que puedas trabajar en la hoja de cálculo como se muestra a continuación:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Proteger algunas celdas en la hoja de cálculo utilizando Microsoft Excel**

Puede haber ciertos escenarios en los que necesites bloquear solo algunas celdas en la hoja de cálculo. Si deseas bloquear celdas específicas en la hoja de cálculo, debes desbloquear todas las demás celdas de la hoja de cálculo. Todas las celdas de una hoja de cálculo ya están inicializadas para bloquearse, puedes verificar esto abriendo cualquier archivo de Excel en MS Excel y haciendo clic en **Formato | Celdas...** para mostrar el cuadro de diálogo **Formato de celdas** y luego hacer clic en la pestaña **Protección** y ver que hay una casilla de verificación etiquetada como "Bloqueada" marcada de manera predeterminada.

Los siguientes puntos describen cómo bloquear algunas celdas usando MS Excel. Este método se aplica a las versiones de Microsoft Office Excel 97, 2000, 2002, 2003 y posteriores.

1. Selecciona toda la hoja de cálculo haciendo clic en el botón **Seleccionar todo** (el rectángulo gris directamente arriba del número de fila para la fila 1 y a la izquierda de la letra de la columna A).
1. Haz clic en **Celdas** en el menú **Formato**, haz clic en la pestaña **Protección**, y luego desmarca la casilla de verificación **Bloqueada**.
   Esto desbloquea todas las celdas en la hoja de cálculo
   Si el comando **Celdas** no está disponible, es posible que partes de la hoja de cálculo ya estén bloqueadas. En el menú **Herramientas**, apunta a **Protección**, y luego haz clic en **Desproteger hoja**.
1. Selecciona solo las celdas que deseas bloquear y repite el paso 2, pero esta vez selecciona la casilla de verificación **Bloqueada**.
1. En el menú **Herramientas**, apunta a **Protección**, haz clic en **Proteger hoja** y luego haz clic en **Aceptar**.
1. En el cuadro de diálogo **Proteger hoja**, tienes la opción de especificar una contraseña y seleccionar los elementos que quieres que los usuarios puedan cambiar.

### **Proteger algunas celdas en la hoja de cálculo utilizando Aspose Cells**

En este método, solo utilizamos la API de Aspose.Cells para realizar la tarea.

Ejemplo: El siguiente ejemplo muestra cómo proteger algunas celdas en la hoja de cálculo. Desbloquea todas las celdas en la hoja de cálculo primero y luego bloquea 3 celdas (A1, B1, C1) en ella. Finalmente, protege la hoja de cálculo. El objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) contiene una propiedad booleana, [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Puedes establecer la propiedad [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) en verdadero o falso y aplicar el método *Columna/Fila.AplicarEstilo()* para bloquear o desbloquear la fila/columna con los atributos deseados.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for(int i = 0; i <= 255; ++i)
    {
        Style style = sheet.GetCells().GetColumns().Get(i).GetStyle();
        style.SetIsLocked(false);

        StyleFlag flag;
        flag.SetLocked(true);

        sheet.GetCells().ApplyColumnStyle(i, style, flag);
    }

    auto lockCell = [&](const U16String& cellRef)
    {
        Style style = sheet.GetCells().Get(cellRef).GetStyle();
        style.SetIsLocked(true);
        sheet.GetCells().Get(cellRef).SetStyle(style);
    };

    lockCell(u"A1");
    lockCell(u"B1");
    lockCell(u"C1");

    sheet.Protect(ProtectionType::All);

    U16String outputPath = outDir + u"output.out.xls";
    wb.Save(outputPath, SaveFormat::Excel97To2003);

    std::cout << "Protected workbook created successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Proteger una fila en la hoja de cálculo**

Aspose.Cells te permite bloquear fácilmente cualquier fila en la hoja de cálculo. Aquí, podemos utilizar el método [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/applystyle/) de la clase [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) para aplicar [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) a una fila específica en la hoja de cálculo. Este método toma dos argumentos: un objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) y un objeto [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) que tiene todos los miembros relacionados con el formato aplicado.

El siguiente ejemplo muestra cómo proteger una fila en la hoja de cálculo. Desbloquea todas las celdas en la hoja de cálculo primero y luego bloquea la primera fila en ella. Finalmente, protege la hoja de cálculo. El objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) contiene una propiedad booleana, [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Puedes establecer la propiedad [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) en verdadero o falso para bloquear o desbloquear la fila/columna utilizando el objeto [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Column column = sheet.GetCells().GetColumns().Get(i);
        Style style = column.GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        column.ApplyStyle(style, flag);
    }

    Row firstRow = sheet.GetCells().GetRows().Get(0);
    Style rowStyle = firstRow.GetStyle();
    rowStyle.SetIsLocked(true);

    StyleFlag rowFlag;
    rowFlag.SetLocked(true);
    sheet.GetCells().ApplyRowStyle(0, rowStyle, rowFlag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Proteger una columna en la hoja de cálculo**

Aspose.Cells te permite bloquear fácilmente cualquier columna en la hoja de cálculo. Aquí, podemos utilizar el método [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/column/applystyle/) de la clase [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) para aplicar [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) a una columna específica en la hoja de cálculo. Este método toma dos argumentos: un objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) y un objeto [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) que tiene todos los miembros relacionados con el formato aplicado.

El siguiente ejemplo muestra cómo proteger una columna en la hoja de cálculo. Desbloquea todas las celdas en la hoja de cálculo primero y luego bloquea la primera columna en ella. Finalmente, protege la hoja de cálculo. El objeto [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) contiene una propiedad booleana, [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/). Puede establecer la propiedad [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/) en true o false para bloquear o desbloquear la fila/columna utilizando el objeto [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Style style = sheet.GetCells().GetColumns().Get((uint8_t)i).GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        sheet.GetCells().GetColumns().Get((uint8_t)i).ApplyStyle(style, flag);
    }

    Style style = sheet.GetCells().GetColumns().Get(0).GetStyle();
    style.SetIsLocked(true);

    StyleFlag flag;
    flag.SetLocked(true);
    sheet.GetCells().GetColumns().Get(0).ApplyStyle(style, flag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Permitir a los usuarios editar rangos**

El siguiente ejemplo muestra cómo permitir a los usuarios editar un rango en una hoja de cálculo protegida.

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

    // Instantiate a new Workbook
    Workbook book;

    // Get the first (default) worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Get the Allow Edit Ranges
    ProtectedRangeCollection allowRanges = sheet.GetAllowEditRanges();

    // Create the range and get the ProtectedRange
    int idx = allowRanges.Add(u"r2", 1, 1, 3, 3);
    ProtectedRange protectedRange = allowRanges.Get(idx);

    // Specify the password
    protectedRange.SetPassword(u"123");

    // Protect the sheet
    sheet.Protect(ProtectionType::All);

    // Save the Excel file
    book.Save(outDir + u"protectedrange.out.xls");

    std::cout << "Protected range created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
