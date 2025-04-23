---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /es/net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

A veces, es necesario generar la imagen de la hoja de cálculo como una imagen transparente. Desea aplicar transparencia a todas las celdas que no tienen colores de relleno. Aspose.Cells proporciona la propiedad [**ImageOrPrintOptions.Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent) para aplicar transparencia a la imagen de la hoja de cálculo. Cuando esta propiedad es **false**, entonces las celdas sin colores de relleno se dibujan con color blanco, y cuando es **true**, las celdas sin colores de relleno se dibujan transparentes.

{{% /alert %}} 

En la siguiente imagen de la hoja de cálculo, no se ha aplicado transparencia. Las celdas sin colores de relleno se dibujan de color blanco.

|**Resultado sin transparencia: el fondo de la celda es blanco**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

Mientras que, en la siguiente imagen de la hoja de cálculo, se ha aplicado transparencia. Las celdas sin colores de relleno son transparentes.

|**Resultado con transparencia habilitada**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

El siguiente código de ejemplo genera una imagen transparente a partir de una hoja de cálculo de Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
