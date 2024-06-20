---
title: Pdf
type: docs
weight: 220
url: /es/python-net/convert-excel-to-pdf/
description: Aprenda cómo convertir Excel a PDF con la API Aspose.Cells para Python via .NET.
keywords: Python convertir Excel a PDF, Convertir Excel a PDF usando Python, Guardar Excel como PDF en Python, Excel a PDF en Python
---

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET admite la conversión de libro de Excel a PDF. En este ejemplo, veremos la conversión completa de un libro de Excel a PDF.

{{% /alert %}}

## **Conversión de libro de Excel a PDF**

Los archivos PDF son ampliamente utilizados para intercambiar documentos entre organizaciones, sectores gubernamentales e individuos. Es un formato de documento estándar y a menudo se pide a los desarrolladores de software que encuentren una forma de convertir archivos de Microsoft Excel en documentos PDF.

Aspose.Cells para Python via .NET admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET escribe directamente la información sobre la API y el número de versión en los documentos de salida. Por ejemplo, al convertir un Documento a PDF, Aspose.Cells for Python via .NET completa el campo **Productor PDF** con el valor, por ejemplo, 'Aspose.Cells for Python via .NET v23.2'.

Tenga en cuenta que puede cambiar esta información en los Documentos de salida por medio de la propiedad [**PdfSaveOptions.producer**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/producer/).

{{% /alert %}}

### **Conversión Directa**

Aspose.Cells for Python via .NET admite la conversión de hojas de cálculo a PDF de forma independiente de otro software. Simplemente guarde un archivo de Excel a PDF usando el método [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) de la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). El método [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) proporciona el miembro de enumeración [**SaveFormat.PDF**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) que convierte los archivos nativos de Excel al formato PDF.

Siga los siguientes pasos para convertir directamente las hojas de cálculo de Excel al formato PDF:

1. Instancia un objeto de la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) llamando a su constructor vacío.
1. Puede abrir/cargar un archivo de plantilla existente o saltarse este paso si está creando el libro de trabajo desde cero.
1. Realice cualquier tarea (ingresar datos, aplicar formato, configurar fórmulas, insertar imágenes u otros objetos de dibujo, etc.) en la hoja de cálculo usando las APIs de Aspose.Cells for Python via .NET.
1. Cuando el código de la hoja de cálculo esté completo, llame al método [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) de la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) para guardar la hoja de cálculo.

El formato de archivo debe ser PDF, así que seleccione *PDF* (un valor predefinido) de la enumeración [**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/) para generar el documento PDF final.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

### **Conversión Avanzada**

También puede optar por utilizar la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) para establecer diferentes atributos para la conversión. Configurar diferentes propiedades de la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) le brinda control sobre la impresión, fuente, seguridad y ajustes de compresión para el PDF de salida. La propiedad más importante es [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/) que le permite guardar los archivos de Excel en archivos PDF/A compatibles.

#### **Guardando el Libro de Trabajo en Archivos PDF/A Compilados**

El fragmento de código proporcionado a continuación demuestra cómo utilizar la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) para guardar archivos de Excel en formato PDF/A compatible.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

Tenga en cuenta que la propiedad [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/) se agregó con el lanzamiento de Aspose.Cells for Python via .NET para .NET 5.3.0.

{{% /alert %}}

#### **Establecer la Hora de Creación del PDF**

Con la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions), puede obtener o establecer la hora de creación del PDF. El siguiente código demuestra el uso de la propiedad [**PdfSaveOptions.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/) para establecer la hora de creación del archivo PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

#### **Establecer la opción ContentCopyForAccessibility**

Con la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions), puede obtener o establecer la opción [**PdfSecurityOptions.accessibility_extract_content**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/) del PDF para controlar el acceso al contenido en el PDF convertido.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

#### **Exportar Propiedades Personalizadas a PDF**

Con la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions), puede exportar las propiedades personalizadas en el libro de origen al PDF. Se proporciona el enumerador [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/) para especificar la forma en que se exportan las propiedades. Estas propiedades se pueden observar en Adobe Acrobat Reader haciendo clic en Archivo y luego en la opción Propiedades, como se muestra en la siguiente imagen. El archivo de plantilla "sourceWithCustProps.xlsx" se puede descargar [aquí](sourceWithCustProps.xlsx) para realizar pruebas y el archivo PDF de salida "outSourceWithCustProps" está disponible [aquí](outSourceWithCustProps.pdf) para su análisis.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

### **Atributos de Conversión**

