---
title: Convertir datos numéricos de texto en números
type: docs
weight: 150
url: /es/java/convert-text-numeric-data-to-number/
description: Aprenda a convertir números almacenados como texto en números usando el Aspose.Cells for Java API.
keywords: excel convert text to number, excel convert text to number java, excel convert text numeric data to number, excel convert text numeric data to number java, excel convert numeric text to number, excel convert numeric text to number java, excel convert numeric text to number with java, convert numeric text to number in excel with java, convert numeric text to number in excel with java, convert numeric string to number in excel with java, excel convert text numeric data to number java, excel convert numeric string to number java
---
{{% alert color="primary" %}}

 A veces, desea convertir datos numéricos ingresados como texto en números. Puede ingresar números como texto en Microsoft Excel poniendo un apóstrofo antes de un número, por ejemplo**'12345**. Luego, Excel trata el número como una cadena. Aspose.Cells le permite convertir cadenas en números.

{{% /alert %}}

Aspose.Cells for Java API proporciona la[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) método que se puede utilizar para convertir todos los datos numéricos de cadena o texto en números.

 La siguiente captura de pantalla muestra números de cadena en celdas**A1:A17**. Los números de cadena están alineados a la izquierda.

**Archivo de entrada: números ingresados como cadenas de texto** 

![todo:imagen_alternativa_texto](convert-text-numeric-data-to-number_1.png)

Estos números de cadena se han convertido en números usando[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) en la siguiente captura de pantalla. Como puede ver, ahora están alineados a la derecha.

**Archivo de salida: las cadenas se han convertido en números** 

![todo:imagen_alternativa_texto](convert-text-numeric-data-to-number_2.png)

El siguiente código de ejemplo ilustra cómo convertir todos los datos numéricos de cadenas en números reales en todas las hojas de trabajo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
