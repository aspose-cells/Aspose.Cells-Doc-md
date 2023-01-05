---
title: Personalizar parámetros de inicialización
type: docs
weight: 10
url: /es/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
description: cómo personalizar los parámetros de inicialización en Aspose.Cells. Guión del lado del cliente de GridWeb.
---
{{% alert color="primary" %}} 

 Los desarrolladores pueden establecer un valor de parámetro de inicialización diferente para realizar un comportamiento diferente para el control Aspose.Cells.GridWeb en acwmain.js.

{{% /alert %}} 
 
### **Parámetros**
 
|**Parámetro**|**Descripción**|
|:- |:- |
|necesitaInitAlignmentAdjust|si se debe realizar la alineación vertical para el contenido de la celda en la inicialización, llevará algún tiempo realizar el trabajo de alineación, si la hoja de trabajo tiene celdas grandes, el rendimiento será deficiente, si al usuario no le importa la alineación vertical, entonces puede configurarlo en ser falso, el valor predeterminado es verdadero|
|centrarse en el interior| si se debe enfocar dentro del intervalo de celdas, el valor predeterminado es verdadero|
|Copiar_con_estilo|si se copia con estilo, el valor predeterminado es falso, lo que significa que solo se copia el contenido de la celda|
|usarESCAsDejar|el comportamiento predeterminado cuando se presiona esc funciona como cancelar la operación de edición en la celda, si establecemos este valor en verdadero, solo lo trataremos como una tecla corta para salir de la celda sin volver al valor anterior, y también cambiará la forma de edición interna para la forma de edición rápida, el valor predeterminado es falso|
|necesitaValidartodo|si validar todas las validaciones en la hoja activa cuando se realiza la validación (en la página de control aspx, establezca ForceValidation="True") . el valor predeterminado es falso|
|scrollToInvalidate|si se debe desplazar y traer a la vista la primera celda invalidada cuando needValidateall se establece en verdadero. El valor predeterminado es verdadero.|
 
 
 El resultado del ejemplo de código se muestra a continuación. Verifique el[ejemplo de archivo de Excel](valign.xlsx):

**needInitAlignmentAdjust=verdadero** 

![todo:imagen_alternativa_texto](align_true.png)

**needInitAlignmentAdjust=falso** 

![todo:imagen_alternativa_texto](align_false.png)

**foco dentro = verdadero** 
 dentro de la forma de edición: cuando ingrese texto, el valor de la celda anterior aún se mantendrá

![todo:imagen_alternativa_texto](focus_inside_true.png)

**foco dentro = falso** 
forma de edición rápida: cuando ingrese texto, el valor de la celda anterior se sobrescribirá, si desea editar según el valor de la celda anterior, puede hacer clic en la celda

![todo:imagen_alternativa_texto](focus_inside_false.png)

 
 