---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /es/python-net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

A veces, necesitas generar la imagen de tu hoja de cálculo como una imagen transparente. Quieres aplicar transparencia a todas las celdas que no tengan colores de relleno. Aspose.Cells para Python via .NET proporciona la propiedad [**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent) para aplicar transparencia a la imagen de la hoja de cálculo. Cuando esta propiedad es **falsa**, las celdas sin colores de relleno se dibujan en blanco y cuando es **verdadera**, las celdas sin colores de relleno se dibujan transparentes.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-CreateTransparentImage-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
