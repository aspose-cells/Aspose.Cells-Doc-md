---
title: Convertir archivo XLSX al formato PDF
type: docs
weight: 30
url: /es/python-net/convert-xlsx-file-to-pdf-format/
description: Aprenda a convertir un archivo XLSX al formato PDF con Aspose.Cells for Python via .NET API.
keywords: Python Convert XLSX File to PDF Format, Convert xlsx to pdf using Python, Python xlsx to pdf, Save xlsx to pdf in python, xlsx to pdf format in Python
---
{{% alert color="primary" %}}

PDF (Formato de documento portátil) representa documentos independientemente del software, hardware y sistema operativo utilizados para crearlos. Un archivo PDF puede contener documentos con cualquier combinación de texto, gráficos e imágenes de forma independiente del dispositivo y de la resolución. Los archivos PDF suelen estar comprimidos, por lo que ocupan menos espacio que el archivo original.

 A veces, necesita convertir un archivo Excel Microsoft a PDF. Para ello, necesita una solución rápida, segura, precisa y confiable que le permita distribuir documentos PDF en todo el mundo. Existen numerosas herramientas de conversión que pueden realizar esta tarea. Pero debe asegurarse de que el diseño del documento de Excel original se conserve en el archivo de salida PDF. Las imágenes, gráficos, formas, formato de datos, fuentes, atributos, colores, configuraciones de página, orientación del texto, bordes, gráficos, etc. deben representarse de forma precisa y precisa.[Aspose.Cells for Python via .NET](https://products.aspose.com/cells/python-net/) Garantiza una conversión de alta fidelidad.

Este documento está diseñado para proporcionar una comprensión integral de cómo un documento Excel Microsoft (que contiene imágenes, gráficos, formato, etc.) se puede convertir a PDF. Con ese fin, se muestra cómo crear una aplicación de consola simple en Visual Studio.Net que convierte un archivo de Excel a PDF usando Aspose.Cells for Python via .NET API. La conversión se realiza con un alto grado de precisión y exactitud.

{{% /alert %}}

##  **Convertir Excel a PDF**

Este ejemplo utiliza un archivo de Excel (SampleInput.xlsx) como plantilla. El libro de trabajo contiene hojas de trabajo con gráficos e imágenes. Cada hoja de trabajo contiene diferentes tipos de formatos que utilizan fuentes, atributos, colores, efectos de sombreado y bordes. Hay un gráfico de columnas en la primera hoja de trabajo y una imagen en la última.

###  **El archivo de plantilla de Excel**

El archivo de plantilla tiene tres hojas de trabajo, incluidos gráficos e imágenes como Medios. La primera hoja de trabajo tiene gráficos y la última hoja de trabajo tiene una imagen como se muestra a continuación en las capturas de pantalla.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
| la primera hoja de trabajo**(Pronóstico de ventas)**| La segunda hoja de trabajo.**(Reporte de ventas)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
| La tercera hoja de trabajo.**(Entrada de datos)**| la ultima hoja de trabajo**(Imagen)**|

###  **Proceso de conversión**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXlsxFileToPdf.py" >}}

{{% alert color="primary" %}}

 Si la hoja de cálculo contiene fórmulas, es mejor llamar[Libro de trabajo.calcular_fórmula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) método justo antes de representar la hoja de cálculo en PDF. Al hacerlo, se garantiza que los valores dependientes de la fórmula se vuelvan a calcular y que los valores correctos se representen en PDF.

{{% /alert %}}

###  **Resultado**

Cuando se ejecuta el código anterior, se crea un archivo PDF en la carpeta Archivos del directorio de su aplicación.
Las siguientes capturas de pantalla muestran las páginas PDF. Tenga en cuenta que los encabezados y pies de página también se conservan en el archivo de salida PDF.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
| la primera hoja de trabajo**(Pronóstico de ventas)**| La segunda hoja de trabajo.**(Reporte de ventas)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
| La tercera hoja de trabajo.**(Entrada de datos)**| la ultima hoja de trabajo**(Imagen)**|
