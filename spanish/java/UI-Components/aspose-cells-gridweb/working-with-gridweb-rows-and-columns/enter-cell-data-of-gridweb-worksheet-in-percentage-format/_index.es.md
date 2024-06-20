---
title: Ingresar Datos de Celda de la Hoja de Cálculo de GridWeb en Formato de Porcentaje
type: docs
weight: 1010
url: /es/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---

## **Escenarios de uso posibles**
GridWeb ahora admite que los usuarios ingresen datos de celda en formato de porcentaje, como 3%, y los datos en la celda se formatearán automáticamente como 3.00%. Sin embargo, deberás establecer el estilo de celda en Formato de Porcentaje, que es el GridTableItemStyle.NumberType 9 o 10. El número 9 formateará el 3% como 3%, pero el número 10 formateará el 3% como 3.00%.

{{% alert color="primary" %}} 

Si no has establecido el estilo de celda en Formato de Porcentaje, entonces el dato de entrada 3% se mostrará como 0.03.

{{% /alert %}} 
## **Ingrese los datos de celda de la hoja de cálculo GridWeb en formato de porcentaje**
El siguiente código de muestra establece el estilo de número de celda A1 GridTableItemStyle.NumberType como 10, por lo tanto, los datos de entrada 3% se formatean automáticamente como 3.00% como se muestra en la captura de pantalla.

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
## **Código de muestra**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}






