---
title: Establecer la propiedad DefaultFont de PdfSaveOptions y ImageOrPrintOptions para tener prioridad
type: docs
weight: 30
url: /es/java/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
---

## **Escenarios de uso posibles**

Al establecer la propiedad DefaultFont de [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions) y [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), es posible que espere que al guardar como PDF o imagen, se establezca ese DefaultFont para todo el texto en el libro de trabajo que tenga una fuente faltante (no instalada).

Por lo general, al guardar como PDF o imagen, Aspose.Cells intentará primero establecer la fuente predeterminada del Libro de trabajo (es decir, [**Workbook.DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font-)). Si la fuente predeterminada del libro aún no puede mostrar o renderizar el texto correctamente, Aspose.Cells intentará renderizar con la fuente mencionada en el atributo **DefaultFont** en [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

Para cumplir con sus expectativas, tenemos una propiedad booleana llamada "CheckWorkbookDefaultFont" en [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions). Puede establecerla en false para deshabilitar el intento de usar la fuente predeterminada del libro de trabajo o permitir que la configuración DefaultFont en [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) tenga prioridad.

## **Establecer la propiedad DefaultFont de PdfSaveOptions/ImageOrPrintOptions**

El siguiente código de muestra abre un archivo de Excel. La celda A1 (en la primera hoja de cálculo) tiene un texto configurado como "Texto de Fuente de Tiempo de Navidad". El nombre de la fuente es "Uso Personal de Tiempo de Navidad" que no está instalado en la máquina. Configuramos el atributo DefaultFont de [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) en "Times New Roman". También establecemos la propiedad booleana CheckWorkbookDefaultFont en "false" que garantiza que el texto de la celda A1 se represente con la fuente "Times New Roman" y no use la fuente predeterminada del libro de trabajo ("Calibri" en este caso). El código renderiza la primera hoja de cálculo a los formatos de imagen PNG y TIFF. Finalmente, se renderiza en el formato de archivo PDF.

{{% alert color="primary" %}}

El valor predeterminado de la propiedad ***CheckWorkbookDefaultFont*** es **true**.

{{% /alert %}}

Esta es la captura de pantalla del [archivo de plantilla](49446914.xlsx) utilizado en el código de ejemplo.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Esta es la imagen PNG de salida después de establecer la propiedad [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) en "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Vea la imagen [TIFF](out1_imageTIFF.tiff) de salida después de configurar la propiedad [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) en "Times New Roman".

Vea el archivo [PDF](out1_pdf.pdf) de salida después de configurar la propiedad [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DefaultFont) en "Times New Roman".

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Fonts-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions-1.java" >}}
{{< app/cells/assistant language="java" >}}