Trabajamos para mejorar las características de conversión con cada nueva versión. La conversión de Excel a PDF de Aspose.Cells todavía tiene un par de limitaciones. MapChart no es compatible al convertir a formato PDF. Además, algunos objetos de dibujo no son bien compatibles.

La tabla que sigue enumera todas las características que están totalmente o parcialmente compatibles al exportar a PDF utilizando Aspose.Cells for Python via .NET. Esta tabla no es definitiva y no cubre todos los atributos de la hoja de cálculo, pero identifica aquellas características que no son compatibles o son parcialmente compatibles con la conversión a PDF.

|**Elemento del Documento**|**Atributo**|**Compatible**|**Notas**|
| :- | :- | :- | :- |
|Alineación| |Sí| |
|Configuraciones de fondo| |Sí| |
|Borde|Color|Sí| |
|Borde|Estilo de línea|Sí| |
|Borde|Ancho de línea|Sí| |
|Datos de celda| |Sí| |
|Comentarios| |Sí| |
|Formato condicional| |Sí| |
|Propiedades del documento| |Sí| |
|Objetos de dibujo| |Parcialmente|Las sombras y los efectos 3D para los objetos de dibujo no son bien compatibles; WordArt y SmartArt son parcialmente compatibles.|
|Fuente|Tamaño|Sí| |
|Fuente|Color|Sí| |
|Fuente|Estilo|Sí| |
|Fuente|Subrayado|Sí| |
|Fuente|Efectos|Sí||
|Imágenes| |Sí| |
|Hipervínculo| |Sí| |
|Gráficos| |Parcialmente| El MapChart no es compatible.|
|Celdas fusionadas| |Sí| |
|Salto de página| |Sí| |
|Configuración de página|Encabezado/Pie de página|Sí| |
|Configuración de página|Márgenes|Sí| |
|Configuración de página|Orientación de la página|Sí| |
|Configuración de página|Tamaño de la página|Sí| |
|Configuración de página|Área de impresión|Sí| |
|Configuración de página|Títulos de impresión|Sí| |
|Configuración de página|Escalado|Sí| |
|Altura de fila/Ancho de columna| |Sí| |
|Idioma RTL (de derecha a izquierda)| |Sí| |

{{% alert color="primary" %}}

Si su hoja de cálculo contiene fórmulas, es mejor llamar al método [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) justo antes de renderizar la hoja de cálculo al formato PDF. De esta forma se asegurará de que los valores dependientes de las fórmulas se recalculen y se rendericen los valores correctos en el PDF.

{{% /alert %}}

## **Temas avanzados**
- [Agregar Marcadores de PDF](/cells/es/python-net/add-pdf-bookmarks/)
- [Agregar Marcadores de PDF con Destinos Nombrados](/cells/es/python-net/add-pdf-bookmarks-with-named-destinations/)
- [Evitar Página en Blanco en el PDF de salida cuando no hay nada que imprimir](/cells/es/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Convertir Archivo XLSX a Formato PDF](/cells/es/python-net/convert-xlsx-file-to-pdf-format/)
- [Convertir archivo de Excel a formato PDF compatible con PDFA-1a](/cells/es/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Convertir archivo XLS con imágenes o gráficos a PDF](/cells/es/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Crear entrada de marcador de PDF para hoja de gráfico](/cells/es/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [Ajustar todas las columnas de la hoja de cálculo en una sola página de PDF](/cells/es/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Ignorar errores al renderizar Excel a PDF](/cells/es/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [Limitar el número de páginas generadas - Conversión de Excel a PDF](/cells/es/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Imprimir comentarios al guardar en PDF](/cells/es/python-net/print-comments-while-saving-to-pdf/)
- [Renderizar complementos de Office al convertir Excel a PDF](/cells/es/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Renderizar una página de PDF por hoja de cálculo de Excel - Conversión de Excel a PDF](/cells/es/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Renderizar caracteres suplementarios Unicode en el PDF de salida por Aspose.Cells](/cells/es/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Muestrear imágenes agregadas - Conversión de Excel a PDF](/cells/es/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [Guardar cada hoja de cálculo en un archivo PDF diferente](/cells/es/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [Guardar Excel en PDF con tamaño estándar o mínimo](/cells/es/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Guardar hojas de cálculo especificadas en PDF](/cells/es/python-net/save-specified-worksheets-to-pdf/)
- [Documentos PDF seguros](/cells/es/python-net/secure-pdf-documents/)
- [Especificar cómo cruzar cadenas en el PDF de salida e imagen](/cells/es/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)
