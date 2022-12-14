---
title: Crear una imagen transparente de la hoja de cálculo de Excel
type: docs
weight: 170
url: /es/net/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

 A veces, necesita generar la imagen de su hoja de trabajo como una imagen transparente. Desea aplicar transparencia a todas las celdas que no tienen colores de relleno. Aspose.Cells proporciona el[**ImageOrPrintOptions.Transparente**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)propiedad para aplicar transparencia a la imagen de la hoja de cálculo. Cuando esta propiedad es**falso** , entonces las celdas sin colores de relleno se dibujan con color blanco y cuando es**verdadero**, las celdas sin colores de relleno se dibujan transparentes.

{{% /alert %}} 

En la siguiente imagen de hoja de cálculo, no se ha aplicado transparencia. Las celdas sin colores de relleno se dibujan en blanco.

|**Salida sin transparencia: el fondo de la celda es blanco**|
|:- |
|![todo:imagen_alternativa_texto](create-transparent-image-of-excel-worksheet_1.png)|

Mientras que, en la siguiente imagen de la hoja de trabajo, se ha aplicado transparencia. Las celdas sin colores de relleno son transparentes.

|**Salida con transparencia habilitada**|
|:- |
|![todo:imagen_alternativa_texto](create-transparent-image-of-excel-worksheet_2.png)|

El siguiente código de ejemplo genera una imagen transparente a partir de una hoja de cálculo de Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
