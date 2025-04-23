---
title: Diferentes Formas de Guardar Archivos con C++
linktitle: Guardar archivos
type: docs
weight: 40
url: /es/cpp/different-ways-to-save-files/
description: Aspose.Cells for C++ puede guardar archivos en diferentes formatos. Guardar archivos como PDF. Guardar archivos como HTML. Guardar archivos como DOCX. Guardar archivos como PPTX. Guardar archivos como JSON. Guardar archivos como MHTML.
keywords: Aspose.Cells guarda Excel en PDF, HTML, JSON, CSV, TXT, XML, DOCX, PPTX, MHT, MHTML y otros usando C++, Guardar o Convertir Libro de Trabajo a PDF, HTML, JSON, TXT, SQL en C++.
---

{{% alert color="primary" %}}

Aspose.Cells hace posible crear y guardar archivos. Este artículo explica las varias maneras en las que los archivos pueden ser guardados.

{{% /alert %}}

## **Diferentes formas de guardar archivos**

Aspose.Cells proporciona el [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) que representa un archivo de Microsoft Excel y proporciona las propiedades y métodos necesarios para trabajar con archivos de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) proporciona el método [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) utilizado para guardar archivos de Excel. El método [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) tiene muchas sobrecargas que se utilizan para guardar archivos de diferentes formas.

El formato de archivo en el que se guarda el archivo está decidido por la enumeración [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)

|**Tipos de formato de archivo**|**Descripción**|
| :- | :- |
|CSV|Representa un archivo CSV|
|Excel97To2003|Representa un archivo de Excel 97 - 2003|
|Xlsx|Representa un archivo de Excel 2007 XLSX|
|Xlsm|Representa un archivo de Excel 2007 XLSM|
|Xltx|Representa una plantilla de Excel 2007 XLTX|
|Xltm|Representa un archivo habilitado para macros de Excel 2007 XLTM|
|Xlsb|Representa un archivo binario XLSB de Excel 2007|
|SpreadsheetML|Representa un archivo XML de hoja de cálculo|
|TSV|Representa un archivo de valores separados por tabulaciones|
|TabDelimited|Representa un archivo de texto delimitado por tabulaciones|
|ODS|Representa un archivo ODS|
|Html|Representa archivo(s) HTML|
|MHtml|Representa archivo(s) MHTML|
|Pdf|Representa un archivo PDF|
|XPS|Representa un documento XPS|
|TIFF|Representa el Formato de Archivo de Imágenes Etiquetado (TIFF)|

## **Cómo Guardar un Archivo en Diferentes Formatos**

Para guardar archivos en una ubicación de almacenamiento, especifique el nombre del archivo (junto con la ruta de almacenamiento) y el formato de archivo deseado (de la enumeración [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)) al llamar al método [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) del objeto [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).

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
    U16String filePath = srcDir + u"Book1.xls";

    // Load your source workbook
    Workbook workbook(filePath);

    // Save in Excel 97 to 2003 format
    workbook.Save(outDir + u".output.xls");
    // OR
    XlsSaveOptions xlsSaveOptions;
    workbook.Save(outDir + u".output.xls", xlsSaveOptions);

    // Save in Excel2007 xlsx format
    workbook.Save(outDir + u".output.xlsx", SaveFormat::Xlsx);

    // Save in Excel2007 xlsb format
    workbook.Save(outDir + u".output.xlsb", SaveFormat::Xlsb);

    // Save in ODS format
    workbook.Save(outDir + u".output.ods", SaveFormat::Ods);

    // Save in Pdf format
    workbook.Save(outDir + u".output.pdf", SaveFormat::Pdf);

    // Save in Html format
    workbook.Save(outDir + u".output.html", SaveFormat::Html);

    // Save in SpreadsheetML format
    workbook.Save(outDir + u".output.xml", SaveFormat::SpreadsheetML);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Cómo guardar un libro en formato PDF**
El formato de documento portátil (PDF) es un tipo de documento creado por Adobe a principios de los años 90. El propósito de este formato de archivo fue introducir un estándar para la representación de documentos y otros materiales de referencia en un formato independiente del software de aplicación, hardware y sistema operativo. El formato de archivo PDF tiene la capacidad completa de contener información como texto, imágenes, hipervínculos, campos de formulario, medios enriquecidos, firmas digitales, archivos adjuntos, metadatos, características geoespaciales y objetos 3D que pueden formar parte del documento fuente.

