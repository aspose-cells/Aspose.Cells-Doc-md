---
title: Ingrese Cell Datos de la hoja de trabajo GridWeb en formato de porcentaje
type: docs
weight: 80
url: /es/net/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---
## **Posibles escenarios de uso**
GridWeb ahora permite a los usuarios ingresar datos de celda en formato de porcentaje como 3% y los datos en la celda se formatearán automáticamente como 3.00%. Sin embargo, tendrá que establecer el estilo de celda en Formato de porcentaje, que es GridTableItemStyle.NumberType a 9 o 10. El número 9 formateará el 3 % como 3 %, pero el número 10 formateará el 3 % como 3,00 %.

{{% alert color="primary" %}} 

Si no ha establecido el estilo de celda en Formato de porcentaje, los datos de entrada 3% se mostrarán como 0,03.

{{% /alert %}} 
## **Ingrese Cell Datos de la hoja de trabajo GridWeb en formato de porcentaje**
El siguiente código de muestra establece la celda A1 GridTableItemStyle.NumberType como 10, por lo tanto, los datos de entrada 3 % se formatearán automáticamente como 3,00 %, como se muestra en la captura de pantalla.

![todo:imagen_alternativa_texto](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
### **Código de muestra**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SetCellPercentageFormat.aspx-SetCellPercentageFormat.cs" >}}
