---
title: Guardar archivo en objeto de respuesta con C++
linktitle: Guardando archivo en objeto de respuesta
type: docs
weight: 50
url: /es/cpp/saving-file-to-response-object/
description: Aprenda cómo guardar archivos dinámicamente y enviarlos directamente a un navegador cliente usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells hace posible manipular archivos. Este artículo explica las diferentes formas en las que los archivos se pueden guardar en un objeto de respuesta.

{{% /alert %}}

## **Guardando archivo en objeto de respuesta**

También es posible generar un archivo dinámicamente y enviarlo directamente al navegador del cliente. Para hacerlo, use una versión sobrecargada especial del método [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) que acepta los siguientes parámetros:

- Objeto **HttpResponse**.
- Nombre de archivo.
- [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/), el tipo de disposición de contenido del archivo de salida.
- [**SaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/saveoptions/), el tipo de formato de archivo.

La enumeración [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/) determina si el archivo que se envía al navegador proporciona la opción de abrirse directamente en el navegador o en una aplicación asociada con .xls/.xlsx u otra extensión.

La enumeración contiene los siguientes tipos de guardado predefinidos:

|**Tipo**|**Descripción**|
| :- | :- |
|Archivo adjunto|Envía la hoja de cálculo al navegador y se abre en una aplicación como un archivo adjunto asociado con .xls/.xlsx u otras extensiones|
|En línea|Envía el documento al navegador y presenta una opción para guardar la hoja de cálculo en el disco o abrir dentro del navegador|

### **Archivos XLS**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Save in Excel2003 XLS format
    U16String outputPath = outDir + u"output.xls";
    XlsSaveOptions saveOptions;
    workbook.Save(outputPath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Archivos XLSX**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook;

    // Save in Xlsx format
    OoxmlSaveOptions saveOptions;
    workbook.Save(outputFilePath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Archivos PDF**

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

    // Path of output PDF file
    U16String outputPdf = outDir + u"output.pdf";

    // Creating a Workbook object
    Workbook workbook;

    // Save in Pdf format
    PdfSaveOptions saveOptions;
    workbook.Save(outputPdf, saveOptions);

    Aspose::Cells::Cleanup();
}
```

### **Nota**

Debido al objeto "System.Web.HttpResponse" que no está incluido en .NET5 y .Netstandard,
Por lo tanto, esta función no existe en la versión Aspose.Cells .NET5 y .Netstandard, puede consultar el siguiente código para guardar el archivo en el flujo, y luego realizar operaciones en el flujo.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save workbook to memory stream with explicit FileFormatType
    Vector<uint8_t> data = workbook.SaveToStream();

    std::cout << "File size: " << data.GetLength() << std::endl;

    Cleanup();

    return 0;
}
```
