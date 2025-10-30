---
title: Convertir Excel a PDF con Golang a través de C++
linktitle: Convertir Excel a PDF
type: docs
weight: 220
url: /es/go-cpp/convert-excel-to-pdf/
description: Aprende cómo convertir libros de Excel a formato PDF usando Aspose.Cells con Golang a través de C++
---

{{% alert color="primary" %}}

Aspose.Cells soporta la conversión de libros de Excel a PDF. En este ejemplo, veremos la conversión completa de un libro de Excel a PDF.

{{% /alert %}}

## **Conversión de libro de Excel a PDF**

Los archivos PDF son ampliamente utilizados para intercambiar documentos entre organizaciones, sectores gubernamentales y particulares. Es un formato estándar de documento, y a menudo se pide a los desarrolladores de software que encuentren una forma de convertir archivos de Microsoft Excel en documentos PDF.

Aspose.Cells admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.

{{% alert color="primary" %}}

Aspose.Cells for C++ escribe directamente la información sobre la API y el Número de Versión en los documentos de salida. Por ejemplo, al renderizar un documento a PDF, Aspose.Cells for C++ llena el campo **Productor de PDF** con un valor, por ejemplo, 'Aspose.Cells v23.2'.

Ten en cuenta que puedes cambiar esta información en los documentos de salida usando la propiedad [**PdfSaveOptions.GetProducer()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getproducer/). 

{{% /alert %}}

### **Conversión Directa**

Aspose.Cells for C++ admite la conversión de hojas de cálculo a PDF de forma independiente de otro software. Simplemente guarde un archivo de Excel como PDF usando el método [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) de la clase [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/). El método [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) proporciona el miembro de enumeración [**SaveFormat.Pdf**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) que convierte los archivos nativos de Excel al formato PDF.

Siga los siguientes pasos para convertir directamente las hojas de cálculo de Excel al formato PDF:

1. Instancia un objeto de la clase [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) llamando a su constructor vacío.
1. Puede abrir/cargar un archivo de plantilla existente o saltarse este paso si está creando el libro de trabajo desde cero.
1. Realice cualquier trabajo (introducción de datos, aplicar formato, establecer fórmulas, insertar imágenes u objetos de dibujo, etc.) en la hoja de cálculo usando las API de Aspose.Cells.
1. Cuando el código de la hoja de cálculo esté completo, llame al método [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save/) de la clase [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) para guardar la hoja de cálculo.

El formato de archivo debe ser PDF, así que seleccione *Pdf* (un valor predefinido) de la enumeración [**SaveFormat**](https://reference.aspose.com/cells/go-cpp/saveformat/) para generar el documento PDF final.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf.go" >}}
### **Conversión Avanzada**

También puede optar por usar la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) para establecer diferentes atributos para la conversión. La configuración de diferentes propiedades de la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) le da control sobre la impresión, la fuente, la seguridad y la compresión del PDF de salida.

La propiedad más importante es [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/), que le permite establecer el nivel de cumplimiento de los estándares PDF. Actualmente, puede guardar en formatos PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab, y PDF/A-3u. Tenga en cuenta que con el formato PDF/A, el tamaño del archivo de salida es mayor que el tamaño de un archivo PDF regular.

#### **Guardando el Libro de Trabajo en Archivos PDF/A Compilados**

El fragmento de código proporcionado a continuación demuestra cómo usar la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) para guardar archivos de Excel en formato PDF compatible con PDF/A.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-1.go" >}}
{{% alert color="primary" %}}

Tenga en cuenta que, la propiedad [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/) se agregó con la versión Aspose.Cells for C++ 5.3.0.

{{% /alert %}}

#### **Establecer la Hora de Creación del PDF**

Con la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/), puede obtener o establecer el tiempo de creación del PDF. El siguiente código demuestra el uso de la propiedad [**PdfSaveOptions.GetCreatedTime()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcreatedtime/) para establecer el tiempo de creación del archivo PDF.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-2.go" >}}
#### **Establecer la opción ContentCopyForAccessibility**

Con la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/), puede obtener o establecer la opción [**GetAccessibilityExtractContent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/getaccessibilityextractcontent/) del PDF para controlar el acceso al contenido en el PDF convertido.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-3.go" >}}
#### **Exportar Propiedades Personalizadas a PDF**

Con la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/), puede exportar las propiedades personalizadas en el libro de origen al PDF. Se proporciona el enumerador [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfcustompropertiesexport/) para especificar la forma en que se exportan las propiedades. Estas propiedades se pueden observar en Adobe Acrobat Reader haciendo clic en Archivo y luego en la opción Propiedades como se muestra en la siguiente imagen. El archivo de plantilla "sourceWithCustProps.xlsx" se puede descargar [aquí](sourceWithCustProps.xlsx) para prueba, y el archivo PDF de salida "outSourceWithCustProps" está disponible [aquí](outSourceWithCustProps.pdf) para análisis.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Pdf-4.go" >}}
### **Atributos de Conversión**

