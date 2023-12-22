---
title: Convertir libro de Excel a PDF
type: docs
weight: 80
url: /es/cpp/convert-excel-workbook-to-pdf/
---
##  **Conversión de libro de Excel a PDF**
Los archivos PDF se utilizan ampliamente para intercambiar documentos entre organizaciones, sectores gubernamentales e individuos. Es un formato de documento estándar y a menudo se les pide a los desarrolladores de software que encuentren una manera de convertir archivos de Excel Microsoft en documentos PDF.

Aspose.Cells admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.

{{% alert color="primary" %}} 

 Aspose.Cells escribe directamente la información sobre API y el número de versión en los documentos de salida. Por ejemplo, al representar el documento en PDF, Aspose.Cells for C++ completa el**Solicitud** campo con valor 'Aspose.Cells' y**PDF Productor** campo con valor, por ejemplo, 'Aspose.Cells v18.5.0'.

Tenga en cuenta que no puede indicarle a Aspose.Cells for C++ que cambie o elimine esta información de los documentos de salida.

{{% /alert %}} 
###  **Conversión directa**
Aspose.Cells admite la conversión de hojas de cálculo a PDF independientemente de otro software. Simplemente guarde un archivo de Excel en PDF usando el[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)clase'[Ahorrar](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)método. El[Ahorrar](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)método proporciona la[GuardarFormato_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)Miembro de enumeración que convierte los archivos nativos de Excel al formato PDF.

Siga los pasos a continuación para convertir directamente las hojas de cálculo de Excel al formato PDF:

1.  Instanciar un objeto de la[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)clase llamando a su constructor vacío.
1. Puede abrir/cargar un archivo de plantilla existente u omitir este paso si está creando el libro desde cero.
1. Realice cualquier trabajo (ingrese datos, aplique formato, establezca fórmulas, inserte imágenes u otros objetos de dibujo, etc.) en la hoja de cálculo utilizando las API Aspose.Cells'.
1.  Cuando el código de la hoja de cálculo esté completo, llame al[Libro de trabajo](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)clase'[Ahorrar](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)Método para guardar la hoja de cálculo.

El formato del archivo debe ser PDF, así que seleccione el PDF relevante (un valor predefinido) de la enumeración SaveFormat para generar el documento PDF final.

 Consulte el siguiente código de muestra, su[archivo de Excel de muestra](67338368.xlsx) y[salida PDF](67338369.pdf) para tu referencia.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
###  **Conversión avanzada**
También puede optar por utilizar el[Opciones de guardar PDF](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)clase para establecer diferentes atributos para la conversión. Establecer diferentes propiedades del**Opciones de guardar PDF** La clase le brinda control sobre las configuraciones de impresión, fuente, seguridad y compresión para la salida PDF. La propiedad más importante es[Establecer cumplimiento](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/)que le permite guardar los archivos de Excel en archivos PDF/A compatibles con PDF.
####  **Guardar el libro de trabajo en archivos compilados con PDF/A**
El siguiente fragmento de código demuestra cómo utilizar el**Opciones de guardar PDF**clase para guardar archivos de Excel en formato PDF/A compatible con PDF

 Consulte el siguiente código de muestra y su[salida PDF](67338370.pdf) para tu referencia.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
####  **Establecer la hora de creación PDF**
Con el**Opciones de guardado de IPdf** clase, puede obtener o establecer la hora de creación PDF.

 Consulte el siguiente código de muestra y su[salida PDF](67338371.pdf) para tu referencia.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
