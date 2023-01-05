---
title: Convertir datos numéricos de texto en números
type: docs
weight: 900
url: /es/net/convert-text-numeric-data-to-number/
description: Aprenda a convertir números almacenados como texto en Excel a números usando el Aspose.Cells for .NET API.
keywords: excel convert text to number, excel convert text to number c#, excel convert text numeric data to number, excel convert text numeric data to number c#, excel convert numeric text to number, excel convert numeric text to number c#, excel convert numeric text to number with c#, convert numeric text to number in excel with c#, convert numeric text to number in excel with c#, convert numeric string to number in excel with c#, excel convert text numeric data to number c#, excel convert numeric string to number c#
---
{{% alert color="primary" %}}

 A veces, desea convertir datos numéricos ingresados como texto en números. Puede ingresar números como texto en Microsoft Excel poniendo un apóstrofo antes de un número, por ejemplo**'12345**. Luego, Excel trata el número como una cadena. Aspose.Cells le permite convertir cadenas en números.

{{% /alert %}}

Aspose.Cells proporciona el[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)método que se puede utilizar para convertir todos los datos numéricos de cadena o texto en números.

 La siguiente captura de pantalla muestra números de cadena en celdas**A1:A17**. Los números de cadena están alineados a la izquierda.

|**Archivo de entrada: números ingresados como cadenas de texto**|
|:- |
|![todo:imagen_alternativa_texto](convert-text-numeric-data-to-number_1.png)|

Estos números de cadena se han convertido en números usando[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)en la siguiente captura de pantalla. Como puede ver, ahora están alineados a la derecha.

|**Archivo de salida: las cadenas se han convertido en números**|
|:- |
|![todo:imagen_alternativa_texto](convert-text-numeric-data-to-number_2.png)|

## C# código para convertir datos numéricos de cadena a números reales

El siguiente código de ejemplo ilustra cómo convertir todos los datos numéricos de cadenas en números reales en todas las hojas de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