Trabajamos para mejorar las funciones de conversión con cada nueva versión. La conversión de Excel a PDF de Aspose.Cells aún tiene un par de limitaciones. MapChart no es compatible cuando se convierte al formato PDF. Además, algunos objetos de dibujo no son soportados bien.

La tabla que sigue enumera todas las funciones que son totalmente o parcialmente soportadas al exportar a PDF usando Aspose.Cells. Esta tabla no es definitiva y no cubre todos los atributos de la hoja de cálculo, pero identifica esas funciones que no son soportadas o que solo son parcialmente soportadas para la conversión a PDF.

| **Elemento del Documento** | **Atributo** | **Soportado** | **Notas** |
| :- | :- | :- | :- |
| Alineación |  | Sí |  |
| Configuración de fondo |  | Sí |  |
| Borde | Color | Sí |  |
| Borde | Estilo de línea | Sí |  |
| Borde | Ancho de línea | Sí |  |
| Datos de celda |  | Sí |  |
| Comentarios |  | Sí |  |
| Formato condicional |  | Sí |  |
| Propiedades del Documento |  | Sí |  |
| Objetos de dibujo |  | Parcialmente | Los efectos de sombra y 3D en los objetos de dibujo no son soportados bien; WordArt y SmartArt son soportados parcialmente. |
| Fuente | Tamaño | Sí |  |
| Fuente | Color | Sí |  |
| Fuente | Estilo | Sí |  |
| Fuente | Subrayado | Sí |  |
| Fuente | Efectos | Sí |  |
| Imágenes |  | Sí |  |
| Hipervínculo |  | Sí |  |
| Gráficos |  | Parcialmente | MapChart no es compatible. |
| Celdas combinadas |  | Sí |  |
| Salto de página |  | Sí |  |
| Configuración de página | Encabezado/Pie de página | Sí |  |
| Configuración de página | Márgenes | Sí |  |
| Configuración de página | Orientación de página | Sí |  |
| Configuración de página | Tamaño de página | Sí |  |
| Configuración de página | Área de impresión | Sí |  |
| Configuración de página | Títulos de impresión | Sí |  |
| Configuración de página | Escalado | Sí |  |
| Altura de fila / Ancho de columna |  | Sí |  |
| Lengua RTL (Derecha a Izquierda) |  | Sí |  |

{{% alert color="primary" %}}

Si tu hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) justo antes de renderizar la hoja a formato PDF. Hacerlo asegurará que los valores dependientes de fórmulas sean recalculados y que se rendericen los valores correctos en el PDF.

{{% /alert %}}

## **Temas avanzados**
- [Agregar Marcadores de PDF con Destinos Nombrados](/cells/es/cpp/add-pdf-bookmarks-with-named-destinations/)
- [Cambie la fuente solo en los caracteres Unicode específicos al guardar en PDF](/cells/es/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Convertir Archivo XLSX a Formato PDF](/cells/es/cpp/convert-xlsx-file-to-pdf-format/)
- [Convertir archivo de Excel a formato PDF compatible con PDFA-1a](/cells/es/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Convertir archivo XLS con imágenes o gráficos a PDF](/cells/es/cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Crear entrada de marcador de PDF para hoja de gráfico](/cells/es/cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Ajustar todas las columnas de la hoja de cálculo en una sola página de PDF](/cells/es/cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Obtenga DrawObject y Bound al renderizar a PDF utilizando la clase DrawObjectEventHandler](/cells/es/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Obtenga advertencias por sustitución de fuentes al renderizar el archivo de Excel](/cells/es/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignorar errores al renderizar Excel a PDF](/cells/es/cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Limitar el número de páginas generadas - Conversión de Excel a PDF](/cells/es/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Imprimir comentarios al guardar en PDF](/cells/es/cpp/print-comments-while-saving-to-pdf/)
- [Renderizar complementos de Office al convertir Excel a PDF](/cells/es/cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Renderizar una página de PDF por hoja de cálculo de Excel - Conversión de Excel a PDF](/cells/es/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Renderizar caracteres suplementarios Unicode en el PDF de salida por Aspose.Cells](/cells/es/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Muestrear imágenes agregadas - Conversión de Excel a PDF](/cells/es/cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Guardar cada hoja de cálculo en un archivo PDF diferente](/cells/es/cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Guardar Excel en PDF con tamaño estándar o mínimo](/cells/es/cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Guardar hojas de cálculo especificadas en PDF](/cells/es/cpp/save-specified-worksheets-to-pdf/)
- [Documentos PDF seguros](/cells/es/cpp/secure-pdf-documents/)
- [Especificar cómo cruzar cadenas en el PDF de salida e imagen](/cells/es/cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
