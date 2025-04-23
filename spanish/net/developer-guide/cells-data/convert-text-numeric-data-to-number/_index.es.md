---
title: Convertir Datos Numéricos de Texto a Número
type: docs
weight: 900
url: /es/net/convert-text-numeric-data-to-number/
description: Aprende a convertir números almacenados como texto en Excel a números utilizando la API Aspose.Cells for .NET.
keywords: excel convertir texto a número, excel convertir texto a número c#, excel convertir datos numéricos de texto a número, excel convertir datos numéricos de texto a número c#, excel convertir texto numérico a número, excel convertir texto numérico a número c#, excel convertir texto numérico a número con c#, convertir texto numérico a número en excel con c#, convertir texto numérico a número en excel con c#, convertir cadena numérica en número en excel con c#, excel convertir datos numéricos de texto a número c#, excel convertir cadena numérica a número c#
---

## **Escenarios de uso posibles**
A veces, deseas convertir datos numéricos ingresados como texto a números. Puedes ingresar números como texto en Microsoft Excel poniendo un apóstrofe antes de un número, por ejemplo **'12345**. Entonces, Excel trata el número como una cadena. Aspose.Cells te permite convertir cadenas a números.


## Cómo convertir números almacenados como texto a números en Excel
Puede convertir números almacenados como texto a números siguiendo unos pocos pasos simples.
1. Seleccione cualquier celda individual o rango de celdas que tenga un indicador de error en la esquina superior izquierda.
1. Junto a la celda o rango de celdas seleccionado, haga clic en el botón de error que aparece. En el menú, haga clic en Convertir a Número. 
<br>
<img src="4.png" width=70% />
1. Si el botón de alerta no está disponible, seleccione una columna con este problema. Si no desea convertir toda la columna, puede seleccionar una o más celdas en su lugar. Asegúrese de que las celdas que seleccione estén en la misma columna, de lo contrario este proceso no funcionará. El botón Texto en Columnas se usa típicamente para dividir una columna, pero también se puede usar para convertir una sola columna de texto a números. En la pestaña Datos, haga clic en Texto en Columnas.
<br>
<img src="1.png" width=70% />
1. Haga clic en el botón Finalizar en el cuadro emergente.
<br>
<img src="2.png" width=70% />
1. Los números almacenados como texto se transforman en números.
<br>
<img src="3.png" width=70% />

## Cómo convertir números almacenados como texto a números usando Aspose.Cells for .NET
Aspose.Cells proporciona el método [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue) que se puede utilizar para convertir todos los datos numéricos de texto o cadena en números.

La siguiente captura de pantalla muestra números de cadena en las celdas **A1:A17**. Los números de cadena están alineados a la izquierda.
<br>
<img src="5.png" width=70% />

Estos números de cadena se han convertido en números utilizando [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue) en la siguiente captura de pantalla. Como se puede ver, ahora están alineados a la derecha.
<br>
<img src="6.png" width=70% />

## Código en C# para convertir datos numéricos de cadena en números reales

El siguiente código de muestra ilustra cómo convertir todos los datos numéricos de cadena en números reales en todas las hojas de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
{{< app/cells/assistant language="csharp" >}}
