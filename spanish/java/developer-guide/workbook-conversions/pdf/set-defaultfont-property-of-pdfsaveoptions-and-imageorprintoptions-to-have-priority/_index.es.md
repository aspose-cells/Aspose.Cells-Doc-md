---
title: Establezca la propiedad DefaultFont de PdfSaveOptions e ImageOrPrintOptions para que tenga prioridad
type: docs
weight: 30
url: /es/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---
## **Posibles escenarios de uso**

 Mientras se configura el**Fuente predeterminada** propiedad de[**PdfGuardarOpciones**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions) y[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) , es de esperar que al guardar en PDF o en la imagen se establezca que**Fuente predeterminada** a todo el texto del libro al que le falte una fuente (no instalada).

 Por lo general, al guardar en PDF o imagen, Aspose.Cells primero intentará establecer la fuente predeterminada del Libro de trabajo (es decir,[**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) ). Si la fuente predeterminada del libro de trabajo aún no puede mostrar/representar el texto correctamente, entonces Aspose.Cells intentará representar con la fuente mencionada en contra**Fuente predeterminada** atributo en[**PdfGuardarOpciones**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

Para hacer frente a sus expectativas, tenemos una propiedad booleana llamada "**CheckWorkbookDefaultFont** " en[**PdfGuardarOpciones**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) . Puede establecerlo en falso para deshabilitar la fuente predeterminada del libro de trabajo o dejar que el**Fuente predeterminada** instalándose[**PdfGuardarOpciones**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) tener prioridad.

## **Establecer la propiedad DefaultFont de PdfSaveOptions/ImageOrPrintOptions**

El siguiente código de ejemplo abre un archivo de Excel. La celda A1 (en la primera hoja de trabajo) tiene un texto establecido en "Texto de fuente de Navidad". El nombre de la fuente es "Uso personal de Christmas Time" que no está instalado en la máquina. Nosotros fijamos**Fuente predeterminada**atributo de[**PdfGuardarOpciones**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)a "Times New Roman". también establecemos**CheckWorkbookDefaultFont**propiedad booleana a "**falso**", lo que garantiza que el texto de la celda A1 se represente con la fuente "Times New Roman" y no debe usar la fuente predeterminada del libro de trabajo ("Calibri" en este caso). El código representa la primera hoja de trabajo en los formatos de imagen PNG y TIFF. Finalmente se renderiza al formato de archivo PDF.

{{% alert color="primary" %}}

 El valor predeterminado de***CheckWorkbookDefaultFont*** el atributo es**verdadero**.

{{% /alert %}}

Esta es la captura de pantalla del[archivo de plantilla](49446914.xlsx)utilizado en el código de ejemplo.

![todo:imagen_alternativa_texto](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Esta es la imagen de salida PNG después de configurar el[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)propiedad a "Times New Roman".

![todo:imagen_alternativa_texto](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Ver la salida[TIFF](out1_imageTIFF.tiff)imagen después de configurar el[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont)propiedad a "Times New Roman".

Ver la salida[PDF](out1_pdf.pdf)archivo después de configurar el[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont)propiedad a "Times New Roman".

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
