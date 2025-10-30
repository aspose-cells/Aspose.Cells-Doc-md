---
title: Convertir archivo XLSX a formato PDF con Node.js a través de C++
linktitle: Convertir archivo XLSX a formato PDF
type: docs
weight: 30
url: /es/nodejs-cpp/convert-xlsx-file-to-pdf-format/
description: Esta guía explica cómo convertir un archivo de Excel (XLSX) a formato PDF usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

PDF (Formato de Documento Portátil) representa documentos de manera independiente del software, hardware y sistema operativo utilizados para crear esos documentos. Un archivo PDF puede ser documentos con cualquier combinación de texto, gráficos e imágenes de manera independiente del dispositivo y de la resolución. Los archivos PDF suelen estar comprimidos, por lo que ocupan menos espacio que el archivo original.

En ocasiones, necesitas convertir un archivo de Microsoft Excel a PDF. Para ello, requieres una solución rápida, segura, precisa y confiable que te permita distribuir documentos PDF en todo el mundo. Existen numerosas herramientas de conversión que pueden realizar esta tarea. Pero debes asegurarte de que el diseño del documento original de Excel se conserve en el archivo PDF de salida. Imágenes, gráficos, formas, formato de datos, fuentes, atributos, colores, configuraciones de página, orientación del texto, bordes, gráficos, etc., deben renderizarse de manera precisa y exacta. [Aspose.Cells](https://products.aspose.com/cells/nodejs-cpp/) garantiza una conversión de alta fidelidad.

Este documento está diseñado para proporcionar una comprensión integral de cómo se puede convertir un documento de Microsoft Excel (que contiene imágenes, gráficos, formato, etc.) a PDF. Para ello, muestra cómo crear una aplicación sencilla en consola en Node.js que convierte un archivo de Excel a PDF mediante la API de Aspose.Cells. La conversión se realiza con un alto grado de precisión y exactitud.

{{% /alert %}}

## **Convirtiendo Excel a PDF**

Este ejemplo utiliza un archivo de Excel (SampleInput.xlsx) como plantilla. El libro contiene hojas con gráficos e imágenes. Cada hoja presenta diferentes tipos de formatos usando fuentes, atributos, colores, efectos de sombreado y bordes. Hay un gráfico de columnas en la primera hoja y una imagen en la última.

### **El archivo de plantilla de Excel**

El archivo plantilla tiene tres hojas, incluyendo gráficos e imágenes como medios. La primera hoja tiene gráficos y la última hoja tiene una imagen, como se muestra en las capturas de pantalla.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|La primera hoja de trabajo **(Pronóstico de ventas)**|La segunda hoja de trabajo **(Informe de ventas)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|La tercera hoja de trabajo **(Entrada de datos)**|La última hoja de trabajo **(Imagen)**|

### **Proceso de conversión**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const designerFile = path.join(dataDir, "SampleInput.xlsx");
const pdfFile = path.join(dataDir, "Output.out.pdf");

try {
// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es recomendable llamar al método [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) justo antes de renderizar la hoja a PDF. Esto asegura que los valores dependientes de fórmulas se recalculen y que los valores correctos se muestren en el PDF.

{{% /alert %}}

### **Resultado**

Cuando se ha ejecutado el código anterior, se crea un archivo PDF en la carpeta de archivos de su directorio de aplicación.
Las siguientes capturas de pantalla muestran las páginas del PDF. Tenga en cuenta que los encabezados y pies de página también se conservan en el archivo PDF de salida.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|La primera hoja de trabajo **(Pronóstico de ventas)**|La segunda hoja de trabajo **(Informe de ventas)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|La tercera hoja de trabajo **(Entrada de datos)**|La última hoja de trabajo **(Imagen)**|
{{< app/cells/assistant language="nodejs-cpp" >}}
