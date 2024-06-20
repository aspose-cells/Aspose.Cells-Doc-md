---
title: Convertir libro de Excel a PDF
type: docs
weight: 80
url: /es/cpp/convert-excel-workbook-to-pdf/
---

## **Conversión de libro de Excel a PDF**
Los archivos PDF son ampliamente utilizados para intercambiar documentos entre organizaciones, sectores gubernamentales e individuos. Es un formato de documento estándar y a menudo se pide a los desarrolladores de software que encuentren una forma de convertir archivos de Microsoft Excel en documentos PDF.

Aspose.Cells admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.

{{% alert color="primary" %}} 

Aspose.Cells escribe directamente la información sobre la API y el número de versión en los documentos de salida. Por ejemplo, al representar el documento en PDF, Aspose.Cells for C++ llena el campo **Application** con el valor 'Aspose.Cells' y el campo **Productor de PDF** con el valor, por ejemplo, 'Aspose.Cells v18.5.0'.

Ten en cuenta que no puedes instruir a Aspose.Cells for C++ para cambiar o eliminar esta información de los documentos de salida.

{{% /alert %}} 
### **Conversión Directa**
Aspose.Cells admite la conversión de hojas de cálculo a PDF de forma independiente a otro software. Simplemente guarda un archivo de Excel en PDF usando el método [Save](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) clase [SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) para convertir los archivos de Excel nativos al formato PDF.

Siga los siguientes pasos para convertir directamente las hojas de cálculo de Excel al formato PDF:

1. Instantiate un objeto de la clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) llamando a su constructor vacío.
1. Puede abrir/cargar un archivo de plantilla existente o saltarse este paso si está creando el libro de trabajo desde cero.
1. Realiza cualquier trabajo (ingreso de datos, aplicación de formato, definición de fórmulas, inserción de imágenes u otros objetos de dibujo, etc.) en la hoja de cálculo usando las APIs de Aspose.Cells.
1. Cuando el código de la hoja de cálculo esté completo, llama al método [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) de la clase [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) para guardar la hoja de cálculo.

El formato del archivo debería ser PDF, así que selecciona el PDF relevante (un valor predefinido) de la enumeración SaveFormat para generar el documento PDF final

Por favor, consulta el siguiente código de muestra, su [archivo de Excel de muestra](67338368.xlsx) y [PDF de salida](67338369.pdf) para tu referencia.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
### **Conversión Avanzada**
También puedes optar por usar la clase [PdfSaveOptions](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) para establecer diferentes atributos para la conversión. Establecer diferentes propiedades de la clase **PdfSaveOptions** te da control sobre la impresión, fuente, seguridad y configuración de compresión para el PDF de salida. La propiedad más importante es [SetCompliance](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/) que te permite guardar los archivos de Excel en archivos PDF/A compatibles con PDF.
#### **Guardando el Libro de Trabajo en Archivos PDF/A Compilados**
El siguiente fragmento de código demuestra cómo utilizar la clase **PdfSaveOptions** para guardar archivos de Excel en formato PDF/A compatible

Por favor, consulte el siguiente código de muestra y su [PDF de salida](67338370.pdf) para su referencia.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
#### **Establecer la Hora de Creación del PDF**
Con la clase **IPdfSaveOptions**, puede obtener o establecer la hora de creación del PDF

Por favor, consulte el siguiente código de muestra y su [PDF de salida](67338371.pdf) para su referencia.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
