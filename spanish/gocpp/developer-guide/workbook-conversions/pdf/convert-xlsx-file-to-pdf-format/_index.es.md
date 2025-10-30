---
title: Convertir archivo XLSX a formato PDF con Golang vía C++
linktitle: Convertir archivo XLSX a formato PDF
type: docs
weight: 30
url: /es/go-cpp/convert-xlsx-file-to-pdf-format/
description: Aprende cómo convertir archivos de Excel a formato PDF usando Aspose.Cells for C++ con alta precisión y exactitud.
---

{{% alert color="primary" %}}

 PDF (Formato de Documento Portátil) representa documentos independientemente del software, hardware y sistema operativo usados para crear esos documentos. Un archivo PDF puede contener cualquier combinación de texto, gráficos e imágenes de manera independiente del dispositivo y resoluciones. Los archivos PDF suelen comprimirse, por lo que ocupan menos espacio que el archivo original.

A veces, necesitas convertir un archivo de Microsoft Excel a PDF. Para ello, necesitas una solución rápida, segura, precisa y confiable que te permita distribuir documentos PDF en todo el mundo. Hay varias herramientas de conversión que pueden realizar esta tarea. Pero debes asegurarte de que el diseño del archivo original de Excel se conserve en el archivo PDF de salida. Las imágenes, gráficos, formas, formato de datos, fuentes, atributos, colores, configuraciones de página, orientación del texto, bordes, gráficos, etc., deben representarse de manera precisa y exacta. [Aspose.Cells](https://products.aspose.com/cells/go-cpp/) garantiza una conversión de alta fidelidad.

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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertXlsxFileToPdfFormat.go" >}}
{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es mejor llamar al método [Workbook.CalculateFormula](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) justo antes de renderizar la hoja de cálculo a PDF. Esto asegura que los valores dependientes de fórmulas se vuelvan a calcular y que los valores correctos se muestren en el PDF.

{{% /alert %}}

### **Resultado**

Cuando se ha ejecutado el código anterior, se crea un archivo PDF en la carpeta de archivos de su directorio de aplicación.
Las siguientes capturas de pantalla muestran las páginas del PDF. Tenga en cuenta que los encabezados y pies de página también se conservan en el archivo PDF de salida.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|La primera hoja de trabajo **(Pronóstico de ventas)**|La segunda hoja de trabajo **(Informe de ventas)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|La tercera hoja de trabajo **(Entrada de datos)**|La última hoja de trabajo **(Imagen)**|
