---
title: Convertir archivo de Excel a formato PDF compatible con PDFA 1a con C++
linktitle: Convertir archivo de Excel a formato PDF compatible con PDFA 1a
type: docs
weight: 130
url: /es/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Aprende cómo convertir archivos de Excel a formato PDF/A 1a compatible usando Aspose.Cells con C++.
---

## **Escenarios de uso posibles**

 PDF/A es una variante única de PDF diseñada para la conservación a largo plazo de documentos. PDF/A es una versión estandarizada por ISO del Formato de Documento Portátil (PDF) que es un formato de archivo archivístico que incrusta todas las fuentes utilizadas en el documento dentro del archivo PDF. PDF/A difiere de PDF al prohibir funciones como la vinculación de fuentes (en lugar de incrustarlas) y el cifrado. Aspose.Cells te permite guardar los archivos de Excel en archivos PDF compatibles con PDF/A (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab, y PDF/A-3u son compatibles). Este tema describe cómo guardar el libro de Excel en un archivo PDF compatible con PDF/A (PDF/A-1a).

## **Convertir archivo de Excel al formato PDF compatible con PDF/A-1a**

 Los desarrolladores pueden usar la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) para establecer diferentes atributos para la conversión. Configurar diferentes propiedades de la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) te da control sobre la impresión, fuente, seguridad y configuraciones de compresión para el PDF de salida. La propiedad más importante es [**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/), que te permite guardar los archivos de Excel en archivos PDF compatibles con PDF/A.

El siguiente código de muestra explica cómo convertir un archivo de Excel al formato PDF compatible con PDF/A-1a. Consulta su [PDF de salida](outputCompliancePdfA1a.pdf) así como la captura de pantalla para referencia.

## **Captura de pantalla**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and add some message inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This PDF format is compatible with PDFA-1a.");

    // Create pdf save options and set its compliance to PDFA-1a
    PdfSaveOptions opts;
    opts.SetCompliance(PdfCompliance::PdfA1a);

    // Save the output pdf
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputCompliancePdfA1a.pdf", opts);

    std::cout << "PDF created successfully with PDFA-1a compliance!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