Los siguientes códigos muestran cómo guardar un libro como archivo PDF con Aspose.Cells:
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the Workbook object
    Workbook workbook;

    // Set value to Cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"Hello World!");

    // Save the workbook to PDF
    workbook.Save(u"pdf1.pdf");

    // Save as Pdf format compatible with PDFA-1a
    PdfSaveOptions saveOptions;
    saveOptions.SetCompliance(PdfCompliance::PdfA1a);

    workbook.Save(u"pdfa1a.pdf", saveOptions);

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Cómo guardar un libro en formato de texto o CSV**

A veces, deseas convertir o guardar un libro con múltiples hojas de cálculo en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), tanto Microsoft Excel como Aspose.Cells guardan por defecto el contenido de la hoja de cálculo activa únicamente.

El siguiente ejemplo de código explica cómo guardar un libro de trabajo completo en formato de texto. Cargue el libro de trabajo fuente que podría ser cualquier archivo de hoja de cálculo de Microsoft Excel u OpenOffice (por ejemplo, XLS, XLSX, XLSM, XLSB, ODS, etc.) con cualquier número de hojas de trabajo.

Cuando se ejecuta el código, convierte los datos de todas las hojas del libro de trabajo al formato TXT.

Puede modificar el mismo ejemplo para guardar su archivo en CSV. Por defecto, [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) es la coma, así que no especifique un separador al guardar en formato CSV. Tenga en cuenta: si usa la versión de evaluación y aunque la propiedad [**TxtSaveOptions.GetExportAllSheets()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getexportallsheets/) esté configurada en true, el programa solo exportará una hoja de cálculo.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output text file
    U16String outputFilePath = outDir + u"out.txt";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook data saved to text file successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Cómo guardar archivo en archivos de texto con un separador personalizado**

Los archivos de texto contienen datos de la hoja de cálculo sin formato. El archivo es un tipo de archivo de texto sin formato que puede tener algunos delimitadores personalizados entre sus datos.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and open the file from its path
    Workbook wb(filePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';');

    // Save the file with the options
    wb.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Cómo guardar archivo en un flujo de datos**

Para guardar archivos en un flujo de datos, crea un objeto *MemoryStream* o *FileStream* y guarda el archivo en ese objeto de flujo llamando al método [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) del objeto [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Especifica el formato de archivo deseado al llamar al método [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) usando la enumeración [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/).

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

## **Cómo guardar archivo de Excel en archivos HTML y MHT**
Aspose.Cells puede simplemente guardar un archivo de Excel, JSON, CSV u otros archivos que podrían ser cargados por Aspose.Cells como archivos .html y .mht.
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"Book1.xlsx");
    Workbook workbook(inputFilePath);

    // Save file to MHTML format
    U16String outputFilePath(u"out.mht");
    workbook.Save(outputFilePath);

    std::cout << "File saved successfully to MHTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **Cómo guardar archivo de Excel en OpenOffice (ODS, SXC, FODS, OTS)**
Podemos guardar los archivos en formatos de OpenOffice: ODS, SXC, FODS, OTS, etc.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file
    workbook.Save(u"Out.ods");

    // Save as sxc file
    workbook.Save(u"Out.sxc");

    // Save as fods file
    workbook.Save(u"Out.fods");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Cómo guardar archivo de Excel en JSON o XML**

JSON (Notación de Objetos de JavaScript) es un formato de archivo estándar abierto para compartir datos que utiliza texto legible para almacenar y transmitir datos. Los archivos JSON se almacenan con la extensión .json. JSON requiere menos formato y es una buena alternativa para XML. JSON se deriva de JavaScript, pero es un formato de datos independiente del lenguaje. La generación y análisis de JSON son compatibles con muchos lenguajes de programación modernos. application/json es el tipo de medio utilizado para JSON.

Aspose.Cells es compatible con la posibilidad de guardar archivos en JSON o XML.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output json file
    U16String outputFilePath = outDir + u"book1.json";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


## **Temas avanzados**
- [Ajustar el nivel de compresión del libro de trabajo](/cells/es/cpp/adjust-workbook-compression-level/)
- [Guardar libro de trabajo en formato de hoja de cálculo de Open XML estricto](/cells/es/cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Guardando archivo en objeto de respuesta](/cells/es/cpp/saving-file-to-response-object/)
