---
title: Personalizar parámetros de inicialización
type: docs
weight: 10
url: /es/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
keywords: GridWeb, personalizar, parámetros de personalización
description: cómo personalizar los parámetros de inicialización en el script del lado del cliente de Aspose.Cells.GridWeb.
---

{{% alert color="primary" %}} 

Los desarrolladores pueden establecer diferentes valores de parámetros de inicialización para realizar diferentes comportamientos para el control Aspose.Cells.GridWeb en acwmain.js.  

{{% /alert %}} 

### **Parámetros**

|**Parámetro**|**Descripción**|
| :- | :- |
|needInitAlignmentAdjust| si se debe realizar alineación vertical para el contenido de celda en la inicialización, tomará algún tiempo realizar el trabajo de alineación, si la hoja de cálculo tiene celdas grandes, el rendimiento será pobre, si al usuario no le importa la alineación vertical, entonces puede establecerlo en falso, el valor predeterminado es verdadero |
|focusinside| si se debe enfocar dentro del espacio de la celda, el valor predeterminado es verdadero |
|copy_with_style| si se debe copiar con estilo, el valor predeterminado es falso, lo que significa que solo copiará el contenido de la celda |
|useESCAsLeave| el comportamiento predeterminado al presionar ESC funciona como operación de edición de cancelación en la celda, si configuramos este valor en verdadero, simplemente lo trataremos como una tecla rápida para salir de la celda sin cambiar al valor anterior, y también cambiará la forma de edición interna a la forma de edición rápida, el valor predeterminado es falso |
|needValidateall| si se deben validar todas las validaciones en la hoja activa al hacer validación, (en la página de control aspx establezca ForceValidation="Verdadero"). el valor predeterminado es falso |
|scrollToInvalidate| si se debe desplazar y llevar la primera celda no válida a la vista cuando se necesita validar todo, el valor predeterminado es verdadero |


La salida del ejemplo de código se muestra a continuación, consulte el [archivo de excel de muestra](valign.xlsx):

**needInitAlignmentAdjust=true** 

![todo:image_alt_text](align_true.png)

**needInitAlignmentAdjust=false** 

![todo:image_alt_text](align_false.png)

**focusinside=true** 
modo de edición interna -- cuando se ingresa texto, el valor anterior de la celda seguirá siendo   

![todo:image_alt_text](focus_inside_true.png)

**focusinside=false** 
modo de edición rápida -- cuando se ingresa texto, el valor anterior de la celda será sobrescrito, si desea editar basado en el valor anterior de la celda, puede hacer clic en la celda

![todo:image_alt_text](focus_inside_false.png)



