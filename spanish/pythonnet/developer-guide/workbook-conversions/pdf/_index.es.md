---
title: Pdf
type: docs
weight: 220
url: /es/python-net/convert-excel-to-pdf/
description: Aprenda cómo convertir Excel a PDF con Aspose.Cells for Python via .NET API.
keywords: Python converT Excel to PDF, ConverT Excel to PDF using Python, Python save Excel to PDF, Excel to PDF in Python
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET admite la conversión de un libro de Excel a PDF. En este ejemplo, veremos la conversión completa de un libro de Excel a PDF.

{{% /alert %}}

##  **Conversión de libro de Excel a PDF**

Los archivos PDF se utilizan ampliamente para intercambiar documentos entre organizaciones, sectores gubernamentales e individuos. Es un formato de documento estándar y a menudo se les pide a los desarrolladores de software que encuentren una manera de convertir archivos de Excel Microsoft en documentos PDF.

Aspose.Cells for Python via .NET admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.

{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET escribe directamente la información sobre API y el número de versión en los documentos de salida. Por ejemplo, al representar el documento en PDF, Aspose.Cells for Python via .NET se completa**PDF Productor** campo con valor, por ejemplo, 'Aspose.Cells for Python via .NET v23.2'.

 Tenga en cuenta que puede cambiar esta información en los documentos de salida haciendo clic en**[PdfSaveOptions.producer](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/producer/)** propiedad.

{{% /alert %}}

###  **Conversión directa**

 Aspose.Cells for Python via .NET admite la conversión de hojas de cálculo a PDF independientemente de otro software. Simplemente guarde un archivo de Excel en PDF usando el**[Libro de trabajo](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**clase'**[guardar](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)** método. El**[guardar](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)** método proporciona la**[SaveFormat.PDF](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)**Miembro de enumeración que convierte los archivos nativos de Excel al formato PDF.

Siga los pasos a continuación para convertir directamente las hojas de cálculo de Excel al formato PDF:

1.  Instanciar un objeto de la**[Libro de trabajo](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**clase llamando a su constructor vacío.
1. Puede abrir/cargar un archivo de plantilla existente u omitir este paso si está creando el libro desde cero.
1. Realice cualquier trabajo (ingrese datos, aplique formato, establezca fórmulas, inserte imágenes u otros objetos de dibujo, etc.) en la hoja de cálculo utilizando las API Aspose.Cells for Python via .NET'.
1.  Cuando el código de la hoja de cálculo esté completo, llame al**[Libro de trabajo](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**clase'**[guardar](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)**Método para guardar la hoja de cálculo.

 El formato del archivo debe ser PDF, así que seleccione*PDF* (un valor predefinido) del**[Guardar formato](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)**enumeración para generar el documento PDF final.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

###  **Conversión avanzada**

 También puede optar por utilizar el**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** clase para establecer diferentes atributos para la conversión. Establecer diferentes propiedades del**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** La clase le brinda control sobre las configuraciones de impresión, fuente, seguridad y compresión para la salida PDF. La propiedad más importante es**[PdfSaveOptions.compliance](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)**que le permite guardar los archivos de Excel en archivos PDF/A compatibles con PDF.

####  **Guardar el libro de trabajo en archivos compilados con PDF/A**

 El fragmento de código que se proporciona a continuación demuestra cómo utilizar el**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)**clase para guardar archivos de Excel en formato compatible con PDF/A PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

Tenga en cuenta que el**[PdfSaveOptions.compliance](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)**La propiedad se agregó con el lanzamiento de Aspose.Cells for Python via .NET for .NET 5.3.0.

{{% /alert %}}

####  **Establecer la hora de creación PDF**

 Con el**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)**clase, puede obtener o establecer la hora de creación PDF. El siguiente código demuestra el uso de**[PdfSaveOptions.created_time](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/)** propiedad para establecer la hora de creación del archivo PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

####  **Establecer la opción ContentCopyForAccessibility**

Con el**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** clase, puede obtener o configurar el PDF**[PdfSecurityOptions.accessibility_extract_content](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/)** Opción para controlar el acceso al contenido en el PDF convertido.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

####  **Exportar propiedades personalizadas a PDF**

Con el**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** clase, puede exportar las propiedades personalizadas en el libro de origen al PDF.**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/)**Se proporciona un enumerador para especificar la forma en que se exportan las propiedades. Estas propiedades se pueden observar en Adobe Acrobat Reader haciendo clic en Archivo y luego en la opción Propiedades como se muestra en la siguiente imagen. Se puede descargar el archivo de plantilla "sourceWithCustProps.xlsx"[aquí](sourceWithCustProps.xlsx) para probar y generar el archivo PDF "outSourceWithCustProps" está disponible[aquí](outSourceWithCustProps.pdf) para analizar.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

###  **Atributos de conversión**

Trabajamos para mejorar las funciones de conversión con cada nueva versión. La conversión de Excel de Aspose.Cell a PDF todavía tiene un par de limitaciones. MapChart no es compatible al convertir al formato PDF. Además, algunos objetos de dibujo no son compatibles.

La siguiente tabla enumera todas las funciones que son total o parcialmente compatibles al exportar a PDF usando Aspose.Cells for Python via .NET. Esta tabla no es definitiva y no cubre todos los atributos de la hoja de cálculo, pero sí identifica aquellas funciones que no son compatibles o no son compatibles para la conversión. al PDF.

|**Elemento de documento**|**Atributo**|**Soportado**|**Notas**|
| :- | :- | :- | :- |
|Alineación| |Sí| |
|Configuración de fondo| |Sí| |
|Borde|Color|Sí| |
|Borde|Estilo de línea|Sí| |
|Borde|Ancho de línea|Sí| |
|Cell Datos| |Sí| |
|Comentarios| |Sí| |
|Formato condicional| |Sí| |
|Propiedades del documento| |Sí| |
|Dibujar objetos| |Parcialmente|Los efectos de sombras y 3D para dibujar objetos no son compatibles; WordArt y SmartArt son parcialmente compatibles.|
|Fuente|Tamaño|Sí| |
|Fuente|Color|Sí| |
|Fuente|Estilo|Sí| |
|Fuente|Subrayar|Sí| |
|Fuente|Efectos|Sí||
|Imágenes| |Sí| |
|Hipervínculo| |Sí| |
|Gráficos| |Parcialmente|MapChart no es compatible.|
|Fusionado Cells| |Sí| |
|Salto de página| |Sí| |
|Configuración de página|Encabezado/pie de página|Sí| |
|Configuración de página|Márgenes|Sí| |
|Configuración de página|Orientación de la página|Sí| |
|Configuración de página|Tamaño de página|Sí| |
|Configuración de página|Área de impresión|Sí| |
|Configuración de página|Imprimir títulos|Sí| |
|Configuración de página|Escalada|Sí| |
|Alto de fila/Ancho de columna| |Sí| |
|Idioma RTL (de derecha a izquierda)| |Sí| |

{{% alert color="primary" %}}

 Si su hoja de cálculo contiene fórmulas, es mejor llamar[Libro de trabajo.calcular_fórmula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)método justo antes de renderizar la hoja de cálculo al formato PDF. Al hacerlo, se garantizará que los valores dependientes de la fórmula se vuelvan a calcular y que los valores correctos se representen en PDF.

{{% /alert %}}

##  **Temas avanzados**
- [Agregar PDF Marcadores](/cells/es/python-net/add-pdf-bookmarks/)
- [Agregar PDF marcadores con destinos con nombre](/cells/es/python-net/add-pdf-bookmarks-with-named-destinations/)
- [Evite páginas en blanco en la salida PDF cuando no hay nada que imprimir](/cells/es/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Convertir archivo XLSX al formato PDF](/cells/es/python-net/convert-xlsx-file-to-pdf-format/)
- [Convierta un archivo Excel al formato PDF compatible con PDFA-1a](/cells/es/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Convierta el archivo XLS con imágenes o gráficos a PDF](/cells/es/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Crear PdfBookmarkEntry para hoja de gráfico](/cells/es/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [Ajustar todas las columnas de la hoja de trabajo en una sola página PDF](/cells/es/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Ignorar errores al representar Excel en PDF](/cells/es/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [Limite el número de páginas generadas: conversión de Excel a PDF](/cells/es/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Imprimir comentarios mientras se guardan en PDF](/cells/es/python-net/print-comments-while-saving-to-pdf/)
- [Renderice complementos de Office mientras convierte Excel a PDF](/cells/es/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Representar una página PDF por hoja de cálculo de Excel: conversión de Excel a PDF](/cells/es/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Renderizar caracteres suplementarios Unicode en la salida PDF por Aspose.Cells](/cells/es/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Remuestreo de imágenes agregadas: conversión de Excel a PDF](/cells/es/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [Guarde cada hoja de trabajo en un archivo PDF diferente](/cells/es/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [Guarde Excel en PDF con tamaño estándar o mínimo](/cells/es/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Guarde las hojas de trabajo especificadas en PDF](/cells/es/python-net/save-specified-worksheets-to-pdf/)
- [Documentos seguros PDF](/cells/es/python-net/secure-pdf-documents/)
- [Especifique cómo cruzar la cadena en la salida PDF y la imagen](/cells/es/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)
