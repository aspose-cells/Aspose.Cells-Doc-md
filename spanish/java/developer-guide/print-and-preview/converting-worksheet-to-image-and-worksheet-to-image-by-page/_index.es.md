---
title: Convertir hoja de cálculo a imagen y hoja de cálculo a imagen por página
type: docs
weight: 210
url: /es/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Este documento está diseñado para brindar a los desarrolladores una comprensión detallada de cómo convertir una hoja de cálculo a un archivo de imagen y una hoja de cálculo con varias páginas a un archivo de imagen por página.

A veces, es posible que necesites presentar hojas de cálculo como imágenes, por ejemplo, para usarlas en aplicaciones o páginas web. Es posible que necesites insertar las imágenes en un documento de Word, un archivo PDF, una presentación de PowerPoint o utilizarlas en algún otro escenario. Simplemente, quieres renderizar la hoja de cálculo como una imagen. Las API de Aspose.Cells admiten la conversión de hojas de cálculo en archivos de Microsoft Excel a imágenes. Además, Aspose.Cells admite la conversión de un libro de trabajo a varios archivos de imagen, uno por página.

{{% /alert %}}

## **Usar Aspose.Cells para convertir hoja de cálculo a archivo de imagen**

Este artículo muestra cómo usar la API Aspose.Cells for Java para convertir una hoja de cálculo a imagen. La API proporciona varias clases valiosas, como [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), y así sucesivamente. La clase [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) representa una hoja de cálculo para renderizar imágenes de la hoja de cálculo y tiene un método sobrecargado de [**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)) que puede convertir una hoja de cálculo a archivos de imagen directamente con cualquier atributo u opciones establecidas.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **Resultado**

Después de ejecutar el código anterior, la hoja de cálculo nombrada Hoja1 se convierte en un archivo de imagen HojaImagen.jpg.

**La salida JPG**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **Usar Aspose.Cells para convertir hoja de cálculo a archivo de imagen por página**

Este ejemplo muestra cómo usar Aspose.Cells para convertir una hoja de cálculo de un libro de trabajo que tiene varias páginas a un archivo de imagen por página.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **Resultado**

Después de ejecutar el código anterior, la hoja de cálculo llamada Hoja1 se convierte en dos archivos de imagen (uno por página) Hoja 1 Página 1.Tiff y Hoja 1 Página 2.Tiff.

**Archivo de imagen generado (Hoja 1 Página 1.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**Archivo de imagen generado (Hoja 1 Página 2.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

Este artículo muestra cómo convertir una hoja de cálculo en un archivo de imagen y convertir hojas de cálculo con varias páginas en varios archivos de imagen (uno por página) usando Aspose.Cells. Aspose.Cells ofrece más flexibilidad que otros componentes y proporciona una velocidad, eficiencia y confiabilidad excepcionales. Los resultados muestran que Aspose.Cells se ha beneficiado de años de investigación, diseño y ajuste cuidadoso.

{{% /alert %}}

## Artículos relacionados

- [Conversión de hoja de cálculo a diferentes formatos de imagen](/cells/es/java/converting-worksheet-to-different-image-formats/)
- [Exportar hoja de cálculo o gráfico a imagen con ancho y alto deseados](/cells/es/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
