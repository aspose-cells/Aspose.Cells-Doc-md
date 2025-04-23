---
title: Pdf
type: docs
weight: 220
url: /es/net/convert-excel-to-pdf/
---

{{% alert color="primary" %}}

Aspose.Cells admite la conversión de Libro de Trabajo de Excel a PDF. En este ejemplo, veremos la conversión completa de un Libro de Trabajo de Excel a PDF.

{{% /alert %}}

## **Conversión de libro de Excel a PDF**

Los archivos PDF son ampliamente utilizados para intercambiar documentos entre organizaciones, sectores gubernamentales e individuos. Es un formato de documento estándar y a menudo se pide a los desarrolladores de software que encuentren una forma de convertir archivos de Microsoft Excel en documentos PDF.

Aspose.Cells admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.

{{% alert color="primary" %}}

Aspose.Cells for .NET escribe directamente la información sobre la API y el número de versión en los documentos de salida. Por ejemplo, al renderizar el documento a PDF, Aspose.Cells for .NET populiza el campo **Productor de PDF** con el valor, por ejemplo 'Aspose.Cells v23.2'.

Tenga en cuenta que puede cambiar esta información en los Documentos de salida por medio de la propiedad [**PdfSaveOptions.Producer**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/producer/).

{{% /alert %}}

### **Conversión Directa**

Aspose.Cells for .NET admite la conversión de hojas de cálculo a PDF independientemente de otro software. Simplemente guarde un archivo de Excel a PDF mediante el método [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). El método [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) proporciona el miembro de la enumeración [**SaveFormat.Pdf**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) que convierte los archivos de Excel nativos al formato PDF.

Siga los siguientes pasos para convertir directamente las hojas de cálculo de Excel al formato PDF:

1. Instancia un objeto de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) llamando a su constructor vacío.
1. Puede abrir/cargar un archivo de plantilla existente o saltarse este paso si está creando el libro de trabajo desde cero.
1. Realiza cualquier trabajo (ingreso de datos, aplicación de formato, definición de fórmulas, inserción de imágenes u otros objetos de dibujo, etc.) en la hoja de cálculo usando las APIs de Aspose.Cells.
1. Cuando el código de la hoja de cálculo esté completo, llame al método [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) para guardar la hoja de cálculo.

El formato de archivo debe ser PDF, por lo que seleccione *Pdf* (un valor predefinido) de la enumeración [**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) para generar el documento final en PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **Conversión Avanzada**

También puede optar por usar la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) para configurar diferentes atributos para la conversión. El establecimiento de diferentes propiedades de la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) le da control sobre la impresión, la fuente, la seguridad y la configuración de compresión para el PDF de salida. 

La propiedad más importante es [**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) que le permite configurar el nivel de cumplimiento de los estándares PDF. Actualmente, puede guardar en los formatos PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab y PDF/A-3u. Tenga en cuenta que con el formato PDF/A, el tamaño de archivo de salida es más grande que el tamaño de archivo PDF regular.

#### **Guardando el Libro de Trabajo en Archivos PDF/A Compilados**

El fragmento de código proporcionado a continuación demuestra cómo utilizar la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions) para guardar archivos de Excel en formato PDF/A compatible.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

Tenga en cuenta que la propiedad [**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance) se agregó con el lanzamiento de Aspose.Cells for .NET 5.3.0.

{{% /alert %}}

#### **Establecer la Hora de Creación del PDF**

Con la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions), puede obtener o establecer la hora de creación del PDF. El siguiente código demuestra el uso de la propiedad [**PdfSaveOptions.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime) para establecer la hora de creación del archivo PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **Establecer la opción ContentCopyForAccessibility**

Con la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions), puede obtener o establecer la opción [**AccessibilityExtractContent**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent) del PDF para controlar el acceso al contenido en el PDF convertido.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **Exportar Propiedades Personalizadas a PDF**

