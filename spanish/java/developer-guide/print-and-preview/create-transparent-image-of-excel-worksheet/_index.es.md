---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 80
url: /es/java/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

A veces, es necesario generar la imagen de su hoja de cálculo como una imagen transparente. Desea aplicar transparencia a todas las celdas que no tienen colores de relleno. Aspose.Cells proporciona la propiedad [**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent) para aplicar transparencia a la imagen de la hoja de cálculo. Cuando esta propiedad es **falsa**, las celdas sin colores de relleno se dibujan con color blanco y cuando es **verdadero**, las celdas sin colores de relleno se dibujan de manera transparente.

{{% /alert %}}

En la siguiente imagen de la hoja de cálculo, no se ha aplicado transparencia. Las celdas sin colores de relleno se dibujan de color blanco.

**Imagen de la hoja de cálculo sin aplicar transparencia**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)

Mientras que, en la siguiente imagen de la hoja de cálculo, se ha aplicado transparencia. Las celdas sin colores de relleno son transparentes.

**Imagen de la hoja de cálculo después de aplicar transparencia**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)

Puede usar el siguiente código de ejemplo para generar una imagen transparente de su hoja de cálculo de Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
{{< app/cells/assistant language="java" >}}
