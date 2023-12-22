---
title: Convertir datos numéricos de texto a números
type: docs
weight: 900
url: /es/net/convert-text-numeric-data-to-number/
description: Aprenda a convertir números almacenados como texto en Excel en números utilizando Aspose.Cells for .NET API.
keywords: excel convert text to number, excel convert text to number c#, excel convert text numeric data to number, excel convert text numeric data to number c#, excel convert numeric text to number, excel convert numeric text to number c#, excel convert numeric text to number with c#, convert numeric text to number in excel with c#, convert numeric text to number in excel with c#, convert numeric string to number in excel with c#, excel convert text numeric data to number c#, excel convert numeric string to number c#
---
##  **Posibles escenarios de uso**
A veces, desea convertir datos numéricos ingresados como texto en números. Puede ingresar números como texto en Microsoft Excel poniendo un apóstrofe antes de un número, por ejemplo *'12345**. Luego, Excel trata el número como una cadena. Aspose.Cells le permite convertir cadenas en números.


##  Cómo convertir números almacenados como texto a números en Excel
Puede convertir números almacenados como texto en números siguiendo unos sencillos pasos.
1. Seleccione cualquier celda o rango de celdas que tenga un indicador de error en la esquina superior izquierda.
1.  Junto a la celda o rango de celdas seleccionado, haga clic en el botón de error que aparece. En el menú, haga clic en Convertir a número.
<br>
<img src="4.png" width=70% />
1. Si el botón de alerta no está disponible, seleccione una columna con este problema. Si no desea convertir toda la columna, puede seleccionar una o más celdas. Solo asegúrese de que las celdas que seleccione estén en la misma columna; de lo contrario, este proceso no funcionará. El botón Texto en columnas se utiliza normalmente para dividir una columna, pero también se puede utilizar para convertir una sola columna de texto en números. En la pestaña Datos, haga clic en Texto en columnas.
<br>
<img src="1.png" width=70% />
1. Haga clic en el botón Finalizar en el cuadro emergente.
<br>
<img src="2.png" width=70% />
1. Los números almacenados como texto se transforman en números.
<br>
<img src="3.png" width=70% />

## Cómo convertir números almacenados como texto a números usando Aspose.Cells for .NET
Aspose.Cells proporciona la[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)método que se puede utilizar para convertir todos los datos numéricos de cadena o texto en números.

La siguiente captura de pantalla muestra números de cadena en las celdas *A1:A17**. Los números de cadena están alineados a la izquierda.
<br>
<img src="5.png" width=70% />

 Estos números de cadena se han convertido en números usando[**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue)en la siguiente captura de pantalla. Como puede ver, ahora están alineados a la derecha.
<br>
<img src="6.png" width=70% />

##  Código C# para convertir datos numéricos de cadena en números reales

El siguiente código de muestra ilustra cómo convertir todos los datos numéricos de cadena en números reales en todas las hojas de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
