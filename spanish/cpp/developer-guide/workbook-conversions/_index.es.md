---
title: Convertir Excel a Pdf, Imagen y otros formatos con C++
linktitle: Conversiones de libros de trabajo
type: docs
weight: 65
url: /es/cpp/convert-workbook-to-different-formats/
description: Convertir archivos de Excel a Word, Excel, PowerPoint, PDF, CSV, JPG, HTML, MHT, ODS, BMP, PNG, SVG, TIFF, XPS, JSON, SQL, XML y más usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells soporta la conversión entre muchos formatos. Técnicamente, la conversión implica cargar un libro en un formato de archivo y guardarlo en otro.

{{% /alert %}}

## **Convertir libro de trabajo de Excel a PDF**

Los archivos PDF son ampliamente utilizados para intercambiar documentos entre organizaciones, sectores gubernamentales y particulares. Es un formato estándar de documento, y a menudo se pide a los desarrolladores de software que encuentren una forma de convertir archivos de Microsoft Excel en documentos PDF.

Aspose.Cells admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Instantiate the Workbook object and open an Excel file
    Workbook workbook(u"Book1.xlsx");

    // Save the document in PDF format
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    std::cout << "Excel file converted to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir Libro de Excel a JPG**
Aspose.Cells admite la conversión de archivos de Excel a JPG.
El ejemplo de código a continuación muestra cómo guardar un libro como JPG.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String inputFilePath(u"Book1.xlsx");
    Workbook book(inputFilePath);

    U16String outputFilePath(u"Image1.jpg");
    book.Save(outputFilePath, SaveFormat::Jpg);

    std::cout << "Workbook converted to JPG image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir Libro de Excel a Imagen**
Aspose.Cells admite la conversión de archivos de Excel a imágenes.
El ejemplo de código a continuación muestra cómo guardar un libro como imágenes.

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook(srcDir + u"Book1.xlsx");

    workbook.Save(outDir + u"Image1.bmp", SaveFormat::Bmp);
    workbook.Save(outDir + u"Image1.jpg", SaveFormat::Jpg);
    workbook.Save(outDir + u"Image1.png", SaveFormat::Png);
    workbook.Save(outDir + u"Image1.emf", SaveFormat::Emf);
    workbook.Save(outDir + u"Image1.gif", SaveFormat::Gif);

    std::cout << "Workbook converted to images successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convirtiendo Libro de Excel a XPS**

El formato de documento XPS consta de marcado XML estructurado que define el diseño de un documento y la apariencia visual de cada página, junto con reglas de renderizado para distribuir, archivar, renderizar, procesar e imprimir documentos.

El lenguaje de marcado para XPS es un subconjunto de XAML, lo que permite incorporar elementos gráficos vectoriales en los documentos, usando XAML para marcar las primitivas de Windows Presentation Foundation (WPF). Los elementos utilizados se describen en términos de rutas y otras primitivas geométricas.

Un archivo XPS es, en realidad, un archivo ZIP en formato Unicode que utiliza las Normas de Empaquetado Abierto, que contiene los archivos que conforman el documento. Estos incluyen un archivo de marcado XML para cada página, texto, fuentes incrustadas, imágenes rasterizadas, gráficos vectoriales 2D, así como información de gestión de derechos digitales. El contenido de un archivo XPS se puede examinar simplemente abriéndolo en una aplicación que soporte archivos ZIP.

A partir de Aspose.Cells 6.0.0, se admite la conversión de Microsoft Excel a XPS.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xls";
    Workbook workbook(inputFilePath);

    Worksheet sheet = workbook.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    SheetRender sr(sheet, options);
    sr.ToImage(0, outDir + u"out_image.png");

    XpsSaveOptions xpsOptions;
    workbook.Save(outDir + u"out_whole_printingxps.out.xps", xpsOptions);

    std::cout << "Files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir Excel a Ods, Sxc y Fods (OpenOffice / LibreOffice Calc)**
Aspose.Cells soporta la conversión de archivos de Excel a archivos Ods, Sxc y Fods. El ejemplo de código a continuación muestra cómo convertir la [plantilla](book1.xlsx) a archivos Ods, Sxc y Fods.

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

## **Convirtiendo Libro de Excel a Archivos MHTML**

