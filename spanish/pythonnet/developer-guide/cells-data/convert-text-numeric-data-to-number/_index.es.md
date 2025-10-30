---
title: Convertir Datos Numéricos de Texto a Número
type: docs
weight: 900
url: /es/python-net/convert-text-numeric-data-to-number/
description: Aprenda cómo convertir números almacenados como texto en Excel a números utilizando la API Aspose.Cells para Python via .NET.
keywords: python excel convertir texto a número, python excel convertir texto a número, python excel convertir datos numéricos de texto a número, python excel convertir datos numéricos de texto a número, python excel convertir texto numérico a número, python excel convertir texto numérico a número, excel convertir texto numérico a número con python, convertir texto numérico a número en excel con python, convertir texto numérico a número en excel con la biblioteca python, python excel convertir datos numéricos de texto a número, python excel convertir cadena numérica a número.
---

## **Escenarios de uso posibles**
A veces, desea convertir datos numéricos ingresados como texto a números. Puede ingresar números como texto en Microsoft Excel poniendo un apóstrofe antes de un número, por ejemplo **'12345**. Excel luego trata el número como una cadena. Aspose.Cells para Python via .NET le permite convertir cadenas a números.


## **Cómo Convertir números almacenados como texto a números en Excel**
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

## **Cómo Convertir números almacenados como texto a números utilizando la Biblioteca Excel de Aspose.Cells para Python**
Aspose.Cells para Python via .NET proporciona el método [**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/) que se puede utilizar para convertir todos los datos numéricos de cadena o texto en números.

La siguiente captura de pantalla muestra números de cadena en las celdas **A1:A17**. Los números de cadena están alineados a la izquierda.
<br>
<img src="5.png" width=70% />

Estos números de cadena se han convertido en números utilizando [**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/) en la siguiente captura de pantalla. Como se puede ver, ahora están alineados a la derecha.
<br>
<img src="6.png" width=70% />

## **Código Python para convertir datos numéricos de cadena en números reales**

El siguiente código de muestra ilustra cómo convertir todos los datos numéricos de cadena en números reales en todas las hojas de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.py" >}}
{{< app/cells/assistant language="python-net" >}}
