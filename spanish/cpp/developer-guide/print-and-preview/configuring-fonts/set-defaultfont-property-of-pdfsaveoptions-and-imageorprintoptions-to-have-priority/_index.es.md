---
title: Establecer la propiedad DefaultFont de PdfSaveOptions y ImageOrPrintOptions para tener prioridad con C++
linktitle: Establecer la propiedad DefaultFont de PdfSaveOptions y ImageOrPrintOptions para tener prioridad
type: docs
weight: 30
url: /es/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Aprende a priorizar la configuración de fuentes al guardar documentos con Aspose.Cells en C++.
---

## **Escenarios de uso posibles**

Al establecer la propiedad **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), podrías esperar que al guardar en PDF o imagen se establezca ese DefaultFont para todo el texto en un libro de trabajo que tiene fuente faltante (no instalada).

Por lo general, al guardar en PDF o imagen, Aspose.Cells intentará primero establecer la fuente predeterminada del libro (es decir, Workbook.DefaultStyle.Font). Si la fuente predeterminada del libro aún no puede mostrar/render el texto correctamente, entonces Aspose.Cells intentará renderizar con la fuente mencionada contra el atributo DefaultFont en [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/).

Para cumplir con tus expectativas, tenemos una propiedad booleana llamada "**CheckWorkbookDefaultFont**" en [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/). Puedes configurarla en **false** para desactivar el intento de usar la fuente predeterminada del libro o dejar que la configuración **DefaultFont** en [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) tenga prioridad.

## **Establecer la propiedad DefaultFont de PdfSaveOptions/ImageOrPrintOptions**

El siguiente código de ejemplo abre un archivo Excel. La celda A1 (en la primera hoja) tiene un texto establecido como "Texto de fuente Navidad". El nombre de la fuente es "Personal Use Navidad" que no está instalada en la máquina. Establecemos el atributo **DefaultFont** de [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) en "Times New Roman". También configuramos la propiedad booleana **CheckWorkbookDefaultFont** en **"false"** lo que garantiza que el texto de la celda A1 se renderice con la fuente "Times New Roman" y no use la fuente predeterminada del libro ("Calibri" en este caso). El código renderiza la primera hoja a formatos de imagen PNG y TIFF. Finalmente, renderiza a un archivo PDF.

{{% alert color="primary" %}}

El valor predeterminado del atributo **CheckWorkbookDefaultFont** es **true**.

{{% /alert %}}

Esta es la captura de pantalla del [archivo de plantilla](49446913.xlsx) utilizado en el código de ejemplo.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Esta es la imagen PNG de salida después de establecer la propiedad [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) en "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Ver la imagen [TIFF](48496672.tiff) de salida después de establecer la propiedad [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) en "Times New Roman".

Ver el archivo [PDF](48496673.pdf) de salida después de establecer la propiedad [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) en "Times New Roman".

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Input and output directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open an Excel file
    Workbook workbook(sourceDir + u"sampleSetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.xlsx");

    // Rendering to PNG file format while setting the CheckWorkbookDefaultFont attribute to false.
    // So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
    ImageOrPrintOptions imgOpt;
    imgOpt.SetImageType(ImageType::Png);
    imgOpt.SetCheckWorkbookDefaultFont(false);
    imgOpt.SetDefaultFont(u"Times New Roman");

    // Create a SheetRender instance for the first worksheet and render to PNG.
    SheetRender sr(workbook.GetWorksheets().Get(0), imgOpt);
    sr.ToImage(0, outputDir + u"out1_imagePNG.png");

    // Rendering to TIFF file format while setting the CheckWorkbookDefaultFont attribute to false.
    imgOpt.SetImageType(ImageType::Tiff);
    WorkbookRender wr(workbook, imgOpt);
    wr.ToImage(outputDir + u"out1_imageTIFF.tiff");

    // Rendering to PDF file format while setting the CheckWorkbookDefaultFont attribute to false.
    PdfSaveOptions saveOptions;
    saveOptions.SetDefaultFont(u"Times New Roman");
    saveOptions.SetCheckWorkbookDefaultFont(false);

    // Save the workbook as PDF
    workbook.Save(outputDir + u"out1_pdf.pdf", saveOptions);

    std::cout << "Files exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
