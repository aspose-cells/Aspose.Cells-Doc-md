---
title: Desproteger una hoja de cálculo con C++
linktitle: Desproteger una hoja de cálculo
type: docs
weight: 20
url: /es/cpp/unprotect-a-worksheet/
description: Aprenda cómo desproteger una hoja de cálculo usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Si un desarrollador necesita eliminar la protección de una hoja protegida en tiempo de ejecución para realizar algunos cambios en el archivo, esto se puede hacer fácilmente con Aspose.Cells.

{{% /alert %}}

## **Desproteger una Hoja de Cálculo**

### **Usar Microsoft Excel**

Para quitar la protección de una hoja de cálculo:

Desde el menú **Herramientas**, seleccione **Protección** seguido de **Desproteger hoja**. La protección se eliminará a menos que la hoja esté protegida con contraseña. En ese caso, aparece un diálogo que solicita la contraseña. Ingresa la contraseña y la hoja quedará desprotegida.

### **Desproteger una hoja de cálculo simplemente protegida utilizando Aspose.Cells**

Una hoja de cálculo puede ser desprotegida llamando al método [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) de la clase [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Una hoja protegida simple es aquella que no está protegida con contraseña. Este tipo de hojas puede ser desprotegido llamando al método [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) sin pasar ningún parámetro.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create a Workbook object
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unprotect the worksheet without a password
    worksheet.Unprotect();

    // Save the Workbook in Excel97-2003 format
    workbook.Save(outputFilePath, SaveFormat::Excel97To2003);

    std::cout << "Worksheet unprotected and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Desproteger una hoja de cálculo protegida con contraseña utilizando Aspose.Cells**

Una hoja protegida con contraseña es aquella que está protegida con una contraseña. Tales hojas pueden ser desprotegidas llamando a una versión sobrecargada del método [**Unprotect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unprotect/) que recibe la contraseña como parámetro.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Unprotecting the worksheet with a password
    worksheet.Unprotect(u"");

    // Save Workbook
    workbook.Save(outputFilePath);

    std::cout << "Worksheet unprotected and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
