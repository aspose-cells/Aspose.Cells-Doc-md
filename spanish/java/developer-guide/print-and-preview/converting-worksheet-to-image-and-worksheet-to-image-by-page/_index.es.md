---
title: Conversión de hoja de trabajo a imagen y hoja de trabajo a imagen por página
type: docs
weight: 210
url: /es/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

Este documento está diseñado para proporcionar a los desarrolladores una comprensión detallada de cómo convertir una hoja de trabajo en un archivo de imagen y una hoja de trabajo con varias páginas en un archivo de imagen por página.

A veces, es posible que necesite presentar hojas de trabajo como imágenes, por ejemplo, para usarlas en aplicaciones o páginas web. Es posible que deba insertar las imágenes en un documento de Word, un archivo PDF, una presentación PowerPoint o usarlas en algún otro escenario. Simplemente, desea representar la hoja de trabajo como una imagen. Aspose.Cells Las API admiten la conversión de hojas de trabajo en Microsoft archivos de Excel a imágenes. Además, Aspose.Cells admite la conversión de un libro de trabajo en varios archivos de imagen, uno por página.

{{% /alert %}}

## **Uso de Aspose.Cells para convertir la hoja de trabajo en un archivo de imagen**

Este artículo muestra cómo usar Aspose.Cells for Java API para convertir una hoja de trabajo en una imagen. El API proporciona varias clases valiosas, como[**HojaRenderizar**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) , y así. los[**HojaRenderizar**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) class representa una hoja de trabajo para representar imágenes para la hoja de trabajo y tiene una sobrecarga[**a la imagen**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)) que puede convertir una hoja de trabajo en archivos de imagen directamente con cualquier atributo u opción establecida.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **Resultado**

Después de ejecutar el código anterior, la hoja de trabajo denominada Sheet1 se convierte en un archivo de imagen SheetImage.jpg.

**La salida JPG**

![todo:imagen_alternativa_texto](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **Uso de Aspose.Cells para convertir la hoja de trabajo en un archivo de imagen por página**

Este ejemplo muestra cómo usar Aspose.Cells para convertir una hoja de cálculo de un libro de plantilla que tiene varias páginas a un archivo de imagen por página.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **Resultado**

Después de ejecutar el código anterior, la hoja de trabajo denominada Hoja1 se convierte en dos archivos de imagen (1 por página): Hoja 1 Página 1.Tiff y Hoja 1 Página 2.Tiff.

**Archivo de imagen generado (Hoja 1 Página 1.Tiff)**

![todo:imagen_alternativa_texto](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**Archivo de imagen generado (Hoja 1 Página 2.Tiff)**

![todo:imagen_alternativa_texto](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

Este artículo muestra cómo convertir una hoja de trabajo en un archivo de imagen y convertir hojas de trabajo con varias páginas en varios archivos de imagen (uno por página) usando Aspose.Cells. Aspose.Cells ofrece más flexibilidad que otros componentes y brinda una velocidad, eficiencia y confiabilidad sobresalientes. Los resultados muestran que Aspose.Cells se ha beneficiado de años de investigación, diseño y ajuste cuidadoso.

{{% /alert %}}

## Artículos relacionados

- [Conversión de hoja de trabajo a diferentes formatos de imagen](/cells/es/java/converting-worksheet-to-different-image-formats/)
- [Exportar hoja de trabajo o gráfico a una imagen con el ancho y la altura deseados](/cells/es/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
