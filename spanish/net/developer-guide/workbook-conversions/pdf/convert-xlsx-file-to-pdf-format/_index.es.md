---
title: Convierta el archivo XLSX al formato PDF
type: docs
weight: 30
url: /es/net/convert-xlsx-file-to-pdf-format/
---
{{% alert color="primary" %}}

PDF (formato de documento portátil) representa documentos independientemente del software, hardware y sistema operativo utilizado para crear esos documentos. Un archivo PDF puede ser documentos con cualquier combinación de texto, gráficos e imágenes, independientemente del dispositivo y de la resolución. Los archivos PDF suelen estar comprimidos, por lo que ocupan menos espacio que el archivo original.

 veces, necesita convertir un archivo Excel Microsoft a PDF. Para esto, necesita una solución rápida, segura, precisa y confiable que le permita distribuir documentos PDF en todo el mundo. Existen numerosas herramientas de conversión que pueden realizar esta tarea. Pero debe asegurarse de que el diseño del documento de Excel original se conserve en el archivo de salida PDF. Las imágenes, los gráficos, las formas, el formato de los datos, las fuentes, los atributos, los colores, la configuración de configuración de la página, la orientación del texto, los bordes, los gráficos, etc. deben representarse con precisión y precisión.[Aspose.Cells](https://products.aspose.com/cells/net/) asegura una conversión de alta fidelidad.

Este documento está diseñado para proporcionar una comprensión completa de cómo un documento de Excel Microsoft (que contiene imágenes, gráficos, formato, etc.) se puede convertir a PDF. Con ese fin, muestra cómo crear una aplicación de consola simple en Visual Studio.Net que convierte un archivo de Excel a PDF usando Aspose.Cells API. La conversión se realiza con un alto grado de precisión y exactitud.

{{% /alert %}}

##  **Convertir Excel a PDF**

Este ejemplo utiliza un archivo de Excel (SampleInput.xlsx) como plantilla. El libro de trabajo contiene hojas de trabajo con gráficos e imágenes. Cada hoja de trabajo contiene diferentes tipos de formatos utilizando fuentes, atributos, colores, efectos de sombreado y bordes. Hay un gráfico de columnas en la primera hoja de trabajo y una imagen en la última.

###  **El archivo de plantilla de Excel**

El archivo de plantilla tiene tres hojas de trabajo, incluidos gráficos e imágenes como Medios. La primera hoja de trabajo tiene gráficos y la última hoja de trabajo tiene una imagen como se muestra a continuación en las capturas de pantalla.

|![todo:imagen_alt_texto](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:imagen_alt_texto](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
| La primera hoja de trabajo**(Pronóstico de ventas)**| La segunda hoja de trabajo**(Reporte de ventas)**|
|![todo:imagen_alt_texto](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:imagen_alt_texto](Convert_an_XLS_File_to_PDF_Sheet4.png)|
| La tercera hoja de trabajo**(Entrada de datos)**| la última hoja de trabajo**(Imagen)**|

###  **Proceso de conversión**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Docs-Pdf-ConvertXlsxFileToPdf.cs" >}}

{{% alert color="primary" %}}

 Si la hoja de cálculo contiene fórmulas, es mejor llamar[Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)justo antes de representar la hoja de cálculo en PDF. Al hacerlo, se asegura que los valores dependientes de la fórmula se vuelvan a calcular y los valores correctos se representen en el PDF.

{{% /alert %}}

###  **Resultado**

Cuando se ha ejecutado el código anterior, se crea un archivo PDF en la carpeta Archivos en el directorio de su aplicación.
Las siguientes capturas de pantalla muestran las páginas PDF. Tenga en cuenta que los encabezados y pies de página también se conservan en el archivo de salida PDF.

|![todo:imagen_alt_texto](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:imagen_alt_texto](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
| La primera hoja de trabajo**(Pronóstico de ventas)**| La segunda hoja de trabajo**(Reporte de ventas)**|
|![todo:imagen_alt_texto](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:imagen_alt_texto](Convert_an_XLS_File_to_PDF_Converted4.png)|
| La tercera hoja de trabajo**(Entrada de datos)**| la última hoja de trabajo**(Imagen)**|
