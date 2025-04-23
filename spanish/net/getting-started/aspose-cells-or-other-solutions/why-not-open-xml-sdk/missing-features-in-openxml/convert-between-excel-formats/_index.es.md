---
title: Convertir entre formatos de Excel
type: docs
weight: 20
url: /es/net/convert-between-excel-formats/
---

## **Convirtiendo Excel a PDF**

Los archivos **PDF** se utilizan ampliamente para intercambiar documentos entre organizaciones, sectores gubernamentales e individuos. Es un formato de documento estándar y a menudo se pide a los desarrolladores de software que encuentren una forma de convertir archivos de Microsoft Excel en documentos **PDF**.
**Aspose.Cells** admite la conversión de archivos de Excel a PDF y mantiene una alta fidelidad visual en la conversión.

Aspose.Cells for .NET admite la conversión de hojas de cálculo a PDF de forma independiente a otro software. Guarde un archivo de Excel a PDF utilizando el método Save de la clase Workbook. El método Save proporciona el miembro de enumeración SaveFormat.Pdf que convierte los archivos nativos de Excel al formato PDF.

**La conversión** directamente desde la hoja de cálculo a PDF, en lugar de utilizar una herramienta de terceros o una API externa, tiene varias **ventajas**:

1. La conversión directa no requiere archivos temporales porque todo el proceso se puede realizar en memoria.
1. No se necesita archivo XML, por lo que los archivos grandes se pueden convertir fácilmente.
1. La velocidad de conversión es mucho más rápida.

**Para convertir archivos a PDF:**

1. Instantiate un objeto de la clase **Workbook** llamando a su constructor vacío.
1. Puede **abrir/cargar** un archivo de plantilla existente o omitir este paso si está creando el libro de trabajo desde cero.
1. Realice el trabajo deseado (ingrese datos, aplique formato, establezca fórmulas, inserte imágenes u otros objetos de dibujo, etc.) en la hoja de cálculo utilizando las API de Aspose.Cells.
1. Cuando el código de la hoja de cálculo esté completo, llame al **método Save de la clase Workbook** para guardar la hoja de cálculo. El formato de archivo debe ser PDF, así que seleccione Pdf (un valor predefinido) de la enumeración SaveFormat para generar el documento PDF final.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **Convertir Excel a MHTML**

**MHTML** combina HTML normal con recursos externos (es decir, contenido que generalmente está vinculado, como imágenes, animaciones, audio, etc.) en un solo archivo. Se utilizan para correos electrónicos con la extensión de archivo .mht.
Aspose.Cells admite la lectura y escritura de archivos MHTML.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **Convertir Excel a XPS**

A veces, es posible que desee convertir o guardar un libro de trabajo con varias hojas de cálculo en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), tanto Microsoft Excel como Aspose.Cells guardan por defecto el contenido de la hoja de cálculo activa únicamente.

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **Descargar Código de Ejemplo**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
