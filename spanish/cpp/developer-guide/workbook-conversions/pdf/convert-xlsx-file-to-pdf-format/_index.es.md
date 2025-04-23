---
title: Convertir archivo XLSX a formato PDF con C++
linktitle: Convertir archivo XLSX a formato PDF
type: docs
weight: 30
url: /es/cpp/convert-xlsx-file-to-pdf-format/
description: Aprende cómo convertir archivos de Excel a formato PDF usando Aspose.Cells for C++ con alta precisión y exactitud.
---

{{% alert color="primary" %}}

 PDF (Formato de Documento Portátil) representa documentos independientemente del software, hardware y sistema operativo usados para crear esos documentos. Un archivo PDF puede contener cualquier combinación de texto, gráficos e imágenes de manera independiente del dispositivo y resoluciones. Los archivos PDF suelen comprimirse, por lo que ocupan menos espacio que el archivo original.

En ocasiones, necesitas convertir un archivo de Microsoft Excel a PDF. Para esto, necesitas una solución rápida, segura, precisa y confiable que te permita distribuir documentos PDF en todo el mundo. Existen numerosas herramientas de conversión que pueden realizar esta tarea. Pero debes asegurarte de que el diseño del documento original de Excel se mantenga en el archivo PDF de salida. Las imágenes, gráficos, formas, formato de datos, fuentes, atributos, colores, configuraciones de página, orientación del texto, bordes, gráficos, etc., deben renderizarse de manera precisa y exacta. [Aspose.Cells](https://products.aspose.com/cells/cpp/) garantiza una conversión de alta fidelidad.

Este documento está diseñado para proporcionar una comprensión completa de cómo un documento de Microsoft Excel (que contiene imágenes, gráficos, formateo, etc.) puede convertirse a PDF. Para ello, muestra cómo crear una aplicación de consola simple en C++ que convierte un archivo de Excel a PDF utilizando la API Aspose.Cells. La conversión se realiza con un alto grado de precisión y exactitud.

{{% /alert %}}

## **Convirtiendo Excel a PDF**

Este ejemplo utiliza un archivo de Excel (SampleInput.xlsx) como plantilla. El libro contiene hojas con gráficos e imágenes. Cada hoja presenta diferentes tipos de formatos usando fuentes, atributos, colores, efectos de sombreado y bordes. Hay un gráfico de columnas en la primera hoja y una imagen en la última.

### **El archivo de plantilla de Excel**

El archivo plantilla tiene tres hojas, incluyendo gráficos e imágenes como medios. La primera hoja tiene gráficos, y la última hoja tiene una imagen, como se muestra en las capturas de pantalla.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|La primera hoja de trabajo **(Pronóstico de ventas)**|La segunda hoja de trabajo **(Informe de ventas)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|La tercera hoja de trabajo **(Entrada de datos)**|La última hoja de trabajo **(Imagen)**|

### **Proceso de conversión**

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

    try
    {
        // Get the template excel file path
        U16String designerFile = srcDir + u"SampleInput.xlsx";

        // Specify the pdf file path
        U16String pdfFile = outDir + u"Output.out.pdf";

        // Open the template excel file
        Workbook wb(designerFile);

        // Save the pdf file
        wb.Save(pdfFile, SaveFormat::Pdf);

        std::cout << "PDF file saved successfully!" << std::endl;
    }
    catch (const std::exception& e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es mejor llamar al método [Workbook.CalculateFormula](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) justo antes de renderizar la hoja de cálculo a PDF. Hacer esto garantiza que los valores dependientes de fórmulas se recalculen y que los valores correctos se muestren en el PDF.

{{% /alert %}}

### **Resultado**

Cuando se ha ejecutado el código anterior, se crea un archivo PDF en la carpeta de archivos de su directorio de aplicación.
Las siguientes capturas de pantalla muestran las páginas del PDF. Tenga en cuenta que los encabezados y pies de página también se conservan en el archivo PDF de salida.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|La primera hoja de trabajo **(Pronóstico de ventas)**|La segunda hoja de trabajo **(Informe de ventas)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|La tercera hoja de trabajo **(Entrada de datos)**|La última hoja de trabajo **(Imagen)**|
