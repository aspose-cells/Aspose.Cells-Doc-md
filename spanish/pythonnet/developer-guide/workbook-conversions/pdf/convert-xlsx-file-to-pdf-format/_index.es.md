---
title: Convertir archivo XLSX a formato PDF
type: docs
weight: 30
url: /es/python-net/convert-xlsx-file-to-pdf-format/
description: Aprende cómo convertir un archivo XLSX a formato PDF con la API de Aspose.Cells para Python via .NET.
keywords: Convertir archivo XLSX a formato PDF con Python, Convertir xlsx a pdf usando Python, Python xlsx a pdf, Guardar xlsx como pdf en Python, Formato xlsx a pdf en Python
---

{{% alert color="primary" %}}

PDF (Formato de Documento Portátil) representa documentos de manera independiente del software, hardware y sistema operativo utilizados para crear esos documentos. Un archivo PDF puede ser documentos con cualquier combinación de texto, gráficos e imágenes de manera independiente del dispositivo y de la resolución. Los archivos PDF suelen estar comprimidos, por lo que ocupan menos espacio que el archivo original.

En ocasiones, es necesario convertir un archivo de Microsoft Excel a PDF. Para ello, se requiere una solución rápida, segura, precisa y confiable que te permita distribuir documentos PDF en todo el mundo. Existen numerosas herramientas de conversión que pueden realizar esta tarea. Sin embargo, debes asegurarte de que el diseño del documento Excel original se mantenga en el archivo PDF de salida. Las imágenes, gráficos, formas, formato de los datos, fuentes, atributos, colores, configuración de página, orientación del texto, bordes, gráficos, etc., deben representarse con precisión y exactitud. [Aspose.Cells para Python via .NET](https://products.aspose.com/cells/python-net/) garantiza una conversión de alta fidelidad.

Este documento está diseñado para proporcionar una comprensión completa de cómo se puede convertir un documento de Microsoft Excel (que contiene imágenes, gráficos, formato, etc.) a PDF. Para ello, muestra cómo crear una aplicación de consola simple en Visual Studio.Net que convierte un archivo de Excel a PDF usando la API de Aspose.Cells para Python via .NET. La conversión se realiza con un alto grado de precisión y exactitud.

{{% /alert %}}

## **Convirtiendo Excel a PDF**

Este ejemplo utiliza un archivo de Excel (SampleInput.xlsx) como plantilla. El libro contiene hojas de cálculo con gráficos e imágenes. Cada hoja de cálculo contiene diferentes tipos de formatos utilizando fuentes, atributos, colores, efectos de sombreado y bordes. Hay un gráfico de columnas en la primera hoja de cálculo y una imagen en la última.

### **El archivo de plantilla de Excel**

El archivo de plantilla tiene tres hojas de cálculo, incluyendo gráficos e imagen como medios. La primera hoja de cálculo tiene gráficos y la última hoja de cálculo tiene una imagen como se muestra a continuación en las capturas de pantalla.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|La primera hoja de trabajo **(Pronóstico de ventas)**|La segunda hoja de trabajo **(Informe de ventas)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|La tercera hoja de trabajo **(Entrada de datos)**|La última hoja de trabajo **(Imagen)**|

### **Proceso de conversión**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ConvertXlsxFileToPdf.py" >}}

{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es mejor llamar al método [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) justo antes de renderizar la hoja de cálculo a PDF. De esta manera se asegura que los valores dependientes de la fórmula se recalculen y los valores correctos se representen en el PDF.

{{% /alert %}}

### **Resultado**

Cuando se ha ejecutado el código anterior, se crea un archivo PDF en la carpeta de archivos de su directorio de aplicación.
Las siguientes capturas de pantalla muestran las páginas del PDF. Tenga en cuenta que los encabezados y pies de página también se conservan en el archivo PDF de salida.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|La primera hoja de trabajo **(Pronóstico de ventas)**|La segunda hoja de trabajo **(Informe de ventas)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|La tercera hoja de trabajo **(Entrada de datos)**|La última hoja de trabajo **(Imagen)**|
{{< app/cells/assistant language="python-net" >}}