Con la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions), puede exportar las propiedades personalizadas en el libro de origen al PDF. Se proporciona el enumerador [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport) para especificar la forma en que se exportan las propiedades. Estas propiedades se pueden observar en Adobe Acrobat Reader haciendo clic en Archivo y luego en la opción Propiedades, como se muestra en la siguiente imagen. El archivo de plantilla "sourceWithCustProps.xlsx" se puede descargar [aquí](sourceWithCustProps.xlsx) para realizar pruebas y el archivo PDF de salida "outSourceWithCustProps" está disponible [aquí](outSourceWithCustProps.pdf) para su análisis.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

### **Atributos de Conversión**

Trabajamos para mejorar las características de conversión con cada nueva versión. La conversión de Excel a PDF de Aspose.Cells todavía tiene un par de limitaciones. MapChart no es compatible al convertir a formato PDF. Además, algunos objetos de dibujo no son bien compatibles.

La tabla que sigue lista todas las características que son completamente o parcialmente soportadas al exportar a PDF con Aspose.Cells. Esta tabla no es final y no cubre todos los atributos de la hoja de cálculo, pero identifica aquellas características que no son soportadas o parcialmente soportadas para la conversión a PDF.

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

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) justo antes de renderizar la hoja de cálculo al formato PDF. Al hacerlo, asegurará que los valores dependientes de las fórmulas se recalculen y se rendericen los valores correctos en el PDF.

{{% /alert %}}

## **Temas avanzados**
- [Agregar Marcadores de PDF](/cells/es/net/add-pdf-bookmarks/)
- [Agregar Marcadores de PDF con Destinos Nombrados](/cells/es/net/add-pdf-bookmarks-with-named-destinations/)
- [Evitar Página en Blanco en el PDF de salida cuando no hay nada que imprimir](/cells/es/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Cambie la fuente solo en los caracteres Unicode específicos al guardar en PDF](/cells/es/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Controlar la carga de recursos externos en el libro de Excel de MS al renderizar a PDF](/cells/es/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [Convertir Archivo XLSX a Formato PDF](/cells/es/net/convert-xlsx-file-to-pdf-format/)
- [Convertir archivo de Excel a formato PDF compatible con PDFA-1a](/cells/es/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Convertir archivo XLS con imágenes o gráficos a PDF](/cells/es/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [Crear entrada de marcador de PDF para hoja de gráfico](/cells/es/net/create-pdfbookmarkentry-for-chart-sheet/)
- [Ajustar todas las columnas de la hoja de cálculo en una sola página de PDF](/cells/es/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [Obtenga DrawObject y Bound al renderizar a PDF utilizando la clase DrawObjectEventHandler](/cells/es/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Obtenga advertencias por sustitución de fuentes al renderizar el archivo de Excel](/cells/es/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignorar errores al renderizar Excel a PDF](/cells/es/net/ignore-errors-while-rendering-excel-to-pdf/)
- [Limitar el número de páginas generadas - Conversión de Excel a PDF](/cells/es/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Imprimir comentarios al guardar en PDF](/cells/es/net/print-comments-while-saving-to-pdf/)
- [Renderizar complementos de Office al convertir Excel a PDF](/cells/es/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Renderizar una página de PDF por hoja de cálculo de Excel - Conversión de Excel a PDF](/cells/es/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Renderizar caracteres suplementarios Unicode en el PDF de salida por Aspose.Cells](/cells/es/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Muestrear imágenes agregadas - Conversión de Excel a PDF](/cells/es/net/resampling-added-images-excel-to-pdf-conversion/)
- [Guardar cada hoja de cálculo en un archivo PDF diferente](/cells/es/net/save-each-worksheet-to-a-different-pdf-file/)
- [Guardar Excel en PDF con tamaño estándar o mínimo](/cells/es/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Guardar hojas de cálculo especificadas en PDF](/cells/es/net/save-specified-worksheets-to-pdf/)
- [Documentos PDF seguros](/cells/es/net/secure-pdf-documents/)
- [Especificar cómo cruzar cadenas en el PDF de salida e imagen](/cells/es/net/specify-how-to-cross-string-in-output-pdf-and-image/)
{{< app/cells/assistant language="csharp" >}}
