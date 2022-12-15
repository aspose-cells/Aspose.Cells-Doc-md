---
title: Convertir entre formatos de Excel
type: docs
weight: 20
url: /es/net/convert-between-excel-formats/
---
## **Convertir Excel a PDF**

**PDF** Los archivos se utilizan ampliamente para el intercambio de documentos entre organizaciones, sectores gubernamentales e individuos. Es un formato de documento estándar y a menudo se les pide a los desarrolladores de software que encuentren una manera de convertir archivos de Excel Microsoft en**PDF** documentos.
**Aspose.Cells** admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.

Aspose.Cells for .NET admite la conversión de hojas de cálculo a PDF independientemente de otro software. Guarde un archivo de Excel en PDF utilizando el método Guardar de la clase Workbook. El método Save proporciona el miembro de enumeración SaveFormat.Pdf que convierte los archivos nativos de Excel a formato PDF.

**Mudado** directamente desde la hoja de cálculo a PDF, en lugar de usar una herramienta de terceros o un API externo, tiene varios**ventajas**:

1. La conversión directa no requiere archivos temporales porque todo el proceso se puede realizar en la memoria.
1. No se necesita ningún archivo XML, por lo que los archivos grandes se pueden convertir fácilmente.
1. La velocidad de conversión es mucho más rápida.

**Para convertir archivos a PDF:**

1.  Instanciar un objeto de la**Libro de trabajo** clase llamando a su constructor vacío.
1.  Puedes**abrir/cargar** un archivo de plantilla existente u omita este paso si está creando el libro de trabajo desde cero.
1. Realice el trabajo deseado (ingresar datos, aplicar formato, establecer fórmulas, insertar imágenes u otros objetos de dibujo, etc.) en la hoja de cálculo utilizando las API Aspose.Cells'.
1.  Cuando el código de la hoja de cálculo esté completo, llame al**Método de guardado de la clase del libro de trabajo** para guardar la hoja de cálculo. El formato de archivo debe ser PDF, así que seleccione Pdf (un valor predefinido) de la enumeración SaveFormat para generar el documento PDF final.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **Convertir Excel a MHTML**

**MHTML** combina HTML normal con recursos externos (es decir, contenido que suele estar vinculado, como imágenes, animaciones, audio, etc.) en un solo archivo. Se utilizan para correos electrónicos con la extensión de archivo .mht.
Aspose.Cells admite la lectura y escritura de archivos MHTML.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **Conversión de Excel a XPS**

A veces, desea convertir o guardar un libro de trabajo con varias hojas de trabajo en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), de forma predeterminada, tanto Microsoft Excel como Aspose.Cells guardan solo el contenido de la hoja de trabajo activa.

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **Descargar código de muestra**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