MHTML combina HTML normal con recursos externos (es decir, contenido que suele estar vinculado, como imágenes, animaciones, audio, etc.) en un solo archivo. Se utilizan para correos electrónicos con la extensión de archivo .mht.

Aspose.Cells admite la lectura y escritura de archivos MHTML.

El ejemplo de código a continuación muestra cómo guardar un libro como un archivo MHTML.

```cpp
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

    // Specify the HTML Saving Options
    HtmlSaveOptions sv(SaveFormat::MHtml);

    // Instantiate a workbook and open the template XLSX file
    Workbook wb(filePath);

    // Save the MHT file
    wb.Save(filePath + u".out.mht", sv);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convirtiendo Libro de Excel a HTML**

La API de Aspose.Cells ofrece soporte para exportar hojas de cálculo a formato HTML. Para esto, Aspose.Cells usa la clase [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/) para ofrecer flexibilidad en el control de varios aspectos del HTML de salida.

El ejemplo de código a continuación muestra cómo guardar un libro como un archivo HTML.

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

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"ConvertingToHTMLFiles_out.html";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in HTML format
    wb.Save(outputFilePath, SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Configuración de las Preferencias de Imagen para HTML**

A partir de la versión 8.0.2, Aspose.Cells ha expuesto [**GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) para la clase [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/), permitiendo a los desarrolladores especificar preferencias de imagen al guardar hojas de cálculo en formato HTML.

A continuación, se detallan algunos de los ajustes de imagen que se pueden aplicar:

- [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/): Especifica el tipo de imagen. Por favor, tenga en cuenta que todas las formas, incluidos los gráficos, se renderizan como imágenes en el HTML de salida.
- [**GetQuality()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getquality/): Especifica la calidad de la imagen entre 0 y 100 cuando [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) se especifica como Jpeg.
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/): Obtiene o establece la resolución vertical de la imagen en puntos por pulgada.
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/): Obtiene o establece la resolución horizontal de la imagen en puntos por pulgada.
- [**TiffCompression**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/): Obtiene o establece el tipo de compresión para las imágenes cuando [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) se especifica como Tiff.
- [**GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/): Indica si el fondo de una imagen debe ser transparente cuando se especifica ImageFormat como Png.

El código a continuación demuestra cómo usar [**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) para especificar diferentes preferencias.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"Book1.xlsx";

    Workbook book(filePath);
    HtmlSaveOptions saveOptions(SaveFormat::Html);

    saveOptions.GetImageOptions().SetImageType(ImageType::Png);

    book.Save(outDir + u"output.html", saveOptions);

    std::cout << "Spreadsheet converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir Libro de Excel a Markdown**

La API de Aspose.Cells soporta la exportación de hojas de cálculo a formato Markdown. Para exportar la hoja de cálculo activa a Markdown, pase [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) como el segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). También puede usar la clase [**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/) para especificar configuraciones adicionales para exportar la hoja a Markdown.

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a Markdown usando el miembro del enumerador [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). Por favor, consulte el [archivo Markdown de salida](md_sample.txt) generado por el código como referencia.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Markdown file
    U16String outputFilePath = outDir + u"Book1.md";

    // Create workbook from the input Excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as Markdown
    workbook.Save(outputFilePath, SaveFormat::Markdown);

    std::cout << "Workbook saved as Markdown successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir Libro de Excel a JSON**

Aspose.Cells soporta convertir un libro en un archivo JSON (JavaScript Object Notation).

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a JSON usando el miembro del enumerador [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). Por favor, consulte el código para convertir el [archivo fuente](Book1.xlsx) al [archivo JSON de salida](Book1.Json) generado por el código como referencia.

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

## **Convertir Excel a XML**
Aspose.Cells admite la conversión de un libro de trabajo a XML de Hoja de Cálculo Excel 2003 y datos XML sin formato.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath = u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save as Excel 2003 Spreadsheet XML
    U16String outputFilePath1 = u"Spreadsheet.xml";
    workbook.Save(outputFilePath1);

    // Save as plain XML data
    U16String outputFilePath2 = u"data.xml";
    XmlSaveOptions xmlSaveOptions;
    workbook.Save(outputFilePath2, xmlSaveOptions);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir libro de Excel a TIFF**
Aspose.Cells admite la conversión de un libro de trabajo a un archivo TIFF.

El fragmento de código a continuación muestra cómo convertir Excel a TIFF:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open a template excel file
    U16String inputFilePath(u"Book1.xlsx");
    Workbook book(inputFilePath);

    // Save file to TIFF
    U16String outputFilePath(u"out.tiff");
    book.Save(outputFilePath);

    std::cout << "File saved successfully to TIFF format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir libro de Excel a DOCX**

La API de Aspose.Cells proporciona soporte para convertir hojas de cálculo a formato DOCX. Para exportar el libro de trabajo a DOCX, pase [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) como el segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). También puede usar la clase [**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/) para especificar configuraciones adicionales para exportar la hoja a DOCX.

El siguiente ejemplo de código demuestra cómo exportar la hoja activa a DOCX usando el miembro del enumerador [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/). Por favor, consulte el [archivo DOCX de salida](Book1.docx) generado por el código como referencia.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output docx file
    U16String outputFilePath = outDir + u"Book1.docx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save as DOCX
    workbook.Save(outputFilePath, SaveFormat::Docx);

    std::cout << "File saved successfully as DOCX!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir libro de Excel a PPTX**

La API de Aspose.Cells proporciona soporte para convertir hojas de cálculo a formato PPTX. Para exportar el libro de trabajo a PPTX, pase [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) como el segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). También puede usar la clase [**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/) para especificar configuraciones adicionales para exportar la hoja a PPTX.

El siguiente ejemplo de código demuestra cómo exportar la hoja de trabajo activa a PPTX usando [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) miembro de enumeración. Por favor, consulte el [archivo PPTX de salida](Book1.pptx) generado por el código como referencia.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output PowerPoint file
    U16String outputFilePath = outDir + u"Book1.pptx";

    // Create workbook from the input Excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as a PowerPoint file
    workbook.Save(outputFilePath, SaveFormat::Pptx);

    std::cout << "Workbook saved as PowerPoint successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir Libro de Excel a EPUB**

La API Aspose.Cells ofrece soporte para convertir hojas de cálculo a formato EPUB. Para exportar el libro a EPUB, pase [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) como el segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). También puede usar la clase [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) para especificar configuraciones adicionales para exportar la hoja de trabajo a EPUB.

El siguiente ejemplo de código demuestra cómo exportar la hoja de trabajo activa a EPUB usando [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) miembro de enumeración.

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

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output EPUB file
    U16String outputFilePath = outDir + u"ConvertingToEPUBFiles_out.epub";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in EPUB format
    wb.Save(outputFilePath, SaveFormat::Epub);

    std::cout << "File converted to EPUB format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Convertir Libro de Excel a AZW3**

La API Aspose.Cells proporciona soporte para convertir hojas de cálculo a formato AZW3. Para exportar el libro a AZW3, pase [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) como el segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). También puede usar la clase [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) para especificar configuraciones adicionales para exportar la hoja de trabajo a AZW3.

El siguiente ejemplo de código demuestra cómo exportar la hoja de trabajo activa a AZW3 usando [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) miembro de enumeración.

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
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output AZW3 file
    U16String outputFilePath = outDir + u"ConvertingToEPUBFiles_out.azw3";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in AZW3 format
    wb.Save(outputFilePath, SaveFormat::Azw3);

    std::cout << "File converted to AZW3 format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Convertir Revisión de XLSB a XLSM](/cells/es/cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/es/cpp/convert-excel-to-html/)
- [Imagen](/cells/es/cpp/convert-excel-to-image/)
- [Json](/cells/es/cpp/convert-workbook-to-json/)
- [Convertir libro de Excel a Ods, Sxc y Fods (OpenOffice / LibreOffice calc).](/cells/es/cpp/convert-excel-to-ods/)
- [Pdf](/cells/es/cpp/convert-excel-workbook-to-pdf/)
- [Convertir Excel a CSV, TSV y Txt](/cells/es/cpp/convert-excel-to-csv-tsv-and-txt/)
- [Seguimiento del progreso de conversión de documentos](/cells/es/cpp/track-document-conversion-progress/)
- [Convertir CSV, TSV y TXT a Excel](/cells/es/cpp/convert-csv-tsv-and-txt-to-excel/)
